import telebot

TOKEN = "135590410:AAHt91I6GrFBQv9QTxEsU6YeA0Aj1qfOBKE"
pesatbot = telebot.TeleBot(TOKEN)

@pesatbot.message_handler(func=lambda m: True)
def pole_reply(message):
	if message.text.lower().contains('pole')
		pesatbot.reply_to(message, 'Tio, eres un puto pesat')

pesatbot.polling(none_stop=True, interval=0)


