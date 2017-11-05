import CHIP_IO.GPIO as GPIO
import time

from inputs import get_key
from inputs import devices
for device in devices:
     print(device)

GPIO.setup("CSID4", GPIO.OUT, initial=1)
GPIO.setup("CSID6", GPIO.OUT, initial=1)

current_state=0
unlock_time=0

while True:
          print("current state: ", current_state)
          if ((time.time()-unlock_time) < 5.0): 
               GPIO.output("CSID4", GPIO.LOW)
               GPIO.output("CSID6", GPIO.LOW)
          else :
               GPIO.output("CSID4", GPIO.HIGH)
               GPIO.output("CSID6", GPIO.HIGH)
     
          events = get_key()
          for event in events:
               print(event.ev_type, event.code, event.state)
               if event.state==1 :
                    if current_state == 0 and event.code == 'KEY_D' :
                         current_state = 1
                    elif current_state == 1 and event.code == 'KEY_A' :
                         current_state = 2
                    elif current_state == 2 and event.code == 'KEY_N' :
                         current_state = 3
                         unlock_time = time.time()
                    else :
                         current_state = 0
