#import socket
#
#UDP_IP = "192.168.1.98"
#
#UDP_PORT = 5006
#
#sock = socket.socket(socket.AF_INET, # Internet
#
#socket.SOCK_DGRAM) # UDP
#
#sock.bind((UDP_IP, UDP_PORT))
#
#while True:
#  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#  print "received message:", data

import RPi.GPIO as GPIO
import socket
import time



def init():
    GPIO.setmode(GPIO.BOARD)
   
    GPIO.setup(37,GPIO.OUT)

init()
GPIO.output(37,False)

def relay(r_flag):
    print r_flag
    init()
    if(r_flag==0):
      GPIO.output(37,True)
      print("Bulb On")
    elif(r_flag==1):
      GPIO.output(37,False)
      print("Bulb Off")
    
   
      
UDP_IP = "192.168.1.98"

UDP_PORT = 5006

UDP_IP_sender = "192.168.1.80"



sockrecv = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP


socksend = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP

sockrecv.bind(('', UDP_PORT))

#socksend.bind((UDP_IP_sender, UDP_PORT_reply))
r_flag=0
while True:
    send_flag = 0
    pi2_flag=0
    data, addr = sockrecv.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    if data == '9':
      pi2_flag = 1
      print "Turning Bulb on"
      relay(r_flag)
      if(r_flag==0):
        r_flag = 1
      else: 
        r_flag = 0  

    else: 
      print "pass"  
    if(pi2_flag): 
      sockrecv.sendto(str(UDP_IP), (UDP_IP_sender, UDP_PORT))
      send_flag=1
    if(send_flag == 1):
      print "sent"
      
    
    

      
      
    




    
   