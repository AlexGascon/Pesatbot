import telebot
import os

TOKEN = "135590410:AAHt91I6GrFBQv9QTxEsU6YeA0Aj1qfOBKE"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def pole_reply(message):
	if 'pole' in message.text.lower():
		print message.text.lower()
		bot.reply_to(message, 'Tio, eres un puto pesat')

bot.polling(none_stop=True)