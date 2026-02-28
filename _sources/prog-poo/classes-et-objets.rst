..  footer::

    OCI 3 -- Programmation orientée objets -- page ###Page###

Classes et objets
#################

..  contents:: Contenu de la page
    :depth: 3


..  only:: html

    ..  admonition:: Documents

        Voici une version PDF de cette section pour vous permettre d'étudier et
        annoter le code sur papier.

        *   Version PDF de cette section :
            https://eduetatfr.sharepoint.com/:b:/t/CSUD-GT-BrancheInformatiqueBureautique/Ee7Pg_jhzIxOpge9rVdjsrQBLD6U_A8cRPlDzR_3K4KUYA?e=YcuGjh

Récapitulation des notions de base de la POO
============================================

Observez attentivement le code ci-dessous et répondre aux questions. Toutes
les questions posées sont vraiment essentielles et donc des questions types
qui peuvent être posées lors d'un oral de BAC.

..  code-block:: python
    :linenos:

    from gamegrid import *

    # ---------------- classe Animal ----------------
    class Animal():

        def __init__(self, imgPath):
            self.imagePath = imgPath


        def showMe(self, x, y):
             bg.drawImage(self.imagePath, x, y)


    def pressCallback(e):
        myAnimal = Animal("sprites/animal.gif")
        myAnimal.showMe(e.getX(), e.getY())

    makeGameGrid(600, 600, 1, False, mousePressed = pressCallback)
    setBgColor(Color.green)
    show()
    doRun()
    bg = getBg()

Analyse de code
---------------

1)  Décrire le rôle de la fonction ``__init__`` aux lignes 6 et 7

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: html

        ..  shortanswer:: classes-et-objets-comprehension-01

            Entrez votre réponse ici
            
        ..  reveal:: fff91914-a262-4297-9b1d-270e0335ecab
            :showtitle: Solution

            ..  admonition:: Réponse

                La fonction ``__init__`` est le constructeur de la classe
                ``Animal``. Cette fonction est appelée automatiquement à chaque
                fois que l'on crée un animal avec

                ::

                    mon_animal = Animal("sprites/example.png")

2)  Décrire précisément ce qui se passe à la ligne 7

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: html

        ..  shortanswer:: classes-et-objets-comprehension-02

            Entrez votre réponse ici

        ..  reveal:: e30e74c1-9e51-4314-82fb-7c9fec6646b6
            :showtitle: Réponse

            ..  admonition:: Réponse

                Cette ligne crée la variable d'instance ``self.imagePath`` et
                l'initialise avec le contenu de la variable locale ``igmPath``.

3)  Que représente le premier paramètre ``self`` dans la définition des méthodes d'instance ?

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: html

        ..  shortanswer:: classes-et-objets-comprehension-03

            Entrez votre réponse ici

        ..  reveal:: 82e9f23b-377f-4d2c-820f-3e80e0fdb4df
            :showtitle: Réponse

            ..  admonition:: Réponse

                Le paramètre ``self`` est propre à toutes les méthodes d'instance
                et doit toujours se trouver en première position. Il s'agit d'une
                référence vers l'instance concrète sur laquelle la méthode a été
                invoquée.

                Lors de l'invocation de la méthode avec

                ::

                    mon_animal.showMe(10, 20)

                on ne renseigne pas ce paramètre ``self`` car Python s'en charge
                pour nous en transformant notre appel dans le code suivant avant
                de l'exécuter :

                ::

                    Animal.showMe(mon_animal, 10, 20)

4)  À quoi sert la fonction ``pressCallback(e)`` définie aux lignes 14 à 16 ?

    ..  raw:: pdf

        Spacer 0 120

    ..  only:: html

        ..  shortanswer:: classes-et-objets-comprehension-04

            Entrez votre réponse ici

        ..  reveal:: 7bb6f629-3e75-4682-bef8-348944f55378
            :showtitle: Réponse

            ..  admonition:: Réponse

                Cette fonction est un **gestionnaire d'événement** (*Event
                handler* en anglais). Elle sera appelée à par le système du jeu à
                chaque fois qu'un événement de type ``MousePressed`` est généré
                par le système.

                C'est uniquement à la ligne 18

                ::

                    makeGameGrid(600, 600, 1, False, mousePressed = pressCallback)

                que notre fonction ``pressCallback`` est "connectée" à l'événemnt
                ``mousePressed``. Ce qui se passe à la ligne 18 est très nouveau
                : on passe à la fonction ``makeGameGrid`` la fonction
                ``pressCallback`` en guise de paramètre. Notez bien que l'on n'a pas
                écrit ``mousePressed = pressCallback()`` mais bien ``mousePressed
                = pressCallback`` sans appeler la fonction ``pressCallback`` avec
                des parenthèses ``()``.

5)  Que représente le paramètre ``e`` de la fonctoin ``pressCallback(e)`` ?

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: html

        ..  shortanswer:: classes-et-objets-comprehension-05

            Entrez votre réponse ici

        ..  reveal:: 73785b3d-2dac-405d-9173-087661eb7265
            :showtitle: Réponse

            ..  admonition:: Réponse

                Il s'agit d'un objet représentant l'événement qui a déclenché
                l'appel de ``pressCallback``. Cet objet ``e`` contient des
                informations sur l'événement généré par le clic de souris, en
                particulier les coordonnées du clic récupérables avec ``e.getX()``
                et ``e.getY()``.

6)  Décrire précisément ce qui se passe à la ligne 16 ?

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: html

        ..  shortanswer:: classes-et-objets-comprehension-06

            Entrez votre réponse ici

        ..  reveal:: 4b7f2025-26a5-416f-a545-52ecda106279
            :showtitle: Réponse

            ..  admonition:: Réponse

                En gros, on crée une instance de la classe ``Animal`` à la ligne
                15 que l'on affiche à la ligne 16 à l'emplacement du clic de la
                souris.

7)  Expliquer ce que fait globalement ce code Python?

    ..  raw:: pdf

        Spacer 0 130

    ..  only:: html

        ..  shortanswer:: classes-et-objets-comprehension-07

            Entrez votre réponse ici

        ..  reveal:: a7403b65-2bea-40c3-8b50-422250ac905f
            :showtitle: Réponse

            ..  admonition:: Réponse

                Globalement, le programme affiche des petits animaux lorsqu'on
                clique dans l'espace de jeu. Le coin supérieur gauche du rectangle
                contenant le sprite de l'animal correspondra aux coordonnées du
                clic de la souris.


