from gamegrid import *
import random

# ---------------- class Alien ----------------
class Alien(Actor):

    # variable de classe
    nb_alien_atterri = 0

    def __init__(self):
        Actor.__init__(self, "sprites/alien_0.gif")

    def act(self):
        self.move()

        if self.getY() == 9:
            landedAlien = LandedAlien()
            addActor(landedAlien, Location(self.getX(), 9))

            try:
                free_columns.remove(self.getX())
            except:
                pass

            Alien.nb_alien_atterri += 1
            setStatusText(
                "Nombre d'aliens qui ont atterri : {n}".format(
                    str(Alien.nb_alien_atterri)
                )
            )


class LandedAlien(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/alien_1.gif")


def pressCallback(e):
    location = toLocationInGrid(e.getX(), e.getY())
    actor = getOneActorAt(location)
    if actor != None:
        removeActor(actor)
    refresh()


makeGameGrid(
    10, 10, 60, Color.red, "sprites/town.jpg", False, mousePressed=pressCallback
)
setSimulationPeriod(100)
addStatusBar(30)
setStatusText("Nombre d'aliens qui ont atterri : " + str(0))
show()
doRun()

free_columns = list(range(10))

while not isDisposed():
    alien = Alien()
    try:
        addActor(alien, Location(random.choice(free_columns), 0), 90)
    except:
        setStatusText("Game over !!!")
    delay(1000)
