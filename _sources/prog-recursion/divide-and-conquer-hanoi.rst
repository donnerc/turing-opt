Stratégie "Divide and Conquer" : tours de Hanoï
###############################################

..  contents:: Contenu de la page
    :depth: 3

Introduction
============

La récursion est une méthode de résolution de problèmes qui consiste à
décomposer un problème en sous-problèmes de plus en plus petits jusqu'à ce qu'il
se réduise à un problème suffisamment petit pour qu'il puisse être résolu de
façon triviale. Habituellement, la récursion implique une fonction qui s'appelle
elle-même. Bien que cela ne semble pas grand-chose à première vue, la
récursivité permet d'écrire des solutions élégantes à des problèmes qui,
autrement, seraient très difficiles à programmer.

Introduction à la pensée récursive
==================================

Les vidéos ci-dessous présentent bien la philosophie "diviser pour régner", qui
est un paradigme de résolution de problèmes fondamental en sciences, tout
particulièrement en informatique.

Le jeu des tours de Hanoi
-------------------------

..  youtube:: w_9P7icYh7Y
    :divid: presentation-tours-hanoi
    :width: 800
    :height: 430

Présentation de la stratégie de résolution
------------------------------------------

..  youtube:: U3nGNJTxYc4
    :divid: resolution-recursive-tours-hanoi
    :width: 800
    :height: 430

Voici en résumé la description de la méthode récursive présentée dans la vidéo.
Cette stratégie est très importante, car elle peut être utilisée pour résoudre
un très grand nombre de problèmes importants.

..  admonition:: Description de la stratégie pour résoudre les tours de Hanoi

    Bouger :math:`N`  disques depuis la première tige (tige A) vers la troisième
    tige (tige C) peut se réduire aux trois problèmes suivants :

    #.  Déplacer :math:`N-1` disques de la tige A à la tige B
    #.  Déplacer le gros disque tout en bas de la tige A à la tige C
    #.  Déplacer les :math:`N-1` disques de la tige B vers la tige C

    Il va sans dire que l'on peut raisonner de la même manière pour déplacer les
    :math:`N-1` disques de la tige A à la tige B: il suffit de réduire le problème :

    #.  Déplacer :math:`N-2` disques de la tige A à la tige C
    #.  Déplacer le disque qui se trouve en haut de la pile A (l'avant-dernier) vers la pile B
    #.  Déplacer les :math:`N-2` disques de la tige C vers la tige B

    etc ...

    Au voit bien que ce processus est récursif et que l'on peut en fait définir une
    fonction récursive qui va opérer les mouvements. Le cas de base
    consiste à déplacer une pile de taille 1 (à savoir un seul disque), ce qui peut
    se faire de manière triviale. 

Mettre les mains à la pâte
==========================

Consigne
--------

#.  Coder les mouvements pour déplacer les 4 disques de la pile A vers la pile C.

    ..  reveal:: 817fbb7f-1792-40c8-aeb6-5a08dfe77bee
        :showtitle: Solution

        ..  admonition:: Solution

            Les mouvements sont les suivants
        
            ::

                A > B
                A > C
                B > C
                A > B
                C > A
                C > B
                A > B
                A > C
                B > C
                B > A
                C > A
                B > C
                A > B
                A > C
                B > C

#.  Combien faut-il de mouvements au minimum pour résoudre le problème pour :math:`N = 4`.

    ..  reveal:: ede16855-df4f-4996-a6a6-06b4333a3dfd
        :showtitle: Solution

        ..  admonition:: Solution
            :class: important

            Il faut 15 déplacements, à savoir :math:`2^N - 1` déplacements.

#.  Compléter la fonction récursive ``move_disks()`` suivante pour résoudre le
    problème pour une taille :math:`N` quelconque :

    ..  activecode:: solve_hanoi_rec.py
        
        def move_disks(n, s_from, s_to, s_tmp):
            # compléter le code ici
            pass

    où ``s_from`` est la pile de départ, ``s_to`` la pile d'arrivée et ``s_tmp``
    la pile intermédiaire (temporaire).

    ..  admonition:: Conseil
        :class: note

        Si vous n'arrivez pas à trouver la réponse, regardez plus attentivement
        les deux vidéos présentant la stratégie "diviser pour régner" au début
        du chapitre.

        Pour implémenter la stratégie à l'aide de fonctions récursives,
        n'hésitez pas à vous aider de la page Wikipedia sur les tours de Hanoi
        ou une autre source sur le Web.

    ..  reveal:: 82d3dbd8-01c7-4675-aba4-df7b398e72fa
        :showtitle: Solution

        ..  admonition:: Solution
            :class: important

            La fonction permettant de résoudre le problème est bien plus simple
            que ce que pourrait laisser croire la difficulté du problème
            lorsqu'on le résout à la main :

            ..  code-block:: python
                :linenos:

                def move_disks(n, s_from, s_to, s_tmp):
                    if n > 0:
                        move_disks(n-1, s_from, s_tmp, s_to)
                        print(f"{s_from} > {s_to}")
                        move_disks(n-1, s_tmp, s_to, s_from)

                move_disks(4, "A", "B", "C")

            À l'aide de cette fonction, le problème peut donc se résoudre de la
            manière suivante si les variables ``A``, ``B`` et ``C`` désignent
            les trois tours :

            ::

                move_disks(n, A, C, B)


#.  Sans utiliser l'ordinateur, déterminer le nombre de mouvements nécessaires
    pour résoudre le problème pour :math:`N = 5`, :math:`N = 6` et :math:`N = 10`.

    ..  reveal:: e2834bdb-6506-4c40-acb9-098efb2cac5c
        :showtitle: Solution

        ..  admonition:: Solution
            :class: important

            Pour déplacer une pile de taille :math:`N`, il faut déplacer deux
            fois une pile de taille :math:`N-1` plus encore un disque. On a donc
            la relation de récurrence suivante pour le nombre de déplacements:

            ..  math::

                x_{n} = 
                    \begin{cases}
                    1 & \text{si $n = 1$},\\
                    2\cdot x_{n-1} + 1 & \text{si $n > 1$}
                    \end{cases}

            Ceci correspond à la suite de nombres 

            ..  math::

                1, 3, 7, 15, 31, 63, 127, 255 \ldots

            On constate que c'est presque la suite des puissances de 2 :

            ..  math::

                2, 4, 8, 16, 32, 64, 128, 256 \ldots = 2^n

            Plus précisément, c'est la suite :math:`x_n = 2^n - 1`

             ..  math::

                2, 4, 8, 16, 32, 64, 128, 256 \ldots = 2^n - 1

            On a donc, pour :math:`N = 5` 
            
            ..  math:: 
            
                x_N = 2^{N} - 1 = 2^5 -1 = 31

            et :math:`x_6 = 63` et  :math:`x_{10} = 1023`.


Curiosité : lien avec les nombres binaires
==========================================

En étudiant le problème des tours de Hanoï, on constate qu'il entretien un lien
très étroit avec le fonctionnement des nombres binaires. 

..  note:: Les tours de Hanoï et le binaire (variante : base 3)

    http://accromath.uqam.ca/2016/02/les-tours-de-hanoi-et-la-base-trois/