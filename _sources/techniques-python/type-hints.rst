..  _type-hints-basics:

Annotations de type
###################

..  contents:: Contenu de la page
    :depth: 3


..  admonition:: Référence
    :class: info

    Vous trouverez un aide-mémoire concernant les annotations de types sous
    https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

Comme nous l'avons vu dans la section :ref:`types`, Python est un langage à
typage dynamique. Le type de données d'une variable peut donc changer à tout
moment au cours de l'exécution du programme. Si cette fonctionnalité permet
d'aborder Python sans prise de tête au niveau du type de variables, les
professionnels se méfient de cette fonctionnalité, car elle permet aussi de
faire des erreurs au niveau des types des variables.

Pour remédier à ce désavantage du typage dynamique, Python a introduit la notion
d'**annotation de types**. Il s'agit d'une notation supplémentaire utilisée lors
de la création de variables et la définition de fonctions.

Définir une variable en spécifiant son type
===========================================

Les annotations de type permettent de spécifier le type d'une variable lors de
sa création. Le programme ci-dessous crée par exemple une variable ``nom`` de
type ``str`` et une variable ``poids`` de type ``float``.

..  activecode:: 0AD681C1-7DF2-4202-911E-AA11288B0F7E

    nom: str = input("Indiquez votre nom: ")
    poids: float = float(input("Indiquez votre poids [kg]: "))

Vous avez sans doute remarqué l'annotation de type après le nom de la variable.
La syntaxe est la suivante:

::

    nom_variable: type = valeur

Définition de fonctions avec indications des types
==================================================

On peut également clarifier la définition des fonctions en indiquant le type de
données de ses arguments et de sa valeur de retour. Le programme ci-dessous
définit la fonction ``count`` qui prend deux paramètres :

* ``text``, qui est une chaine de caractères
* ``char_to_find``, qui est un caractère à chercher dans la chaine
* ``start``, qui est l'indice du caractère à partir duquel chercher le caractère ``char_to_find``
* ``match_case``, qui est un booléen indiquant s'il faut tenir compte de la casse 

Cette fonction compte le nombre d'occurrences du caractère ``char`` dans la
sous-chaîne de la chaîne ``text`` qui commence à la position ``start`` et
s'étend jusqu'à la fin de la chaîne.

..  activecode:: 927E22A7-D4FC-414B-B9F2-79EECFC92561

    def count(text: str, char_to_find: str, start: int, match_case: bool) -> int:

        substring = text[start:]
        if not match_case:
            char_to_find = char_to_find.lower()
            substring = substring.lower()

        count = 0
        for c in substring:
            if c == char_to_find:
                count += 1

        return count

    print(count("Ananas", "a", 0, True))
    print(count("Ananas", "a", 0, False))

..  admonition:: Réflexion
    :class: info

    Dès à présent, vous devez prendre l'habitude de toujours indiquer le type
    des paramètres et de la valeur de retour d'une fonction. Cette pratique
    présente notamment les avantages suivants:

    * Documentation : le fait d'indiquer les types de données de chaque
      paramètre permet de rendre le code plus clair
    
    * Utiliser les annotations de types correspond un peu à la pratique de la
      physique de spécifier les unités des différentes grandeurs manipulées.
      Cela permet notamment de faire un "contrôle d'unités" en physique. Dans le
      contexte de la programmation, cela permet à des outils automatisés de
      faire certaines vérification de type (type checking) et de détecter
      certaines erreurs d'étourderie.

    * Cela permet à certains éditeurs modernes de mieux comprendre le code et de
      fournir une meilleure assistance automatique pendant l'écriture du code
      (complétion automatique, linting, etc ...).

    En somme, les annotations de types représentent un certain coût initial (il
    faut écrire un peu plus), mais elles améliorent de manière générale la
    qualité du code.


Union de types
==============

Si une variable peut prendre plusieurs types, on peut l'indiquer avec une barre
verticale (pipe):

..  code-block:: python
    :linenos:

    username: str = 'guido'
    grade: int | float = get_grade(username)


Type ``Any``
============

Lorsqu'on ne sait pas quoi mettre comme type (si on débute avec les types) ou si
une fonction peut renvoyer des données dont le type pas très bien spécifié, on
peut utiliser le type ``Any``, qu'il faut toutefois importer depuis le module
``typing``:

..  code-block:: python
    :linenos:

    from typing import Any

    something: Any = get_something()


Alias de types
==============

Dans les versions récentes de Python, on peut créer des types personnalisés en
utilisant la syntase suivante:

..  code-block:: python
    :linenos:

    type Student = str
    type Number = int | float
    type Grade = Number

On peut ensuite utiliser ces types pour annoter des variables ou des fonction:

..  code-block:: python
    :linenos:

    def greet(student: Student) -> None:
        print(f"Hi {student}, How are you?")
    
    john: Student = "John Doe"

    greet(john)


Typage de listes
================

Pour spécifier le type d'une liste, on a généralement deux choix

1.  Tous les éléments de la liste doivent avoir le même type

    ..  code-block:: python
        :linenos:

        type Student = str

        def get_students() -> list[Student]:
            return ['guido', 'ada', 'alan']

        students: list[Student] = get_students()

2.  La liste peut contenir un peu n'importe quoi comme type de données (possible
    en Python, car il est dynamiquement typé):

    ..  code-block:: python
        :linenos:

        stuff: list[Any] = get_stuff()

Typage de tuples
================

Pour typer les tuples, on indique le type des différents éléments (pas
nécessairement tous pareils)

..  code-block:: python
    :linenos:

    type Student = tuple[str, str, int]

    s1 = ("Guido", "Van Rossum", 1956)

Si le tuple contient de nombreux éléments de même type, on le spécifie de la
manière suivante:

..  code-block:: python
    :linenos:

    type Number = int | float
    type Data = tuple[Number, ...]

    data: Data = (2, 4, 6, 3, 6,)


Typage des dictionnaires
========================

Le typage d'un dictionnaire dont les clés sont de type ``K`` et les valeurs de
type ``V``, on note l'annotation de type avec la syntaxe

::

    my_dict: dict[K, V] = get_dict(...)

Type d'une fonction
===================

L'annotation de type permettant de typer une variable de type fonction est assez
kabbalistique. L'annotation ci-dessous désigne par exemple une fonction dont le
premier paramètre est de type ``list[int]`` et dont la valeur de retour est
``None``.

..  code-block:: python
    :linenos:

    type SolutionHandler = Callable[[list[int]], None]


Rérérences sur le typage et les annotations de type
===================================================

- Niveau 1 (introduction) : https://fastapi.tiangolo.com/python-types/
- Niveau 2 (aide-mémoire) : https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
- Niveau 3 (niveau spécialiste) : L'ensemble de la documentation Mypy (le
  vérificateur de types de Python) : https://mypy.readthedocs.io/en/stable/
- Niveau 3 (documentation officielle) : https://docs.python.org/3/library/typing.html
 

Exercices
=========

Exercice 1
----------

..  activecode:: annotations-types-base-exercice-01

    Complétez le programme suivant avec les annotations de type appropriées:

    ~~~~

    age = 50
    poids = 43.5
    est_majeur = age >= 18
    message = "L'habit ne fait pas le moine."

    ====        

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):   

        def test_correct_annotations(self):
            tests = [
                ('age', int), 
                ('poids', float), 
                ('est_majeur', bool), 
                ('message', str)
            ]

            try: __annotations__
            except:
                self.assertTrue(False, "Aucune annotation de type détectée")
                return

            for varname, expected_type in tests:
                try:
                    feedback = f"La variable '{varname}' annotée correctement avec le bon type de données"
                    self.assertTrue(__annotations__.get(varname, None) == expected_type, feedback)
                except Exception as e:
                    self.assertTrue(False, str(e))
            
    myTests().main()    

Exercice 2
----------

..  activecode:: annotations-types-base-exercice-02

    Complétez la définition de la fonction ``caesar_encrypt`` définie ci-dessous
    en rajoutant une annotation de type pour chaque paramètre et pour la valeur
    de retour. La fonction chiffre le message ``plaintext`` en appliquant un
    décalage de ``shift`` positions dans l'alphabet. Les paramètres sont les suivants

    * ``plaintext`` est le texte en clair à chiffrer
    * ``shift`` indique le décalage de César dans l'alphabet

    La fonction retourne le message chiffré.

    ..  admonition:: Indication

        Vous n'avez pas besoin de comprendre précisément le fonctionnement de la
        fonction. Il suffit d'annoter correctement le type de ses paramètres et
        de sa valeur de retour.

    ~~~~

    def caesar_encrypt(plaintext, shift):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''

        for c in plaintext.upper():
            index = ord(c) - ord('A')
            shifted_index = (index + shift) % len(alphabet)
            cyphered = alphabet[shifted_index]
            result += cyphered

        return result

    ====

    from unittest.gui import TestCaseGui
    import re

    class myTests(TestCaseGui):   

        def test_func_annotations(self):
            code = self.getEditorText()

            expected_params_annotation = [
                ('plaintext', str), 
                ('shift', int)
            ]
            expected_return_annotation = str

            if not caesar_encrypt.__annotations__:
                self.assertTrue(False, "Aucune annotation détectée dans la définition de la fonction")
                return

            for argname, argtype in expected_params_annotation:
                self.assertTrue(caesar_encrypt.__annotations__.get(argname, None) == argtype,
                    f"L'annotation du paramètre {argname} est correcte")

            self.assertTrue(
                caesar_encrypt.__annotations__.get('return', "No return") == expected_return_annotation,
                "L'annotation de la valeur de retour est correcte"
            )

            
    myTests().main()
