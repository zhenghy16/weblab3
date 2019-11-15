from scapy.all import *
a = TCP_SERVICE
a.send(HTTPRequest())
a.recv()