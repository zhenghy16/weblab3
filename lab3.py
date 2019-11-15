from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(('188.166.199.77', 80))
f=open('content.txt','rb')
data=f.read()
sendData = data

s.send(sendData)

ret = s.recv(1024)

print(ret.decode('utf-8'))
f.close()
s.close()