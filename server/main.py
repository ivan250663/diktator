from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/web", StaticFiles(directory="web"), name="web")

@app.get("/", response_class=HTMLResponse)
async def root():
    return open("web/index.html", encoding="utf-8").read()

@app.post("/nahraj")
async def nahraj(audio: UploadFile = File(...)):
    obsah = await audio.read()
    velkost = len(obsah)
    return {"status": "ok", "velkost_bajtov": velkost}