Sprites animés, patrons de conception en POO
############################################

..  contents:: Contenu de la page
    :depth: 3


..  admonition:: lecture
    :class: warning

    TigerJython :
    https://programmierkonzepte.ch/franz/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=gamegrid/spriteanimation.inc.php


Objectifs
=========

Cette partie apporte un complément au cours TigerJython par le biais d'une
analyse de code, compétence essentielle pour bien appréhender l'oral de BAC.

Les éléments développés dans cette sections sont les suivants

* Animation de sprites en mettant en mémoire tampon plusieurs sprites ainsi que leurs rotations
* Utilisation de classes intermédiaires pour éviter la duplication de code
* Pattron Singleton
* Pattron fabrique pour créer des objets dynamiquement

Code à analyser
===============

..  code-block:: python
    :linenos:

    from gamegrid import *
    import random
    import math

    # ---------- class Fruit ------------------------
    class Fruit(Actor):
        def  __init__(self, spriteImg, vx):
            Actor.__init__(self, True, spriteImg, 2)
            self.vx = vx
            self.vy = 0
            self.isSliced = False

        def reset(self): # Called when Fruit is added to GameGrid
            self.px = self.getX()
            self.py = self.getY()

        def act(self):
            self.movePhysically()
            self.turn(10)

        def movePhysically(self):
            self.dt = 0.002 * getSimulationPeriod()
            self.vy = self.vy + g * self.dt
            self.px = self.px + self.vx * self.dt
            self.py = self.py + self.vy * self.dt
            self.setLocation(Location(int(self.px), int(self.py)))
            self.cleanUp()

        def cleanUp(self):
            if not self.isInGrid():
                if not self.isSliced:
                    FruitFactory.nbMissed += 1
                self.removeSelf()

        def sliceFruit(self):
            if not self.isSliced:
                self.isSliced = True
                self.show(1)
                FruitFactory.nbHit += 1

        def collide(self, actor1, actor2):
           actor1.sliceFruit()
           return 0

    # ------ class Melon -----------
    class Melon(Fruit):
        def __init__(self, vx):
            Fruit.__init__(self, "sprites/melon.gif", vx)

    # ------ class Orange -----------
    class Orange(Fruit):
        def __init__(self, vx):
            Fruit.__init__(self, "sprites/orange.gif", vx)

    # ------ class Strawberry -----------
    class Strawberry(Fruit):
        def __init__(self, vx):
            Fruit.__init__(self, "sprites/strawberry.gif", vx)

    # ------------------- class FruitFactory -------------------
    class FruitFactory(Actor):
        myCapacity = 0
        myFruitFactory = None
        nbGenerated = 0
        nbMissed = 0
        nbHit = 0

        @staticmethod
        def create(capacity, slowDown):
            if FruitFactory.myFruitFactory == None:
                FruitFactory.myCapacity = capacity
                FruitFactory.myFruitFactory = FruitFactory()
                FruitFactory.myFruitFactory.setSlowDown(slowDown)
            return FruitFactory.myFruitFactory

        def act(self):
            self.createRandomFruit()

        @staticmethod
        def createRandomFruit():
            if FruitFactory.nbGenerated == FruitFactory.myCapacity:
                return
            vx = -(random.random() * 20 + 30)
            fruitClass = random.choice([Melon, Orange, Strawberry])
            fruit = fruitClass(vx)
            FruitFactory.nbGenerated += 1
            y = int(random.random() * screenHeight / 2)
            addActorNoRefresh(fruit, Location(screenWidth-50, y), 180)
            # for a new fruit, the collision partners are all existing darts
            fruit.addCollisionActors(getActors(Dart))

    # ------------------- class Crossbow -----------------------
    class Crossbow(Actor):
        def __init__(self):
            Actor.__init__(self, True, "sprites/crossbow.gif", 2)

    # ------ class Dart ----------------
    class Dart(Actor):
        def __init__(self, speed):
            Actor.__init__(self, True, "sprites/dart.gif")
            self.speed = speed
            self.dt = 0.005 * getSimulationPeriod()

        # Called when actor is added to GameGrid
        def reset(self):
            self.px = self.getX()
            self.py = self.getY()
            dx = math.cos(math.radians(self.getDirectionStart()))
            self.vx = self.speed * dx
            dy = math.sin(math.radians(self.getDirectionStart()))
            self.vy = self.speed * dy

        def act(self):
            if isGameOver:
                return
            self.vy = self.vy + g * self.dt
            self.px = self.px + self.vx * self.dt
            self.py = self.py + self.vy * self.dt
            self.setLocation(Location(int(self.px), int(self.py)))
            self.setDirection(math.degrees(math.atan2(self.vy, self.vx)))
            if not self.isInGrid():
                self.removeSelf()
                crossbow.show(0) # Load crossbow

        def collide(self, actor1, actor2):
            actor2.sliceFruit()
            return 0

    # ------ End of class definitions --------------------

    def keyCallback(e):
        code = e.getKeyCode()
        if code == KeyEvent.VK_UP:
            crossbow.setDirection(crossbow.getDirection() - 5)
        elif code == KeyEvent.VK_DOWN:
            crossbow.setDirection(crossbow.getDirection() + 5)
        elif code == KeyEvent.VK_SPACE:
            if isGameOver:
                return
            if crossbow.getIdVisible() == 1: # Wait until crossbow is loaded
                return
            crossbow.show(1) # crossbow is released
            dart = Dart(100)
            addActorNoRefresh(dart, crossbow.getLocation(), crossbow.getDirection())
            # for a new dart, the collision partners are all existing fruits
            dart.addCollisionActors(getActors(Fruit))


    FACTORY_CAPACITY = 20
    FACTORY_SLOWDOWN = 35
    screenWidth = 600
    screenHeight = 400
    g = 9.81
    isGameOver = False

    makeGameGrid(screenWidth, screenHeight, 1, False, keyPressed = keyCallback)
    setTitle("Use Cursor up/down to target, Space to shoot.")
    setBgColor(makeColor("skyblue"))
    addStatusBar(30)
    factory = FruitFactory.create(FACTORY_CAPACITY, FACTORY_SLOWDOWN)
    addActor(factory, Location(0, 0))  # needed to run act()
    crossbow = Crossbow()
    addActor(crossbow, Location(80, 320))
    setSimulationPeriod(30)
    doRun()
    show()

    while not isDisposed() and not isGameOver:
       # Don't show message if same
       oldMsg = ""
       msg = "#hit: "+str(FruitFactory.nbHit)+" #missed: "+str(FruitFactory.nbMissed)
       if  msg != oldMsg:
            setStatusText(msg)
            oldMsg = msg
       if FruitFactory.nbHit + FruitFactory.nbMissed == FACTORY_CAPACITY:
           isGameOver = True
           removeActors(Dart)
           setStatusText("You smashed " + str(FruitFactory.nbHit) + " out of "
           + str(FACTORY_CAPACITY) + " fruits")
           addActor(Actor("sprites/gameover.gif"), Location(300, 200))

       delay(100)


Analyse de code
===============

Répondre aux questions d'analyse ci-dessous.

Question 1
----------

Mettre en évidence les éléments suivants dans le code

a)  Un variable d'instance

b)  Une instance

c)  Une variable de classe

d)  Une méthode d'instance

e)  Une méthode statique

Question 2
----------

..  shortanswer:: 9152a62e-58db-4635-93d2-6899eaa605df
    
    Expliquer en détail ce que fait l'appel ``self.turn(10)`` à la ligne 19

Question 3
----------

..  shortanswer:: c0d9b413-cdf1-48a4-beac-e444333bcf3d
    
    Expliquer comment fonctionne la méthode ``movePhysically()`` de la classe ``Fruit``

Question 4
----------

..  shortanswer:: 934fed0c-5792-4b1d-ab2f-d39012eca5b6
    
    Expliquer l'intérêt de développer une classe ``Fruit``

Question 5
----------

..  shortanswer:: 1a94e941-2995-4e9f-8b2f-88cb9abcc7c7
    
    Expliquer le rôle de la classe ``FruitFactory`` et expliquer pourquoi cette
    méthode doit dériver de la classe ``Actor``

Question 6
----------

..  shortanswer:: 40512d39-9467-4312-9f78-14794eb5391e
    
    Expliquer ce qu'est le patron singleton (Singleton Pattern) et comment il est
    mis en oeuvre en répondant aux questions ci-dessous

    a)  Pourquoi le classe FruitFactory ne dispose-t-elle d'aucun constructeur

    b)  Que fait la méthode ``create()`` de la classe ``FruitFactory``

Question 7
----------

..  shortanswer:: 19f44945-7a91-46b3-a714-6715509e0a15
    
    Expliquer pourquoi il y a une méthode ``act()`` dans la classe FruitFactory
    alors qu'elle n'est même pas visible à l'écran ?

Question 8
----------

..  shortanswer:: 42293ccf-b266-4a0f-97b7-3524b611b11b
    
    Expliquer précisément ce que fait la ligne 83

Question 9
----------

..  shortanswer:: 4631cfda-e942-413f-b052-fa6b0f93bd0a
    
    Expliquer toutes les étapes nécessaires pour utiliser le système de détection de
    collision dans ce code

Question 10
-----------

..  shortanswer:: 5bc20d2d-c19b-401b-9ae8-990a01c572e8
    
    Que fait l'appel ``setSimulationPeriod(30)`` (ligne 164) et à quoi sert-elle ?
