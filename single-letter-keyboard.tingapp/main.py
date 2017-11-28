import tingbot
from tingbot import *
import pygame

# setup code here
screen.fill(color='black')
screen.text('Press a key', color='red')

@every(seconds=1.0/10)
def loop():
    # drawing code here
    if pygame.key.get_focused():
        press=pygame.key.get_pressed()
        for i in xrange(0,len(press)): 
            if press[i]==1:
                name=pygame.key.name(i) 
                if len(name) == 1:
                    screen.fill(color='black')
                    screen.text(name.upper(), color='blue', font_size=150)

tingbot.run()
