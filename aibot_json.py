import json


class Aibot_JSON:

    data = ""

    @staticmethod
    def load():
        fi = open('bday.json', encoding='utf-8')
        g = fi.read()
        global data
        data = json.loads(g)
        fi.close()

    @staticmethod
    def find_birthdays(theday):
        bd = []
        for idol in data:
            if idol['birthday'][5:] == theday:
                bd.append(idol['surname'] + ' ' + idol['name'] + ' (' + idol['group'] + ')')
        return bd