from socket import *
rec=socket()
rec.connect(('192.168.56.1',5000))
msg1=rec.recv(1024)
msg2=rec.recv(1024)
msg3=rec.recv(1024)
msg4=rec.recv(1024)
li=[msg1.decode(),msg2.decode(),msg3.decode(),msg4.decode()]
print('List of binary values from server : ',li)
total=int(msg1.decode(),2)+int(msg2.decode(),2)+int(msg3.decode(),2)
total1=total+int(msg4.decode(),2)
binary=bin(total1)[2:]
flag=0
for i in binary:
    if(i=='0'):
        flag=0
        break
    else:
        flag=1
if(flag==0):
    print('Message received with error')
else:
    print('Message received without error')
rec.close()