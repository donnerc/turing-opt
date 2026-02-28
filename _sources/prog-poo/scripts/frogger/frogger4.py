from gamegrid import *
from soundsystem import *

# ---------------- class Frog ----------------
class Frog(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/frog.gif")

    def collide(self, actor1, actor2):
        global nbHit
        nbHit += 1
        openSoundPlayer("wav/boing.wav")
        play()
        self.setLocation(Location(400, 560))
        return 0

    def act(self):
        global nbSuccess
        if self.getY() < 15:
            nbSuccess += 1
            openSoundPlayer("wav/notify.wav")
            play()
            self.setLocation(Location(400, 560))
 
# ---------------- class Car ----------------
class Car(Actor):
    def __init__(self, path):
        Actor.__init__(self, path)
    
    def act(self):
        self.move()
        if self.getX() < -100:
            self.setX(1650)
        if self.getX() > 1650:
            self.setX(-100)

def initCars():
    for i in range(20):
        car = Car("sprites/car" + str(i) + ".gif")
        frog.addCollisionActor(car)
        if i < 5:
            addActor(car, Location(350 * i, 90), 0)
        if i >= 5 and i < 10:
            addActor(car, Location(350 * (i - 5), 220), 180)
        if i >= 10 and i < 15:
            addActor(car, Location(350 * (i - 10), 350), 0)
        if i >= 15:
            addActor(car, Location(350 * (i - 15), 470), 180)

def keyCallback(keyCode):
    if keyCode == 37: # left
        frog.setX(frog.getX() - 5)
    elif keyCode == 38: # up
        frog.setY(frog.getY() - 5)
    elif keyCode == 39: # right
        frog.setX(frog.getX() + 5)
    elif keyCode == 40: # down
        frog.setY(frog.getY() + 5)

makeGameGrid(800, 600, 1, None, "sprites/lane.gif", False, 
             keyRepeated = keyCallback)
setSimulationPeriod(50)
setTitle("Frogger")
frog = Frog()
addActor(frog, Location(400, 560), 90)
initCars()
show()
doRun()

# Game supervision
maxNbLifes = 3
nbHit = 0
nbSuccess = 0
while not isDisposed():   
    if nbHit + nbSuccess == maxNbLifes:  # game over
        addActor(Actor("sprites/gameover.gif"), Location(400, 285))
        removeActor(frog)
        doPause()
    setTitle("#Success: " + str(nbSuccess) + " #Hits " + str(nbHit))
    delay(100)

