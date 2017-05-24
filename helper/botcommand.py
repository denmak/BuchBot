from config import config as cf
from helper import googlehelper as glhlp



def get_help(bot,message):
	msg = 'list of command: \n'+' \n'.join(takeaction.keys()) +'\n ' +cf.HELP_MSG
	bot.send_message(message.chat.id, msg)


def get_sheet_link(bot,message):
	bot.send_message(message.chat.id, 'sheet link: '+cf.LINK_SHEET_BASE+cf.spreadsheetId)


def get_current_week_report(bot,message):
	bot.send_message(message.chat.id, cf.COMMAND_IN_DEV_MSG)


def get_last10_report(bot,message):
	rows = glhlp.read_rows_spreadsheet('A2:F')
	msg = ' list of last 10 inputs: \n'
	num = 10
	if len(rows)<10: num=len(rows)
	for cell in rows[:num]:
		msg = msg + ' '.join(cell) + '\n'
	bot.send_message(message.chat.id, msg)


def get_total(bot,message):
	total = glhlp.read_cell_spreadsheet('I1') # TODO remove hardcode #https://docs.google.com/spreadsheets/d/1-iKub0vWhJ4RTIyiKJ-F_J8FdEVFovilD258XJHURRw/edit#gid=0&range=H2
	bot.send_message(message.chat.id, ' your family total: ' +str(total))


def save_input_to_sheet(bot,message):
	glhlp.write_spreadsheet(message)
	bot.send_message(message.chat.id, message.text + ' confirmed')

takeaction = {
    "/exp": save_input_to_sheet,
    "/help": get_help,
    "/sheet": get_sheet_link,
	"/week": get_current_week_report,
    "/last10": get_last10_report,
	"/total": get_total
}
