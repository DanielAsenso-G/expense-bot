import os
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException

load_dotenv()
WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET")
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/webhook")
def webhook(payload : dict, x_telegram_bot_api_secret_token: str = Header(None)):
    if x_telegram_bot_api_secret_token != WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")
    print(payload)
    return {"ok": True}