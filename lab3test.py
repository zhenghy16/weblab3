from scapy.all import *
a=IP(src='59.66.130.21',dst='188.166.199.77',ttl=(1,10))/ICMP()
ans=sr(a)