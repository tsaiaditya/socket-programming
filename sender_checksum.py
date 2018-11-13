from socket import *
temp=socket()
temp.bind(('192.168.56.1',5000))
temp.listen(5)
send,addr=temp.accept()
print('Got connection from : ',addr[0])
list_of_binary_values=[]
print('Enter 3 binary values : ')
msg1=input()
msg2=input()
msg3=input()
total=bin(int(msg1,2)+int(msg2,2)+int(msg3,2))[2:]
compliment=''
for i in total:
    if(i=='0'):
        compliment+='1'
    else:
        compliment+='0'
send.send(msg1.encode())
send.send(msg2.encode())
send.send(msg3.encode())
send.send(compliment.encode())
send.close()
temp.close()
