
.. _part3-introduction.rst:

Introduction
############

..  contents:: Contenu de la page
    :depth: 3

Le solveur ToyCSP développé dans la partie :ref:`part-toycsp` présente de gros
soucis de performance, car sa vocation était de présenter les concepts de base
de la programmation par contraintes : variables, domaines, contraintes et
recherche en profondeur en utilisant les algoritmes de filtrage des contraintes
(propagation).

Nous allons développer à présent un solveur plus solide apportant de nombreux
avantages

- Utilisation de structures de données plus performantes, notamment pour
  représenter les domaines des variables

  ..  note::

      Nous allons aborder les structures de données suivantes : Piles, files,
      listes chaînées, ensemble d'entiers creux (*sparse set* en anglais).

- Sauvegarde et restauration de l'état plus performant et flexible lors d'un
  retour-arrière dans la recherche.

- Procédure de recherche plus flexible permettant d'influencer facilement le
  solveur au niveau de l'ordre dans lequel il choisit la prochaine variable à
  assigner et le choix des valeurs à assigner aux variables, ce qui peut
  accélérer drastiquement la recherche de solutions

- Ajout d'autres contraintes, notamment des contraintes globales avec des
  algorithmes de propagation plus performants.