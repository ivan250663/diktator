# DIKTATOR — stav projektu

## Čo je hotové
- Python 3.13, VS Code, Git nainštalované
- Štruktúra: server/main.py, web/index.html
- Server beží cez uvicorn, webová stránka funguje
- Mikrofón nahrá hlas, server prijme audio
- Git inicializovaný, 2 commity

## Stack
- Python + FastAPI + uvicorn
- Cloud: Railway (zatiaľ lokálne)
- Prepis: OpenAI Whisper API (ešte nenainštalované)

## Ďalší krok — Krok 2
Pridať OpenAI Whisper API na prepis hlasu na text.
Potrebujeme API kľúč z platform.openai.com.

## Štruktúra priečinka
DIKTATOR/
├── server/
│   └── main.py
├── web/
│   └── index.html
├── .gitignore
└── STAV.md