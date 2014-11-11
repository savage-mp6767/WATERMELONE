##  WATERMELONE  ##
##  SERVER BUILD ##
##  11/9/14      ##

import socket
import sys

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
