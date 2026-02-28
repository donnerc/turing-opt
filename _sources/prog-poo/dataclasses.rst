.. _dataclasses.rst:

Définir des classes efficacement avec ``dataclass``
###################################################

..  contents:: Contenu de la page
    :depth: 3

..  note:: 

    Le contenu de cette page n'est pas indispensable pour faire de la POO en
    Python, mais permet de travailler bien plus efficacement et de rendre le
    code plus lisible.

Depuis la version 3.7, Python dispose d'un module ``dataclasses`` très pratique
permettant de définir des classes de données bien plus efficacement que la
manière traditionnelle.

Les bases (en français)
=======================

..  admonition:: Vidéo de la chaîne Docstrings

    ..  youtube:: 6Ltk49YhrWY
        :divid: docstrings-dataclasses
        :width: 635
        :height: 360


Résumé de la vidéo
------------------

Le module ``dataclass`` permet de définir des classes de manière beaucoup plus
efficace. Elles permettent d'économiser beaucoup de *boilerplate code*, à savoir
du code qui est le même dans toutes les classes, comme la définition des
variables d'instance dans le constructeur.

..  activecode:: 1154bd84-8574-4893-a88a-e2a99f7e45e6
    :language: webtp

    from dataclasses import dataclass, field

    @dataclass
    class User:
        firstname: str
        lastname: str
        # Ce champ sera initialisé par le post init et non
        # par le constructeur
        fullname: str = field(init=False)

        def __post_init__(self):
            self.fullname = f"{self.firstname} {self.lastname}"

    guido = User(firstname="Guido", lastname="Van Rossum")
    print(guido)
    print("Fullname:", guido.fullname)

Concepts plus avancés (anglais)
===============================

La vidéo suivante de la chaîne mcoding va encore plus loin et montre des options
avancées des dataclasses, permettant d'économiser encore plus de travail et de
personnaliser davantage les classes.

..  admonition:: Vidéo de la chaîne Docstrings

    ..  youtube:: vBH6GRJ1REM
        :divid: mcoding-dataclasses
        :width: 635
        :height: 360

..  activecode:: 5a7d51d6-516f-4138-b96a-360d31f4308c
    :language: webtp

    from dataclasses import dataclass, astuple, asdict, field

    @dataclass(frozen=True, order=True)
    class Comment:
        id: int = field()
        text: str = field(default="")
        replies: list[int] = field(default_factory=list, compare=False, hash=False, repr=False)

    
    def main():
        comment = Comment(1, "I just subscribed")
        print(comment)
        print(astuple(comment))
        print(asdict(comment))
        print("================")
        for attr in comment.__dict__:
            print(attr)

        
        print("================")
        try:
            comment.text = "Try to modify the comment"
        except Exception as e:
            print("Cannot modify the comment : it's immutable !!!")
            print(e)

    if __name__ == '__main__':
        main()
        

