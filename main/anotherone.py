# -*- coding: utf-8 -*-
#from __future__ import print_function
import config.config as cf
import telebot
import helper.googlehelper as glhlp

from oauth2client import tools



def errhandler (message):
	bot.send_message(message.chat.id, cf.UNKNOWN_COMMAND_MSG)

def run_bot_command(message):
	body = message.text.split(' ')
	command = body[0] #"/expences"
	takeaction[command](message)

def save_input_to_sheet(message):
	glhlp.write_spreadsheet(message)
	bot.send_message(message.chat.id, message.text + ' confirmed')

def get_help(message):
	msg = 'list of command: \n'+' \n'.join(takeaction.keys()) +'\n ' +cf.HELP_MSG
	bot.send_message(message.chat.id, msg)

def get_sheet_link(message):
	bot.send_message(message.chat.id, 'sheet link: '+cf.LINK_SHEET_BASE+cf.spreadsheetId)

def get_current_week_report(message):
	bot.send_message(message.chat.id, cf.COMMAND_IN_DEV_MSG)

def get_last10_report(message):
	rows = glhlp.read_rows_spreadsheet('A2:F')
	msg = ' list of last 10 inputs: \n'
	num = 10
	if len(rows)<10: num=len(rows)
	for cell in rows[:num]:
		msg = msg + ' '.join(cell) + '\n'
	bot.send_message(message.chat.id, msg)

def get_total(message):
	total = glhlp.read_cell_spreadsheet('I1') # TODO remove hardcode #https://docs.google.com/spreadsheets/d/1-iKub0vWhJ4RTIyiKJ-F_J8FdEVFovilD258XJHURRw/edit#gid=0&range=H2
	bot.send_message(message.chat.id, ' your family total: ' +str(total))

bot = telebot.TeleBot(cf.token)
# TODO create configuration dialog

takeaction = {
    "/exp": save_input_to_sheet,
    "/help": get_help,
    "/sheet": get_sheet_link,
	"/week": get_current_week_report,
    "/last10": get_last10_report,
	"/total":get_total
}

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

