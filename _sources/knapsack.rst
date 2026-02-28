.. _01-knapsack.rst:

Problème de sac à dos (01-knapsack)
###################################

..  contents:: Contenu de la page
    :depth: 3

Introduction
============

Le problème du sac à dos est un problème algorithmique classique connu pour être
NP-complet. Ce problème d'optimisation combinatoire peut être formulé de très
nombreuses manières et il existe de nombreuses variantes du problème. Cette
section présente la variante la plus simple et classique, le **0-1 Knapsack
Problem**. Comme ce problème est NP-complet, on ne connaît pas d'algorithme
efficace pour résoudre de manière exactes de grosses instances du problème. Il
existe de très nombreuses approches possibles. Parmi les approches exactes, il y
a notamment la programmation dynamique et la programmation en nombres entiers
(0-1 Integer Programming) qui sont capables de résoudre de petites et moyennes
instances du problème. Pour résoudre les instances plus grandes, il faut
recourir à des méthodes par approximation que nous n'aborderons pas ici.

..  
    admonition:: Références

    - Présentation donnée dans le cadre du programme GymInf à l'EPFL :
      https://gyminf-ads2-dp.surge.sh/knapsack-dp.html
    - https://fr.wikipedia.org/wiki/Problème_du_sac_à_dos
    

Présentation du problème
========================

Présentation intuitive
----------------------

..  only:: html

    ..  youtube:: HvAK6HxZ190
        :align: center
        :width: 640
        :height: 360
        :divid: knapsack-short-introduction-short

    
    ..  youtube:: w0Q-X4F2iFU
        :align: center
        :width: 640
        :height: 360
        :divid: knapsack-short-introduction-promath-short

Applications
------------

Le problème du sac à dos possède de nombreuses applications pratiques. On peut
notamment citer le problème d'allocation d'actifs en finance. Dans ce contexte,
on a une somme à investir, qui correspond à la capacité maximale du sac à dos et
des projets ou investissements qui demandent tous une certaine partie du capital
à investir et une "promesse" de retour sur investissement. Comme il y a souvent
plus de projet à financer que d'actifs disponibles, on peut déterminer les
projets à financer en priorité en résolvant un problème du sac à dos. Le
problème revêt aussi une grande importance dans le domaine de la logistique.

Un des premiers protocoles cryptographiques à clé publique était basé sur la
résolution d'un problème du sac à dos.

Le problème revêt également une certaine importance théorique vu qu'il s'agit
d'un problème NP-complet. Découvrir un algorithme polynomial pour le sac à dos
reviendrait à résoudre P = NP.

Dépôt de base
=============

Faites un fork du dépôt https://github.com/informatiquecsud/01-knapsack dans
votre GitHub et travaillez à l'aide de Gitpod.

.. _small-instance-by-hand:

Résoudre une petite instance à la main
======================================

..  shortanswer:: 01-knapsack-intro-alamain

    Résolvez à la main la petite instance suivante du problème et notez, pour
    chaque article, si vous le mettez dans le sac ou non (volume du sac : 50
    litres). Calculez également le volume emporté dans le sac, ainsi que la
    valeur nutritive emportée.

    ..  csv-table:: Articles disponibles dans la réserve alimentaire
        :header-rows: 1
        :class: longtable

        No article, Description, Volume [l], Valeur nutritive [kcal]
        0, Paquet de pâtes, 13, 2600
        1, Paquet de pâtes, 13, 2600
        2, Paquet de pâtes, 13, 2600
        3, Pommes, 10, 500
        4, Paquet de riz, 24, 4500
        5, Yogourt, 11, 960

..  note:: Conseil

    Faites une feuille de calcul dans Excel au lieu de faire les calculs sur la
    calculatrice.

Formulation mathématique
========================

Mathématiquement, le problème peut se formuler de la manière suivante. Comme
pour tout problème d'optimisation combinatoire, on utilise des **variables de
décision** pour formuler le problème, ainsi que des **contraintes** et une
**fonction objectif** à optimiser. On considère que :math:`N` est le nombre
d'objets emportés. Les données du problème sont les suivantes:

..  admonition:: Données connues du problème

    On peut représenter le problème à l'aide de trois listes et de la capacité
    ``C`` du sac à dos:

    - La liste ``W`` dont chaque élément ``W[i]`` indique le poids (weight) de
      l'objet numéro :math:`i`.

    - Liste ``V`` dont chaque élément ``V[i]`` indique la valeur de l'objet
      numéro :math:`i`.

..  admonition:: Variables de décision

    Dans ce problème, les variables de décision sont des variables binaires
    :math:`x_i \in \{0, 1\}` définies de la manière suivante pour tout
    :math:`0 \leq i \leq N`,

    ..  math::

        x_i = \begin{cases}
        1 &\text{si on prend l'objet $i$} \\
        0 &\text{sinon} \\
        \end{cases}

    Pour l'instance considérée en exemple, il y a six variable de décision
    :math:`x_0, \ldots, x_5`, une pour chacun des articles que l'on peut
    potentiellement emporter.


..  admonition:: Contraintes

    Dans un problème d'optimisation combinatoire les contraintes doivent être
    respectées pour qu'une solution soit considéré comme valide (*feasible* en
    anglais). Dans le cas du problème du sac à dos, il n'y a qu'une seule
    contrainte, formulée comme une inéquation linéaire:

    ..  math::

        \sum_{i=0}^{N-1}
        x_i \cdot W[i]
        \leq 
        C

    Pour l'instance considérée en exemple, pour un sac à dos de 50 litres, la
    contrainte s'écrit

    ..  math::
        
        x_0 \cdot 13 + x_1 \cdot 13 + x_2 \cdot 13 + x_3 \cdot 10 + x_4 \cdot 24 + x_5 \cdot 11 \leq 50

..  admonition:: Fonction objectif

    La fonction objectif indique la valeur qui doit être optimisée. Dans notre
    cas, il s'agit de la valeur nutritive totale emportée dans le sac à dos. En
    l'occurrence, la valeur objectif à optimiser est donnée par la fonction

    ..  math::

        f(X) = f(x_0, \ldots, x_{N-1}) = \sum_{i=0}^{N-1} x_i \cdot V[i]

    Pour l'instance considérée en exemple, la fonction objectif est donc

    ..  math::

        f(X) &= f(x_0, x_1, x_2, x_3, x_4, x_5) \\
        &= x_0 \cdot 2600 + x_1 \cdot 2600 + x_2
        \cdot 2600 + x_3 \cdot 500 + x_4 \cdot 4500 + x_5 \cdot 960

        
Résoudre le problème du sac à dos consiste à attribuer à chaque variable de
décision :math:`x_i` une valeur dans :math:`\{0, 1\}` de telle manière que
toutes les contraintes soient satisfaites. De plus, il faut trouver une solution
optimale, à savoir une solution qui maximise la fonction objectif :math:`f`. 

Méthodes de résolution
======================

Tout au long du cours, nous verrons plusieurs approches pour résoudre le
problème du sac à dos, notamment

- la programmation dynamique (DP)
- la programmation par contraintes (PPC) 
- les méthodes d'approximation et les métaheuristiques d'optimisation
  combinatoire
- la programmation en nombres entiers (0-1 Integer Programming) si le temps le
  permet.

Mais avant toute chose, nous allons poser les bases en considérant des problèmes
de satisfaction de contraintes, dans lesquels il ne s'agit pas d'optimiser une
fonction objectif, mais simplement de trouver une solution qui satisfait les
contraintes. 