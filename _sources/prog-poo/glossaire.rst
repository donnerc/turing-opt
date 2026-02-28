Glossaire du chapitre (POO)
###########################

..  contents:: Contenu du chapitre
    :depth: 3

..  admonition:: Conseil

    La liste suivante répertorie dans l'ordre alphabétique les principaux termes
    introduits dans ce chapitre. La connaissance de leur définition est
    indispensable.

Attribut d'instance
===================

Caractéristique de chaque instance d'une classe qui n'existe, par rapport à
une allocation mémoire, que dans une instance de cette classe. Avant qu'une
instanciation de la classe ne soit effectuée, l'attribut n'a aucune
existence physique. Si plusieurs instances de la même classe coexistent, il
y a un exemplaire de chaque attribut d'instance de la classe par instance
créée.

Attribut de classe
==================

Caractéristique propre à chaque instance d'une classe qui existe, par
rapport à une allocation mémoire, dès que la classe est chargée en mémoire.
Quel que soit le nombre d'instanciations de la classe (0, 1 ou plus), un
attribut de classe existe en un et un seul exemplaire. Un tel attribut joue
un peu le rôle d'un variable globale d'un programme non-objet : sa classe
lui sert de "boîte de rangement".

Classe fille (sous-classe)
==========================

Nouvelle classe créée par dérivation d'une classe existante.

Classe parente
==============

Classe de laquelle une classe fille hérite ses attributs et méthodes.

Classe
======

Type de données abstrait défini par l'utilisateur et servant de moule à une
famille d'objets ayant une structure et un comportement commun. Une classe
décrit le nom et la nature des attributs que possèdera chaque objet ainsi
que les méthodes qui s'appliqueront aux objets.

Constructeur
============

Méthode portant le nom ``__init__`` renvoyant implicitement la référence de
l'instance construite. Un constructeur sert en particulier à initialiser les
attributs d'instance. Lorsqu'une classe ne contient pas de constructeur,
l'interpréteur en ajoute automatiquement un qui ne comporte qu'un appel au
constructeur sans paramètre de la classe parente.

Dérivation
==========

Synonyme d'héritage.

Encapsulation
=============

Possibilité de "cacher" des données à l'intérieur d'une classe en ne
permettant de les manipuler qu'au travers de méthodes. L'intérêt essentiel
d'une telle opération est d'interdire à l'utilisateur de modifier
directement les données d'une classe en l'obligeant à utiliser les fonctions
définies pour les modifier (appelées *interfaces*), ce qui permet de
maintenir l'ensemble des données de la classe dans un état cohérent.

..
    Espace de noms
    ==============

    Un espace de noms est semblable à un dictionnaire dans lequel les clés sont les
    noms des variables et les valeurs du dictionnaire sont les valeurs des
    variables. A n'importe quel point d'un programme Python, il y a plusieurs
    espaces de noms disponibles. Chaque fonction a son propre espace de noms, appelé
    *espace de noms local*, qui suit les variables de la fonction, y compris ses
    arguments et les variables définies localement. Il y a en plus l'espace de nom
    global qui stocke les variables définies hors de toute fonction.

Héritage
========

Principe propre à la programmation orientée objet permettant de créer une
nouvelle classe à partir d'une classe existante. Le nom d'\ *héritage*
(parfois appelé *dérivation*) provient du fait que la classe dérivée
contient les attributs et les méthodes de sa classe parente. L'intérêt
majeur est de pouvoir définir de nouveaux attributs et de nouvelles méthodes
pour la classe dérivée, qui viennent s'ajouter à ceux et celles héritées.

Instance
========

Synonyme d'objet.

Interface
=========

Définition d'un contrat qu'une classe s'engage à respecter via une image
abstraite qu'elle fournit d'elle-même à l'extérieur. On y spécifie la
fonctionnalité de la méthode à l'aide de commentaires.

Méthode
=======

Fonction encapsulée dans une classe et applicable aux objets de cette
classe.

Objet
=====

Une classe A est un modèle décrivant un type d'objets. Une instance de la
classe A est un objet construit selon le modèle fourni par la classe A. Il
s'agit d'une réalisation concrète de la classe A possédant des
caractéristiques qui leur sont propres.

Paradigme de programmation
==========================

Façon de programmer, modèle qui oriente notre manière de penser pour
formuler et résoudre un problème. Un paradigme fournit la vue qu'a le
développeur de l'exécution de son programme. Parmi les paradigmes les plus
connus, nous retiendrons la programmation impérative, la programmation
fonctionnelle et la programmation orientée objet.

Polymorphisme ad hoc
====================

Possibilité d'avoir des méthodes de même nom, avec des fonctionnalités
similaires, dans des classes sans aucun rapport entre elles. Le
polymorphisme ad hoc permet ainsi de redéfinir des opérateurs dont
l'utilisation sera différente selon le type des paramètres qui leur sont
passés.

Polymorphisme d'héritage
========================

Spécialisation d'une méthode héritée, possibilité de redéfinir une méthode
héritée d'une classe parente. Ce principe permet d'appeler la méthode d'un
objet sans se soucier de son type

Programmation orientée objet
============================

Paradigme de programmation consistant en la définition et en l'interaction
de briques logicielles appelées objets. Un objet représente un concept, une
idée ou toute entité du monde physique, comme une voiture, une personne ou
encore une page d'un livre.

Référence d'instance
====================

Paramètre obligatoire dans la définition d'une méthode et désignant
l’instance à laquelle la méthode sera associée. Par convention, ce paramètre
prend le nom self.

Spécialisation (overriding)
===========================

Possibilité de redéfinir une méthode dans des classes héritant d'une classe
de base.

Structure de données
====================

Structure logique destinée à contenir des données, afin de leur donner une
organisation permettant de simplifier leur traitement. En informatique, il
existe différents types de structure de données : les structures finies
(constantes, variables,...), indexées (séquences, tableaux associatifs,...),
récursives (arbres, graphes,...)

Superclasse
===========

Classe de base située au sommet de la hiérarchie des classes. En Python,
elle est appelée la classe Object.

Surcharge (overloading)
=======================

Possibilité d'avoir des méthodes de même nom, avec des fonctionnalités
similaires, dans des classes sans aucun rapport entre elles.