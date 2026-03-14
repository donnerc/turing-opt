.. _advanced-functions.rst:

Fonctions avancées
##################

..  contents:: Contenu de la page
    :depth: 3

Définir des fonctions très flexibles 
====================================

Il est possible de définir une fonction qui accepte un nombre quelconque de
paramètres. Pour cela, on utilise l'opérateur ``*`` pour les paramètres
positionnels et l'opérateur ``**`` pour les paramètres nommés.

Exemple 1 : liberté totale au niveau des paramètres
---------------------------------------------------

Voici un exemple de fonction qui accepte un nombre quelconque de paramètres:

..  activecode:: 79c66f99-f0a6-4e36-8cd4-9f360f5f34c7
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    def ma_fonction(*args, **kwargs):
        print("=" * 10)
        print("Paramètres positionnels :", args)
        print("Paramètres nommés :", kwargs)

    # liberté totale au niveau des paramètres
    ma_fonction()
    ma_fonction(1, 2, 3, a=4, b=5)
    ma_fonction(1, 2, a=4, b=5, c=10)

Exemple 2
---------

Dans l'exemple précédent, tous les paramètres sont optionnels. Il est également
possible de définir des paramètres obligatoires, suivis de paramètres
optionnels. Par exemple:

..  activecode:: cf2b2e2e-d71d-420f-8b70-9a88a85b1dc3
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    def ma_fonction(a, b, *args, **kwargs):
        print("=" * 10)
        print("Paramètres obligatoires :", a, b)
        print("Paramètres positionnels :", args)
        print("Paramètres nommés :", kwargs)

    # a et b sont obligatoires, les autres paramètres sont optionnels
    ma_fonction(1, 2)
    ma_fonction(1, 2, 3, 4, c=5, d=6)
    ma_fonction(1, 2, 5, d=6, e=10)

    # cause des erreurs (plusieurs valeurs pour a)
    ma_fonction(1, 2, a=5, d=6, e=5)

Appeler des fonctions de manière très flexible
==============================================

Il est également possible d'appeler une fonction de manière très flexible en
utilisant les opérateurs ``*`` et ``**`` pour décompresser des listes, des
tuples ou des dictionnaires en arguments positionnels ou nommés.

..  activecode:: 7f8ad687-8b34-490e-840d-7a9a73a971fd
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    def ma_fonction(a, b, c):
        print(f"a={a}, b={b}, c={c}")

    # Appel classique
    ma_fonction(1, 2, 3)

    # Appel avec des arguments nommés
    ma_fonction(a=1, b=2, c=3)

    # Appel avec une liste décompressée
    args = [1, 2, 3]
    ma_fonction(*args)

    # Appel avec un dictionnaire décompressé
    kwargs = {"a": 1, "b": 2, "c": 3}
    ma_fonction(**kwargs)

Exercices
=========

Exercice 1
----------

Définissez une fonction ``add`` qui accepte un nombre quelconque de paramètres
positionnels et qui retourne la somme de tous ces paramètres. 

Si la fonction est appelée sans paramètres, elle doit retourner 0. Si un des
paramètres n'est pas un nombre, la fonction doit lever une exception de type
``TypeError`` avec le message "Cannot add non numeric value: <value>", où
``<value>`` est la valeur du paramètre non numérique.

..  admonition:: Exemples

    ::

        >>> add()
        0
        >>> add(1, 2, 3)
        6
        >>> add(1, 2, 3, 4.5, 5)
        15.5
        >>> add("Guido", " ", "van", " ", "Rossum")
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "<stdin>", line 2, in add
        TypeError: Cannot add non numeric value: 'Guido'

..  activecode:: advanced-functions-add
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]


..  reveal:: advanced-functions-add-solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:
    
    ..  code-block:: python
        :linenos:

        def add(*args):
            total = 0
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise TypeError(f"Cannot add non numeric value: {arg!r}")
                total += arg
            return total

Exercice 2 : Le Gestionnaire de Commandes "Python Bistro"
---------------------------------------------------------

Vous devez créer une fonction ``preparer_commande`` qui permet de gérer les
commandes d'un restaurant de manière très souple.

..  admonition:: Étape 1

    Les ingrédients de base (``*args``) La fonction doit accepter un premier
    argument obligatoire ``plat`` (le nom du plat), puis un nombre variable
    d'ingrédients supplémentaires.

    **Consigne** : Affichez le nom du plat et listez tous les ingrédients supplémentaires
    fournis.

..  admonition:: Étape 2

    Les options de personnalisation (``**kwargs``) Certains clients ont des
    demandes spécifiques (cuisson, sans gluten, supplément sauce, etc.).

    **Consigne** : Modifiez la fonction pour qu'elle accepte des options de
    personnalisation sous forme de mots-clés. Affichez ces options proprement.

..  admonition:: Résultat final
    :class: note

    La fonction doit pouvoir gérer des commandes très variées, par exemple:

    ::

        >>> preparer_commande("Pizza Margherita")
        --- Commande : Pizza Margherita ---

        >>> preparer_commande("Burger", "Bacon", "Oignons frits", cuisson="Saignant", sans_oignon=True)
        --- Commande : Burger ---
        Ingrédients supplémentaires :
        - Bacon
        - Oignons frits
        Personnalisations :
        - cuisson: Saignant
        - sans_oignon: True
        >>> preparer_commande("Salade", "Avocat", sauce="Vinaigrette")
        --- Commande : Salade ---
        Ingrédients supplémentaires :
        - Avocat
        Personnalisations :
        - sauce: Vinaigrette

..  activecode:: advanced-functions-commande
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    

..  reveal:: advanced-functions-commande-solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    Notez que dans la vraie vie, on nomme souvent les paramètres ``*args`` et
    ``**kwargs`` par des noms plus explicites, comme ``*ingredients`` et
    ``**options`` dans cet exemple, pour rendre le code plus lisible.

    ..  activecode:: advanced-functions-commande-solution-code
        :language: webtp
        :interpreterargs: branch=branch&layout=["Editor", "Console"]

        def preparer_commande(plat, *ingredients, **options):
            print(f"--- Commande : {plat} ---")
            
            if ingredients:
                print("Ingrédients supplémentaires :")
                for ing in ingredients:
                    print(f"- {ing}")
                    
            if options:
                print("Personnalisations :")
                for cle, valeur in options.items():
                    print(f"- {cle}: {valeur}")
            print("\n")

        # Tests pour les élèves
        preparer_commande("Pizza Margherita")
        preparer_commande("Burger", "Bacon", "Oignons frits", cuisson="Saignant", sans_oignon=True)
        preparer_commande("Salade", "Avocat", sauce="Vinaigrette")

Exercice 3
----------

Appelez la fonction ``preparer_commande`` efficacement en utilisant les
variables globales ``plat``, ``ingredients`` et ``options``.


..  activecode:: advanced-functions-commande-call
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    # Variables globales
    plat = "Pâtes Carbonara"
    ingredients = ["Pâtes", "Lardons", "Crème fraîche", "Parmesan"]
    options = {"cuisson": "Al dente", "sans_oignon": True}

..  reveal:: advanced-functions-commande-call-solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    ..  code-block:: python
        :linenos:

        # Appel efficace de la fonction en utilisant les variables globales
        preparer_commande(plat, *ingredients, **options)