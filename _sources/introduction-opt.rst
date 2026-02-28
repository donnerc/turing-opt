.. _introduction-opt:

Introduction à l'optimisation combinatoire
##########################################

..  contents:: Table des matières
    :depth: 3

Lien avec le précédent module de programmation fonctionnelle
============================================================

Dans le précédent module du cours Turing (programmation fonctionnelle), vous
avez développé un framework d'autodifférentiation pour calculer des gradients de
fonctions à partir de leurs définitions. Il s'agissait dans ce cadre de pouvoir
optimiser (minimiser) des fonctions 

..  math::

    f : \mathbb{R}^n \to \mathbb{R}

L'**optimisation combinatoire** s'intéresse à la recherche de solutions
optimales dans des espaces de solutions discrets et souvent très vastes. Dans ce
contexte, on optimise des **fonctions objectif** (*objective function*) définies
sur des ensembles finis ou dénombrables :math:`S \subseteq \mathbb{Z}^n`

..  math::

    f : S \to \mathbb{R} 
    
où :math:`S` est un ensemble de combinaisons d'objets (par exemple, des
permutations, des sous-ensembles, des graphes, etc.). Comme le domaine de
définition de ces fonctions est discret, les méthodes d'optimisation classiques
basées sur le calcul de gradients ne sont pas directement applicables.
L'optimisation combinatoire nécessite donc le développement de techniques
spécifiques pour explorer efficacement l'espace de solutions et trouver des
solutions optimales ou quasi-optimales. 

Applications de l'optimisation combinatoire
===========================================

Les problèmes d'optimisation combinatoire sont omniprésents dans de nombreux
domaines, tels que 

- la logistique
- la planification
- la création d'horaires dans les écoles
- l'allocation de ressources dans un entreprise
- ...
- 
  
L'objectif de ce module est de vous introduire aux concepts fondamentaux de
l'optimisation combinatoire, ainsi qu'aux techniques et algorithmes utilisés
pour résoudre ces problèmes.

Ce que nous allons voir dans ce module
======================================

Problèmes d'optimisation sous contraintes (POC)
-----------------------------------------------
        
Nous allons spécialement nous intéresser à une classe de problèmes appelés
**problèmes d'optimisation sous contraintes** (POC), qui sont des problèmes
d'optimisation combinatoire où les solutions doivent satisfaire un ensemble de
contraintes. Nous allons découvrir comment modéliser ces problèmes, les
algorithmes de résolution associés, et comment implémenter un solveur de
contraintes en Python.

Problèmes de satisfaction de contraintes (PSC)
----------------------------------------------

Avant d'aborder les problèmes d'optimisation sous contraintes, nous allons
commencer par voir comment résoudre des problèmes de satisfaction de contraintes
(PSC), qui sont une sous-classe de problèmes d'optimisation sous contraintes où
l'objectif est simplement de trouver une solution qui satisfait les contraintes,
sans nécessairement optimiser une fonction objectif. Les techniques et
algorithmes que nous allons découvrir pour les problèmes de satisfaction de
contraintes seront ensuite étendus pour traiter les problèmes d'optimisation de
contraintes.

Programmation par contraintes (PPC)
-----------------------------------

Nous allons introduire le paradigme de programmation par contraintes (PPC), qui
est une approche de programmation particulièrement adaptée pour résoudre des
problèmes de satisfaction et d'optimisation sous contraintes. La PPC permet de
modéliser les problèmes de manière déclarative, en spécifiant les contraintes
que les solutions doivent satisfaire, plutôt que de décrire explicitement les
étapes pour trouver ces solutions. Nous allons voir comment utiliser la PPC pour
modéliser et résoudre des problèmes d'optimisation sous contraintes.

Un solveur de contraintes en Python
-----------------------------------

Enfin, nous allons implémenter un solveur de contraintes en Python, qui nous
permettra de modéliser et résoudre des problèmes de satisfaction et
d'optimisation sous contraintes. Nous allons découvrir les différentes techniques
utilisées dans les solveurs de contraintes, telles que la propagation de
contraintes, le backtracking, et les heuristiques de recherche, et comment les
implémenter efficacement en Python.

Métaheuristiques d'optimisation combinatoire
--------------------------------------------

Nous allons également aborder les métaheuristiques d'optimisation combinatoire,
qui sont des algorithmes génériques utilisés pour trouver des solutions
approximatives à des problèmes d'optimisation combinatoire complexes. Les
métaheuristiques telles que les algorithmes génétiques, le recuit simulé, et les
algorithmes de colonies de fourmis sont souvent utilisées pour résoudre des
problèmes d'optimisation sous contraintes qui sont difficiles à résoudre
exactement. Nous allons découvrir comment ces métaheuristiques fonctionnent et
comment les implémenter en Python pour résoudre des problèmes d'optimisation de
contraintes.

Programmation dynamique
-----------------------

Nous allons également aborder la programmation dynamique, qui est une technique
d'optimisation utilisée pour résoudre certains types de problèmes d'optimisation
combinatoire. La programmation dynamique permet de résoudre des problèmes en les
décomposant en sous-problèmes plus petits et en mémorisant les solutions de ces
sous-problèmes pour éviter les calculs redondants. Nous allons voir comment
utiliser la programmation dynamique pour résoudre des problèmes d'optimisation
de contraintes tels que le problème du sac à dos (knapsack problem).