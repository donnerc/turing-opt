..  header::

    OCI 3, Programmation Orientée Objets,                  Prénom : ....................... / Note : ...........

..  footer::

    Page ###Page### / ###Total###


***************************************
Programmation Orientée Objets : examen pratique
***************************************

..  admonition:: Consignes générales

    *   Barème : ...... / 25 points
    *   Si vous ne parvenez pas à voir comment coder quelque chose en Python,
        expliquez au mieux les étapes de résolution en pseudo-code et/ou en français dans un commentaire
    *   Compléter le fichier qui fourni
        
Code de base
============

..  admonition:: Téléchargement

    :download:`frogger_complet.py`

..  literalinclude:: frogger_complet.py
    :language: python

Question 1
==========

Remplacez le fond du jeu de base par le fond suivant 

..  only:: html

    ..  figure:: figures/riviere.gif
        :width: 80%
        :align: center

        Fond à utiliser

Question 2
==========

Remplacez les voitures du jeu de base par des troncs d'arbres basés sur
l'image de :math:`180 \times 42` pixels ci-dessous :

    ..  figure:: figures/fond.png
        :width: 30%
        :align: center

        Troncs d'arbres

Pour ce faire, créer une classe ``Tronc`` basée sur la classe Véhicules. 

Question 3
==========

Dans la version de base, la grenouille se déplace de 5 pixels dès que 

Gestion événements ==> pas de répétition ==> presser à chaque touche pour faire un saut
Gestion collision avec troncs arbres
Modification move() pour se déplacer avec arbres
Détection si elle arrive dans les bords gauche / droit ==> faire qu'elle ne disparaisse pas
Faire qu'elle meurt si elle tombe dans l'eau
Certains troncs disparaissent après un certain temps (aléatoire)
