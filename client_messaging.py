from socket import *
receive=socket()
receive.connect(('192.168.56.1',8000))
msg=receive.recv(1024)
while(msg.decode()!='Finish'):
    print('Message received from the server : ',msg.decode())
    msg=input('Enter the message to be sent to the server : ')
    receive.send(msg.encode())
    msg=receive.recv(1024)
print('Connection done with server.')
receive.close()