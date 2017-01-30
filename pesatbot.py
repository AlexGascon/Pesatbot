import telebot
import os

TOKEN = "135590410:AAHt91I6GrFBQv9QTxEsU6YeA0Aj1qfOBKE"
pesatbot = telebot.TeleBot(TOKEN)


@pesatbot.message_handler(func=lambda message: True)
def pole_reply(message):
	if 'pole' in message.text.lower():
		print message.text.lower()
		pesatbot.reply_to(message, 'Tio, eres un puto pesat')

updater = Updater(TOKEN)
updater.start_webhook(listen="0.0.0.0", port=5000, url_path=TOKEN)

updater.bot.set_webhook("https://pesatbot.herokuapp.com/" + TOKEN)
updater.idle()