#from Quartz.CoreGraphics import *
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp

#using pyauto gui temp to get it running at first
from pyautogui import position as getPosition 
from pyautogui import size as getScreenSize

from random import randint

#using pyweening as a base. Will eventuall write additonal tweening algorithims inclusing curved mouse movement.
from pytweening import linear 

import time #for testing

def createMouseEvent(source, posX, posY):
    event = CGEventCreateMouseEvent(
                    None, 
                    source, 
                    (posX, posY), 
                    kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event)
 
def mouseMove(posX,posY):
    createMouseEvent(kCGEventMouseMoved, posX,posY)

def mouseLeftClick():
    ##clicks at the current position the mouse is at
    posX, posY = getPosition()
    createMouseEvent(kCGEventLeftMouseDown, posX, posY)
    createMouseEvent(kCGEventLeftMouseUp, postX, posY)

def moveTo(targetX, targetY, duration, tween):
    '''Moves to the given x,y coordinate
    targetX (int) is the desintation X coordination
    targetY (int) is the destination Y coordination
    duration (float/double) is the ammount of time in seconds you want to add to the mouse's travel time
    tween (not implemented yet)'''
    startX, startY = getPosition()
    width, height = getScreenSize()

    numOfSteps = max(width, height) ##should be changed and randomized
    if duration == None or duration <=0:
        sleepAmmount = 0
    else:
        sleepAmmount = duration/numOfSteps
    
    steps = [(startX, startY)]

    for i in range(numOfSteps):
        steps.append(getNextPoint(startX, startY, targetX, targetY, tween(i/numOfSteps)))
        pass
                     
    steps.append(targetX, targetY)
    
    for x, y in steps:
        moveMouse(x,y)
        time.sleep(sleepAmmount)

def getNextPoint(x1, y1, x2, y2, n):
    pass

def main():
    start = time.time()
    
    print(getPosition())
    mouseMove(10,10)
    
    end = time.time()
    print(end-start)
    print("done")

main()
