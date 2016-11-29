from scapy.all import *
from socket import *  
import sys

HOST = '127.0.0.1'  
PORT = 21567    
ADDR = (HOST, PORT)  

if (len(sys.argv) == 1):
	print "Please input pcap file directory"
else:
	pcap = rdpcap(sys.argv[1])
	print "%d frames loaded"%len(pcap)
	for index,packet in enumerate(pcap):
		try:
			data = packet['Raw'].load
			udpCliSock = socket(AF_INET, SOCK_DGRAM)  
			udpCliSock.sendto(data,ADDR)   
		except: 
			print "%d frame has no raw data"%index
	udpCliSock.close()  

