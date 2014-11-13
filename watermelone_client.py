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
        self.server_addr = ""
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        print "Init Networking"
        
    def NetUpdate(self):
        print 'receiving net message'
        while True:
            content = self.connection.recv(1024)
            if not content:
                break
            else:
                print content

    def NetSetServerInfo(self,addr,port):
        self.server_addr = (addr,port)

    def NetConnect(self):
        if not self.connected:
            try:
                self.connection.connect(self.server_addr)
                print 'Connected to' + str(self.server_addr)
                self.connected = True
            except:
                print 'ERROR: Could not connect to server at ', str(self.server_addr)
        else:
            print 'Already connected.'

    def NetDisconnect(self):
        if self.connected:
            self.connection.close()
            print "Disconnected"

class WMClient:
    def __init__(self, parent):
        #UI elements
        self.drawpad = Canvas(root, width=480,height=320, background='white') #TODO: width and height based on user-set options. (config.cfg?)
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.drawpad.pack(side=BOTTOM)
        
        self.Network = WMCNetworking()
        self.Network.NetSetServerInfo('localhost',12737)
        self.Network.NetConnect()
        
        #begin update loop
        self.drawpad.after(2,self.Update)
    
    def Update(self):
        #update network stuff
        self.Network.NetUpdate()

if __name__ == "__main__":
    myapp = WMClient(root)
    root.mainloop()
    if sys.platform == 'win32':
        import win32_sysinfo as sysinfo
    print "WATERMELONE"
    print "OS - ", sys.platform
    print 'Memory available:', sysinfo.memory_available()
    
    
