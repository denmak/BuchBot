# -*- coding: utf-8 -*-
exampleconf='this is an example'
token = '327670438:AAH30zDGavR6-Ht3u-lMOFR6F3xqJnSS2IU'
email ='@gmail.com'
password = '159'
weight = '180'
# Find this value in the url with 'key=XXX' and copy XXX below
spreadsheet_key = '1-iKub0vWhJ4RTIyiKJ-F_J8FdEVFovilD258XJHURRw'
# All spreadsheets have worksheets. I think worksheet #1 by default always
# has a value of 'od6'
worksheet_id = 'od6'

clid='220360779726-9udn1qo31ie4096mbtg4k0hojog8llil.apps.googleusercontent.com'
clsec='qNkn1n6BQDNir-ZEB-_CR_u2'

discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
				'version=v4')
spreadsheetId = '1-iKub0vWhJ4RTIyiKJ-F_J8FdEVFovilD258XJHURRw'
value_input_option = u'RAW'  # TODO: Update placeholder value "[u'INPUT_VALUE_OPTION_UNSPECIFIED', u'RAW', u'USER_ENTERED']"

# How the input data should be inserted.
insert_data_option = u'OVERWRITE'  # TODO: Update placeholder value.

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret_220360779726-9udn1qo31ie4096mbtg4k0hojog8llil.apps.googleusercontent.com.json'
APPLICATION_NAME = 'telebot_buh'

LINK_SHEET_BASE = 'https://docs.google.com/spreadsheets/d/'

HELP_MSG = 'If you whant to save some expences  you have to type me : /exp product_name 100.00  comment  '
UNKNOWN_COMMAND_MSG = 'Sorry, I cant recognse what did you type. type /help to get help'
ERR_MSG = 'uups... something goes wrong '
COMMAND_IN_DEV_MSG = 'OMG!!! this commang is in developemt still. May be next sprint...'

