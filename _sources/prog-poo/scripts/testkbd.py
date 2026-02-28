from gamegrid import *

def pressCallback(e):
    print "Press: ", e.getKeyCode()

def releaseCallback(e):
    print "Release: ", e.getKeyCode()

makeGameGrid(800, 600, 1, None, "sprites/lane.gif", False, 
             keyPressed = pressCallback,
             keyReleased = releaseCallback)
show()

