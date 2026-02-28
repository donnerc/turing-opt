..  _regles-eval-expressions-booleennes:

Règles d'évaluation des expressions booléennes
##############################################

..  contents:: Contenu de la page
    :depth: 3


..  admonition:: Remarque
    :class: tip

    Cette section permet de comprendre certaines utiliations subtiles des
    opérateurs logiques et, parfois, de simplifier un peu le code.

    Les programmes professionnels utilisent abondamment les notions expliquées
    dans cette section.

Conversion de n'importe quelle valeur en booléen
================================================

Nous avons vu qu'il existe deux valeurs de vérité (booléennes) en Python :
``True`` et ``False``. Nous avons vu également que l'instruction ``if`` prend sa
décision sur la base de l'évaluation d'une expression booléenne. Comme le montre
le programme ci-dessous, cela doit être précisé.

Exemple
-------

..  activecode:: f64acc2f-5055-4e79-b3de-6bcae530c992

    message = input("Entrez votre message: ")

    if message:
        print(f"Votre message contient {len(message)} caractères.")
    else:
        print(f"Erreur! Votre message ne contient aucun caractère")

..  admonition:: Explication

    Comment ce programme fonctionne-t-il? En effet, la variable ``message`` ne
    contient ni ``True`` ni ``False``, **mais un texte**. A priori, la condition
    dans le ``if message:`` ne fait donc aucun sens. En réalité, le programme
    fonctionne car, quel que soit le **type** (nombre entier, nombre à virgule,
    texte, ...) de l'expression utilisée dans le ``if``, elle sera d'abord
    **convertie** par Python en une valeur booléenne avant d'être utilisée
    (conversion de type implicite).

Fonction ``bool()``
-------------------

La fonction ``bool(valeur)`` permet de convertir une valeur en un booléen.

..  activecode:: 59085432-c337-4ba2-ab42-d2f70cd65ba0
    
    a = 1
    print(f"La valeur booléenne de {repr(a)} est {bool(a)}")
    a = 0
    print(f"La valeur booléenne de {repr(a)} est {bool(a)}")
    a = 1.5
    print(f"La valeur booléenne de {repr(a)} est {bool(a)}")
    a = 10
    print(f"La valeur booléenne de {repr(a)} est {bool(a)}")
    a = "salut"
    print(f"La valeur booléenne de {repr(a)} est {bool(a)}")
    a = ""
    print(f"La valeur booléenne de {repr(a)} est {bool(a)}")

..  admonition:: À retenir

    Il faut retenir les éléments suivants de ce petit programme

    - On peut utiliser des expressions de n'importe quel type en guise de
      condition (numérique, textuelle, logique, ...). Lorsqu'une valeur ou une
      expression non booléenne est utilisée à un endroit où Python attend
      normalement une valeur booléenne, la valeur en question est d'abord
      **implicitement** (automatiquement) convertie en valeur booléenne avant
      d'être utilisée.
    - Le nombre ``0`` est équivalent à ``False``
    - Tout nombre non nul est équivalent à ``True``
    - Un texte vide est équivalent à ``False``
    - Un texte non vide est équivalent à ``True``.
    - Une liste vide est équivalente à ``False``.
    - Une liste non vide est équivalente à ``True``.
    - La valeur spéciale ``None`` est équivalente à ``False``.

    ::

        >>> bool(0)
        False
        >>> bool(1)
        True
        >>> bool('')
        False
        >>> bool('salut')
        True
        >>> bool(True)
        True
        >>> bool(False)
        False
        >>> bool([])
        False
        >>> bool(['pommes', 'carottes'])
        True
        >>> bool(None)
        False

Règles d'évaluation des opérateurs booléens
===========================================

Les programmeurs expérimentés utilisent parfois les opérateurs logiques de
manière spéciale, en exploitant leur évaluation court-circuitée. En effet, si la
valeur de l'expression logique est déjà certaine lorsque l'évaluation de la
partie gauche a été effectuée, **il n'y a pas besoin d'évaluer la partie de
droite**. 

..  list-table:: Court-circuitage de l'expression logique
    :widths: 10 40 40 40
    :header-rows: 1
    :align: left

    * - Opérateur
      - Valeur expression à gauche
      - Valeur expression à droite
      - Valeur de toute l'expression

    * - ``or``
      - ``True`` ou équivalent
      - Pas évalué (court-circuit)
      - Valeur de l'expression à gauche du ``or``
    
    * - ``or``
      - ``False`` ou équivalent
      - évalué
      - Valeur de l'expression à droite du ``or``
    
    * - ``and``
      - ``False`` ou équivalent
      - Pas évalué (court-circuit)
      - Valeur de l'expression à gauche du ``and``
    
    * - ``and``
      - ``True`` ou équivalent
      - évalué
      - Valeur de l'expression à droite du ``and``

..  admonition:: Conseil de pro

    - Pour optimiser l'évaluation d'une expression booléenne avec un opérateur
      ``or``, il vaut souvent la peine de mettre l'expression qui a le plus de
      chances d'être "truty" à gauche, car l'expression de droite n'a ainsi
      souvent pas besoin d'être évaluée.
      
    - Pour optimiser l'évaluation d'une expression booléenne avec un opérateur
      ``and``, il vaut souvent la peine de mettre l'expression qui a le plus de
      chances d'être "falsy" à gauche, car l'expression de droite n'a ainsi
      souvent pas besoin d'être évaluée.


     
    
..
    Ce phénomène se produit ...

    - ... avec l'opérateur ``or`` lorsque l'expression à gauche du ``or`` est
    ``True`` ou équivalente à ``True``. En effet, dans ce cas, il n'est pas
    nécessaire d'évaluer la partie de droite puisque l'expression dans son
    ensemble est de toute manière vraie.

    - ... avec l'opérateur ``and``, lorsque l'expression à gauche du ``and`` est
    ``False``. En effet, l'expression dans son ensemble n'a à ce moment aucune
    chance d'être vraie et il n'est de ce fait pas nécessaire d'évaluer
    l'expression à droite du ``and``.

Exemple de court-circuitage du ``or``
-------------------------------------

Voici des exemples de court-circuitage avec l'opérateur ``or``

..  activecode:: 4b9b13ea-f8cf-4dff-8880-cfec947c4152

    print('' or 15)
    print('' or 'salut')
    print(0 or 10 * 2)

Dans tous ces exemples, comme la partie de gauche de l'opérateur est "falsy"
(équivalente à ``False`` lorsqu'on utilise la fonction de conversion
``bool()``), l'expression dans son ensemble prend la valeur de l'expression à
droite du ``or``.

Voici un exemple typique de court-circuitage de l'évaluation d'une expression
``or`` très souvent utilisée pour donner une valeur par défaut à la variable
``choix`` si l'utilisateur saisit un texte vide.

..  activecode:: aa546b4e-8a4a-4e63-a56c-0562d74f9b62

    Essayez ce programme en saisissant les trois variantes ci-dessous:

    #. le texte ``oui``
    #. le texte ``non``
    #. le texte vide (ne rien entrer du tout et juste appuyer sur ENTER)

    ~~~~

    def save():
        print("Document sauvegardé!")

    def quit():
        print("L'exécution du programme est terminée.")

    choix = input("Voulez-vous enregistrer avant de quitter? ") or 'oui'

    if choix == 'oui':
        save()
        quit()
    elif choix == 'non':
        quit()
    else:
        print("Répondre par 'oui' ou par 'non'")

..  shortanswer:: 71eb0f7b-7f21-4817-9623-727ef690e23a

    Comment le programme se comporte-t-il lorsque vous avez validé la saisie sans
    rien écrire ?

..  reveal:: 05400111-50c1-4758-95b0-945e8de54702
    :showtitle: Réponse
    
    Lorsqu'on valide une saisie vide, le programme se comporte exactement comme
    lorsque l'on répond 'oui'. L'option 'oui' est donc une valeur par défaut qui a
    été indiquée après le ``or``. 

Pour comprendre ce comportement un peu spécial, il faut comprendre la manière
dont l'opérateur ``or`` est évalué.

..  admonition:: Évaluation de l'opérateur ``or``

    Lors de l'évaluation d'une expression
    
    ::

        expression_gauche or expression_droite
    
    impliquant l'opérateur ``or``, l'expression à droite du ``or`` n'est évaluée
    que si l'expression à gauche prend la valeur ``False`` ou une valeur "falsy"
    (équivalente à ``False``). En effet, il n'y a pas besoin d'évaluer
    l'expression de droite puisque, quelle que soit sa valeur (truthy ou falsy),
    l'expression sera de toute manière vraie dans son ensemble.

    L'opérateur est donc évalué de la manière suivante:

    - Python évalue d'abord l'expression à gauche du ``or`` (il peut s'agir
      d'une expression booléenne ou un autre type d'expression). 
    
    - Si la valeur de cette expression est "truthy" (équivalente à ``True``),
      l'évaluation est interrompue (court-circuitée) et l'expression ``or`` dans
      son ensemble prend la valeur de l'expression de gauche.

    - Si, en revanche, l'expression de gauche est équivalente à ``False``, ce
      qui est le cas du texte vide, Python évalue la partie droite. La valeur de
      l'expression dans son ensemble est à ce moment déterminée par la valeur de
      l'expression à droite du ``or``.

    Ainsi, si l'utilisateur ne saisit rien, la valeur de l'expression de gauche
    est le texte vide ``''``, équivalent à ``False`` et l'expression dans son
    ensemble prend la valeur de l'expression droite, à savoir le texte
    ``'oui'``. En revanche, si l'utilisateur saisit un texte non vide au
    clavier, la valeur de l'expression dans son ensemble sera égale à la valeur
    de l'expression à gauche du ``or``.

Exemple de court-circuitage du ``and``
--------------------------------------

Comme l'opérator ``or``, l'opérateur ``and`` est également évalué avec un
court-circuit. Dans le cas de l'opérateur ``and``, le court-circuit se produit
lorsque l'expression gauche est fausse, car, dans ce cas, on peut déjà dire
d'entrée de jeu que l'expression en entier doit être considérée comme fausse.



..
    ..  note::

        On utilise particulièrement le court-circuit avec l'opérateur ``and``
        lorsqu'on veut effectuer une opération sur un objet uniquement si cet objet
        n'est pas falsy.

    ..  admonition:: Exemple : minimum d'une liste

        Dans l'exemple ci-dessous, on simplifie le test pour garantir que la liste
        passée en paramètre soit non vide en utilisant l'évaluation court-circuitée
        du ``and``:

        ..  list-table:: titr edu tabeleau
            :header-rows: 1
            :align: left
            :width: 100%
            :widths: 50 50

            * - Programme
            - Programme avec le court-circuitage du ``and``

            * - ..  code-block:: python

                    # code à trouver
                    

            - ..  code-block:: python
                    
                    # code à trouver


Application : valeur par défaut pour paramètres de types mutables
=================================================================

Vous savez qu'il est possible d'attribuer des valeurs par défaut aux paramètres
des fonctions comme suit.

..  activecode:: ea24bd2a-ce90-4347-bf15-6dd5dd703aa1

    def greetings(name='Guido'):
        print(f'Hello {name}. How are you?')

    greetings('Ada')

    # Utilisation de Guido par défaut
    greetings()

Il faut toutefois faire attention avec cette manière de faire lorsque l'argument
est d'un type mutable (liste, dictionnaire, set, ...). Pour vous en convaincre,
essayez de deviner la sortie du programme ci-dessous:

..  shortanswer:: c35a1435-5f36-41b0-8cd6-321de664ca8b

    Qu'affiche le code suivant?

    ::

        def add3(items = []):
            items.append(3)
            return items

        x = add3()
        x = add3()
        x = add3()

        print(x)

..  reveal:: 19249918-6356-4134-8284-cb7e9c14ffa6
    :showtitle: Réponse

    Contre toute attente, la sortie n'est pas ::

        [3]

    mais ::

        [3, 3, 3]

    Cela vient du fait que les paramètres par défaut sont évalués **une seule
    fois lors de la définition de la fonction** et non à chaque appel de la
    fonction. De ce fait, le paramètre par défaut ``items = []`` est exactement
    le même objet lors de chaque appel sans paramètre. Pour confirmer cela, vous
    pouvez rajouter un ``print(id(items))`` dans la fonction avant le
    ``return``.

    ..  activecode:: 92705959-68c0-49f4-bf71-d01ffdd6efd7

        def add3(items = []):
            print(f'identité : {id(items)}')
            items.append(3)
            return items

        x = add3()
        x = add3()

Pour éviter ce problème, la bonne manière d'assigner une valeur par défaut à un
paramètre de type mutable (liste, dictionnaire, set, ...) est de lui attribuer
par défaut la valeur ``None`` (qui est falsy) et d'utiliser ensuite une
évaluation court-circuitée avec l'opérateur ``or`` pour assigner la valeur par
défaut, dans le corps de la fonction, qui est évalué lors de chaque exécution.

..  code-block:: python
    :linenos:
    :emphasize-lines: 2

        def add3(items=None):
            items = items or []
            print(f'identité : {id(items)}')
            items.append(3)
            return items

        x = add3()
        print(x)
        x = add3()
        print(x)
        x = add3([4, 5, 6])
        print(x)

..  note::

    Si la fonction a été appelée sans paramètre, ``items`` prend la valeur
    ``None`` par défaut, qui est falsy. De ce fait, la partie gauche de
    l'expression ``items or []`` est falsy et l'expression dans son ensemble est
    évaluaée à ``[]`` qui correspond à la valeur par défaut de la liste
    ``items``.

Lecture supplémentaire
======================

Lisez le billet de blog
https://mathspp.com/blog/pydonts/boolean-short-circuiting. Il présente quelques
techniques de programmation avancées qui utilisent élégamment la technique
d'évaluation court-circuitée des opérateurs booléens ``or`` et ``and``.

Questions de compréhension
==========================

Question 1
----------

Dans chacun des cas suivants, indiquez ce qu'affiche le programme sans
l'exécuter dans Python. Vérifiez ensuite votre réponse avec Python

..  shortanswer:: boolean-operators-eval-1

    ::

        print(10 or 5)
    
..  shortanswer:: boolean-operators-eval-2

    ::

        print(5 or 10)
    
..  shortanswer:: boolean-operators-eval-3

    ::

        print(0 or 10)
    
..  shortanswer:: boolean-operators-eval-4

    ::

        print(10 or 0)
    
..  shortanswer:: boolean-operators-eval-5

    ::

        print('' or 'salut')
    
..  shortanswer:: boolean-operators-eval-6

    ::
        
        x = None
        print(x or [])
    
..  shortanswer:: boolean-operators-eval-7

    ::

        print(5 and 3)
    
..  shortanswer:: boolean-operators-eval-8

    ::

        print(3 and 5)
    
..  shortanswer:: boolean-operators-eval-9

    ::

        print(0 and 3)
    
..  shortanswer:: boolean-operators-eval-10

    ::

        print(3 and 0)
    
..  shortanswer:: boolean-operators-eval-11

    ::
        
        x = []
        print(x and x[0])
    

Question 2
----------

..  mchoice:: 5ffa39f7-83cb-47d1-9baa-44747ed1fc32
    :random:

    Cochez les expressions ci-dessous qui sont équivalentes à l'expression ``a
    or b``

    ..  note:: 

        On considère que deux expressions sont équivalentes si, pour toutes les
        valeurs possibles de l'ensemble des variables qui interviennent dans les
        deux expressions, la valeur de l'expression est la même.

    - ``True and (a or b)``

      + Vrai. L'expression ``True`` à gauche du ``and`` est toujours vraie et
        l'expression dans son ensemble vaut donc toujours ``a or b``.

    - ``b or a``

      - Faux. Les deux expressions suivantes ne fournissent par exemple pas la
        même valeur: ::

            >>> 2 or 5
            2
            >>> 5 or 2
            5

    - ``b if not a else a``
      
      + Vrai. Cette expression est la seule qui est équivalente à ``a or b``
    
    - ``b if a == False else a``

      - Faux 0``, ce n'est pas le cas pour ``a = ''`` ou ``a = []`` par exemple.
        En effet,

        ::
            
            # Python considère vraiment `False` comme 0
            >>> 0 == False
            True
            # Même si '' est falsy, la chaîne vide n'est pas égale à ``False``
            >>> '' == False
            False
    
    - ``a if not b else b``
      
      - Faux
    
    - ``a if not a else b``
      
      - Faux
    
    - ``b if not b else a``
      
      - Faux

Question 3
----------

..  reveal:: 592665c8-a38a-45c6-a400-5657f5e7642e
    :showtitle: Précision technique
    :instructoronly:

    Le code suivant permet de confirmer que ``a if not a else b`` est équivalent
    à ``a and b`` pour les exemples fournis.

    ::

        def test(a, b):
            left = (a and b)
            #right = (b if not a else a)
            right = (a if not a else b)
            assert left == right, f"({a}, {b}) -> {left} / {right}"


        test(0, 2)
        test(2, 0)
        test(3, 2)
        test(2, 3)
        test(False, 6)
        test(6, False)
        test(False, False)


..  mchoice:: 4ce0427f-11d4-4a69-91b9-4da96c0d2d36
    :random:

    Cochez les expressions ci-dessous qui sont équivalentes à l'expression ``a
    and b``

    ..  note:: 

        On considère que deux expressions sont équivalentes si, pour toutes les
        valeurs possibles de l'ensemble des variables qui interviennent dans les
        deux expressions, la valeur de l'expression est la même.

    - ``False or a and b``

      + Vrai. L'expression ``False`` à gauche du ``or`` est toujours fausse et
        l'expression dans son ensemble vaut donc toujours ``a and b``.

    - ``a if not a else b``
    
      + Vrai. Cette expression est la seule qui est équivalente à ``a and b``
    
    - ``b if a == False else a``

      - Faux. Bien que cette expression fournisse le même résultat pour ``a =
        0``, ce n'est pas le cas pour ``a = ''`` ou ``a = []`` par exemple. En
        effet,

        ::
            
            # Python considère vraiment `False` comme 0
            >>> 0 == False
            True
            # Même si '' est falsy, la chaîne vide n'est pas égale à ``False``
            >>> '' == False
            False
    
    - ``a if not b else b``
      
      - Faux
    
    - ``b if not a else a``
      
      - Faux
    
    - ``b if not b else a``
      
      - Faux

Question 4
----------

..  shortanswer:: implicit_convert_bool_1

    Déterminez la sortie du programme ci-dessous

    ::

        x = 10
        if x % 2:
            print("A")
        else:
            print("B")


..  shortanswer:: implicit_convert_bool_2

    Déterminez la sortie du programme ci-dessous

    ::

        message = ''
        if not message:
            print("A")
        else:
            print("B")



Question 5
----------

..  shortanswer:: bool_compare_two_computations

    Parmi les programmes ci-dessous, indiquez celui qui est le plus performant
    lorsque l'utilisateur entre un nombre entier pair. **Justifiez votre
    réponse**.

    ..  glossary::

        Programme A

            ::

                from math import sqrt
                
                x = int(intput())
                if x % 2 == 0 and sum(k * sin(x) ** k for k in range(1, 1000, 2)) > 0:
                    print("A")
                else:
                    print("B")

        Programme B

            ::

                from math import sqrt
                
                x = int(intput())
                if sum(k * sin(x) ** k for k in range(1, 1000, 2)) > 0 and x % 2 == 0:
                    print("A")
                else:
                    print("B")

..  reveal:: 761e2a8a-73a9-43bb-b704-8d530e915ad6
    :showtitle: Réponse

    Le programme A est plus performant pour une saisie qui donne lieu à un
    nombre ``x`` impair. En effet, dans ce cas, le gros calcul
    
    ::
        
        sum(k * sin(x) ** k for k in range(1, 1000, 2))
        
    n'est même pas effectué, puisque la sous-expression gauche ``x % 2 == 0``,
    rapide à calculer, est "falsy".

Exercices
=========

Exercice 1
----------

On donne ci-dessous deux codes pour implémenter une fonction ``min(items:
list[Any]) -> Any`` qui retourne le plus petit élément de la liste ``items``. Le
premier exemple utilise une instruction conditionnelle pour gérer le cas d'une
liste vide et le deuxième une évaluation court-circuitée du ``and`` et du ``or``.

Le code B, plus court, fonctionne dans tous les cas donnés, sauf avec le
dernier. 

..  shortanswer:: d0cdabd2-3246-4eca-ab67-c230f445a9e2

    Expliquez pourquoi, dans le cas du programme B, la fonction ``min``
    fonctionne correctement dans les trois premiers cas


..  shortanswer:: 37940f30-6c10-4d84-af86-d8b299b4fc79

    Expliquez pourquoi, dans le cas du programme B, la fonction ``min`` ne
    fonctionne pas correctement dans le dernier cas

..  activecode:: ec74f914-2511-4e24-99ab-ae4cca3f841b
    :language: webtp

    Programme A avec l'instruction conditionnelle

    ~~~~

    def min(items):
        if len(items) == 0:
            print("Unable to get min of empty list")
            return

        current_min = items[0]

        for i in range(1, len(items)):
            if items[i] < current_min:
                current_min = items[i]

        return current_min

    print(min([]))
    print(10 * '=')
    print(min([5, 3, -1]))
    print(10 * '=')
    print(min([-1, 3, 5]))
    print(10 * '=')
    print(min([0, 2, 5, 7]))
    print(10 * '=')

..  activecode:: 1c0fc2d8-f3a3-4485-80bb-0d05f8222601
    :language: webtp

    Programme B avec un opérateur ``and`` et un opérateur ``or``

    ~~~~

    def min(items):
        '''
        >>> min([])
        >>> min([5, 3, -1])
        >>> min([-1, 3, 5])
        >>> min([0, 2, 5, 7])
        '''
        current_min = items and items[0] or print("problème: liste vide")

        for i in range(1, len(items)):
            if items[i] < current_min:
                current_min = items[i]
            
        return current_min

    print(min([]))
    print(10 * '=')
    print(min([5, 3, -1]))
    print(10 * '=')
    print(min([-1, 3, 5]))
    print(10 * '=')
    print(min([0, 2, 5, 7]))
    print(10 * '=')

..  reveal:: 8f3fa259-a74b-44b6-afe4-f1ae6f9f7f9a
    :showtitle: Solution
    
    ..  admonition:: Solution

        Le dernier cas ne fonctionne pas correctement, car la liste passée en
        paramètre est ``[0, 2, 5, 7]``, dont le premier élément est une valeur
        falsy. Or, l'expression ``(items and items[0])`` à gauche du ``or`` vaut
        ``items[0]`` puisque ``items`` n'est pas liste vide, à savoir 0, qui est
        une valeur falsy. À cause du court-circuitage du ``or``, ``current_min``
        vaut ``None``, puisque ``print(...)`` retourne ``None``.

        Les autres exemples fonctionnent, car ``items[0]`` n'est pas falsy.

