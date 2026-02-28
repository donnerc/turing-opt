Introduction
############

..  contents:: Contenu de la page
    :depth: 3

..  reveal:: 40fff299-0ee7-4b2b-946c-6a357c7ddc72
    :showtitle: Commentaires sur la vidéo de Jonathan
    :instructoronly:
    
    - pas très efficace (commence par présenter la POO de manière très
      générique, à savoir avec du blabla)

    - Trop de concepts présentés en même temps, sans le temps de les assimiler

    - Une seule grosse vidéo n'est pas idéale du tout ... OK pour en présenter
      un petit extrait, mais pas toute la vidéo

    - Il serait mieux de trouver des alternatives

    - Il reprend l'image de la recette de cuisine pour parler d'objets, alors
      que c'est l'exemple traditionnel pour des procédures ... on ne considère
      jamais tellement les ingrédients comme des objets. Il vaut vraiment mieux
      partir du concept de jeu vidéo avec les acteurs ou les GUI ...

..  
    ..  admonition:: Remarque concernant la vidéo

        La vidéo ci-dessous présente en gros tout ce qu'il y a à savoir sur la POO
        au niveau OC. Il ne s'agit pas de la regarder en entier. La vidéo s'arrête
        quelques minutes plus tard, car cette partie de la vidéo introduit bien le
        chapitre.
        
        Libre à vous de la regarder en entier, mais il s'agit de la matière de tout
        le chapitre ...

    ..  youtube:: Y-wXK0Wu5pc
        :divid: poo_introduction
        :width: 800
        :height: 430
        :start: 1
        :end: 840

..  youtube:: 3-qqjlY3tCM
    :divid: poo_introduction_info_sans_complexe
    :width: 800
    :height: 430
    :start: 1
    :end: 840

La programmation orientée objet est un *paradigme de programmation* informatique
qui consiste en la définition et l'assemblage de "briques informatiques",
appelées objets. Un objet est une entité que l’on construit par instanciation à
partir d’une classe. Une classe est en qsuelque sorte une « catégorie » ou un
« type » d’objets représentant un concept, une idée ou toute entité du monde
physique comme une voiture, une personne ou encore un livre. En fait, vous avez
déjà rencontré et manipulé des objets en Python puisque toutes les variables
existant en Python sont des objets, ainsi que les listes, tuples et
dictionnaires. En Python, même les fonctions sont des objets.

L'objectif de ce chapitre est d'apprendre à définir de nouvelles classes
d’objets. Il s’agit là d’un sujet relativement ardu, mais vous l’aborderez de
manière très progressive, en commençant par définir des classes d’objets très
simples, que vous perfectionnerez ensuite. En effet, comme les objets de la vie
courante, les objets informatiques peuvent être très simples ou très compliqués.
Ils peuvent être composés de différentes parties, qui sont elles-mêmes des
objets, ceux-ci étant faits à leur tour d’autres objets plus simples, etc.

..  tip::

    L'utilisation de classes dans vos programmes vous permettra, entre autres
    avantages, d'éviter au maximum l'emploi de variables globales. Vous devez
    savoir en effet que l'utilisation de variables globales comporte des
    risques, d'autant plus importants que les programmes sont volumineux, parce
    qu'il est toujours possible que de telles variables soient modifiées, ou
    même redéfinies, n'importe où dans le corps du programme. Ce risque
    s'aggrave particulièrement si plusieurs programmeurs travaillent sur un même
    logiciel.
