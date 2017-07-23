from config import config as cf
from helper import googlehelper as glhlp



def get_help(bot,message):
	msg = 'list of command: \n'+' \n'.join(takeaction.keys()) +'\n ' +cf.HELP_MSG
	bot.send_message(message.chat.id, msg)


def login(bot,message):
	bot.send_message(message.chat.id, 'sheet link: '+cf.LINK_SHEET_BASE+cf.spreadsheetId)


def logout(bot,message):
	bot.send_message(message.chat.id, cf.COMMAND_IN_DEV_MSG)


def get_week(bot,message):
	rows = glhlp.read_rows_spreadsheet('A2:F')
	msg = ' list of last 10 inputs: \n'
	num = 10
	if len(rows)<10: num=len(rows)
	for cell in rows[:num]:
		msg = msg + ' '.join(cell) + '\n'
	bot.send_message(message.chat.id, msg)


def get_limits(bot,message):
	total = glhlp.read_cell_spreadsheet('I1') # TODO remove hardcode #https://docs.google.com/spreadsheets/d/1-iKub0vWhJ4RTIyiKJ-F_J8FdEVFovilD258XJHURRw/edit#gid=0&range=H2
	bot.send_message(message.chat.id, ' your family total: ' +str(total))


def get_bygroup(bot,message):
	glhlp.write_spreadsheet(message)
	bot.send_message(message.chat.id, message.text + ' confirmed')

def get_month():
	print('get month')


#Получить список групп расходов по категориям
def get_groups():
	print('get groups')

#Получить остатки по счетам в разбивке по неделям месяца, к которому принадлежить 'startDate'.
def get_accounts():
	print('get accounts')

# Добавить или изменить запись о расходе или доходе.
# 'tid' может быть равен 0, в этом случае будет добавлена новая запись
def modify_update():
	print('modify_update')

def modify_delete():
	print('modify delete')

# Добавить\изменить остаток, наименование или статус счета 'aid'.
# 'isActive' = 0|1. Если ‘aid’ не указан, то будет добавлен новый счет

def modify_editAccount():
	print('edit account')

#  Изменить лимит по группе расходов на месяц.
# На текущий момент возможно задать лимит только на месяц. Gid - группа расходов, lid - id записи о лимите по группе расходов. Если lid не указан, то будет создана новая запись.
def modify_updateLimit():
	print('update limit')





takeaction = {
    "/exp": save_input_to_sheet,
    "/help": get_help,
    "/sheet": get_sheet_link,
	"/week": get_current_week_report,
    "/last10": get_last10_report,
	"/total": get_total
}
