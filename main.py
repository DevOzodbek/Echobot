from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("7778448241:AAFbefkZNVpF6n9toMaW-IAOOcZQIqGHjDo")  # Tokenni Render'ga Environment variable orqali beramiz

URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/')
def index():
    return "Bot ishlayapti!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        if text:
            send_message(chat_id, f"Siz yozdingiz: {text}")
    return "OK"

def send_message(chat_id, text):
    url = f"{URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(debug=True)