import telebot

TOKEN = "135590410:AAHt91I6GrFBQv9QTxEsU6YeA0Aj1qfOBKE"
pesatbot = telebot.TeleBot(TOKEN)

@pesatbot.message_handler(func=lambda message: True)
def pole_reply(message):
	if 'pole' in message.text.lower():
		pesatbot.reply_to(message, 'Tio, eres un puto pesat')

pesatbot.polling(none_stop=True, interval=0)


