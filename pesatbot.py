# -*- coding: utf-8 -*-   

import random

import telebot
import os

# Creating the bot
TOKEN = os.environ['TELEGRAM_BOT_TOKEN'] # Token previously stored in an environment var
bot = telebot.TeleBot(TOKEN)


def select_response(message):
	responses = ['Ie {} tio, no et canses?', '{}, eres un puto pesat de tio', 'Ie {}, ja hi ha prou que ja cansa',
				'Collons {}, que pesat eres quan vols', "Que si {}, tio pesat, que ja t'hem llegit"]

	response_to_use = random.choice(responses)
	response = response_to_use.format(message.from_user.first_name)

	return response


# The decorator (@bot.message_handler) indicates the type of messages that will activate this function
# In this case, we'll activate it for every message. See telebot API for more possibilities 
@bot.message_handler(func=lambda message: True)
def pole_reply(message):
	# If the message contains the word 'pole' (case insensitive), the bot replies
	if 'pole' in message.text.lower():
		resposta = select_response(message)
		bot.reply_to(message, resposta)

bot.polling(none_stop=True)