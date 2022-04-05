import socket
import threading
import os
from random import randint

host = '10.3.141.1'                                              
port = 8881
format = "utf-8"
client = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

def handle_client(connection, address):
	print(f'Client {address} connected')
	connected = True
	while connected:
		message = connection.recv(1024).decode(format)
		if message == "A toi":
			mon_coup = randint(1,3)
			#print(f'mon coup : {mon_coup}')
			connection.send(str(mon_coup).encode(format))
		elif message == "quit":
			connected = False
			
def start():
	s.listen()
	connected = True
	client = None
		
	while connected:
		c, addr = s.accept()
		if client is not None:
			c.send('Server full'.encode(format))
		else:
			client = c
			c.send('accepted'.encode(format))	
			thread = threading.Thread(target=handle_client, args=(c, addr))
			thread.start()
	c.close()

start()
os._exit(0)
	
	
