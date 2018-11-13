from socket import *
temp=socket()
temp.bind(('192.168.56.1',8000))
temp.listen(5)
connection,addr=temp.accept()
print('Got the connection from : ',addr[0])
flag=1
while(flag==1):
    inp=input('Enter the message to be sent to client : ')
    connection.send(inp.encode())
    msg=connection.recv(1024)
    print('Message got from client : ',msg.decode())
    flag=int(input('Do you want to continue the connection (yes-1/no-0) : '))
    if(flag==0):
        connection.send('Finish'.encode())
print('Connection is done with the client.')
connection.close()
temp.close()