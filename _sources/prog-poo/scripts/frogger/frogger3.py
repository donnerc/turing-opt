from gamegrid import *

# ---------------- Constantes clavier --------
K_LEFT      = 37
K_UP        = 38
K_RIGHT     = 39
K_DOWN      = 40

# ---------------- classe Frog ---------------
class Frog(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/frog.gif")

    def collide(self, actor1, actor2):
        self.setLocation(Location(400, 560))
        return 0

# ---------------- classe Car ---------------
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
            addActor(car, Location(350 * i, 100), 0)
        if i >= 5 and i < 10:
            addActor(car, Location(350 * (i - 5), 220), 180)
        if i >= 10 and i < 15:
            addActor(car, Location(350 * (i - 10), 350), 0)
        if i >= 15:
            addActor(car, Location(350 * (i - 15), 470), 180)

def keyCallback(keyCode):
    if keyCode == K_LEFT:
        frog.setX(frog.getX() - 5)
    elif keyCode == K_UP:
        frog.setY(frog.getY() - 5)
    elif keyCode == K_RIGHT:
        frog.setX(frog.getX() + 5)
    elif keyCode == K_DOWN:
        frog.setY(frog.getY() + 5)


makeGameGrid(800, 600, 1, None, "sprites/lane.gif", False, 
             keyRepeated = keyCallback)
setSimulationPeriod(50);
frog = Frog()
addActor(frog, Location(400, 560), 90)
initCars()
show()
doRun()