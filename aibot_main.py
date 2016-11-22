# AiBorGftW

import json
from irc import *
from datetime import date
from aibot_json import *

# Get application settings
f = open('settings.json', encoding='utf-8')
f_settings = f.read()
settings = json.loads(f_settings)
f.close()

irc = IRC(settings)
aijs = Aibot_JSON()

aijs.load()

irc.connect()


# bday_dict = {
#     'ayaka': '2016-11-14',
#     'sayaka': '2016-11-15',
#     'momoka': '2016-11-16'
# }


def get_birthdays(bdate):
    bday_idols = aijs.find_birthdays(bdate)
    last = len(bday_idols)
    bdstr = "Today is a birthday of "
    for idols in bday_idols[:-1]:
        bdstr += idols
        if last > 2 and idols != bday_idols[-2]:
            bdstr += ', '
    bdstr += ' and ' + bday_idols[-1]
    return bdstr

cmd_dict = {
    '!load': aijs.load(),
    '!quiz': 'quiz starting',
    '!time': date.today(),
    #'!bday': get_birthdays('{0:%m-%d}'.format(date.today()))
    "!bday": "placeholder"

}

while True:
    # sleep(0.1)
    text = irc.get_text().strip()
    print(text)
    text_a = text.split(bytes(' ', 'utf8'))
    if len(text_a) > 3 and text_a[3][1:2] == bytes("!", 'utf8'):
        cmd = text_a[3][1:]
        if str(cmd, 'utf8') in cmd_dict:
            irc.send(settings["irc"]["channel"], cmd_dict[str(cmd, 'utf8')])


