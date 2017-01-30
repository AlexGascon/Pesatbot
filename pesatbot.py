import telebot
import os
from flask import Flask, request

TOKEN = "135590410:AAHt91I6GrFBQv9QTxEsU6YeA0Aj1qfOBKE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def pole_reply(message):
	if 'pole' in message.text.lower():
		print message.text.lower()
		bot.reply_to(message, 'Tio, eres un puto pesat')

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://pesatbot.herokuapp.com/bot")
return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)
"""
bot.polling(none_stop=True)
"""