import os
import telebot
from flask import Flask, request

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(content_types=['text'])
def yanitla(message):
    text = message.text.strip().lower()
    if text == "cp seviyeleri":
        yanit = (
            "CP Seviyeleri ve Gereken Hediyeler:\n\n"
            "0 - 1 → 1.000.000\n"
            "1 - 2 → 5.000.000\n"
            "2 - 3 → 10.000.000\n"
            "3 - 4 → 20.000.000\n"
            "4 - 5 → 50.000.000\n"
            "5 - 6 → 100.000.000\n\n"
            "Toplam: 186.000.000"
        )
        bot.reply_to(message, yanit)
    else:
        bot.reply_to(message, "Bu konuda bilgi bulunamadı.")

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
