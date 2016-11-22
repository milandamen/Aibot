import socket


class IRC:
    irc = socket.socket()
    settings = None

    def __init__(self, settings):
        #self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.settings = settings

    def send(self, chan, msg):
        # print('sending..')
        # self.irc.send(bytes("PRIVMSG %s :test message\n" % self.settings["channel"], 'utf8'))
        self.irc.send(bytes("PRIVMSG %s :%s\n" % (chan, msg), 'utf8'))

    def connect(self):
        settings = self.settings["irc"]
        
        # defines the socket
        print("connecting to: " + settings["server"])
        self.irc.connect((settings["server"], 6667))  # connects to the server

        self.irc.send(bytes("NICK %s\n" % settings["nickname"], 'utf8'))
        self.irc.send(bytes("USER %s %s Ibot :%s\n" % (settings["nickname"], settings["nickname"], settings["nickname"]), 'utf8'))
        self.irc.send(bytes("JOIN %s\n" % settings["channel"], 'utf8'))
        self.irc.send(bytes("PRIVMSG NickServ IDENTIFY %s %s\n" % (settings["nickname"], settings["password"]), 'utf8'))
        self.irc.send(bytes("PRIVMSG %s :Hello Master\n" % settings["channel"], 'utf8'))

    def get_text(self):
        text = self.irc.recv(2040)  # receive the text

        if text.find(bytes('PING', 'utf8')) != -1:
            self.irc.send(bytes('PONG ' + str(text.split()[1], 'utf8') + 'rn', 'utf8'))

        return text
