##  WATERMELONE  ##
##  SERVER BUILD ##
##  11/9/14      ##

import socket
import sys
import threading

class ClientThread ( threading.Thread ):
   # Override Thread's __init__ method to accept the parameters needed:
   def __init__ ( self, channel, details ):
      self.channel = channel
      self.details = details
      threading.Thread.__init__ ( self )

   def run ( self ):
      print 'Received connection:', self.details [ 0 ]
      for x in xrange ( 10 ):
         data = self.channel.recv ( 1024 )
         if not data:
             break
         else:
             print data
      self.channel.close()
      print 'Closed connection:', self.details [ 0 ]
   
   def sendData(self,data):
       self.channel.send(data)

class WMServer:
    def __init__(self):
        self.server_addr = ('localhost',12347)
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind(self.server_addr)
        self.connection.listen(5)
        self.Update()
        self.clients = []
    
    def Update(self):
        channel, details = self.connection.accept()
        ClientThread ( channel, details ).start()
        self.Update()
    
    def GetClients(self):
        return self.clients
		
server = WMServer()