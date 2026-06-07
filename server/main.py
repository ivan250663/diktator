import os
import sqlite_utils
from datetime import datetime
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
klient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DB_PATH = "data/diktator.db"
os.makedirs("data", exist_ok=True)
os.makedirs("data/nahravky", exist_ok=True)

def get_db():
    db = sqlite_utils.Database(DB_PATH)
    if "zaznamy" not in db.table_names():
        db["zaznamy"].create({
            "id": int,
            "cas": str,
            "povodny_text": str,
            "opraveny_text": str,
            "audio_subor": str,
        }, pk="id")
    return db

@app.get("/", response_class=HTMLResponse)
async def root():
    return open("web/index.html", encoding="utf-8").read()

@app.post("/nahraj")
async def nahraj(audio: UploadFile = File(...)):
    obsah = await audio.read()

    cas_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_subor = f"data/nahravky/{cas_str}.webm"

    with open(audio_subor, "wb") as f:
        f.write(obsah)

    with open(audio_subor, "rb") as f:
        prepis = klient.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="sk"
        )

    text = prepis.text

    db = get_db()
    db["zaznamy"].insert({
        "cas": datetime.now().isoformat(),
        "povodny_text": text,
        "opraveny_text": "",
        "audio_subor": audio_subor,
    })

    return {"status": "ok", "text": text}

@app.post("/oprava")
async def oprava(request: Request):
    data = await request.json()
    povodny = data.get("povodny", "")
    opraveny = data.get("opraveny", "")

    db = get_db()
    zaznam = list(db["zaznamy"].rows_where(
        "povodny_text = ?", [povodny],
        order_by="id desc",
        limit=1
    ))

    if zaznam:
        db["zaznamy"].update(zaznam[0]["id"], {"opraveny_text": opraveny})

    return {"status": "ok"}

@app.get("/audio/{subor}")
async def audio(subor: str):
    cesta = f"data/nahravky/{subor}"
    if os.path.exists(cesta):
        return FileResponse(cesta, media_type="audio/webm")
    return {"error": "nenajdene"}

@app.get("/admin", response_class=HTMLResponse)
async def admin():
    return open("admin/index.html", encoding="utf-8").read()

@app.get("/api/zaznamy")
async def api_zaznamy():
    db = get_db()
    rows = list(db["zaznamy"].rows_where(order_by="id desc"))
    return rows