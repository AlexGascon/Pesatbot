import telebot

TOKEN = "135590410:AAHt91I6GrFBQv9QTxEsU6YeA0Aj1qfOBKE"
pesatbot = telebot.TeleBot(TOKEN)

pesatbot.polling(none_stop=True, interval=0, block=True)

pesatbot.set_webhook('http://pesatbot.herokuapp.com')


@bot.message.handler(func=lambda m: True)
def pole_reply(message):
	pesatbot.reply_to(message, 'Tio, eres un puto pesat')