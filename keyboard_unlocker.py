while True:
     events = get_key()
     for event in events:
          print(event.ev_type, event.code, event.state)
          if event.state==1 :
               if current_state == 0 and event.code == 'KEY_1' :
                    current_state = 1
               elif current_state == 1 and event.code == 'KEY_2' :
                    current_state = 2
               elif current_state == 2 and event.code == 'KEY_3' :
                    current_state = 3
               else :
                    current_state = 0
                    
     print('Current state: ', current_state)
     
     if current_state == 3 : 
          GPIO.output("CSID6", GPIO.LOW)
     else :
          GPIO.output("CSID6", GPIO.HIGH)
