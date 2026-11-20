#!/usr/bin/env python3
"""Собирает чистый zip для Chrome Web Store из /workspace/wa_translate (без тестов, без тестовых хуков) и проверяет его."""
import json, os, re, shutil, sys, zipfile
SRC='/workspace/wa_translate'; OUT='/workspace/wa_translate_store/extension'
man=json.load(open(SRC+'/manifest.json')); ver=man['version']
stage=f'/tmp/wa_store_stage'; shutil.rmtree(stage,ignore_errors=True); os.makedirs(stage+'/icons')
FILES=['manifest.json','background.js','translate.js','content.js','content.css','popup.html','popup.css','popup.js']
for f in FILES: shutil.copy(f'{SRC}/{f}',f'{stage}/{f}')
for n in ('icon16','icon32','icon48','icon128'): shutil.copy(f'{SRC}/icons/{n}.png',f'{stage}/icons/{n}.png')
# убрать тестовые хуки (строки с маркером @test-only)
for f in FILES:
    if f.endswith('.js'):
        lines=open(f'{stage}/{f}').read().split('\n'); keep=[l for l in lines if '@test-only' not in l]
        if len(keep)!=len(lines): print(f'  {f}: убрано тестовых строк: {len(lines)-len(keep)}')
        txt='\n'.join(keep)
        txt=txt.replace(", _setBases: b => { root.__bases = b; }, _setFetch: f => { root.__fetch = f; }",'')
        open(f'{stage}/{f}','w').write(txt)
zp=f'{OUT}/wa-translate-{ver}.zip'
for old in os.listdir(OUT):
    if old.endswith('.zip'): os.remove(f'{OUT}/{old}')
with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED) as z:
    for r,_,fs in os.walk(stage):
        for n in sorted(fs): p=os.path.join(r,n); z.write(p,os.path.relpath(p,stage))
# ---------- валидация ----------
errs=[]; z=zipfile.ZipFile(zp); names=z.namelist()
m=json.loads(z.read('manifest.json'))
assert m['manifest_version']==3
def need(p):
    if p not in names: errs.append('нет файла '+p)
need(m['background']['service_worker'])
for cs in m['content_scripts']:
    for p in cs.get('js',[])+cs.get('css',[]): need(p)
need(m['action']['default_popup'])
for p in list(m['icons'].values())+list(m['action']['default_icon'].values()): need(p)
for w in m.get('web_accessible_resources',[]):
    for p in w['resources']: need(p)
html=z.read('popup.html').decode()
for p in re.findall(r'(?:src|href)="([^"#]+)"',html):
    if not p.startswith('http'): need(p)
if len(m['description'])>132: errs.append('description >132')
if len(m['name'])>75: errs.append('name >75')
bad_perm=[p for p in m.get('permissions',[]) if p not in ('storage',)]
if bad_perm: errs.append('лишние permissions: '+str(bad_perm))
if 'host_permissions' in m: errs.append('есть host_permissions (должны быть optional)')
code=''.join(z.read(n).decode('utf8','ignore') for n in names if n.endswith(('.js','.html')))
for pat,why in [(r'\beval\s*\(','eval'),(r'new\s+Function\s*\(','new Function'),(r'<script[^>]+src="https?://','удалённый скрипт'),(r'importScripts\(\s*[\'"]https?:','удалённый importScripts'),
                (r'sk-[A-Za-z0-9_-]{16,}','похоже на ключ OpenAI'),(r'AIza[0-9A-Za-z_-]{20,}','похоже на ключ Google'),(r'sk-ant-[A-Za-z0-9_-]{8,}','ключ Anthropic'),(r'xai-[A-Za-z0-9]{16,}','ключ xAI'),
                (r'127\.0\.0\.1|localhost','локальные адреса'),(r'_setBases|baseUrls','тестовый хук'),(r'console\.(log|debug)\(','console.log')]:
    if re.search(pat,code): errs.append(f'найдено: {why}')
for n in names:
    if re.search(r'test|\.txt$|README|\.py$|\.svg$|\.map$',n,re.I): errs.append('лишний файл: '+n)
print('zip:',zp,os.path.getsize(zp),'bytes;',len(names),'files'); print('\n'.join(' ',) if False else '\n'.join('  '+n for n in sorted(names)))
print('name:',m['name'],'| version:',m['version'],'| permissions:',m['permissions'],'| optional hosts:',m['optional_host_permissions'],'| content script:',m['content_scripts'][0]['matches'])
if errs: print('ОШИБКИ:'); [print(' -',e) for e in errs]; sys.exit(1)
print('VALID: manifest parses, all referenced files exist, no secrets/remote code/test hooks')
