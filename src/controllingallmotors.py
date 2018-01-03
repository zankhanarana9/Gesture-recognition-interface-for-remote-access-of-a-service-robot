import RPi.GPIO as GPIO
import socket
import time



def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    GPIO.setup(40,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    
def m1m2rev(tf):
    init()
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(38,True)
    GPIO.output(40,False)
    GPIO.output(21,False)
    GPIO.output(23,False)
    time.sleep(tf)
    GPIO.cleanup()
    
def m1m2fwd(tf):
    init()
    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(38,False)
    GPIO.output(40,True)
    GPIO.output(21,False)
    GPIO.output(23,False)
    time.sleep(tf)
    GPIO.cleanup()

def m2rev(tf):
    init()
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(38,False)
    GPIO.output(40,False)
    GPIO.output(21,False)
    GPIO.output(23,False)
    time.sleep(tf)
    GPIO.cleanup()

def m2fwd(tf):
    init()
    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(38,False)
    GPIO.output(40,False)
    GPIO.output(21,False)
    GPIO.output(23,False)
    time.sleep(tf)
    GPIO.cleanup()
def m1rev(tf):
    init()
    GPIO.output(38,True)
    GPIO.output(40,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(21,False)
    GPIO.output(23,False)
    time.sleep(tf)
    GPIO.cleanup()

def m1fwd(tf):
    init()
    GPIO.output(38,False)
    GPIO.output(40,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(21,False)
    GPIO.output(23,False)
    time.sleep(tf)
    GPIO.cleanup()
def m3fwd(tf):
    init()
    GPIO.output(21,True)
    GPIO.output(23,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(38,False)
    GPIO.output(40,False)
    time.sleep(tf)
    GPIO.cleanup()

def m3rev(tf):
    init()
    GPIO.output(21,False)
    GPIO.output(23,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(38,False)
    GPIO.output(40,False)
    time.sleep(tf)
    GPIO.cleanup()

      
UDP_IP = "192.168.1.87"

UDP_PORT = 5006

UDP_IP_sender = "192.168.1.80"
#UDP_PORT_reply = 6789


sockrecv = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP


socksend = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP

sockrecv.bind((UDP_IP, UDP_PORT))

#socksend.bind((UDP_IP_sender, UDP_PORT_reply))
r_flag=0
while True:
    send_flag = 0
    pi1_flag=1
    data, addr = sockrecv.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    if data == '1':
      print "Gripper open"
      m3fwd(4)
    elif data== '2':  
      print "Gripper Close"
      m3rev(3)
    elif data == '3':
      print "Right rev"
      m1rev(0.5)
    elif data == '4':
      print "Right fwd"
      m1fwd(0.5)
    elif data == '5':
      print "Left rev"
      m2rev(0.5)
    elif data == '6':
      print "Left fwd"
      m2fwd(0.5)
    elif data == '7':
      print "Both Fwd"
      m1m2fwd(5)
    elif data == '8':
      print "Both Rev"
      m1m2rev(5)
    elif data == '9':
      print "pi 2 working"
      pi1_flag = 0
    else: 
      print "pass"  
    if(pi1_flag): 
      sockrecv.sendto(str(UDP_IP), (UDP_IP_sender, UDP_PORT))
      send_flag=1
    if(send_flag == 1):
      print "sent"
      
    
    

      
      
    



