#Riley Johnston
#101088019
#SYSC 3010 Lab 2

#This program allows the user to navigate the 'curser' around the sense HAT display

import sense_hat

sense = sense_hat.SenseHat()
sense.clear()

X = [255, 0, 0]  # Red
O = [0, 0, 0]  # White
curserIndex = 0
display_curser = [
X, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

keyPressed = sense_hat.ACTION_PRESSED
sense.set_pixels(display_curser)

while True:
    events = sense.stick.get_events()
    if events:
      for event in events:
        if event.action != 'pressed':
            continue
        if event.direction == 'left':
            display_curser[curserIndex] = O
            #if (curserIndex >= 0):
            curserIndex -= 1
            display_curser[curserIndex] = X
        elif event.direction == 'right':
            display_curser[curserIndex] = O
            #if (curserIndex%8 <= 7):
            print(curserIndex)
            if (curserIndex == 63):
                curserIndex = -1
            curserIndex += 1
            display_curser[curserIndex] = X
        elif event.direction == 'down':
            display_curser[curserIndex] = O
            if (curserIndex <= 55):
                curserIndex += 8
            display_curser[curserIndex] = X
        elif event.direction == 'up':
            display_curser[curserIndex] = O
            if (curserIndex >= 8):
                curserIndex -= 8
            display_curser[curserIndex] = X
        
        sense.set_pixels(display_curser)
        
