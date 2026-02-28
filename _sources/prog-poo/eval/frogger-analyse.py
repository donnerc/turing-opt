from gamegrid import *
from soundsystem import *

import time
import random

class FroggerGame(object):

    K_LEFT      = 37
    K_UP        = 38
    K_RIGHT     = 39
    K_DOWN      = 40

    def __init__(self):

        self.nb_succes = 0
        self.max_temps = 15
        self.temps_restant = self.max_temps
        self.is_game_over = False
        
        makeGameGrid(800, 600, 1, None, "sprites/lane.gif", False, 
             keyRepeated = self.keyCallback)
        setSimulationPeriod(50);
        self.frog = Frog()
        addActor(self.frog, Location(400, 560), 90)
        self.initCars()
        show()
        doRun()
        self.manager()

    def manager(self):
        while not isDisposed() and not self.is_game_over:
            t0 = time.time()
            if self.frog.vies == 0:
                self.gameover()

            infos = '#Vies : {vies} // ' + \
            		'#Succès : {success} // ' + \
            		'#Points : {points} // ' + \
            		'Temps restant : {temps}'
            infos = infos.format(vies=self.frog.vies,
                                 success=self.nb_succes,
                                 points=self.frog.points,
                                 temps=self.frog.temps_restant)
            setTitle(infos)
            delay(100)

            t1 = time.time()
            print(t1-t0)
            self.frog.temps_restant -= (t1 - t0)

            if self.frog.temps_restant <= 0:
                self.frog.reset()
                self.frog.points -= 10
            
    def initCars(self):
        speeds = [9, 10, 11, 12]
        random.shuffle(speeds)
        for i in range(20):
            car = Car("sprites/car" + str(i) + ".gif")
            self.frog.addCollisionActor(car)
            
            if i < 5:
                addActor(car, Location(350 * i, 100))
                car.speed = speeds[0]
            if i >= 5 and i < 10:
                addActor(car, Location(350 * (i - 5), 220))
                car.speed = -speeds[1]
            if i >= 10 and i < 15:
                addActor(car, Location(350 * (i - 10), 350))
                car.speed = speeds[2]
            if i >= 15:
                addActor(car, Location(350 * (i - 15), 470))
                car.speed = -speeds[3]
    
    def keyCallback(self, keyCode):
        if keyCode == FroggerGame.K_LEFT:
            self.frog.setX(self.frog.getX() - 5)
        elif keyCode == FroggerGame.K_UP:
            self.frog.setY(self.frog.getY() - 5)
        elif keyCode == FroggerGame.K_RIGHT:
            self.frog.setX(self.frog.getX() + 5)
        elif keyCode == FroggerGame.K_DOWN:
            self.frog.setY(self.frog.getY() + 5)
            
        if self.frog.hasSucceeded():
            self.nb_succes += 1
            self.frog.points += 5
            self.frog.max_temps -= 1
            openSoundPlayer("wav/notify.wav")
            play()
            self.frog.reset()
            

    def gameover(self):
        addActor(Actor("sprites/gameover.gif"), Location(400, 285))
        removeActor(self.frog)
        self.is_game_over = True
        doPause()
        

class Frog(Actor):
    def __init__(self, vies = 3):
        Actor.__init__(self, "sprites/frog.gif")
        self.vies = vies
        self.points = 0
        self.max_temps = 15
        self.temps_restant = self.max_temps
        
    def collide(self, actor1, actor2):
        openSoundPlayer("wav/boing.wav")
        play()
        self.reset()
        self.vies -= 1
        self.points -= 5    
        return 0

    def hasSucceeded(self):
        return self.getY() < 20

    def reset(self):
        self.setLocation(Location(400, 560))
        self.temps_restant = self.max_temps

class Car(Actor):
    def __init__(self, path, speed=10):
        Actor.__init__(self, path)
        self.speed = speed
    
    def act(self):
        self.move()
        if self.getX() < -100:
            self.setX(1650)
        if self.getX() > 1650:
            self.setX(-100)

    def move(self):
        self.setX(self.getX() + self.speed)

game = FroggerGame()
