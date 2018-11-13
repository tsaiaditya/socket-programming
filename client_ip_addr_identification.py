from socket import *
s=socket(AF_INET,SOCK_STREAM)
port=12344
s.connect(('192.168.0.103',port))
msg=s.recv(1024)
string=str(msg)
string=string[2:]
string=string[::-1]
string=string[1:]
string=string[::-1]
print(string)
ip=input('Enter the ip to be sent : ')
s.send(ip.encode())
s.close()
