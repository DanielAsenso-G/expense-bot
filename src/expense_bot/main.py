import os
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
import httpx

load_dotenv()
WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

def send_message(chat_id: int, text: str):
    httpx.post(f"{TELEGRAM_API}/sendMessage", json={"chat_id": chat_id, "text": text})

@app.post("/webhook")
def webhook(payload : dict, x_telegram_bot_api_secret_token: str = Header(None)):
    if x_telegram_bot_api_secret_token != WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")

    chat_id = payload["message"]["chat"]["id"]
    text = payload["message"]["text"]
    send_message(chat_id, f"You said: {text}")
    print(payload)

    return {"ok": True}