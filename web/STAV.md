# DIKTATOR — stav projektu

## Čo je hotové
- Python 3.13, VS Code, Git nainštalované
- Štruktúra: server/main.py, web/index.html
- Server beží cez uvicorn, webová stránka funguje
- Mikrofón nahrá hlas, server prijme audio
- Whisper API prepíše hlas na text ✓
- Git inicializovaný, commity uložené

## Stack
- Python + FastAPI + uvicorn
- Cloud: Railway (zatiaľ lokálne)
- Prepis: OpenAI Whisper API (ešte nenainštalované)

## Ďalší krok — Krok 2
Pridať OpenAI Whisper API na prepis hlasu na text.
Potrebujeme API kľúč z platform.openai.com.

## Ďalší krok — Krok 3
Nasadiť na cloud (Railway) aby server bežal bez počítača.

## Štruktúra priečinka
DIKTATOR/
├── server/
│   └── main.py
├── web/
│   └── index.html
├── .gitignore
└── STAV.md