import socket

#create a socket object
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get local machine name
host=socket.gethostbyname("127.0.0.1") 
port=1234

#bind to the port
serversocket.bind((host,port))

#queue up to 5 request
serversocket.listen(5)

while True:
	#establish a connection
	clientsocket,addr=serversocket.accept()
	print("Got a connection from %s" %str(addr))
	msg="Thank you for connection"+"\r\n"
	clientsocket.send(msg.encode('ascii'))
	clientsocket.close()

