import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(daily, monthly, go_home):
    msg = (
        "⏱ NetTime\n\n"
        f"📅 Solde journalier : {daily}\n"
        f"📆 Solde mensuel : {monthly}\n\n"
        f"🏠 Départ estimé : {go_home}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })
