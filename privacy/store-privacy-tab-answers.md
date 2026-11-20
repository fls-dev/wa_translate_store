# Chrome Web Store → вкладка «Privacy practices» — готовые ответы
(копируй текст в поля как есть; англ. версии — для вставки в форму, русские пояснения — для тебя)

## Single purpose description (макс. ~1000 симв.)
```
WA Translate has a single purpose: translating conversations on WhatsApp Web. It shows a translation under each incoming message and translates the user's own reply before it is sent, only in chats the user has enabled.
```
Пояснение: узкая цель = перевод переписки в WhatsApp Web. Статистика, кэш, диагностика — вспомогательные части этой же цели.

## Permission justifications

**storage**
```
Stores the user's settings (selected translation engine, languages, per-chat on/off and language), the user's own API keys, a local cache of recent translations and usage counters in chrome.storage.local. Nothing is synced or sent to the developer.
```

**Host permission: https://web.whatsapp.com/* (content script)**
```
The content script runs only on web.whatsapp.com. It reads the text of messages in the open chat (only in chats the user enabled) to translate them, inserts the translation under the message, and — after the user confirms a previewed translation — puts the translated text into the message box and presses the Send button. It does not run on any other site.
```

**Optional host permissions (optional_host_permissions)** — по одному, запрашиваются в окне расширения только при выборе провайдера:
```
https://api.openai.com/*  – user selected OpenAI (GPT) as the translation engine; message text is sent to the OpenAI API with the user's own key.
https://api.anthropic.com/*  – user selected Anthropic (Claude); same purpose.
https://generativelanguage.googleapis.com/*  – user selected Google Gemini API; same purpose.
https://api.x.ai/*  – user selected xAI (Grok); same purpose.
https://openrouter.ai/*  – user selected OpenRouter; same purpose.
https://api-free.deepl.com/*, https://api.deepl.com/*  – user selected DeepL (free or Pro key); same purpose.
https://translate.googleapis.com/*  – user selected the free Google Translate engine or enabled the optional Google fallback.
These are optional: they are requested at runtime only for the one provider the user picks. No broad host access (no <all_urls>) is requested.
```
Если форма даёт ОДНО поле для host permissions — вставь весь блок выше.

Примечание: `activeTab`, `tabs`, `scripting`, `webRequest`, `cookies` и т. п. НЕ используются — в форме их быть не должно.

## Remote code
Ответ: **No, I am not using remote code.**
```
All code is bundled in the package. The extension only sends text to translation APIs and receives JSON/text back; it never evaluates or executes anything fetched from the network (no eval, no new Function, no remote <script>).
```

## Data usage — какие типы данных отмечать
Отметь галочками (принцип: «передаётся ли это за пределы устройства»):

| Категория | Отметить? | Почему |
|---|---|---|
| Personally identifiable information | **Нет** | имена/телефоны/почта не читаются и не отправляются |
| Health information | Нет | — |
| Financial and payment information | Нет | — |
| **Authentication information** | **Да** | пользователь вводит API-ключи (хранятся локально, отправляются только своему провайдеру как credential) |
| **Personal communications** | **Да** | текст сообщений WhatsApp отправляется выбранному провайдеру перевода |
| Location | Нет | — |
| Web history | Нет | — |
| User activity | Нет | клики/ввод не отслеживаются (счётчики использования лежат локально) |
| **Website content** | **Да** | текст страницы (сообщений) читается для перевода |

## Certifications (три чекбокса — отметить ВСЕ)
- ☑ I do not sell or transfer user data to third parties, outside of the approved use cases. *(текст уходит только провайдеру, выбранному пользователем, ради перевода — это approved use case)*
- ☑ I do not use or transfer user data for purposes that are unrelated to my item's single purpose.
- ☑ I do not use or transfer user data to determine creditworthiness or for lending purposes.

## Privacy policy URL
```
https://fls-dev.github.io/wa_translate_store/privacy.html
```
(красивая страница с переключателем EN/RU; публикуется из папки `docs/` репозитория fls-dev/wa_translate_store через GitHub Pages)

## Account tab (не Privacy practices, но нужно)
- Contact email (подтвердить письмом).
- Trader / non-trader (EU DSA): бесплатное хобби-расширение без дохода → «non-trader»; если планируешь продавать/монетизировать → «trader» (придётся указать публичный адрес/телефон).
