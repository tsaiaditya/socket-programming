import hashlib
valid_ip_addrs=['192.168.5.100','192.168.0.201','172.16.13.209','172.21.25.69','191.220.200.60']
hash_table=[]
for i in valid_ip_addrs:
    o=hashlib.md5(i.encode())
    hash_table.append(o.hexdigest())
for i in range(0,len(valid_ip_addrs)):
    print(hash_table[i])

incoming_ip_addr=input('Enter the IP address requesting to connect : ')
p=hashlib.md5(incoming_ip_addr.encode())
if(p.hexdigest() in hash_table):
    print('Valid IP connection.')
else:
    print('Invalid IP connection.')