############################
Applications de la récursion
############################

..  contents:: Contenu de la page
    :depth: 3

Dans la suite du cours, nous allons utiliser de nombreuses fois le principe de
la récursion. Dans cette section, nous appliquons cependant déjà ce principe à
quelques problèmes pour montrer la puissance et l'élégance de ce principe.

Conversion d'un entier en chaîne dans n'importe quelle base
===========================================================

On veut convertir un entier en une chaîne de caractères dans une base quelconque
entre 2 (binaire) et 16 (héxadécimal). Par exemple, convertir l'entier ``10`` en
sa représentation de chaîne en décimal comme ``"10"``, ou en sa représentation
de chaîne binaire ``"1010"``. Bien qu'il existe de nombreuses approches pour
résoudre ce problème, la formulation récursive du problème est particulièrement
élégante.

Prenons un exemple concret en utilisant la base 10 et le nombre 769. Supposons
qu'on ait une séquence de caractères correspondant aux 10 premiers chiffres,
comme ``conv_string = "0123456789"``. Il est facile de convertir un nombre
inférieur à 10 en une chaine équivalente en le recherchant dans la séquence. Par
exemple, si le nombre est 9, alors la chaîne est correspondante est
``conv_string[9]``. Si on peut s'arranger pour diviser le nombre 769 en trois
nombres à un chiffre, 7, 6, et 9, il est alors simple de le convertir en une
chaîne de caractères en base 10. Un nombre inférieur à 10 semble être un bon cas
de base.

Notre cas de base suggère que l'algorithme global comportera trois étapes:

#.  Réduire le nombre d'origine à une série de nombres à un chiffre.

#.  Convertir le nombre à un chiffre en une chaîne de caractères à l'aide d'une
    recherche dans ``conv_string``.

#.  Concaténer les chaînes de caractères à un chiffre pour former le résultat
    final.


Code à étudier
--------------

Voici le code de l'algorithme en question qui fonctionne pour n'importe quelle
base entière :math:`base \leq 16` vers laquelle on voudrait convertir le nombre.
Étudiez ce code avec le Codelens. Si nécessaire, lisez ensuite l'explication du
code.

..  admonition:: Conseil

    Testez la fonction ``to_str`` sur quelques nombres naturel ``n`` et modifiez
    la base ``base`` pour observer le fonctionnement de l'algorithme.

..  activecode:: convert_decimal_to_base_a.py

    def to_str(n, base):
        alphabet = "0123456789ABCDEF"
        if n < base:
            return alphabet[n]
        else:
            return to_str(n // base, base) + alphabet[n % base]

    print(to_str(1453, 16))

L'étape suivante consiste à déterminer comment changer d'état et progresser vers
le cas de base. Puisque l'on travaille avec un entier, considérons les
opérations mathématiques qui pourraient réduire un nombre. Les candidats les
plus probables sont la division et la soustraction. En ce qui concerne la
soustraction, on ne voit pas bien ce qu'il faudrait soustraire de quoi. La
division entière avec reste (euclidienne) fournit une direction plus
prometteuse. Voyons ce qui se passe si l'on divise un nombre par la base vers
laquelle nous essayons de le convertir.

En utilisant la division entière pour diviser 769 par 10, on obtient 76 avec un
reste de 9, ce qui nous donne deux bons résultats. Tout d'abord, le reste est un
nombre inférieur à la base qui peut être converti en chaîne immédiatement par
recherche. Deuxièmement, on obtient un nombre plus petit que notre nombre
original, ce qui nous rapproche du cas de base où il nous reste un nombre à un
chiffre  inférieur à la base vers laquelle on veut convertir. Le problème se
réduit maintenant à convertir 76 vers sa représentation en chaîne de caractères
dans la base donnée. Encore une fois, on utilise la division entière plus le
reste pour obtenir les résultats de 7 et 6 respectivement. Enfin, nous avons
réduit le problème à la conversion 7, ce qui est trivial puisqu'il s'agit d'un
nombnre à un chiffre qui satisfait le cas de base :math:`n<base`, où
:math:`base=10`. La série d'opérations que nous venons d'effectuer est illustrée
à la figure :ref:`label-recursive-number-base-conversion`. Notez que les nombres
qui nous intéressent  se trouvent dans les cases restantes sur la droite du
diagramme.

..  figure:: figures/toStr.png
    :align: center
    :width: 60%

    Conversion d'un nombre entier décimal en chaine de caractère en base 10


Notez qu'à la ligne 3, on vérifie le cas de base où :math:`n` est inférieur à la
base vers laquelle on veut convertir. Quand on détecte le cas de base, on arrête
la récursion et on retourne simplement la chaîne de caractères de la séquence
``alphabet``. À la ligne 6, on satisfait à la fois au deuxième et au
troisième principe de la récursion - en faisant l'appel récursif et en réduisant
la taille du problème - grâce à la division euclidienne.

Traçons à nouveau l'algorithme ; en convertissant cette fois-ci le nombre 10 en
sa représentation binaire (``"1010"``).

..  figure:: figures/toStrBase2.png
    :align: center
    :width: 60%

    Conversion d'un nombre entier décimal en base 2 (binaire)




