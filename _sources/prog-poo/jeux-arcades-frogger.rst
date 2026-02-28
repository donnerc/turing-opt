
Gestion du clavier et conception de jeux
########################################

..  contents:: Contenu de la page
    :depth: 3


Objectifs
=========

Dans cette section, tu vas apprendre les éléments suivantes

*   Comment réaliser un jeu d'arcades bien connu : Frogger
*   Comment gérer les événements du clavier grâce aux *callbacks*
*   Gestion des collisions entre les objets du jeu
*   Raffraichissement rapide et fluide (25 fps) de l'image
*   Comment développer un jeu un peu plus compliqué (environ 100 lignes de code)

Matériel
========

Dans cette section, la base du code du jeu sera développée pas-à-pas. Une
version imprimable du code a été distribuée en cours.

..  admonition:: Téléchargement

    *   :download:`scripts/frogger/handout-code.pdf`

Scénario du jeu et cahier des charges
=====================================

..  only:: html

    ..  figure:: figures/frogger.gif
        :align: center

Avant de se lancer dans le codage d'un jeu, il faut définir clairement les
règles et les fonctionnalités qu'il devra mettre à disposition. En somme, il
faut écrire le scénario du jeu. En génie logiciel et dans la gestion de
projet, cela s'appelle "dresser le cahier des charges" du projet. Il s'agit
d'un document qui décrit de manière succincte, par des mots-clés et des
phrases très courtes, mais dans les détails, toutes les fonctionnalités
désirées dans le produit fini.

La plupart du temps, le premier scénario projeté  est trop compliqué et il ne
sera pas possible de l'implémenter du premier coup. Le programmeur doit donc
simplifier le cahier des charges du jeu (logiciel) jusqu'à ce qu'il soit en
mesure de l'implémenter pour une version 0.1. Il sera ensuite possible de
rajouter des règles, des variantes, des effets et fonctionnalités
supplémentaires. Cela nécessite cependant d'écrire le code de façon modulable
et bien structurée pour pouvoir rajouter les fonctionnalités ultérieures avec
le minimum de modifications. Un développement intelligent qui permet un code
flexible et évolutif  constitue un véritable défi même pour les meilleurs
programmeurs.

Cependant, développer son propre jeu / programme et pouvoir l'exécuter est
extrêmement gratifiant, surtout s'il est utile et apprécié par d'autres
personnes. Dans notre cas, ce n'est pas tant le produit fini que les
compétences et les connaissances que tu vas acquérir pendant le développement
(et le débogage !!!)

Cahier des charges
------------------

..  admonition:: À compléter

    Le cahier des charges se trouve dans le document GoogleDocs modifiable
    suivant :
    https://docs.google.com/document/d/1zaWUF-Erd_0qmbAar9z98FhnQ4RvtNIJERj7RTOalg8/edit?usp=sharing.
    N'hésitez pas à rajouter des fonctionnalités que vous trouverez
    intéressantes en couleur rouge.


Principes de développement
==========================

Étape 1
-------

Il y a plusieurs façons de créer un petit jeu tel que Frogger. Voici celle que
nous allons adopter :

#.   D'abord les mouvements de la grenouille et ceux des véhicules
#.   Gestion des collisions
#.   Comptage des points et gestion de la fin du jeu

Les voitures sont représentées par des instances de la classe ``Car`` qui
dérive de la classe ``Actor``. Dans leur méthode ``act()``, on programme la
direction dans laquelle elles se déplacent. On utilisera les sprites
``car0.gif`` jusqu'à ``car19.gif`` qui se trouvent dans l'archive TigerJython.
Il est possible d'utiliser tes propres images, mais leur taille ne doit pas
dépasser 70 pixels de hauteur et 200 pixels de largeur.

Pour les jeux d'arcades, on utilise généralement une grille de jeu dont la
taille des carrés est 1x1 pixel, ce qui fait correspondre chaque carré de la
grille à un pixel de l'écran. Nous utiliserons une grille de taille :math:`800 \times 600`
pour commencer, ce qui paraîtra un peu petit sur des écrans haute définition.
Dans la fonction ``initCars()``, tu peux générer les 20 véhicules en
déterminant leur lieu de création et leur sens de déplacement.

Le déplacement des véhicules avec la méthode ``act()`` est simple : dès qu'ils
sortent de la grille de jeu d'un côté, tu peux les faire réapparaitre de
l'autre côté. Il faut noter à cet effet que l'acteur existe encore dans le
moteur du jeu même s'il se trouve en dehors de la grille. Il est donc possible
de le faire apparaître de l'autre côté de la grille, mais en dehors de la zone
visible.

Code de base
++++++++++++

..  literalinclude:: scripts/frogger/frogger1.py
    :linenos:
    :language: python

Étape 2 (Bouger la grenouille avec le clavier)
----------------------------------------------

Nous allons maintenant faire intégrer la grenouille dans le jeu. Le joueur la
bougera grâce aux touches haut, bas, gauche, droite du clavier. Ensuite, il
faut faire le suivant :

*   Définir une classe ``Frog`` qui dérive de la classe ``Actor``. Aucune
    méthode n'est nécessaire hormis le construteur puisque ce seront des événements
    clavier qui vont la faire bouger.

*   Définir le gestionnaire d'événements ``keyCallback()`` qui sera signalé au
    moteur de jeu comme gestionnaire d'événements du clavier avec

    ..  code-block:: python

        makeGameGrid(..., keyRepeated=keyCallback)

    On associe le gestionnaire ``keyCallback`` au paramètre ``keyRepeated``
    pour qu'il ne soit pas uniquement appelé de manière unique lorsqu'on
    appuie courtement sur une touche, mais qu'il le soit de manière rapide et
    répétée lorsque la touche est maintenue enfoncée.

    ..  tip::

        Attention à **ne pas mettre de parenthèses** lorsque le gestionnaire est passé
        en paramètre à la fonction ``makeGameGrid``. Il faut bien passer la
        fonction en tant qu'objet et non sa valeur de retour avec ``makeGameGrid(...)``

*   Dans le gestionnaire ``keyCallback``, le paramètre ``keyCode`` sera
    renseigné avec le code (nombre entier) de la touche pressée. Il suffit de
    déplacer la grenouille de 5 pixels dans la direction indiquée sur la base
    de ``keyCode`` ou de ne rien faire si une autre touche a été pressée.

    Pour augmenter la lisibilité du programme, on définit les constantes
    constantes suivantes en début de code:

    ..  code-block:: python

        # ---------------- Constantes clavier --------
        K_LEFT      = 37
        K_UP        = 38
        K_RIGHT     = 39
        K_DOWN      = 40


    ..  tip::

        Si tu ne connais pas le ``keyCode`` d'une touche du clavier, il suffit
        d'essayer en exécutant ce programme qui fait appel à un gestionnaire
        d'événements affichant le code reçu avec un ``print`` :

        ..  literalinclude:: scripts/testkbd.py
            :language: python

Code
++++

..  literalinclude:: scripts/frogger/frogger2.py
    :linenos:
    :language: python

Détection de collisions
=======================

Il est très facile d'installer une détection des collisions avec le module
*JGameGrid* car il s'occupe de faire les calculs géométriques pour nous. Il
suffit, lors de la création d'une instance ``car`` de la classe ``Car``,
d'appeler la méthode ``addCollisionActor`` de la grenouille :

..  code-block:: python

    frog.addCollisionActor(car)

Cet appel va indiquer à l'instance ``frog`` de la classe ``Frog`` que lors de
chaque collision avec l'acteur ``car``, elle doit générer un événement spécial
qui va se charger d'invoquer la méthode ``Actor.collide()`` de l'instance
``frog``. C'est dans cette méthode qu'on peut ensuite décider de la manière de
réagir à la collision, en l'occurrence faire sauter la grenouille à sa
position de départ.

..  admonition:: Code

    ..  literalinclude:: scripts/frogger/frogger3.py
        :linenos:
        :language: python
        :emphasize-lines: 14-16,33-33

La méthode ``collide()``
------------------------

La méthode ``collide()`` est définie à la base dans la classe ``Actor``
sans comportement particulier et doit être surchargée (*overriden*) dans
la classe ``Frog`` pour implémenter le comportement désiré.

Par défaut, la détection se fait par calcul géométrique avec les
coordonnées des sommets des rectangles entourants les sprites, comme
représenté sur la figure ci-dessous :

..  figure:: figures/collision-rect.png
    :width: 60%
    :align: center

    Illustration de la détection de collision avec la méthode des
    rectangles

Il est possible de personnaliser ce comportement en précisant la région de
l'espace qui sera prise en compte pour la détection de la superposition.
Voici les méthodes utiles à cet effet permettant de spécifier la forme, la
taille et les coordonnées de la zone du sprite sensible à la collision :


*   ``setCollisionCircle(centerPoint, radius)`` :  Cercle de centre ``centerPoint`` et de rayon ``radius`` (en pixels)

*   ``setCollisionImage()`` : Définit les pixels non transparents de l'image de
    sprite comme sensibles à la collision avec un autre acteur. Possible
    uniquement avec des acteurs qui définissent leur zone de collision comme
    ``setCollisionCircle``, ``setCollisionLine`` ou ``setCollisionSpot``

*   ``setCollisionLine(startPoint, endPoint)`` : Segment de droite dont les extrémités sont les points ``startPoint`` et ``endPoint``

*   ``setCollisionRectangle(center, width, height)`` : Rectangle de centre ``center``, de largeur ``width`` et de hauteur ``height``

*    ``setCollisionSpot(spotPoint)`` : Un point particulier de l'image

..  admonition:: Remarque

    Pour toutes les méthodes décrites ci-dessus, le système de coordonnées
    utilisé est relatif au sprite. Son origine se trouve au centre du
    rectangle délimitant le sprite et l'axe :math:`Oy` est dirigé vers le bas :

    ..  figure:: figures/actor-relative-axis.png
        :align: center
        :width: 50%

        Système d'axe relatif au sprite

Le sprite de la grenouille a une taille de :math:`71 \times 41` pixels. On
peut changer la zone de la grenouille sensible aux collisions dans le
construteur de la classe ``Frog`` :

..  code-block:: python

    self.setCollisionCircle(Point(0, -10), 5)

de sorte qu'une collision sera générée lorsqu'une voiture roule sur le cercle
de centre :math:`(0;-15)` et de rayon :math:`5` qui entoure sa tête :

..  figure:: figures/frog.png
    :align: center

..  list-table::
    :header-rows: 1
    :align: left

    *   - Méthode
        - Zone de collision

    *   - ``setCollisionCircle(centerPoint, radius)``
        - Cercle de centre ``centerPoint`` et de rayon ``radius`` (en pixels)

    *   - ``setCollisionImage()``
        - Nicht-transparente Bildpixels (nur mit einem Partner der Kreis, Linie oder Punkt als Kollisionsarea hat)

    *   - ``setCollisionLine(startPoint, endPoint)``
        - Segment de droite dont les extrémités sont les points ``startPoint`` et ``endPoint``

    *   - ``setCollisionRectangle(center, width, height)``
        - Rectangle de centre ``center``, de largeur ``width`` et de hauteur ``height``

    *   -  ``setCollisionSpot(spotPoint)``
        - Une point particulier de l'image


Moteur de jeu
=============

Maintenant que nous avons développé tout ce qui tourne autour des mouvements
des acteurs de notre jeu, il nous faut implémenter la logique du jeu, à savoir
le comptage des points et les conditions de fin de jeu.

Pour ce faire, on pourrait utiliser des variables globales pour stocker le
nombre de fois que la grenouille a traversé avec succès toute la route et le
nombre de fois que la grenouille a été écrasée.

Si la grenouille a trois vies, on peut stoper le jeu et afficher un message de
*Game Over* lorsqu'elle s'est faite écraser trois fois.

Mais comme vous le savez, l'utilisation de variables globales n'est pas
indiquée dans le 99% des cas et le nôtre ne fait pas exception. Le mieux
serait de créer une classe ``FroggerGame`` qui va stocker ces différents
paramètres en tant que variables d'instances.


Extensions / Exercices
======================

Exercice 1
----------

..  activecode:: frogger-exercice-01

    Créer une nouvelle classe ``FroggerGame`` pour pour modéliser le moteur de jeu dans
    une classe qui constituera le programme principal. Il ne doit y avoir aucune
    variable dans l'espace de noms global.

    ..  admonition:: Remarque

        Tout le code du programme principal doit donc se trouver dans la classe
        ``FroggerGame``.

    ~~~~

..  reveal:: fc4a1fb4-ab0b-41fb-93db-1b58ea4120dc
    :showtitle: Corrigé

    ..  admonition:: Corrigé

        ..  youtube::   kTO-P4ridIY
            :divid: frogger-solution-exercice-01
            :width: 635
            :hei

        Le code mis à disposition ci-dessous encapsule toute la logique du et
        tous les objets précédemment définis dans l'espace de noms global à
        l'intérieur de la classe ``FroggerGame`` qui est instancié à la toute
        dernière ligne.

        *   La grenouille devient une variable d'instance de ``FroggerGame`` et
            tous les ``frog`` doivent être remplacés par ``self.frog``

        *   Le gestionnaire d'événement ``keyCallback`` devient également
            une méthode d'instance de la classe ``FroggerGame`` puisque cette
            méthode doit accéder à la variable d'instance ``self.frog``. Il faut donc modifier
            l'appel de ``makeGameGrid`` aux lignes 13-14 pour faire référence à la méthode
            d'instance ``self.keyCallback`` :

            ::

                makeGameGrid(800, 600, 1, None, "sprites/lane.gif", False,
                            keyRepeated = self.keyCallback )

        *   Les codes d'accès ``K_LEFT`` etc ... sont devenus des variables de classe, définis en dehors du constructeur et accessibles avec ``FroggerGame.K_LEFT`` etc ...

        ..  literalinclude:: scripts/frogger/exo-01_cor.py
            :language: python
            :linenos:


Exercice 2
----------

..  activecode:: frogger-exercice-02

    Rajouter les fonctionnalités suivantes dans le jeu :

    ..  admonition:: Consignes

        *   La grenouille a trois vies
        *   À chaque fois que la grenouille traverse la route, augmenter un compteur ``nb_succes``
            défini judicieusement
        *   À chaque fois que la grenouille se fait écraser, diminuer le nombre de vies de 1
        *   Afficher dans le titre de la fenêtre le nombre de succès et le nombre de vies restantes
        *   La grenouille revienne à la position de départ lorsqu'elle a fini de
            traverser la route

    ..  admonition:: Indications

        *   On peut afficher la chaine ``texte`` dans la barre de titre de la fenêtre avec

            ::

                setTitle(texte)

        *   On peut mettre le jeu en pause avec

            ::

                doPause()

        *   On sait que la fenêtre principale a été fermée lorsque ``isDisposed() == True``
        *   Pour afficher le *Game Over*, on peut créer un acteur ``gameOver`` avec le sprite ``"sprites/gameover.gif"`` ou avec un sprite personnalisé dont le fond est transparent.

    ~~~~

..  reveal:: 596a6a8f-f1d5-42fa-99a1-8245ea56d754
    :showtitle: Corrigé vidéo

    ..  admonition:: Corrigé

        ..  youtube::   shY6zKr3CGQ
            :divid: frogger-solution-exercice-02a
            :width: 635
            :hei

        ..  youtube::   Zxlglu7izng
            :divid: frogger-solution-exercice-02b
            :width: 635
            :hei


Exercice 3
----------

..  activecode:: 21307042-e0f2-4d9b-9b6d-aad6616c7fd9

    Jouer le son ``"wav/boing.wav"`` lorsque la grenouille se fait écraser et le
    son ``"wav/notify.wav"`` lorsqu'elle parvient avec succès à traverser la route.

    ~~~~

..  reveal:: 5322c714-4574-4878-b775-763d0b7d6d02
    :showtitle: Corrigé

    ..  admonition:: Corrigé

        ..  youtube::   YKnEHSy6xfk
            :divid: frogger-solution-exercice-03-ajout-son
            :width: 635
            :height: 360


        Il suffit d'ajouter l'importation du module ``soundsystem`` et de
        jouer ensuite le son au bon moment avec

        ::

            from soundsystem import *

            # jouer le son stocké dans le fichier "wav/boing.wav"
            openSoundPlayer("wav/boing.wav")

        ..
            ..  literalinclude:: scripts/frogger/exo-02_cor.py
                :language: python

Exercice 4
----------

..  activecode:: 45e28ac1-27f6-4b52-8289-575fef0ed687

    Modifiez le code pour pouvoir bouger la grenouille avec les touches ``A``,
    ``S``, ``D``, ``W``, au lieu des touches "flèches" du clavier

    ~~~~

..  reveal:: 850b167a-b4b9-4011-9e8d-44091ec69f2b
    :showtitle: Corrigé

    ..  admonition:: Corrigé

        ..  youtube::   zdc6BeRn-MM
            :divid: frogger-solution-exercice-04-ASDW
            :width: 635
            :height: 360

Exercice 5
----------

..  activecode:: 618ea0e4-b670-4f75-9a8b-0fc4deaecb44

    Modifiez le code pour Faire un comptage de points qui sera affiché dans
    la barre de titre de la fenêtre.

    *   Lorsque la grenouille traverse avec succès, le joueur marque 5 points.
    *   Lorsque la grenouille se fait écraser, le joueur perd 5 points

    ~~~~

..  reveal:: 5e10a24f-e7e0-483e-a61a-1e0d76a98806
    :showtitle: Corrigé

    ..  admonition:: Corrigé

        ..  youtube::   xD4LCQjzhY4
            :divid: frogger-solution-exercice-05-score
            :width: 635
            :height: 360

Exercice 6
----------

..  activecode:: bf4e0ab1-98ab-46e6-a8e1-4582361d1946

    Modifier le code en incluant un temps limite pour chaque traversée de la
    route. Si le temps est dépassé, supprimer 10 points et remettre la
    grenouille au point de départ.

    ~~~~

..  reveal:: db0477c6-78ad-46e6-bcbd-471e599a7e67
    :showtitle: Corrigé

    ..  admonition:: Corrigé

        ..  youtube:: cwu7Zdic4g4
            :divid: frogger-solution-exercice-06-time-limit
            :width: 635
            :height: 360


Fonctionnalités supplémentaires
-------------------------------

#.  Faire en sorte que les voitures ne roulent pas à la même vitesse sur
    toutes les voies.

#.  Au lieu d'avoir un décallage régulier entre les voitures, introduis
    une distance aléatoire comprise entre 20 et 100 pixels.

#.  Sois créatif et ajoute tes propres fonctionnalités au jeu.

Solution complète
-----------------

..  reveal:: d542d53b-e289-4a28-974f-c35822362d21
    :showtitle: Montrer la solution
    :hidetitle: Cacher la solution

    ..  literalinclude:: scripts/frogger/frogger_complet.py
        :language: python

