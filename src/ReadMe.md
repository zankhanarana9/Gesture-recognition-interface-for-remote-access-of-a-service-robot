!--READ ME--!

folder structure

src
--Raj's folder
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


