# -*- coding: utf-8 -*-
#from __future__ import print_function
import telebot
import sys
import os
__path__=[os.path.dirname(os.path.abspath("/var/www/html/config"))]
print(__path__)

sys.path.append(os.path.dirname(os.path.abspath("/var/www/html/config")))
print(sys.path)

from config import config as cf
import  helper.botcommand as bc


def errhandler (message):
	bot.send_message(message.chat.id, cf.UNKNOWN_COMMAND_MSG)

def run_bot_command(message):
	body = message.text.split(' ')
	command = body[0] #"/expences"
	bc.takeaction[command](bot,message)


bot = telebot.TeleBot(cf.token)
# TODO create configuration dialog



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	#print message.text
	try:
		run_bot_command(message)
	except Exception as e:
		bot.send_message(message.chat.id, cf.ERR_MSG)
		print('ERROR: '+str(e))


if __name__ == '__main__':
	bot.polling(none_stop=True)

