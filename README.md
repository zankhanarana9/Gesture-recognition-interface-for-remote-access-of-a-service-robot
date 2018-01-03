# Gesture-recognition-interface-for-remote-access-of-a-service-robot
Hand gesture controlled rover that lifts and moves objects using raspberry pi (Python programming)

src
--handGesture
  --datacollection.py
  --dataset.py
  --traingest.py
  --predictgest.py  
--controllingallmotors.py
--receive.py

predictgest.py in the folder handGesture does the image processing using CNN. 
It takes hand gesture as an input and returns the index of the most probable gesture read.

controllingallmotors.py takes in the index value as the parameter passed by the code above and runs the rover as specified 
in the code.

receive.py takes in the index value as the parameter passed by the code above and runs the bulb to switch on/off.


Steps to execute:

1. Run  controllingallmotors.py and receive.py as servers ready to listen.
2. Run predictgest.py which reads gesture and multicasts index value corresponding to a pre-defined gesture.
