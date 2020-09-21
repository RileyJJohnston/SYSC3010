#Riley Johnston
#101088019
#SYSC 3010 Lab 2

import sense_hat

sense = sense_hat.SenseHat()
sense.clear()

initials = ['R','J']
index = 0

upKey = sense_hat.DIRECTION_UP
keyPressed = sense_hat.ACTION_PRESSED

while True:
    events = sense.stick.get_events()
    if events:
      for event in events:
        if event.action != 'pressed':
            continue
        if event.direction == 'left':
            print(initials[index%2])
        elif event.direction == 'right':
            print(initials[index%2])
        elif event.direction == 'down':
            print(initials[index%2])
        elif event.direction == 'up':
            print(initials[index%2])
        index+=1
