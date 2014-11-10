##  WATERMELONE  ##
##  SERVER BUILD ##
##  11/9/14      ##

import socket
import sys

class WMServer:
    def __init__(self):
        self.server_addr = ('localhost',1337)
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind(self.server_addr)
        self.connection.listen(5)
    
    def Update(self):
        print 'waiting for a connection'
        (connection, client_address) = self.connection.accept()
        thread = client_thread(connection)
        self.Update()
		
server = WMServer()
server.Update()