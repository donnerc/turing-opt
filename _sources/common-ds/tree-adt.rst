.. _tree-adt.rst:

Type abstrait d'arbre
#####################

Comme nous l'avons fait pour les files et les piles, nous définissons le type
abstrait pour les arbres (classe abstraite de base), qui doit supporter les
opérations suivantes pour un arbre :math:`T`:

..  admonition:: Méthodes associées aux arbres

    - ``T.root()`` : Renvoie la position de la racine de l'arbre :math:`T`, ou
      None si :math:`T` est vide.

    - ``T.is_root(p)`` : Renvoie ``True`` si la position :math:`p` est la racine
    - de l'arbre :math:`T`.

    - ``T.parent(p)`` : Renvoie la position du parent de la position :math:`p`,
      ou None si :math:`p` est la racine de :math:`T`.

    - ``T.num_children(p)`` : Renvoie le nombre d'enfants de la position
      :math:`p`.

    - ``T.children(p)`` : Génère un itérateur sur les enfants de la position
      :math:`p`.

    - ``T.is_leaf(p)`` : Renvoie ``True`` si la position :math:`p` n'a pas
      d'enfants et ``False`` sinon.

    - ``len(T)`` : Renvoie le nombre de positions (et donc d'éléments) contenus
      dans l'arbre :math:`T`.

    - ``T.is_empty()`` : Renvoie True si l'arbre :math:`T` ne contient aucune
      position.

    - ``T.positions()`` : Génère une itération de toutes les positions de
      l'arbre :math:`T`.

    - ``iter(T)`` : Génère une itération de tous les éléments stockés dans
      l'arbre :math:`T`.

