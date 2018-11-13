from socket import *
s=socket(AF_INET,SOCK_STREAM)
print('Socket success')
port=12344
s.bind(('',port))
print('socket binded to : ',port)
s.listen(5)
print('socket listening')
c,addr=s.accept()
print('got connection from : ',addr)
c.send(b'Thank you')
ip_addr=c.recv(1024)
print('msg from client : ',ip_addr)
type(ip_addr)
ip=str(ip_addr)
ip=ip[2:]
ip=ip[::-1]
ip=ip[1:]
ip=ip[::-1]
ip_addr_numbers=ip.split('.')
flag=0
for i in ip_addr_numbers:
    if(len(i)==1):
        flag=0
    elif(len(i)>=2):
        if(i[0]=='0'):
            flag=1
            break
    number=int(i)
    if(number>255 or number<0):
        flag=1
        break
if(flag==1):
    print('The IP Address sent was Invalid or does not follow the format.')
else:
    print('The IP Address sent was Valid and followed the format.')
    x=int(ip_addr_numbers[0])
    if(x>=0 and x<=127):
        print('The IP Address belongs to class A.')
    elif(x>=128 and x<=191):
        print('The IP Address belongs to class B.')
    elif(x>=192 and x<=223):
        print('The IP Address belongs to class C.')
    elif(x>=224 and x<=251):
        print('The IP Address belongs to class D.')
    elif(x>=252 and x<=255):
        print('The IP Address belongs to class E.')
c.close()