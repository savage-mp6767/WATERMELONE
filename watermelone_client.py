##  WATERMELONE  ##
##  CLIENT BUILD ##
##  11/9/14      ##

import socket
import sys
from Tkinter import *

root = Tk()

class WMCNetworking():
    def __init__(self):
        #server connection
        self.server_addr = ('localhost',12347)
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect(self.server_addr)
        print 'connected to' + str(self.server_addr)
        
    def NetUpdate(self):
        print 'receiving net message'
        while True:
            content = self.connection.recv(1024)
            if not content:
                break
            else:
                print content

class MyApp:
    def __init__(self, parent):
        #UI elements
        self.drawpad = Canvas(root, width=480,height=320, background='white') #TODO: width and height based on user-set options. (config.cfg?)
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.drawpad.pack(side=BOTTOM)
        
        self.Network = WMCNetworking()
        
        #begin update loop
        self.Update()
    
    def Update(self):
        #update network stuff
        self.Network.NetUpdate()
		
myapp = MyApp(root)
root.mainloop()