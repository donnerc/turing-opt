.. _introduction-cp:

Introduction à la programmation par contraintes
###############################################

..  contents:: Parties du cours
    :depth: 3

Dans ce module du cours Turing, vous allez découvrir un nouveau **paradigme de
programmation** appelé **programmation par contraintes** (PPC). Ce paradigme de
programmation est particulièrement adapté pour résoudre des problèmes de
satisfaction de contraintes (PSC) tels que des jeux logiques (par exemple
Sudokus) ou les problèmes d'optimisation sous contraintes (POC), beaucoup plus
compliqués, que rencontrent de nombreuses industries :

- création d'horaires dans une université ou des gymnases (timetabling problems)
- ordonnancement de processus (scheduling problems) : organisation d'une chaîne
  de montage dans l'industrie automobile
- Organisation de journées à thème dans un gymnase ou d'examens oraux de BAC
  dans un gymnase : exemple https://groople.ch/   
- Planification des vols dans une compagnie aérienne
- Gestion des stocks et logistique dans une grosse entreprise de vente (Amazon,
  ...)
- Optimisation d'une flotte aérienne (y compris tous les processus de
  maintenance)
- ...

Notion de paradigme de programmation
====================================

..  admonition:: Paradigme de programmation

    Un **paradigme de programmation** est une manière d'envisager la
    programmation, une sorte de *Weltanschauung*
    (https://fr.wikipedia.org/wiki/Weltanschauung) ou *vision du monde*
    lorsqu'on programme. On pourrait parler aussi de *perspective* lorsqu'on
    programme.

Vous connaissez déjà un peu deux paradigmes de programmation:



La programmation procédurale (ou impérative)
--------------------------------------------

C'est le paradigme que vous avez le plus pratiqué et que vous maîtrisez le mieux
à l'issue de la première année du cours Turing. Il consiste à décrire
précisément, étape par étape ce que l'ordinateur doit faire. Dans cette logique,
on peut définir un programme comme des algorithmes qui transforment des données
pour obtenir d'autres données. Le niveau d'abstraction de ce paradigme de
programmation se focalise sur les structures de données (listes, dictionnaires,
tuples, arbres, graphes, ...) et les fonctions qui agissent sur ces structures
de données.

..  admonition:: Slogan

    Le slogan de la programmation impérative est 

        Algorithmes + Structures de données = Programme

    https://en.wikipedia.org/wiki/Algorithms_%2B_Data_Structures_%3D_Programs

La programmation orientée objets
--------------------------------

Dans ce paradigme, les programmes sont
des collections d'objets qui interagissent entre eux à l'aide de méthodes.
Vous avez pratiqué ce paradigme à la fin du cours Turing, en développant le
langage ALAN en utilisant des **classes** pour développer l'analyseur lexical,
l'analyseur syntaxique, l'arbre syntaxique abstrait, etc... . Ce paradigme de
programmation est particulièrement adapté pour modéliser des systèmes
logiciels complexes comportant de nombreux composants interagissant les uns
avec les autres. Ce paradigme de programmation utilise l'abstraction des
classes pour modéliser la réalité et les interactions entre les objets.

..  admonition:: Slogan

    Pour la POO, on pourrait également trouver des slogans permettant de la
    résumer:

        Objets + messages (méthodes) = application

    ou encore

        Réutilisabilité + extensibilité = flexibilité

    ou encore

        Tout est objet


Programmation par contraintes
-----------------------------

    Constraint Programming represents one of the closest approaches computer
    science has yet made to the Holy Grail of programming: the user states the
    problem, the computer solves it. [E. Freuder]

..  reveal:: e1b4892c-664c-478d-b47b-4d4fa025f223
    :showtitle: Parenthèse culturelle (PPC et IA)

    La programmation par contraintes est issue du domaine de l'intelligence
    artificielle. On parle ici de la "vieille" intelligence artificielle développée
    depuis les années 1980 et non les sujets à la mode actuellement (apprentissage
    machine, IA génératives).

La **programmation par contraintes** est très adaptée à la résolution de PSCs,
car elle ne se focalise pas sur les structures de données ou les algorithmes
précis à utiliser pour exprimer et résoudre le problème. En effet, les problèmes
rencontrés dans la pratique possèdent des structures internes et propriétés qui
impliquent de très nombreux détails très dynamiques qui peuvent changer d'une
fois à l'autre. La programmation par contraintes consiste non pas à expliquer à
l'ordinateur comment résoudre un problème, mais à permettre de spécifier de
manière très précise le problème à résoudre et de déléguer sa résolution à des
**solveurs de contraintes**.

  ..  admonition:: Slogan

      Le slogan de la programmation par contraintes peut être formulé de la
      manière suivante: 

          Programmation par contraintes = modèle + recherche

La résolution d'un CSP se déroule donc en deux temps, que l'on recommence
souvent en pratique:

#.  Formuler le problème sous forme de variables et de contraintes. On appelle
    cette étape la **modélisation**. Elle consiste à identifier les variables du
    problème et établir des contraintes entre ces variables.
#.  Tester différentes stratégies de résolution pour attribuer à chaque variable
    une valeur de telle manière que toutes les contraintes soient satisfaites.
#.  Revenir à l'étape 1 si le problème a un peu changé (par exemple de nouvelles
    règles pour le déroulement des examens de BAC d'une année à l'autre) et
    recommencer.

