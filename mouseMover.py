## Human like mouse movement
import pyautogui
import time
import random

pyautogui.MINIMUM_DURATION = 0
#pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0

## Move to exact coordinate
def moveMouse(targetX, targetY, givenCords = True):
    currentX, currentY = pyautogui.position()
    
    if givenCords == False: #gets coordinates input from user
        print("Enter the x coordinatie and y in in this format x,y")
        targetX, targetY = input().split(',')

    moves = random.randint(3, 8)
    print(moves)
    start = time.time()
    
    while moves > 0:
        deltaX = ((targetX - currentX) / moves ) ##random movement of 8 in either direction
        deltaY = ((targetY - currentY) / moves ) 
        currentX = currentX + deltaX
        currentY = currentY + deltaY
        pyautogui.moveTo(currentX, currentY, 0.1, pyautogui.easeInQuad)
        moves = moves - 1

    print(pyautogui.position())   
    end = time.time()
    print(end - start)

def checkCoordinate(targetX, targetY):
    currentX, currentY = pyautogui.position()
    if (currentX == targetX and currentY == targetY):
        return True
    else:
        return False


def main():
    moveMouse(10,10)
    print("Done")
    
main()
