from scapy.all import *
port=18478
f=open('content.txt','rb')
s=f.read()
a=IP(src='59.66.130.21',dst='188.166.199.77')/TCP(sport=port,flags='S',dport=80)
a.show()    
ans=sr(a)
b=IP(src='59.66.130.21',dst='188.166.199.77')/TCP(sport=port,ack=ans[0][0][1][1].seq+1,seq=1,flags='A',dport=80)
ans2=sr(b)
