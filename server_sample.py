from socket import *
temp=socket()
temp.bind(('192.168.43.254',8000))
temp.listen(5)
connection,addr=temp.accept()
print('Got the connection from : ',addr[0])
msg1=connection.recv(1024)
msg2=connection.recv(1024)
a=int(msg1.decode())
b=int(msg2.decode())
if(a>b):
    connection.send(str(a).encode())
else:
    connection.send(str(b).encode())
connection.close()
temp.close()