Arbres binaires de recherche (Binary Search Trees)
##################################################

..  contents:: Contenu de la page
    :depth: 3

..  reveal:: ea3b1503-aae5-4404-8525-aee8665cd0a1
    :showtitle: Code pour générer les arbres
    :instructoronly:

    L'idée de ce code est de permettre de produire le code DOT pour générer
    les visualisations des abres dans https://dreampuf.github.io/GraphvizOnline/

    ..  literalinclude:: bst/scripts/bst2dotfile.py
        :language: python
    
    https://webtigerpython.ethz.ch/?code=NobwRAdghgtgpmAXGGUCWEB0AHAnmAGjABMoAXKJMAMwCcB7GAAjXpZm3trKYGUzaGAOYBJAPIAdCGg5ceAZ1zypKiAGMANlHnymAEQCu2DWjXk4AaTi4AFAFEAHmrjYyrCAEpEUpr6bZtZQhVTUCmACFeABUAOXpiOBt6ACMAKzg1Mi8fPwkwPIKIPyYRDg04eAgKN3oi6i4mMgALOCYIeNb6agiMKFpcPjg-tSamKNo4OBzfAvz84KK_aQ0AfTV6AyqmAF4mAAZVYoTulZWMNDJTm3k4DWoCJgBraweANygNAzgHgImq7biEG-THK1DIANqwMEQia4MBcGyi2Kvhud0wzwGuwx02RqOomHen1au0JXxxxTxOD6cC2u1-NLI5L8lNBPF2rKZKNu-OhsJ2TF5jIWRzgJxul1Z125D3aCURyOZ3MwrP5sqmSOREzIBloRRZoqFOOOTBW4pWgqldxlHXlCqYlMFqo6nIFcG1uvtSsFhz8xrOEBu3Et9zaNu8GuKaG6avR1h2u0pGPDds16Bu-iMJjMZEs1hdtyjoYSsYGAB5PWiky7ilqdXqlSqoBBiBX8azMP7A2QbGqPEwGpTTW6VpLe_mNDdkym_LWPQ60DCeE2W_PFx2MF2ezb-7RWx2zRax8LfaL_IIqis4MQhHB5MHbQrC_qwVPp2eMN3qAByPIgRPWABfPImAAWgAPiYX9nzIEsgLAL8PGrRU0XbbBz0uK8bzvRCIz8W5JyQ3xIliDpMGWNYNi2ABqXYAEZCPfKobG_ZYQGIuJi3I9ZNjIACmGAeQmigbA4G2TgPwedYNC4bYJmIABdABuBCGLQj9mJ_MA_yVDE4NAiC8lY9jSK4yjeLyFTcJmKyWG6VdYVfac1KY78oJ0wDgPAyCtPsmDdIsnC3y5NFBRwdDL2vW8bECu18LgRyU2Mzi0FWbjqLo1T0I0ozog4uAyJSiieL4gShJEsT6AkpgpJkuSlMsoLGM_TTtMrDywH07ycpI5LUrMuCGrtH1fD9c0XFoK48QfTU3TrJhqDyJLEgxbZWvxXS3g-L5VspUk4AAh5WR2hsDQOgUF1hY6Qou3jEPmI1T1OeQBEm7lpprWaPQmND71UKRQh0HpoH6XghloEZxkmRzZkKYpSmMCoGXIdx5oacJen6QZhlGSHbxxGH7o1UbzkuFZ7wS5CeXoeg2SYeEXUpeQ0AAL2JfZhqYY0NzgbgxrUYMHgxTaiXepYOn5JabCFpg9pix87K9ameDQXR4QphUHSVp0EnHAibIpRWafXAMee7I8U0ZlnWhoph6OPEbT25oM8UFl4Za2hF1e8mGbJEE3uEaFomClt3ZcaNhmlaYiOeKAABX5YCeaxEED1oMXDlh_aFFN476RO9pTyP3aJDOnezu1Y9nCAU_GL5bMzrt7QMNRnB0agDA0DRcEU_tI9oAB3FXWirpgADEPhuF0CZdQt4XjPcGBpr2DZCrXdkl6XZYYkfa_VF01B1P5LjVflNZpl1-6aFLWgP2gj5WNVl78Qt0-2XZb_vmMq31u1aDTVpDDGFMOYKwuAGIFm6OncsH8GQP1It_RqkZugwIvDGVkT83woOPuLd-h9YFoINAxYocUMHTiwXA4sKp165Q6CHXAwsvhy0QSvfETNWZMBtnbZhCod60DJD_XwJCiHP2QXg1BpFBSkJTOQk-uC774IkTdYRgiJzxWUciGRijFwSxoQkOhDCETqJYZgNh1sMoCOnLw_hD07JNHoP3AW_ZXDuHkBCIEotfD0A0MQU0ZBiAbFpooeQJi_EBIZkoEJ_iDC0xgEoUJ0T-T8HPKIMQ0UY5-Gct2PIxAFx_2wKMYiTAQB5CYcYxeMFMkRSwmkmymSbB5DgqUvwABiJgyQtCjHaVAUY0kyC6C6NVcWmBhnpJRBE56UTaZeJ8RMsJ9sZruiKLE2Z0SOajW-hNMmU0vYjwWmAdGwNcCg2xrjGw5SrpUxpmdUxFyTFWwAndP6EA6CMAFMuV5MhOAB0EgYag1ByiqGSM9CWGMjlgwhhMRIOEMS6HZCrbsf8IA3hsAAJgAKweBwj8v55Q6HyBwvUXcjxM5JyUI5VpdS8hl2EHkQWTCgUwTLnzKWDx4Q4X8WQag19-QMpMXYhxHhMA3jIHtGpFKsobJsByrl5RMVSDqdK6-OFVDivUgy5VEBWm8sEvYmpYAALySAA


Introduction
============

Nous avons vu que la recherche par dichotomie dans un tableau trié était très
efficace vu que la complexité de la recherche d'un élément est logarithmique. Le
problème de la recherche dichotomique dans les tableaux trié se situe au niveau
de l'insertion de nouveaux éléments dans le tableau. Cette insertion est
malheureusement en :math:`\mathcal{O}(n)` puisqu'il faut placer l'élément au bon
endroit dans le tableau pour qu'il demeure trié après l'insertion.

Pour pouvoir néanmoins utiliser une recherche efficace dans les situations qui
impliquent de nombreuses insertions, il est nécessaire de développer une
structure de données plus dynamique que les tableaux, qui permette de conserver
l'ordre des éléments. Les **arbres binaires de recherche** (binary search tree)
présentent une telle structure.

Fonctionnement d'un arbre binaire de recherche
==============================================

.. admonition:: Définition
   :class: important

   Un arbre binaire de recherche (ABR) est un arbre présentant les propriétés
   suivantes :

   *  Chaque nœud de l'arbre possède au plus deux fils : le fils gauche et le fils droit
   *  Tous les nœuds du sous-arbre gauche sont inférieurs à sa racine
   *  Tous les nœuds du sous-arbre droit sont supérieurs à sa racine
   *  Les sous-arbres gauche et droit sont également des arbres binaires de recherche

.. figure:: bst/figures/bst-example.png
   :align: center
   :width: 80%

   Exemple d'arbre binaire de recherche

Représentation des ABR
======================

Pour implémenter les ABR en Python, nous allons définir les classes

*  ``BinarySearchTree`` pour représenter l'arbre dans son ensemble
*  ``BSTNode`` pour représenter les nœuds qui constituent cet arbre

.. 
   La classe ``BSTNode`` représente les nœuds individuels de l'arbre et contient
   la valeur à y stocker (``self.value``) ainsi que la clé d'accès à l'élément
   (``self.key``) qui doit supporter les opérateurs de comparaison et sur la base
   de laquelle la propriété d'arbre binaire de recherche doit être vérifiée en
   permanence. Chaque nœud maintient donc une référence au fils gauche et au fils
   droit (sous-arbre gauche et sous-arbre droit). De plus, chaque nœud maintient
   une référence ``self.parent`` à son parent, ce qui permettra notamment de
   remonter d'un fils vers son parent.

le code suivant montre comment la classe ``BSTNode`` représente un nœud de
l'ABR :

.. literalinclude:: bst/scripts/bst.py
   :pyobject: BSTNode
   :linenos:

La classe ``BinarySearchTree`` ne contient essentiellement que deux variables
d'instance : une référence vers la racine de l'arbre (``self.root``) et le
nombre de nœuds présents dans l'arbre (``self.size``) :

.. code-block:: python

   class BinarySearchTree(object):
       """
       Implementation for Binary Search Trees
       """
       def __init__(self):
           self.root = None
           self.size = 0

On peut donc représenter l'ABR

.. figure:: bst/figures/simple-BST-example.png
   :align: center
   :width: 60%

de la manière suivante à l'aide des deux classes ``BinarySearchTree`` et
``BSTNode`` :

.. figure:: bst/figures/simple-BST-example-repr.png
   :align: center
   :width: 95%

..  admonition:: Visualisation avec Python Tutor

    On peut également utiliser l'outil Python Tutor pour visualiser l'exécution du
    programme suivant ainsi que la structure des données en mémoire :

    ::

        keys = [4,2,5]
        bst = BinarySearchTree()
        for x in keys:
            bst.insert(x, x)

    ..  figure:: bst/figures/simple-BST-example-repr-python-tutor.png
        :align: center
        :width: 50%

        Visualisation obtenue à l'aide de `Python Tutor <http://tinyurl.com/gozejez>`_



Opérations sur les ABR
======================

Recherche
---------

Le but premier des ABR est de pouvoir y trouver très facilement et rapidement
n'importe quel élément sur la base de sa clé d'accès. L'algorithme est très
simple et suit de près la logique de la recherche dichotomique.

Pour chercher la clé 6 dans l'ABR ci-dessous, on procède comme suit :

#. On compare la clé à chercher (6) avec la racine de l'arbre (8)
#. Comme 6 < 8, on poursuit la recherche dans le sous-arbre de gauche
#. On compare avec la racine du sous-arbre de gauche (3)
#. Comme 6 > 3, on poursuit la recherche dans le sous-arbre de droite
#. On compare avec la racine du sous-arbre de droit de (3) et on tombe sur la clé cherchée

.. figure:: bst/figures/bst_lookup.png
   :align: center

   Recherche de la clé 6 dans l'ABR : on parcourt l'ABR depuis la racine jusqu'à
   ce que l'on tombe sur le nœud qui possède la clé recherchée

.. admonition:: Remarque
   :class: tip

   Il est possible que la clé ne soit pas présente dans l'arbre. Dans ce cas,
   la recherche va se terminer sur une des feuilles de l'arbre sans avoir
   trouvé le nœud cherché. Nous verrons que c'est à cet endroit précis qu'il
   faudrait insérer le nœud en question.

   Par exemple, si l'on cherche le nœud de clé 5 qui ne se trouve pas dans
   l'ABR, la recherche se terminerait au sous-arbre droit (``None``) du nœud de
   clé 4, car c'est à cet endroit qu'il devrait se trouver et nulle part
   ailleurs.

Insertion d'un élément
----------------------

Comme vu précédemment, il suffit, pour insérer un nouvel élément de

*  Rechercher le nœud possédant la clé que l'on veut insérer
*  S'il est déjà présent dans l'arbre, il ne faut pas insérer un nouveau nœud mais remplacer son contenu par le nouveau contenu
*  S'il n'est pas présent dans l'arbre, il faut l'insérer à l'endroit même où la recherche s'est terminée

.. admonition:: Exemple
   :class: tip

   Insérons les clés suivantes dans l'ordre 8 - 3 - 10 - 1 avec le code

   ::

      bst = BinarySearchTree()
      for k in [8, 3, 10, 1]:
         bst.insert(k, k)

   L'arbre aura alors la forme suivante

   .. figure:: bst/figures/insertion-8-3-10-1.png
      :align: center
      :width: 80%

      Insertion des clés ``[8, 3, 10, 1]`` dans l'ordre

   Si l'on insère encore les clés ``[6, 4, 7, 14, 13]`` avec

   ::

      for k in [6, 4, 7, 14, 13]:
         bst.insert(k, k)

   on va obtenir l'arbre suivant

   .. figure:: bst/figures/insertion-all.png
      :align: center

      Arbre obtenu après l'insertion des clés ``[8, 3, 10, 1, 6, 4, 7, 14, 13]``
      dans l'ordre

.. admonition:: Remarque importante : ordre d'insertion
   :class: warning

   Il est très important de noter que l'ordre de l'insertion des nœuds est très
   significatif pour la forme finale de l'arbre. Pour vous en convaincre,
   essayez par exemple d'introduire les nœuds dans les ordres suivants
   (solutions en find de page) :

   *  ``[13, 7, 1, 6, 3, 10, 14, 8, 4]``
   *  ``[1, 3, 4, 6, 7, 8, 10, 13, 14]``
   *  ``[14, 13, 10, 8, 7, 6, 4, 3, 1]``


Suppression d'un élément
------------------------

Le plus difficile est de supprimer les nœuds d'un ARB. Fondamentalement, il
faut distinguer trois cas à traiter séparément :

*  Le nœud est une feuille et n'a pas de fils. La suppression est triviale dans ce cas
*  Le nœud ne possède qu'un seul fils et la suppression n'est pas trop compliquée
*  Il s'agit d'un nœud intérieur qui possède deux nœuds fils. Dans ce cas, la suppression est une jolie prise de tête qui nécessite passablement de code ...

Cas 1 : le nœud n'a pas de fils
++++++++++++++++++++++++++++++++++++++

Dans le premier cas, la suppression est évidente puisqu'il s'agit d'une feuille
de l'arbre : il suffit de supprimer le nœud en question en le remplaçant par un
sous-arbre vide (``None``).

.. figure:: bst/figures/bst_delete_0.png
   :align: center

   Suppression du nœud 1 qui est une feuille (pas de fils)

Cas 2 : le nœud n'a qu'un seul fils
++++++++++++++++++++++++++++++++++++++

Si le nœud ne possède qu'un seul fils, il suffit de supprimer le nœud en
question et de rattacher son unique fils à la place qu'il occupait comme fils de
son parent.

.. figure:: bst/figures/bst_delete_1.png
   :align: center

   Suppression du nœud 14 qui possède un seul fils

Cas 2 : le nœud possède deux fils
++++++++++++++++++++++++++++++++++++++

S'il s'agit d'un nœud intérieur possédant deux fils, il le remplacer par son
successeur qui est l'élément minimal de son sous-arbre droit. Il s'agit bien
entendu de la feuille qui se trouve le plus à gauche dans son sous-arbre droit.
Ainsi, pour supprimer le nœud 3 qui possède deux fils, il faut le remplacer par
son successeur qui est la feuille la plus à gauche de son sous-arbre de droit
(le nœud 4).

.. figure:: bst/figures/bst_delete_2.png
   :align: center

   Suppression du nœud 3 qui possède deux fils.

Implémentation des opérations
=============================

Recherche d'un nœud à partir de sa clé : méthode ``search(key)``
----------------------------------------------------------------

Méthode ``find_recursive(key)``
+++++++++++++++++++++++++++++++

La méthode ``BinarySearchTree.find_recursive`` effectue une recherche récursive :

.. literalinclude:: bst/scripts/bst.py
   :pyobject: BinarySearchTree.find_recursive
   :language: python
   :linenos:
   :prepend: class BinarySearchTree(object):
                 ...

.. admonition:: Remarque
   :class: tip

   Si la clé n'est pas trouvée lors de la recherche, la fonction
   ``find_recursive`` retourne la valeur ``None`` (lignes 10-11)

Méthode ``find_iterative(key)``
+++++++++++++++++++++++++++++++

La méthode ``BinarySearchTree.find_iterative`` effectue une recherche itérative,
de ce fait plus efficace, toujours selon le même principe :

.. literalinclude:: bst/scripts/bst.py
   :pyobject: BinarySearchTree.find_iterative
   :language: python
   :linenos:
   :prepend: class BinarySearchTree(object):
                 ...

Insertion d'un élément : ``BinarySearchTree.insert(key, value)``
----------------------------------------------------------------

Pour insérer un élément dans l'ABR, il suffit de chercher l'élément en question.
Si l'élément est déjà présent dans l'arbre, il ne faut pas réinsérer un deuxième
élément avec la même clé car on veut éviter les doublons difficiles à gérer. Si
l'élément n'est pas présent dans l'arbre, il faut l'insérer à l'endroit
(feuille) exact où la recherche s'est terminée sans succès.


.. literalinclude:: bst/scripts/bst.py
   :pyobject: BinarySearchTree.insert
   :language: python
   :linenos:
   :prepend: class BinarySearchTree(object):
                 ...

Suppression d'un éléments : ``BinarySearchTree.delete(key)``
------------------------------------------------------------

Pour supprimer un élément, il faut plusieurs méthodes qui permettent de traiter
les différents cas de figure et d'isoler les bouts de codes compliqués. Ceci
améliore la testabilité de la classe et rend le code plus compréhensible. Il
s'agit des méthodes suivantes

.. literalinclude:: bst/scripts/bst.py
   :pyobject: BinarySearchTree.delete
   :language: python
   :linenos:
   :prepend: class BinarySearchTree(object):
                 ...

.. literalinclude:: bst/scripts/bst.py
   :pyobject: BinarySearchTree.remove_node
   :language: python
   :linenos:

.. literalinclude:: bst/scripts/bst.py
   :pyobject: BinarySearchTree.replace_node
   :language: python
   :linenos:


Étude du code
=============

Le code complet de cette implémentation de l'ABR est téléchargeable sur le lien
suivant : :download:`bst/scripts/bst.py`.

Pour faciliter l'étude du code et le comprendre de manière appronfondie, il est
recommandé d'utiliser l'outil en ligne *Python Tutor* (http://pythontutor.com/)
afin de visualiser l'exécution du code lors de l'insertion, de la recherche et
de la suppression des éléments. Il est recommandé également d'imprimer le code
et de l'annoter sur une version papier.

Le Python Tutor http://tinyurl.com/hfvjvph permet d'exécuter le code pas à pas
pour visualiser son l'exécution de l'insertion, puis de la suppression de tous
les nœuds dans un ordre aléatoire. Chaque exécution engendrera donc une
visualisation différente mais l'arbre finira toujours par être vide (``bst.root ==
None``).

Tests unitaire
==============

Pour la petite histoire, le code étudié dans ce chapitre provient de la page
http://www.cs.uml.edu/~jlu1/doc/source/report/BinarySearchTree1.html. Ce code
comporte néanmoins un bogue qu'il n'a été possible de détecter qu'avec une suite
de tests unitaire présentée ci-dessous. Ce fichier doit se situer dans le même
dossier que le script ``bst.py`` présenté plus haut.

.. literalinclude:: bst/scripts/bst_test.py
   :language: python
   :linenos:
   :caption: Tests unitaires de la classe ``BinarySearchTree``


Implémentation alternative
==========================

Voici une implémentation alternative de l'ABR dans laquelle le nœud vers le
parent n'est pas explicitement stocké dans les nœuds. Il faut en revanche
modifier légèrement la recherche en utilisant la méthode ``__find_min`` et
``__find_and_parent`` retournent le nœud cherché ainsi que son parent.

.. admonition:: Source
   :class: tip

   Cette implémentation provient de https://www.cs.umd.edu/class/spring2008/cmsc420/bst.py

.. literalinclude:: bst/scripts/bst_implicit_parent.py
   :language: python
   :linenos:
   :caption: Implémentation de l'ABR avec un lien implicite vers le parent (méthodes ``__find_min`` et ``__find_and_parent``)

Matériel à télécharger
======================

Le code présenté dans chapitre est téléchargeable sous

*  :download:`bst/scripts/bst.py` pour l'implémentation de l'ABR
*  :download:`bst/scripts/bst_test.py` pour les tests unitaires garantissant le bon fonctionnement de la classe
*  :download:`bst/scripts/bst_implicit_parent.py` implémentation alternative dans laquelle le lien vers le parent n'est pas explicitement stocké dans les nœuds
*  https://www.dropbox.com/s/ykshs985rz2m5vn/etude-code-bst.pdf?dl=0 : version papier des deux codes pour faciliter l'étude
*  :download:`bst/files/exercices-donnee.pdf` : dossier d'exercices

Solutions
=========

Ordre d'insertion
-----------------

L'ordre d'insertion des éléments va fortement déterminer la forme (et
l'efficacité !!!) de l'arbre. Moins l'arbre est équilibré, le plus on va se
rapprocher d'une complexité linéaire au niveau de la recherche, pour perdre tous
les bénéfices de l'ABR dans le cas extrême d'un ordre d'insertion dans l'ordre
croissant ou décroissant:

.. figure:: bst/figures/solution-insertion-order.png
   :align: center
   :width: 95%

   Influence de l'ordre d'insertion des clés dans l'ABR
