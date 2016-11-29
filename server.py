from socket import *  
from time import ctime  
import binascii


HOST = '127.0.0.1'  
PORT = 21567  
BUFSIZE = 1024  
  
ADDR = (HOST,PORT)  
  
udpSerSock = socket(AF_INET, SOCK_DGRAM)  
udpSerSock.bind(ADDR)  
i = 0
while True:  
    print 'wating for message...'  
    data, addr = udpSerSock.recvfrom(BUFSIZE)   
    i += 1
    # print binascii.b2a_hex(data) 
udpSerSock.close()  