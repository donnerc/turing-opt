.. _prog-recursive-pile-appels:

Pile d'appels
#############

..  contents:: Contenu de la page
    :depth: 3

Pour bien comprendre les algorithmes récursifs, il faut comprendre comment la
récursion est réalisée. Pour cela, nous allons reprendre notre exemple de la
somme des éléments d'une liste de nombres ``numbers`` de la section
:ref:`algorithmes-recursifs.rst`.

Le code dont on veut étudier et comprendre l'exécution est 

..  code-block:: python
    :linenos:

    def rec_sum(numbers):
        if numbers == []:
            return 0
        else:
            return numbers[0] + rec_sum(numbers[1:])

    n = 3
    numbers = list(range(n))
    print(rec_sum(numbers))

Pour bien comprendre ce programme, on peut rajouter quelques variables qui vont
faciliter la compréhension de l'exécution dans le débogueur de l'environnement
de programmation, tout en faisant au fond exactement le même calcul.

..  activecode:: 1498c5d0-5fa1-4916-aadc-be9bc142f152
    :language: webtp

    def rec_sum(numbers):
        if numbers == []:
            return 0
        else:
            head = numbers[0]
            tail = numbers[1:]
            sum_tail = rec_sum(tail)
            res = head + sum_tail
            return res

    n = 4
    numbers = list(range(n))
    print(rec_sum(numbers))


Lorsqu'on exécute cette fonction avec le CodeLens, on peut observer la pile
d'appels et l'espace d'exécution réservé pour chaque nouvel appel récursif. À
chaque fois, les variables locales ``numbers``, ``head``, ``tail``, ``sum_tail``
et ``res`` sont différentes des précédents appels. Chaque appel récursif
consomme donc de la mémoire supplémentaire.


Détails du déroulement de l'algorithme récursif
===============================================

Pour comprendre le déroulement de l'algorithme, il faut se rappeler la manière
dont les appels de fonction sont gérés. À chaque fois qu'une fonction est
appelée, Python crée un nouvel espace d'exécution au sommet de la **pile
d'appels** (*call stack* en anglais) contenant les variables locales utilisées
durant l'exécution (et donc les paramètres qui sont des variables locales).

..  figure:: figures/animation-somme-recursive-3.gif
    :align: center
    :width: 100%

    Animation de l'état de la mémoire et du déroulement de la somme récursive
    des éléments de la liste ``numbers``.


..  admonition:: Présentation PowerPoint

    ..
        ..  raw:: html

            <iframe
            src="https://eduetatfr.sharepoint.com/teams/CSUD-GT-BrancheInformatiqueBureautique/_layouts/15/Doc.aspx?sourcedoc={5eb3276f-ec0d-4715-9dbc-119444a126f5}&amp;action=embedview&amp;wdAr=1.7777777777777777&amp;wdEaaCheck=1"
            width="600px" height="370px" frameborder="0">Ceci est un document <a
            target="_blank" href="https://office.com">Microsoft Office</a> incorporé,
            avec <a target="_blank"
            href="https://office.com/webapps">Office</a>.</iframe>

    ..  raw:: html

        <iframe
        src="https://eduetatfr.sharepoint.com/teams/CSUD-GT-BrancheInformatiqueBureautique/_layouts/15/Doc.aspx?sourcedoc={05a49bbe-b2b9-4592-9f70-7cb4be52daf6}&amp;action=embedview&amp;wdAr=1.7777777777777777&amp;wdEaaCheck=1"
        width="600px" height="370px" frameborder="0">Ceci est un document <a
        target="_blank" href="https://office.com">Microsoft Office</a>
        incorporé, avec <a target="_blank"
        href="https://office.com/webapps">Office</a>.</iframe>

Autre visualisation statique de la somme récursive
--------------------------------------------------

L'illustration suivante montre comment faire la somme récursive de la liste
``numbers = [5, 2, 4, 8]``. Les cartes représentent les contextes d'exécution
des différents appels de la fonction récursive (avec les valeurs des variables
locales).

..  figure:: figures/rec_sum_cards.png
    :align: center
    :width: 100%

    Visualisation de la somme récursive de la liste ``numbers = [5, 2, 4, 8]``
    avec des piles de cartes qui indiquent ce qui est calculé à chaque étape.
    Source: The Recursive Book of Recursion, chapitre 3, page 48
    (https://eduetatfr.sharepoint.com/:b:/t/CSUD-GT-BrancheInformatiqueBureautique/EeVgaIX6ibpAsdEJyLYa1bwBQVx7PlQyw60XMoYFvikMIg?e=Tfo45d).


Erreur ``RecursionError``
=========================

Puisque chaque nouvel appel récursif consomme de la mémoire, on ne peut pas
faire un nombre infini d'appels sans saturer la mémoire. C'est pour cette raison
que Python instaure une limite maximale au nombre d'appels récursifs que l'on
peut effectuer. Si une fonction récursive dépasse ce seuil, Python interrompt le
programme avec une exception de type ``RecursionError``.

Exécutez le programme ci-dessous. Comme la liste ``numbers`` contient 9000
nombres à additionner, il produit cette erreur. La limite dépend de
l'interpréteur Python utilisé.

..  activecode:: c01f247b-ea12-47d8-a43a-5a47ce00cb04
    :language: webtp

    def rec_sum(numbers):
        if numbers == []:
            return 0
        else:
            head = numbers[0]
            tail = numbers[1:]
            return head + rec_sum(tail)

    n = 9000
    numbers = list(range(n))
    print(rec_sum(numbers))


Déterminer le nombre maximal d'appels récursifs
===============================================

..  admonition:: note

    La fonction ``getrecursionlimit`` et ``setrecursionlimit`` dont il est
    question ci-dessous ne sont pas disponibles dans le Python sur le site.

On peut connaître la limite fixée par Python avec la fonction
``getrecursionlimit()`` du module ``sys``.

..  code-block:: python

    import sys
    print(sys.getrecursionlimit())

On peut modifier cette limite en appelant la fonction ``setrecursionlimit`` avec
un paramètre:


..  code-block:: python

    import sys
    new_recursion_limit = 2000
    print(sys.setrecursionlimit(new_recursion_limit))

Exercices
=========

Exercice 1
----------

..  activecode:: set_rec_limit_for_rec_sum.py
    :language: webtp

    Essayez d'exécuter le programme suivant sans erreur en modifiant la limite
    d'appels récursifs.

    ~~~~

    def rec_sum(numbers):
        if numbers == []:
            return 0
        else:
            head = numbers[0]
            tail = numbers[1:]
            return head + rec_sum(tail)

    n = 9000
    numbers = list(range(n))
    print(rec_sum(numbers))
