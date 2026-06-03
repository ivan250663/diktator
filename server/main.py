import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
klient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/", response_class=HTMLResponse)
async def root():
    return open("web/index.html", encoding="utf-8").read()

@app.post("/nahraj")
async def nahraj(audio: UploadFile = File(...)):
    obsah = await audio.read()

    with open("docasna_nahravka.webm", "wb") as f:
        f.write(obsah)

    with open("docasna_nahravka.webm", "rb") as f:
        prepis = klient.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="sk"
        )

    os.remove("docasna_nahravka.webm")

    return {"status": "ok", "text": prepis.text}