# Публикация WA Translate в Chrome Web Store — чек-лист

Всё готово. Тебе осталось: **зарегистрироваться ($5) → загрузить zip → скопировать тексты → отправить.** Примерно 20–30 минут.

**Ссылки (уже работают после включения GitHub Pages):**
- Сайт: https://fls-dev.github.io/wa_translate_store/
- Политика конфиденциальности (нужна магазину): `https://fls-dev.github.io/wa_translate_store/privacy.html`

## Шаг 1. Регистрация разработчика (один раз)
1. Открой https://chrome.google.com/webstore/devconsole и войди в свой Google-аккаунт.
2. Прими соглашение и оплати **$5** (единоразово, без подписки).
3. Если попросит — включи двухэтапную аутентификацию в Google-аккаунте.
4. Вкладка **Account** → введи контактную почту → нажми ссылку подтверждения в письме.
5. Вопрос «trader / non-trader»: выбери **non-trader** (бесплатное хобби-расширение).

## Шаг 2. Загрузка
1. В дашборде нажми **Add new item** (Новый элемент).
2. Выбери файл `extension/wa-translate-3.2.0.zip` из этой папки. Если появится ошибка — пришли мне её текст.

## Шаг 3. Вкладка Store listing (карточка)
Открывай файл `listing/listing-en.md` и копируй по полям:
| Поле в магазине | Откуда взять |
|---|---|
| Description (описание) | раздел «Full description» из `listing/listing-en.md` |
| Category | **Social & Communication** |
| Language | English (основной); потом «Add language» → Russian (`listing-ru.md`), Polish (`listing-pl.md`) |
| Icon 128 | `assets/icon-128.png` |
| Screenshots | 5 файлов из `assets/screenshots/en/` (для русской локали — из `ru/`) |
| Small promo tile | `assets/promo-small-440x280.png` |
| Marquee promo | `assets/marquee-1400x560.png` (по желанию) |
| Homepage URL / Official URL | https://fls-dev.github.io/wa_translate_store/ |
| Support URL | https://github.com/fls-dev/wa_translate_store/issues |
Название и краткое описание подтянутся из zip сами.

## Шаг 4. Вкладка Privacy practices
Открой `privacy/store-privacy-tab-answers.md` и по порядку скопируй:
1. **Single purpose** — вставить текст.
2. **Permission justification** — для `storage`, для `web.whatsapp.com` и для списка необязательных API-адресов (там всё готово).
3. **Remote code** → «No».
4. **Data usage** — галочки: *Authentication information*, *Personal communications*, *Website content*. Остальные пустые.
5. Три сертификации — поставить все галочки.
6. **Privacy policy URL**: `https://fls-dev.github.io/wa_translate_store/privacy.html`

## Шаг 5. Вкладка Distribution
- **Visibility:** сначала **Unlisted** (только по ссылке) → проверь, что ставится и работает → потом переключи на **Public**.
- Regions: все. Price: Free.

## Шаг 6. Отправка
Нажми **Submit for review**. Проверка обычно от нескольких дней до пары недель; придёт письмо. Когда расширение одобрят — пришли мне ссылку из магазина, я вставлю её в кнопку на сайте (кнопка «Chrome Web Store — скоро» станет рабочей).

## Как обновлять потом
Подними `version` в `manifest.json` (3.2.1, 3.3.0…), пересобери zip (попроси меня) → Дашборд → **Package → Upload new package → Submit for review**.

## Что может пойти не так
1. **Слово WhatsApp в названии.** Meta иногда жалуется. Если отклонят — переименуем, например, в «Chat Translate AI»; скажи мне, всё поправлю.
2. **Долгая проверка** — это нормально для нового разработчика.
3. **Разрешения и удалённый код** проблем быть не должно: постоянный доступ только к web.whatsapp.com, удалённого кода нет.
4. Интерфейс расширения пока только на русском — это честно указано в описании.
