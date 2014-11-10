##  WATERMELONE  ##
##  CLIENT BUILD ##
##  11/9/14      ##

import socket
import sys
from Tkinter import *

root = Tk()

class MyApp:
    def __init__(self, parent):
        self.drawpad = Canvas(root, width=480,height=320, background='white') #TODO: width and height based on user-set options. (config.cfg?)
        self.server_addr = ('localhost',12342)
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect(self.server_addr)
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.drawpad.pack(side=BOTTOM)
    
    def Update(self):
        try:
            message = 'This is the message.  It will be repeated.'
            print 'sending ' + message
            self.connection.send(message)
            # Look for the response
            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
                data = self.connection.recv(16)
                amount_received += len(data)
                print 'received ' + data
        finally:
            print 'closing socket'
            self.connection.close()
        self.Update()
		
myapp = MyApp(root)
root.mainloop()