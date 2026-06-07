## Čo je hotové
- Python 3.13, VS Code, Git nainštalované
- Whisper API prepíše hlas na text ✓
- Server beží lokálne, syn používa tablet cez WiFi ✓
- Rozhranie pre syna: klik štart/stop, TTS ✓
- Admin rozhranie: záznamy, prehrávanie, opravy ✓
- Ukladanie audio nahrávok na disk ✓
- Dáta nie sú na GitHube ✓

## Stack
- Python + FastAPI + uvicorn
- Lokálny server: http://192.168.1.100:8000
- Prepis: OpenAI Whisper API
- GitHub: https://github.com/ivan250663/diktator

## Spustenie servera
- Dvojklik na start.bat
- Alebo: venv\Scripts\activate → python -m uvicorn server.main:app --host 0.0.0.0 --port 8000 --reload

## Ďalší krok — Krok 3
Nasadiť na cloud (Railway) aby server bežal bez počítača.

## Ďalší krok — Krok 4
Vylepšiť rozhranie pre syna:
- Veľké tlačidlá
- Automatické čítanie textu nahlas (TTS)
- Tlačidlá: Odoslať, Znova, Opraviť

## Ďalší krok — Krok 5
Admin rozhranie pre otca — prezeranie záznamov a opravy.
Ukladanie každej nahrávky do databázy.

## Ďalší krok — Krok 6
Nasadiť aktualizáciu na Render.
Otestovať na tablete syna.

## Ďalší krok — Krok 7
Modul ktorý sa učí z opráv — automatická korekcia prepisu.