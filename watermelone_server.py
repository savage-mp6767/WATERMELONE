##  WATERMELONE  ##
##  SERVER BUILD ##
##  11/9/14      ##

import socket
import sys
import entities

#game client class. represents the client, not the player object.
class WMSClient:
    def __init__(self,connection,ip):
        self.connection = connection
        self.ipaddr = ip
        print '%s connected' % self.ipaddr

    def SetName(self,name):
        self.netname = name

class WMServer:
    def __init__(self):
        self.server_addr = ('localhost',12342)
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind(self.server_addr)
        self.connection.listen(5)
    
    def Update(self):
        print 'waiting for a connection'
        (c, client_address) = self.connection.accept()
        print str(client_address) + 'connected'
        self.Update()
		
server = WMServer()
server.Update()
