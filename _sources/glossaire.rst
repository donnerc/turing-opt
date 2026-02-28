.. _glossaire.rst:

Glossaire
#########

.. glossary::

    Problème de satisfaction de contraintes (PSC)
        Problème déterminé par la donnée d'un ensemble :math:`X` de variables
        caractérisées par un domaine de valeurs admissibles, chacune étant liée
        à une ou plusieurs autres variables par un ensemble :math:`C` de
        contraintes.

        Résoudre un PSC revient à assigner une valeur à chaque variable de sorte
        que toutes les contraintes du problèmes soient satisfaites.

        ..  admonition:: Exemples

            - problème des N dames
            - Coloriage de graphe
            - Problème des mariages stables
            - Sudokus
            - ...


    CSP
        En anglais, Constraint Satisfaction Problem, cf. PSC
    
    PSC
        Voir Problème de satisfaction de contraintes

    PPC
        Programmation par contraintes

    Variable
        En PPC, les variables jouent un rôle différent des variables dans un
        langage de programmation général. En PPC, chaque variable :math:`x_i`
        possède un domaine :math:`D_i` de valeurs admissibles. Les variables
        sont liées par des contraintes et le but d'un modèle de PPC est
        d'assigner une valeur à chaque variable de sorte que toutes les
        contraintes du problèmes soient satisfaites.

    Domaine
        Ensemble des valeurs admissibles pour une variable à un moment donné de
        la résolution. Le solveur de contrainte utilise typiquement les
        algorithmes de filtrage des contraintes pour réduire le domaine des
        variables durant la résolution.

    Contrainte
        ...

    Anticipation
        L'anticipation (look-ahead) est un terme plus général qui englobe
        diverses techniques pour regarder vers l'avant dans l'arbre de
        recherche. Ces techniques peuvent être plus puissantes que la
        vérification avant, mais elles peuvent aussi être plus coûteuses en
        termes de calcul. Un type courant d'anticipation est la consistance
        d'arc, qui garantit que pour chaque paire de variables, il existe au
        moins une valeur dans le domaine de chaque variable qui est compatible
        avec l'autre variable.
    
    Vérification avant
        La **vérification avant** (*forward checking*) est une forme de base
        d'anticipation. Elle fonctionne en maintenant une liste des valeurs
        possibles pour chaque variable non assignée. Lorsqu'une variable se voit
        attribuer une valeur, la vérification avant supprime toutes les valeurs
        des domaines des autres variables non assignées qui sont incompatibles
        avec l'affectation. Cela peut aider à détecter les incohérences dès le
        début et à élaguer l'espace de recherche.

    Espace de recherche
        ...