'''
Library created in order to mimic human like mouse movement. 
'''
#Used for needed mouse events
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
#Used for obtaining screen resolutoin and mouse position
from Quartz import CGDisplayBounds
from Quartz import CGMainDisplayID
from Quartz import CGDisplayPixelsHigh
import AppKit
#using pyweening as a base. Will eventuall write additonal tweening algorithims inclusing curved mouse movement.
from pytweening import *

import time
from random import randint

def _getPosition():
    '''
    Returns the current mouse position as integers in the format of (x,y)
    '''
    loc = AppKit.NSEvent.mouseLocation()
    return (int(loc.x), int(CGDisplayPixelsHigh(0) - loc.y))

def _getScreenSize():
    '''
    Returns the screen resolution as integers in the format of (width, height)
    '''
    screen = CGDisplayBounds(CGMainDisplayID())
    return (int(screen.size.width), int(screen.size.height))

def _createMouseEvent(source, posX, posY):
    '''
    Creates a moust event and adds it to the queue to be processed.
    '''
    event = CGEventCreateMouseEvent(
                    None, 
                    source, 
                    (posX, posY), 
                    kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event)
 
def _mouseMove(posX,posY):
    '''
    Instant mouse movement to the given coordinates.
    '''
    _createMouseEvent(kCGEventMouseMoved, posX,posY)

def _getNextPoint(x1, y1, x2, y2, n):
    '''
    Finds the difference between current and destination point and usses the tween (weight between 0 and 1)
    to pick where to place the next point inbetween the two given points. Uses Bresenham's line algorithim.
    '''
    x = (x2 - x1) * n + x1
    y = (y2 - y1) * n + y1
    return (x, y)

def mouseLeftClick():
    '''
    Cliks at the current mouse location
    '''
    posX, posY = _getPosition()
    _createMouseEvent(kCGEventLeftMouseDown, posX, posY)
    _createMouseEvent(kCGEventLeftMouseUp, postX, posY)

def moveTo(targetX, targetY, duration, tween):
    '''
    Moves to the given x,y coordinate
    targetX (int) is the desintation X coordination
    targetY (int) is the destination Y coordination
    duration (float/double) is the ammount of time in seconds you want to add to the mouse's travel time
    tween (float/double) is a weight from 0 to 1 that determines where the next pixel is.
    '''
    startX, startY = _getPosition()
    width, height = _getScreenSize()
    numOfSteps = max(width, height)
    
    if duration == None or duration <=0:
        sleepAmmount = 0
    else:
        sleepAmmount = duration/numOfSteps
    
    for i in range(numOfSteps):
        x,y =_getNextPoint(startX, startY, targetX, targetY, tween(i/numOfSteps))
        _mouseMove(x,y)
        time.sleep(sleepAmmount)
        
    _mouseMove(targetX, targetY) #Ensures you finish at the target            

#just used for testing
def main():
    start = time.time()
    
    print(_getPosition())
    moveTo(900,900,0, linear)
    moveTo(10,10, 1, easeInQuad)
    
    end = time.time()
    print(end-start)
    print("done")
    print(_getPosition())

main()
