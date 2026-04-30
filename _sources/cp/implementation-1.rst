.. _implementation-1.rst:

Implémentation (étape 1)
########################

..  contents:: Contenu de la page
    :depth: 3

Dans cette première étape, nous allons implémenter une version très basique des
domaines, des variables et de la contrainte ``NotEqual``. Ces contraintes seront
suffisantes pour résoudre des problèmes simples tels que celui des
:math:`n`-reines ou des Sudokus.

Implémentation des domaines
===========================

..  activecode:: toycsp_impl_domain
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    Définissez une classe ``Domain`` qui permet de représenter le domaine de
    variables entières. N'oubliez pas d'implémenter l'exception
    ``Inconsistency`` qui doit être levée lorsqu'on tente de supprimer une
    valeur d'un domaine qui ne contient qu'une seule valeur (le domaine devient
    alors vide, ce qui est incohérent).

    ..  admonition:: Consignes
        :class: note

        On doit pouvoir instancier un domaine de deux manières : 
        
        -   En fournissant un nombre entier ``n``. Dans ce cas, le domaine
            contiendra les valeurs ``{0, 1, 2, ..., n-1}``

        -   En fournissant un ensemble (``set``). Dans ce cas, le domaine
            contiendra les mêmes valeurs que l'ensemble en question.

        La classe doit posséder les méthodes suivantes :

        -   ``is_fixed(self) -> bool`` : retourne ``True`` si le domaine est
            fixé (s'il se réduit à une seule valeur) et ``False`` sinon.
        -   ``size(self) -> int`` : retourne le nombre d'éléments présents dans
            le domaine.
        -   ``__len__(self) -> int`` : idem que ``size``
        -   ``__repr__(self) -> str`` : retourne la représentation du domaine
            sous la forme ``Domain({v1, v2, ..., vn})``.

        -   ``min(self) -> int`` : retourne la valeur minimale du domaine.
        -   ``remove(self, v: int) -> bool`` : supprime la valeur ``v`` du
            domaine. Retourne ``True`` si la valeur se trouvait dans le domaine
            avant d'être supprimée et ``False`` si la valeur n'était pas
            présente dans le domaine. Lève l'exception ``Inconsistency`` si le
            domaine est vide après la suppression de la valeur ``v``.
        -   ``fix(self, v: int)`` : réduit le domaine à la seule valeur ``v``.
        -   ``clone(self) -> "Domain"`` : crée une copie du domaine en
            retournant **une nouvelle instance** de ``Domain`` avec les mêmes
            valeurs.

    ~~~~

    class Domain:
        """ 
        
        Implementation of a very basic domain using a set to store the values

        >>> d = Domain(5)
        >>> d.values
        {0, 1, 2, 3, 4}
        >>> d.min()
        0
        >>> d.size()
        5
        >>> len(d)
        5
        >>> d.is_fixed()
        False
        >>> d.fix(v=6)
        Traceback (most recent call last):
        ...
        Inconsistency
        >>> d.fix(v=4)
        >>> d.values
        {4}
        >>> d.is_fixed()
        True
        >>> d1 = d.clone()
        >>> d1 is d
        False

        >>> d = Domain({1, 3})
        >>> d.values
        {1, 3}
        >>> d.remove(v=3)
        True
        >>> d
        Domain({1})
        >>> d.remove(v=3)
        False
        >>> d.remove(1)
        Traceback (most recent call last):
        ...
        Inconsistency

        """

        ...


..  reveal:: 3230694d-d66c-4dcc-bbf4-65b29790ab56
    :showtitle: Solution
    :hidetitle: Cacher
    :modal:
    :instructoronly:

    ..  activecode:: 5994b380-062a-4d64-9b63-90b8b5a5ce83
        :language: webtp
        :interpreterargs: branch=branch&layout=["Editor", "Console"]

        class Inconsistency(Exception): ...

        class Domain:
            """

            Implementation of a very basic domain using a set to store the values

            >>> d = Domain(5)
            >>> d.values
            {0, 1, 2, 3, 4}
            >>> d.min()
            0
            >>> d.size()
            5
            >>> len(d)
            5
            >>> d.is_fixed()
            False
            >>> d.fix(v=6)
            Traceback (most recent call last):
            ...
            Inconsistency
            >>> d.fix(v=4)
            >>> d.values
            {4}
            >>> d.is_fixed()
            True
            >>> d1 = d.clone()
            >>> d1 is d
            False

            >>> d = Domain({1, 3})
            >>> d.values
            {1, 3}
            >>> d.remove(v=3)
            True
            >>> d
            Domain({1})
            >>> d.remove(v=3)
            False
            >>> d.remove(1)
            Traceback (most recent call last):
            ...
            Inconsistency

            """

            def __init__(self, *args) -> None:
                """
                Initializes a domain. Values are stored as a set.

                - Domain(n) Initializes the domain with {0, 1, 2, ... n-1}
                - Domain(set) Initializes the domain with the given set

                """
                if len(args) != 1:
                    raise TypeError("Domain takes only one parameter")
                elif isinstance(args[0], int):
                    n = args[0]
                    self.values = set(range(n))
                elif isinstance(args[0], set):
                    dom = args[0]
                    self.values = dom.copy()
                else:
                    raise TypeError("Argument must be int or set[int]")

            def is_fixed(self) -> bool:
                """
                Verifies if only one value left

                Returns:
                    True if only one value left, False otherwise.
                """
                return len(self.values) == 1

            def size(self) -> int:
                """
                Gets the domain size

                Returns:
                    The number of values in the domain.
                """
                return len(self.values)

            def __len__(self) -> int:
                """
                Same as .size()
                """
                return self.size()

            def min(self) -> int:
                """
                Gets the minimum of the domain

                Returns:
                    The minimum value in the domain.
                """
                return min(self.values)

            def remove(self, v: int) -> bool:
                """
                Removes value v from the domain

                Args:
                    v: The value to remove.

                Returns:
                    True if the value was present in the domain, False otherwise.
                """
                if v in self.values:
                    self.values.remove(v)
                    if not self.values:
                        raise Inconsistency
                    return True
                return False

            def fix(self, v: int):
                """
                Fixes the domain to value v

                Args:
                    v: The value to fix the domain to.

                Raises:
                    Inconsistency: If the value is not in the domain.
                """
                if v not in self.values:
                    raise Inconsistency
                self.values = {v}

            def clone(self) -> "Domain":
                """
                Creates a copy of the domain.

                Returns:
                    A new Domain object with the same values.
                """
                return Domain(self.values)

            def __repr__(self) -> str:
                ordered_set = ', '.join(str(x) for x in sorted(self.values))
                return f"Domain(§[§[{ordered_set}§]§])"


        if __name__ == '__main__':
            import doctest
            doctest.testmod()


Implémentation des variables de décision
========================================

..
    ############### Importation dans WebTigerPython ############
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
    with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
    ############################################################


..  activecode:: toycsp_impl_vars
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    Définissez une classe ``Variable`` qui permet de représenter les variables
    de décision entières.

    ..  admonition:: Consignes
        :class: note

        On doit pouvoir instancier une variable en passant en paramètre les
        valeurs à insérer initialement dans son domaine sous la forme d'un
        itérable (liste, tuple, range, set, ...). On veut également pouvoir
        indiquer le nom de la variable avec le paramètre nommé ``name=``. Si le
        nom n'est pas donné, il sera créé automatiquement en se basant sur le
        compteur de création de variables (variable de classe) incrémenté lors
        de chaque instanciation.

    ::

        >>> q1 = Variable([3, 5, 7], name="Q1")
        >>> x = Variable(range(5, 8))

    La classe doit posséder les méthodes suivantes en plus du constructeur :

    -   ``__repr__(self) -> str`` : 

    ~~~~

    # Coller votre code de la classe Domain ici ou créez un module domain.py et
    # importez la classe Domain depuis ce module

    class Variable:

        '''
        >>> v = Variable({3, 4, 5})
        >>> v
        Variable(Domain({3, 4, 5}), name='Var0')
        >>> v.dom
        Domain({3, 4, 5})
        >>> v2 = Variable(range(6, 9), name="Q2")
        >>> v2
        Variable(Domain({6, 7, 8}), name='Q2')

        '''


    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: 8a135924-181b-416f-910f-229b7f1bd98c
    :showtitle: Solution
    :hidetitle: Cacher
    :modal:
    :instructoronly:

    ..  raw:: html

        <iframe src="https://exp.webtigerpython.ethz.ch/#?fs=N4IgZglgNgpgziAXKAJgewLYEMIDsB0ADgJ5Ki5YYxIjrZ5GkA0IhWALgBY104EkgWKDljIh2xQtUQgAqnnYAOAIIAnVVma0RNAJoAmAB6cAxgGYAsgHMAygHUArACsARvocAvLAA0AcgAYALUcnGBtOADEYAHFfKBMACQAlQjcAFkIAeQhlAFcAGQg0gGkAYQxfOF0_DwBJAFEkgDcXOwjUpzRi2tLlKx7aiFqrLp6-hqh2E2jDKFaANVyUaIj_LDsATlza6I2MHfqrFAx54jCAIQhq30JdYnOAazcARk51tKO_VIwTK10bc4eQLeACKR2iiis5maJgwsnBnCgtQSgU4LgS83iAHdRr1-gARNIAagAChBHrV8f4rElduxdHYoLlivjZIRSjl-r1SU4PoFSg59AzDM9gRZunjkXAsfleoZZcpiAqPAr_GAQWguX0SbyiTsQblWkyyg8JeN8cozQTiWTHvlcDcYHCuhqtVZfK6xlYdcSdrMXBBOKbPXiPZqvT69dEDT5fGBAhgoGlghriiG-kkMBE4CZ9LIrZSbeSHvkMIEpKVOPoSQAVXTszk9c6yWERJzBABSnAMcCsxWizya5jBsPm7cc_h2vjR0SxVhcKw8KFKDwAbBzxr0CkUC_UmQYtrmoEvootdGZTV7C6Ti6XyzBK9WayCG5vlDy-QKhXYRWKCwk4DVdNvV1fVcljeNE2TOxU2A-YEg7UVgMjfVDEpal-WcBctkCGwrFfLUPysQJ8UOHxrECZRwzxTNs1zfMN0In1iN6DYGmaVp2gDTgAHYLBsOcLDMfwCLGIjMO_X9vHFK8APlXoPHVajtVA6NclHdgXDMQIoGKBJdA2CxiEvSUIiSYgUDsfMr0JG9HkYpt6heN47DSNAYA8CINjTZSQN9NSNK0nS9IMoyTPGepUXROIHO5ZjMOIYJB2OWQ0H48L-jM4gGTiXQsycTQqNaDYl1Kc5ErsOIXFwMEDGzFwyqqPx_GKGtcU3NIChGN17Cw9wvGa4JnBgVMr1KQZhna_poiSKBAnJMBvH0JkfCSRbiE4IEfwwBUAEdqg7XATGMqx8hrD4awwHC2oLSVeiGIZbs3c4OxcRM1jaOAfEIeJ7k4HYOLaVIiiseYszgSz5jqFZEoBE8Ngq2rpL-OHgQNUpurGzdqVpDZ6UZZlogyCZwO8FJhSkE46mSNBcMeZz3iOZa1jKvjSkEgSrAsCA50KTqdjSdgLG8Fqsa1dh2JaIHuKBUFCBJ1bbh_SmoeRJJaYBJ59FeRmUGZrAyrWaJ4UCZb9GCD5c3mfwMd8saJsxu7xmiKB9hmOZA1MDAUA8YobGUTgSX9wxMkdt83SbbLGSBAFZBgbxzigJJvA7YgtNqNBageQGuPJfwGXYX7zhaDBDAcHYcIBLEDrROxreBQYfIjyVTy-uxdCsWNUgdfOQlwzgvZ9uwPHOFBZXObuX1Du2na5c5tipP4U6O55pVBGfw6bLbDB23AooxX7lDYhI4mXTgo4cPfwmZGwMrGxOF1dnZj3WTxlgiXIDFSg6V7XzmrZajdMWYtAh0nQkvQ6JhV5YnXs3TeZVt6733piY6R8AYtBsFhMw5wHAmienPOYJ8oDTzgc3cqDJjx0zjgnJOKc05mAzlnCIiUzDzHYENScA5njDj-HCTuE4K7EGRKfCI7Bu5JBQIMU0sVHjBA7hBBMSYUxoCtnAeaDxTrnV4RsFo-IppYwerUfBTY7DAg7IQRRRcLHkhLmXCuuQ6aSVFACNRpibZhwjhEDsUAUAYjTrgCw65GyzyvFlSy8J1gdzcA4OAFwS7wmONmcJ85Tze3ZjScG9F5xmHVmYswsYoD5A8fbIYxTJQIR8X4gM5xXFuVUfNQUwpRTSXllSNipEyjBNke3KEy1Vz90QX7ZQ7BbSTyCfA8YD1YrhySPoa2x1zhGxNnSCh2wT6UwYsE8OsgTj-BQCndSHh9EhLxPMaIiIdgOGeK0bxJgbHzXOE4sU_CPjLAuTNKWucSjAPuhNYxZVEpk24RgD4C5Fh6SqtEXQSxwaQ19qNFus0HmLSMHMKAGwwAQrmFC-WpR_BRiZCgPR_zlCGP-ecOsdhnhIkXD0Tw31dIrhJWSn55VgRJGBZbOZaiID0u8D9PBMiHhyPnATLFC56w9Hxc_JYxKfmkr-aylEZNqa5IBOwV-qRvBsIrvsGmdMtY61cp0iZVgdnW32R2Q5xzTVnPec8b4kxLLUkSRDKyLyEQ0pzsDb5JyFWPVZYCjlsJQViqIRKmFSS67wv0TNOa5IKrJWdPUnmRxOj8IcC1f2IzyQQDcBsOAJCfkOw3plbxxVzbI1dcklA5IfhXQlvqzWDNjXTLdCCZeJgjkkrdCgdNdqkQojRAfNWTRkTls2ObGwJQ21enNXsg5XabWkPgohOm1jFlYGNkcWF7q9YRGpmyvwcwaoereV6z5wM5y0RzHmbJuSU75OPUU0tAxSmvpdnq-RrlenzB5Y0n8zTAmzpCeGqFka3VQ3tBOjYU6qxN3lXPDdhozAjm5Q0p50lxmkMDRQmOL03q-BaA6Qg0I5gVAcCBzeFTfGnGqS2XAmIqNQl2Za7YkVh0xQ8aAsGOx7yVkQePfQ2QJ7VSnmUzcJacORSkKeVVGt6baxcq8iEO6o0JJGOS84sIfZFr9XPYT5JZBboSbuhJqnFFpDVgpw1ynwSKFyLbHDXi3jHqXT2r0vVXD9VjEEEIMA2q2B6ee5EyCaXHkuU0Zcom84meIisgmL6cPjXfThz9yIolXU4UyYR2LoXVujXp01kc8N01ehUYjNwyOEco1st0KaANSWsEHc4PEUC4BakKkVBhDDxJUehiAGizofCzt6gMtRsPAKmXVr0IIzDeOqLNBZ_1YhDgSBotwHcQsfM4j6k1pD51sfc4h2bAIHHeF-LjfGOXdgQEoGOaLT71bWbph4Bk1LQvDpQcQX1EyWUnKPcGkFNIEvGjA_l3dUMfIFjjci7w834gIXWptYIO8hk5sBL4ibzGtIdmFSnOaXlZZgiDsoXACpycYEIE0d4KicnED0vhPjQ5yRWZdmsojJhcBIoE6jpBX3foPFErPUcC6rU7F0BAK7qy9LsB4jAfQCMeMVTWgAxazxvI2CMRjQgG6UUOFrvMdaR9Se4G8Br67uRzeKFwEV_hzwsS484c0c8S3UMw5dzk-IqGlhyeWIOfk-EMYAF5g8gAAL7h5YPQfgpBkAgAoFQGgMfGCCFYBwbgMgU8CCEDoePEgpA0HkLgJQagNBaGEBqmggRcAdgwecbzhhXEBHWIeYgBu8rWHWA7p3Ewggp27KXKA5RAhp30BhUH2wXZTF2BZMqTklPvDKBUJqvg6gRFRLCKAg_ZjT1ulzjsOI3QoX0t6AE7cU5Kw7Go8IfFiBzl8Ok3wIthfvmYigDxYNmHrAiHm42aBpcw04AVReh_AFRngwBb44BLla5ZANg11TAnAycEM8QT9oVQE8YZEF8jU3IPILBoD8QQQCD5hvJkJQJ9IhFF4v9iAf8_9UpWwHE8w0BfBU1MgoCYDWg4DagoB6ghFBsCxbJbR9BrBfJqDaCFxUpACwc4B9AFQzAFQ0hICHhoDogDdOD4DnheDU5pEtla9iATB9smwhQU4wADxrlud4gch2lLQuselzcNhHV_Brd-s_15o5wMD2ARMOxlhTgGRr9Ag2FxEx4ypP4qViFyQlwEhhgWtMholdJs1bRYj3BiEJN-hwcHEwFF4pDmQiEz4tYRIUDqNIVoU3pRFcI0FVDYDslhgEC7lfhih7hIiM4xC2g6DI1iAloiNLJM0G5X83QWjf8JD2jOiosJwG4-wPBqQLAEVnYkUFp4dbkkdvANpBkEiIisdJsRdWMDkJcIABi6D3IzBiiMi8ZIC5xSj2Eax_BcAYAji8tDQsx2ERZcA_ZtdEx9gvIwALiAiMV0I2JSgUAUUjUHB1oTBNjRME4hxT0MCnAfClwqI3QYS4TlwejmpippFpErBQ8I9I8hAIBVAYATB2A0BVAIB4AkAABtAAXXDyAA&runFile=main.py&filesystemSize=20&error_messages=TigerPython" 
            style="min-width: 100%; min-height: 500px;"
            title="Visually Explained: Generators" frameborder="0" allowfullscreen>
        </iframe>

        <a href="https://exp.webtigerpython.ethz.ch/#?fs=N4IgZglgNgpgziAXKAJgewLYEMIDsB0ADgJ5Ki5YYxIjrZ5GkA0IhWALgBY104EkgWKDljIh2xQtUQgAqnnYAOAIIAnVVma0RNAJoAmAB6cAxgGYAsgHMAygHUArACsARvocAvLAA0AcgAYALUcnGBtOADEYAHFfKBMACQAlQjcAFkIAeQhlAFcAGQg0gGkAYQxfOF0_DwBJAFEkgDcXOwjUpzRi2tLlKx7aiFqrLp6-hqh2E2jDKFaANVyUaIj_LDsATlza6I2MHfqrFAx54jCAIQhq30JdYnOAazcARk51tKO_VIwTK10bc4eQLeACKR2iiis5maJgwsnBnCgtQSgU4LgS83iAHdRr1-gARNIAagAChBHrV8f4rElduxdHYoLlivjZIRSjl-r1SU4PoFSg59AzDM9gRZunjkXAsfleoZZcpiAqPAr_GAQWguX0SbyiTsQblWkyyg8JeN8cozQTiWTHvlcDcYHCuhqtVZfK6xlYdcSdrMXBBOKbPXiPZqvT69dEDT5fGBAhgoGlghriiG-kkMBE4CZ9LIrZSbeSHvkMIEpKVOPoSQAVXTszk9c6yWERJzBABSnAMcCsxWizya5jBsPm7cc_h2vjR0SxVhcKw8KFKDwAbBzxr0CkUC_UmQYtrmoEvootdGZTV7C6Ti6XyzBK9WayCG5vlDy-QKhXYRWKCwk4DVdNvV1fVcljeNE2TOxU2A-YEg7UVgMjfVDEpal-WcBctkCGwrFfLUPysQJ8UOHxrECZRwzxTNs1zfMN0In1iN6DYGmaVp2gDTgAHYLBsOcLDMfwCLGIjMO_X9vHFK8APlXoPHVajtVA6NclHdgXDMQIoGKBJdA2CxiEvSUIiSYgUDsfMr0JG9HkYpt6heN47DSNAYA8CINjTZSQN9NSNK0nS9IMoyTPGepUXROIHO5ZjMOIYJB2OWQ0H48L-jM4gGTiXQsycTQqNaDYl1Kc5ErsOIXFwMEDGzFwyqqPx_GKGtcU3NIChGN17Cw9wvGa4JnBgVMr1KQZhna_poiSKBAnJMBvH0JkfCSRbiE4IEfwwBUAEdqg7XATGMqx8hrD4awwHC2oLSVeiGIZbs3c4OxcRM1jaOAfEIeJ7k4HYOLaVIiiseYszgSz5jqFZEoBE8Ngq2rpL-OHgQNUpurGzdqVpDZ6UZZlogyCZwO8FJhSkE46mSNBcMeZz3iOZa1jKvjSkEgSrAsCA50KTqdjSdgLG8Fqsa1dh2JaIHuKBUFCBJ1bbh_SmoeRJJaYBJ59FeRmUGZrAyrWaJ4UCZb9GCD5c3mfwMd8saJsxu7xmiKB9hmOZA1MDAUA8YobGUTgSX9wxMkdt83SbbLGSBAFZBgbxzigJJvA7YgtNqNBageQGuPJfwGXYX7zhaDBDAcHYcIBLEDrROxreBQYfIjyVTy-uxdCsWNUgdfOQlwzgvZ9uwPHOFBZXObuX1Du2na5c5tipP4U6O55pVBGfw6bLbDB23AooxX7lDYhI4mXTgo4cPfwmZGwMrGxOF1dnZj3WTxlgiXIDFSg6V7XzmrZajdMWYtAh0nQkvQ6JhV5YnXs3TeZVt6733piY6R8AYtBsFhMw5wHAmienPOYJ8oDTzgc3cqDJjx0zjgnJOKc05mAzlnCIiUzDzHYENScA5njDj-HCTuE4K7EGRKfCI7Bu5JBQIMU0sVHjBA7hBBMSYUxoCtnAeaDxTrnV4RsFo-IppYwerUfBTY7DAg7IQRRRcLHkhLmXCuuQ6aSVFACNRpibZhwjhEDsUAUAYjTrgCw65GyzyvFlSy8J1gdzcA4OAFwS7wmONmcJ85Tze3ZjScG9F5xmHVmYswsYoD5A8fbIYxTJQIR8X4gM5xXFuVUfNQUwpRTSXllSNipEyjBNke3KEy1Vz90QX7ZQ7BbSTyCfA8YD1YrhySPoa2x1zhGxNnSCh2wT6UwYsE8OsgTj-BQCndSHh9EhLxPMaIiIdgOGeK0bxJgbHzXOE4sU_CPjLAuTNKWucSjAPuhNYxZVEpk24RgD4C5Fh6SqtEXQSxwaQ19qNFus0HmLSMHMKAGwwAQrmFC-WpR_BRiZCgPR_zlCGP-ecOsdhnhIkXD0Tw31dIrhJWSn55VgRJGBZbOZaiID0u8D9PBMiHhyPnATLFC56w9Hxc_JYxKfmkr-aylEZNqa5IBOwV-qRvBsIrvsGmdMtY61cp0iZVgdnW32R2Q5xzTVnPec8b4kxLLUkSRDKyLyEQ0pzsDb5JyFWPVZYCjlsJQViqIRKmFSS67wv0TNOa5IKrJWdPUnmRxOj8IcC1f2IzyQQDcBsOAJCfkOw3plbxxVzbI1dcklA5IfhXQlvqzWDNjXTLdCCZeJgjkkrdCgdNdqkQojRAfNWTRkTls2ObGwJQ21enNXsg5XabWkPgohOm1jFlYGNkcWF7q9YRGpmyvwcwaoereV6z5wM5y0RzHmbJuSU75OPUU0tAxSmvpdnq-RrlenzB5Y0n8zTAmzpCeGqFka3VQ3tBOjYU6qxN3lXPDdhozAjm5Q0p50lxmkMDRQmOL03q-BaA6Qg0I5gVAcCBzeFTfGnGqS2XAmIqNQl2Za7YkVh0xQ8aAsGOx7yVkQePfQ2QJ7VSnmUzcJacORSkKeVVGt6baxcq8iEO6o0JJGOS84sIfZFr9XPYT5JZBboSbuhJqnFFpDVgpw1ynwSKFyLbHDXi3jHqXT2r0vVXD9VjEEEIMA2q2B6ee5EyCaXHkuU0Zcom84meIisgmL6cPjXfThz9yIolXU4UyYR2LoXVujXp01kc8N01ehUYjNwyOEco1st0KaANSWsEHc4PEUC4BakKkVBhDDxJUehiAGizofCzt6gMtRsPAKmXVr0IIzDeOqLNBZ_1YhDgSBotwHcQsfM4j6k1pD51sfc4h2bAIHHeF-LjfGOXdgQEoGOaLT71bWbph4Bk1LQvDpQcQX1EyWUnKPcGkFNIEvGjA_l3dUMfIFjjci7w834gIXWptYIO8hk5sBL4ibzGtIdmFSnOaXlZZgiDsoXACpycYEIE0d4KicnED0vhPjQ5yRWZdmsojJhcBIoE6jpBX3foPFErPUcC6rU7F0BAK7qy9LsB4jAfQCMeMVTWgAxazxvI2CMRjQgG6UUOFrvMdaR9Se4G8Br67uRzeKFwEV_hzwsS484c0c8S3UMw5dzk-IqGlhyeWIOfk-EMYAF5g8gAAL7h5YPQfgpBkAgAoFQGgMfGCCFYBwbgMgU8CCEDoePEgpA0HkLgJQagNBaGEBqmggRcAdgwecbzhhXEBHWIeYgBu8rWHWA7p3Ewggp27KXKA5RAhp30BhUH2wXZTF2BZMqTklPvDKBUJqvg6gRFRLCKAg_ZjT1ulzjsOI3QoX0t6AE7cU5Kw7Go8IfFiBzl8Ok3wIthfvmYigDxYNmHrAiHm42aBpcw04AVReh_AFRngwBb44BLla5ZANg11TAnAycEM8QT9oVQE8YZEF8jU3IPILBoD8QQQCD5hvJkJQJ9IhFF4v9iAf8_9UpWwHE8w0BfBU1MgoCYDWg4DagoB6ghFBsCxbJbR9BrBfJqDaCFxUpACwc4B9AFQzAFQ0hICHhoDogDdOD4DnheDU5pEtla9iATB9smwhQU4wADxrlud4gch2lLQuselzcNhHV_Brd-s_15o5wMD2ARMOxlhTgGRr9Ag2FxEx4ypP4qViFyQlwEhhgWtMholdJs1bRYj3BiEJN-hwcHEwFF4pDmQiEz4tYRIUDqNIVoU3pRFcI0FVDYDslhgEC7lfhih7hIiM4xC2g6DI1iAloiNLJM0G5X83QWjf8JD2jOiosJwG4-wPBqQLAEVnYkUFp4dbkkdvANpBkEiIisdJsRdWMDkJcIABi6D3IzBiiMi8ZIC5xSj2Eax_BcAYAji8tDQsx2ERZcA_ZtdEx9gvIwALiAiMV0I2JSgUAUUjUHB1oTBNjRME4hxT0MCnAfClwqI3QYS4TlwejmpippFpErBQ8I9I8hAIBVAYATB2A0BVAIB4AkAABtAAXXDyAA&runFile=main.py&filesystemSize=20&error_messages=TigerPython">
        Ouvrir dans une nouvelle fenêtre
        </a>

        

Implémentation de la contrainte ``NotEqual``
============================================

En PPC, l'intérêt des contraintes n'est pas seulement de formuler le problème
dans la phase de modélisation, mais également de constituer des outils de
raisonnement par le biais d'**algorithmes de filtrage spécifiques** à chaque
contrainte. Un algorithme de filtrage permet de supprimer les valeurs
impossibles du domaine des variables impliquées dans la contrainte.

En d'autres termes, chaque contrainte :math:`c \in C` s'accompagne d'un
algorithme de filtrage :math:`\mathcal{F}_c` qui prend en entrée les domaines
des variables sur lesquelles porte la contrainte et qui élimine des domaines
certaines valeurs incohérentes, à savoir incompatibles avec les valeurs
présentes dans les autres domaines.

..  activecode:: toycsp_impl_notequal
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    Définissez une classe ``NotEqual(x, y)`` qui permet de représenter une
    contrainte de non-égalité entre les variables :math:`x` et :math:`y`, à
    savoir :math:`x \neq y`. Le constructeur prend aussi un troisième paramètre
    ``offset`` qui permet de spécifier la contrainte :math:`x \neq y +
    \text{offset}`.

    ..  admonition:: Consignes
        :class: note

        La classe doit également contenir les méthodes suivantes :

        -   ``propagate(self) -> bool`` : effectue la propagation (filtrage) sur
            les domaines des variables impliquées dans la contrainte. La
            contrainte peut effectuer une propagation dès que l'une des
            variables est fixée (n'a plus qu'une seule valeur dans son domaine).

        -   ``__repr__(self) -> str`` : retourne la représentation de la
            contrainte sous la forme ``NotEqual(x=Variable(...),
            y=Variable(...), offset=...)``.

    ..  admonition:: Conseils

        Commencez par créer les fichiers ``domain.py`` et ``variable.py`` dans
        lesquels vous copierez les classes ``Domain`` et ``Variable`` que vous
        avez implémentées précédemment. Ensuite, importez ces classes dans le
        fichier de votre contrainte et utilisez-les pour implémenter la classe
        ``NotEqual``. Vous pouvez aussi choisir de tout implémenter dans un même
        fichier, mais il est conseillé de faire du modularisation dès le début
        pour éviter d'avoir un fichier trop long et difficile à maintenir.


    ~~~~

    from domain import Domain
    from variable import Variable

    class NotEqual:
        """
        Constraint representing x != y + offset.

        >>> x = Variable(range(5, 10))
        >>> y = Variable(range(3, 8))
        >>> x
        Variable(Domain({5, 6, 7, 8, 9}), name='Var0')
        >>> y
        Variable(Domain({3, 4, 5, 6, 7}), name='Var1')
        >>> c1 = NotEqual(x, y)     # x != y
        >>> c2 = NotEqual(x, y, 2)  # x != y + 2
        >>> c3 = NotEqual(x, y, -1) # x != y - 1
        >>> c1
        NotEqual(x=Variable(Domain({5, 6, 7, 8, 9}), name='Var0'), y=Variable(Domain({3, 4, 5, 6, 7}), name='Var1'), offset=0)
        >>> c1.propagate()
        False
        >>> x
        Variable(Domain({5, 6, 7, 8, 9}), name='Var0')
        >>> y
        Variable(Domain({3, 4, 5, 6, 7}), name='Var1')
        >>> x.dom.fix(6)
        >>> c1.propagate()
        True
        >>> x
        Variable(Domain({6}), name='Var0')
        >>> y
        Variable(Domain({3, 4, 5, 7}), name='Var1')
        >>> c2.propagate()
        True
        >>> x
        Variable(Domain({6}), name='Var0')
        >>> y
        Variable(Domain({3, 5, 7}), name='Var1')
        >>> c3.propagate()
        True
        >>> x
        Variable(Domain({6}), name='Var0')
        >>> y
        Variable(Domain({3, 5}), name='Var1')

        """

        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()


..  reveal:: 6f490d63-d9d5-4bb7-b844-bff400627d42
    :showtitle: Solution
    :hidetitle: Cacher
    :modal:
    :instructoronly:

    ..  raw:: html
        
        <iframe 
            src="https://exp.webtigerpython.ethz.ch/#?fs=N4IgZglgNgpgziAXKAJgewLYEMIDsB0ADgJ5Ki5YYxIjrZ5GkA0IhWALgBY104EkgWKDljIh2xQtUQgAqnnYAOAIIAnVVma0RNAJoAmAB6cAxgGYAsgHMAygHUArACsARvocAvLAA0AcgAYALUcnGBtOADEYAHFfKBMACQAlQjcAFkIAeQhlAFcAGQg0gGkAYQxfOF0_DwBJAFEkgDcXOwjUpzRi2tLlKx7aiFqrLp6-hqh2E2jDKFaANVyUaIj_LDsATlza6I2MHfqrFAx54jCAIQhq30JdYnOAazcARk51tKO_VIwTK10bc4eQLeACKR2iiis5maJgwsnBnCgtQSgU4LgS83iAHdRr1-gARNIAagAChBHrV8f4rElduxdHYoLlivjZIRSjl-r1SU4PoFSg59AzDM9gRZunjkXAsfleoZZcpiAqPAr_GAQWguX0SbyiTsQblWkyyg8JeN8cozQTiWTHvlcDcYHCuhqtVZfK6xlYdcSdrMXBBOKbPXiPZqvT69dEDT5fGBAhgoGlghriiG-kkMBE4CZ9LIrZSbeSHvkMIEpKVOPoSQAVXTszk9c6yWERJzBABSnAMcCsxWizya5jBsPm7cc_h2vjR0SxVhcKw8KFKDwAbBzxr0CkUC_UmQYtrmoEvootdGZTV7C6Ti6XyzBK9WayCG5vlDy-QKhXYRWKCwk4DVdNvV1fVcljeNE2TOxU2A-YEg7UVgMjfVDEpal-WcBctkCGwrFfLUPysQJ8UOHxrECZRwzxTNs1zfMN0In1iN6DYGmaVp2gDTgAHYLBsOcLDMfwCLGIjMO_X9vHFK8APlXoPHVajtVA6NclHdgXDMQIoGKBJdA2CxiEvSUIiSYgUDsfMr0JG9HkYpt6heN47DSNAYA8CINjTZSQN9NSNK0nS9IMoyTPGepUXROIHO5ZjMOIYJB2OWQ0H48L-jM4gGTiXQsycTQqNaDYl1Kc5ErsOIXFwMEDGzFwyqqPx_GKGtcU3NIChGN17Cw9wvGa4JnBgVMr1KQZhna_poiSKBAnJMBvH0JkfCSRbiE4IEfwwBUAEdqg7XATGMqx8hrD4awwHC2oLSVeiGIZbs3c4OxcRM1jaOAfEIeJ7k4HYOLaVIiiseYszgSz5jqFZEoBE8Ngq2rpL-OHgQNUpurGzdqVpDZ6UZZlogyCZwO8FJhSkE46mSNBcMeZz3iOZa1jKvjSkEgSrAsCA50KTqdjSdgLG8Fqsa1dh2JaIHuKBUFCBJ1bbh_SmoeRJJaYBJ59FeRmUGZrAyrWaJ4UCZb9GCD5c3mfwMd8saJsxu7xmiKB9hmOZA1MDAUA8YobGUTgSX9wxMkdt83SbbLGSBAFZBgbxzigJJvA7YgtNqNBageQGuPJfwGXYX7zhaDBDAcHYcIBLEDrROxreBQYfIjyVTy-uxdCsWNUgdfOQlwzgvZ9uwPHOFBZXObuX1Du2na5c5tipP4U6O55pVBGfw6bLbDB23AooxX7lDYhI4mXTgo4cPfwmZGwMrGxOF1dnZj3WTxlgiXIDFSg6V7XzmrZajdMWYtAh0nQkvQ6JhV5YnXs3TeZVt6733piY6R8AYtBsFhMw5wHAmienPOYJ8oDTzgc3cqDJjx0zjgnJOKc05mAzlnCIiUzDzHYENScA5njDj-HCTuE4K7EGRKfCI7Bu5JBQIMU0sVHjBA7hBBMSYUxoCtnAeaDxTrnV4RsFo-IppYwerUfBTY7DAg7IQRRRcLHkhLmXCuuQ6aSVFACNRpibZhwjhEDsUAUAYjTrgCw65GyzyvFlSy8J1gdzcA4OAFwS7wmONmcJ85Tze3ZjScG9F5xmHVmYswsYoD5A8fbIYxTJQIR8X4gM5xXFuVUfNQUwpRTSXllSNipEyjBNke3KEy1Vz90QX7ZQ7BbSTyCfA8YD1YrhySPoa2x1zhGxNnSCh2wT6UwYsE8OsgTj-BQCndSHh9EhLxPMaIiIdgOGeK0bxJgbHzXOE4sU_CPjLAuTNKWucSjAPuhNYxZVEpk24RgD4C5Fh6SqtEXQSxwaQ19qNFus0HmLSMHMKAGwwAQrmFC-WpR_BRiZCgPR_zlCGP-ecOsdhnhIkXD0Tw31dIrhJWSn55VgRJGBZbOZaiID0u8D9PBMiHhyPnATLFC56w9Hxc_JYxKfmkr-aylEZNqa5IBOwV-qRvBsIrvsGmdMtY61cp0iZVgdnW32R2Q5xzTVnPec8b4kxLLUkSRDKyLyEQ0pzsDb5JyFWPVZYCjlsJQViqIRKmFSS67wv0TNOa5IKrJWdPUnmRxOj8IcC1f2IzyQQDcBsOAJCfkOw3plbxxVzbI1dcklA5IfhXQlvqzWDNjXTLdCCZeJgjkkrdCgdNdqkQojRAfNWTRkTls2ObGwJQ21enNXsg5XabWkPgohOm1jFlYGNkcWF7q9YRGpmyvwcwaoereV6z5wM5y0RzHmbJuSU75OPUU0tAxSmvpdnq-RrlenzB5Y0n8zTAmzpCeGqFka3VQ3tBOjYU6qxN3lXPDdhozAjm5Q0p50lxmkMDRQmOL03q-BaA6Qg0I5gVAcCBzeFTfGnGqS2XAmIqNQl2Za7YkVh0xQ8aAsGOx7yVkQePfQ2QJ7VSnmUzcJacORSkKeVVGt6baxcq8iEO6o0JJGOS84sIfZFr9XPYT5JZBboSbuhJqnFFpDVgpw1ynwSKFyLbHDXi3jHqXT2r0vVXD9VjEEEIMA2q2B6ee5EyCaXHkuU0Zcom84meIisgmL6cPjXfThz9yIolXU4UyYR2LoXVujXp01kc8N01ehUYjNwyOEco1st0KaANSWsEHc4PEUC4BakKkVBhDDxJUehiAGizofCzt6gMtRsPAKmXVr0IIzDeOqLNBZ_1YhDgSBotwHcQsfM4j6k1pD51sfc4h2bAIHHeF-LjfGOXdgQEoGOaLT71bWbph4Bk1LQvDpQcQX1EyWUnKPcGkFNIEvGjA_l3dUMfIFjjci7w834gIXWptYIO8hk5sBL4ibzGtIdmFSnOaXlZZgiDsoXACpycYEIE0d4KicnED0vhPjQ5yRWZdmsojJhcBIoE6jpBX3foPFErPUcC6rU7F0BAK7qy9LsB4jAfQCMeMVTWgAxazxvI2CMRjQgG6UUOFrvMdaR9Se4G8Br67uRzeKFwEV_hzwsS484c0c8S3UMw5dzk-IqGlhyeWIOfk-EMYAF5g8gAAL7h5YPQfgpBkAgAoFQGgMfGCCFYBwbgMgU8CCEDoePEgpA0HkLgJQagNBaGEBqmggRcAdgwYpo1Hx1gO6d5LXbLh8L1rxp92EUBuyl3C1MXYFkyrtxTkrDsajUw9dMJYKwl0Nj-GThEZ4DIsSTd-QGyU9QiPVQCK2SeLH5hYlHFtTNr9cDIisP0Gs1IwhqF1TX0-pQZ1bKIg-NBERUS9_77MPSXY3oUBdJWQ4BKR6gsQ_Y75bJbRy5F4wZmF1gIg81jYVEswHE8w0piA5xMgVxhd3xmIYAqI3R4DiBEDkDUppcw04BngFR9AFQzAFQ0gFQHAwBb5QDogDdWhZANg11TAnAycEM8QUJ1sCwv8vY-88o_9GhL1uI-IsD3R0lfBOZfBU1fBhJCBx5P4qUoAg5LJqhahDBU4oCixzgnB-I0F6gHAot6h5hDBLJsxGdQD1tcU3wnAr8b879kJVIjJwEF8l9vAV8193J0kwhBJBsuRrAP9A4ARy5ShexrBfIUJogLA6hF4_Dl9V87AcQHw5xQjNF6hcVIjehoicEpUuYvD_ILBDAZFMgtIkgIgTBtU0RKw0gSR5hv9Exf9dJpD29AweIlC5wVDBj5CcDsCRYNCyotDqVdCx9agsQjCnCHgNgSCyCFwKDQdmQAIVReh_AFQaDeg6DegzBWCHh2DOCrIeDRQ-D6hcA_Y5w3AEwAFaxlA8CiJdAPB6h1IEIhwVhcBFtGU74ONoooBpl38iCvQVi2hyC0BKCwdqDaD6DGDmCTizja5uDeCTB-DbiKi9QRDQkOiJCB9igejpY-ijJBjFDlDVD1DND3sdCbA9DvADCjCCxoDWdSwOJMFsBvARgVDjC7IzDMET8rpq47AUBOBlhUpBC-hV0kJEjQIEg-x8TxCujiSxs-jfAOsJj546SZj9D5jjJWSTDatnox9zEGRJ9-4nIlNacPILBQD8QQQHTZAHSUBNd7isx2Fb9GMsxiB-ITBXjmJ3jagvi69pgIg_iyYATRDzJwkjS7I0gZEzSJ81FwhrTG93IgR3T5xPTAhvSSCLBSgAzQSCC4JfTViUDYTNi4BtjlB9jlBji2DLk0TLjv8nAbjpS_IowUj7RyotJzhOBTZVhcIg8ukGMmM38CDwTTlyyoS1iYSNi9I4B9AUTmyuDWy-CBCcTkQ74xCf9JDuj1TeJyT3RxjaTtC9SmTDDDTpkyUuselzcNhHV_Brd-s_15pci9FQZZykC1jFjVxag9zOiDzx4mgExAhicAL2dlw0ELRcVpVLD4kN9N5ptTVepCBlg-9H5-kq1zkkREKUAbC7DPopxKt_AD8xNHMJN-h6hmFAhLBkKcNFSAKzIFNuSOxSpHkDoUzcJftks-gAtNQB1csDwHEyohRx8LTUy-LEMHifg5l_ARNjNt05KAFPt0RMRChzhIpTEJSfxyL7h_AXBiBlAZRqK31JomLIVoUP9j4lSAdBNcANEWsTTSEGswKyxidvQAQPKIK0Z9smxhUelEgwzfj_jxUcUpUow683B19mMJoIBmNZBvjwzIyltDK4t0iAjMi5xRLoQo5CUX8ArZ5DtF1u0TtTkEJnEJ4Hk0QnK1M3UEl9AD1x05hJ0UxiJa968Vt1Tr1Mk706jaZH0Ckkti1UtgF0twdcgHwHAtZ_BSY4xLNlFWpl0xZRc2NcsI0whZq3B5rAptJdIpqZq5rDQxUVxTpUZtpSw9gn8fEmVWVsUn4jrMETqFEoJlqgF9MvR1qDlNrwNjrdr1IThNIDqIqbKXrAajRmRzrih7hBMroywHQ7q747pAdOUMk6I8xirukO5HzAVypXyU0hstF8q7dZJvFaM0460Ox_ArDCLbD7C4BGcNgYAzBrLpqEh_BFiWa2a8tpqRZ2CbqkaiVngeJ3LwLZYkhNcTAyhNNIkrBHypioBrdvRb8rBEIMV290UwAOLY1JhpgEZostYAhgQAghU3ATbmp7Q3ckhNJ9BYJQ8I8o8QAadVA7sXBYBU949E9pAXasA3asAPaYBU8WA2AuAaBXb3bPac9tAq989JBfbi9S91BNA09K9RAZAa8YqARvNDBXEAh1hDxiADc8prBm9Hd5tJw9wggU4ujyhAg059AMINjn4h9Dayp0zlMygKgmpfA6ggLCTZhp5boucOwcQ3RhCO4WtkypL-45CKTBjxiSzeQjgPFITfzKzFytjVQ9jVyOCWyMSsTOzJ6HE6QZFO7bSPB7TKQnTKR5hvJtz9IhE4CfzoTWx0DUohirBMgmz971zagoB6ghFBt4zbR9AEjiDX75yqylzDiGzGC97zj0TnggGWTpla9iAZaZEJKOwwADxrlud4gch2lLR7zcaNdnzCaBs5xQE8YRMOxlhThZ62FxEx5Ji6SRMlwEhhgWtaj3BdJs1bQ-GHBiFzKpraGJZF4YGiEz45rCBOzZJ2a3pRFcI0E_73V051ari7lfhYbMduG0B17yDI1iAloiNLJM0G48DIGEC5zjYTGzGosJwG4-wPBqQLAEVnYkUFp4dbkkdvANpBlBHyQuHscZs8QfrxcoUIAjH5zWb2aJHWCPSVHvT4m-blH2ERZbitdu6n4vIwAMnAh76wB0I2JSgUAUUjUWCAmTAN9RME4hxT1aGnBGGlxpy-hmnWnlxLHmpippFpErBHbI9nba1VAYATB2A0A3b4AkAABtAAXXDyAA&runFile=main.py&filesystemSize=20&error_messages=TigerPython"
            style="min-width: 100%; min-height: 500px;"
            title="Visually Explained: Generators" frameborder="0" allowfullscreen>
        </iframe>

        <a href="https://exp.webtigerpython.ethz.ch/#?fs=N4IgZglgNgpgziAXKAJgewLYEMIDsB0ADgJ5Ki5YYxIjrZ5GkA0IhWALgBY104EkgWKDljIh2xQtUQgAqnnYAOAIIAnVVma0RNAJoAmAB6cAxgGYAsgHMAygHUArACsARvocAvLAA0AcgAYALUcnGBtOADEYAHFfKBMACQAlQjcAFkIAeQhlAFcAGQg0gGkAYQxfOF0_DwBJAFEkgDcXOwjUpzRi2tLlKx7aiFqrLp6-hqh2E2jDKFaANVyUaIj_LDsATlza6I2MHfqrFAx54jCAIQhq30JdYnOAazcARk51tKO_VIwTK10bc4eQLeACKR2iiis5maJgwsnBnCgtQSgU4LgS83iAHdRr1-gARNIAagAChBHrV8f4rElduxdHYoLlivjZIRSjl-r1SU4PoFSg59AzDM9gRZunjkXAsfleoZZcpiAqPAr_GAQWguX0SbyiTsQblWkyyg8JeN8cozQTiWTHvlcDcYHCuhqtVZfK6xlYdcSdrMXBBOKbPXiPZqvT69dEDT5fGBAhgoGlghriiG-kkMBE4CZ9LIrZSbeSHvkMIEpKVOPoSQAVXTszk9c6yWERJzBABSnAMcCsxWizya5jBsPm7cc_h2vjR0SxVhcKw8KFKDwAbBzxr0CkUC_UmQYtrmoEvootdGZTV7C6Ti6XyzBK9WayCG5vlDy-QKhXYRWKCwk4DVdNvV1fVcljeNE2TOxU2A-YEg7UVgMjfVDEpal-WcBctkCGwrFfLUPysQJ8UOHxrECZRwzxTNs1zfMN0In1iN6DYGmaVp2gDTgAHYLBsOcLDMfwCLGIjMO_X9vHFK8APlXoPHVajtVA6NclHdgXDMQIoGKBJdA2CxiEvSUIiSYgUDsfMr0JG9HkYpt6heN47DSNAYA8CINjTZSQN9NSNK0nS9IMoyTPGepUXROIHO5ZjMOIYJB2OWQ0H48L-jM4gGTiXQsycTQqNaDYl1Kc5ErsOIXFwMEDGzFwyqqPx_GKGtcU3NIChGN17Cw9wvGa4JnBgVMr1KQZhna_poiSKBAnJMBvH0JkfCSRbiE4IEfwwBUAEdqg7XATGMqx8hrD4awwHC2oLSVeiGIZbs3c4OxcRM1jaOAfEIeJ7k4HYOLaVIiiseYszgSz5jqFZEoBE8Ngq2rpL-OHgQNUpurGzdqVpDZ6UZZlogyCZwO8FJhSkE46mSNBcMeZz3iOZa1jKvjSkEgSrAsCA50KTqdjSdgLG8Fqsa1dh2JaIHuKBUFCBJ1bbh_SmoeRJJaYBJ59FeRmUGZrAyrWaJ4UCZb9GCD5c3mfwMd8saJsxu7xmiKB9hmOZA1MDAUA8YobGUTgSX9wxMkdt83SbbLGSBAFZBgbxzigJJvA7YgtNqNBageQGuPJfwGXYX7zhaDBDAcHYcIBLEDrROxreBQYfIjyVTy-uxdCsWNUgdfOQlwzgvZ9uwPHOFBZXObuX1Du2na5c5tipP4U6O55pVBGfw6bLbDB23AooxX7lDYhI4mXTgo4cPfwmZGwMrGxOF1dnZj3WTxlgiXIDFSg6V7XzmrZajdMWYtAh0nQkvQ6JhV5YnXs3TeZVt6733piY6R8AYtBsFhMw5wHAmienPOYJ8oDTzgc3cqDJjx0zjgnJOKc05mAzlnCIiUzDzHYENScA5njDj-HCTuE4K7EGRKfCI7Bu5JBQIMU0sVHjBA7hBBMSYUxoCtnAeaDxTrnV4RsFo-IppYwerUfBTY7DAg7IQRRRcLHkhLmXCuuQ6aSVFACNRpibZhwjhEDsUAUAYjTrgCw65GyzyvFlSy8J1gdzcA4OAFwS7wmONmcJ85Tze3ZjScG9F5xmHVmYswsYoD5A8fbIYxTJQIR8X4gM5xXFuVUfNQUwpRTSXllSNipEyjBNke3KEy1Vz90QX7ZQ7BbSTyCfA8YD1YrhySPoa2x1zhGxNnSCh2wT6UwYsE8OsgTj-BQCndSHh9EhLxPMaIiIdgOGeK0bxJgbHzXOE4sU_CPjLAuTNKWucSjAPuhNYxZVEpk24RgD4C5Fh6SqtEXQSxwaQ19qNFus0HmLSMHMKAGwwAQrmFC-WpR_BRiZCgPR_zlCGP-ecOsdhnhIkXD0Tw31dIrhJWSn55VgRJGBZbOZaiID0u8D9PBMiHhyPnATLFC56w9Hxc_JYxKfmkr-aylEZNqa5IBOwV-qRvBsIrvsGmdMtY61cp0iZVgdnW32R2Q5xzTVnPec8b4kxLLUkSRDKyLyEQ0pzsDb5JyFWPVZYCjlsJQViqIRKmFSS67wv0TNOa5IKrJWdPUnmRxOj8IcC1f2IzyQQDcBsOAJCfkOw3plbxxVzbI1dcklA5IfhXQlvqzWDNjXTLdCCZeJgjkkrdCgdNdqkQojRAfNWTRkTls2ObGwJQ21enNXsg5XabWkPgohOm1jFlYGNkcWF7q9YRGpmyvwcwaoereV6z5wM5y0RzHmbJuSU75OPUU0tAxSmvpdnq-RrlenzB5Y0n8zTAmzpCeGqFka3VQ3tBOjYU6qxN3lXPDdhozAjm5Q0p50lxmkMDRQmOL03q-BaA6Qg0I5gVAcCBzeFTfGnGqS2XAmIqNQl2Za7YkVh0xQ8aAsGOx7yVkQePfQ2QJ7VSnmUzcJacORSkKeVVGt6baxcq8iEO6o0JJGOS84sIfZFr9XPYT5JZBboSbuhJqnFFpDVgpw1ynwSKFyLbHDXi3jHqXT2r0vVXD9VjEEEIMA2q2B6ee5EyCaXHkuU0Zcom84meIisgmL6cPjXfThz9yIolXU4UyYR2LoXVujXp01kc8N01ehUYjNwyOEco1st0KaANSWsEHc4PEUC4BakKkVBhDDxJUehiAGizofCzt6gMtRsPAKmXVr0IIzDeOqLNBZ_1YhDgSBotwHcQsfM4j6k1pD51sfc4h2bAIHHeF-LjfGOXdgQEoGOaLT71bWbph4Bk1LQvDpQcQX1EyWUnKPcGkFNIEvGjA_l3dUMfIFjjci7w834gIXWptYIO8hk5sBL4ibzGtIdmFSnOaXlZZgiDsoXACpycYEIE0d4KicnED0vhPjQ5yRWZdmsojJhcBIoE6jpBX3foPFErPUcC6rU7F0BAK7qy9LsB4jAfQCMeMVTWgAxazxvI2CMRjQgG6UUOFrvMdaR9Se4G8Br67uRzeKFwEV_hzwsS484c0c8S3UMw5dzk-IqGlhyeWIOfk-EMYAF5g8gAAL7h5YPQfgpBkAgAoFQGgMfGCCFYBwbgMgU8CCEDoePEgpA0HkLgJQagNBaGEBqmggRcAdgwYpo1Hx1gO6d5LXbLh8L1rxp92EUBuyl3C1MXYFkyrtxTkrDsajUw9dMJYKwl0Nj-GThEZ4DIsSTd-QGyU9QiPVQCK2SeLH5hYlHFtTNr9cDIisP0Gs1IwhqF1TX0-pQZ1bKIg-NBERUS9_77MPSXY3oUBdJWQ4BKR6gsQ_Y75bJbRy5F4wZmF1gIg81jYVEswHE8w0piA5xMgVxhd3xmIYAqI3R4DiBEDkDUppcw04BngFR9AFQzAFQ0gFQHAwBb5QDogDdWhZANg11TAnAycEM8QUJ1sCwv8vY-88o_9GhL1uI-IsD3R0lfBOZfBU1fBhJCBx5P4qUoAg5LJqhahDBU4oCixzgnB-I0F6gHAot6h5hDBLJsxGdQD1tcU3wnAr8b879kJVIjJwEF8l9vAV8193J0kwhBJBsuRrAP9A4ARy5ShexrBfIUJogLA6hF4_Dl9V87AcQHw5xQjNF6hcVIjehoicEpUuYvD_ILBDAZFMgtIkgIgTBtU0RKw0gSR5hv9Exf9dJpD29AweIlC5wVDBj5CcDsCRYNCyotDqVdCx9agsQjCnCHgNgSCyCFwKDQdmQAIVReh_AFQaDeg6DegzBWCHh2DOCrIeDRQ-D6hcA_Y5w3AEwAFaxlA8CiJdAPB6h1IEIhwVhcBFtGU74ONoooBpl38iCvQVi2hyC0BKCwdqDaD6DGDmCTizja5uDeCTB-DbiKi9QRDQkOiJCB9igejpY-ijJBjFDlDVD1DND3sdCbA9DvADCjCCxoDWdSwOJMFsBvARgVDjC7IzDMET8rpq47AUBOBlhUpBC-hV0kJEjQIEg-x8TxCujiSxs-jfAOsJj546SZj9D5jjJWSTDatnox9zEGRJ9-4nIlNacPILBQD8QQQHTZAHSUBNd7isx2Fb9GMsxiB-ITBXjmJ3jagvi69pgIg_iyYATRDzJwkjS7I0gZEzSJ81FwhrTG93IgR3T5xPTAhvSSCLBSgAzQSCC4JfTViUDYTNi4BtjlB9jlBji2DLk0TLjv8nAbjpS_IowUj7RyotJzhOBTZVhcIg8ukGMmM38CDwTTlyyoS1iYSNi9I4B9AUTmyuDWy-CBCcTkQ74xCf9JDuj1TeJyT3RxjaTtC9SmTDDDTpkyUuselzcNhHV_Brd-s_15pci9FQZZykC1jFjVxag9zOiDzx4mgExAhicAL2dlw0ELRcVpVLD4kN9N5ptTVepCBlg-9H5-kq1zkkREKUAbC7DPopxKt_AD8xNHMJN-h6hmFAhLBkKcNFSAKzIFNuSOxSpHkDoUzcJftks-gAtNQB1csDwHEyohRx8LTUy-LEMHifg5l_ARNjNt05KAFPt0RMRChzhIpTEJSfxyL7h_AXBiBlAZRqK31JomLIVoUP9j4lSAdBNcANEWsTTSEGswKyxidvQAQPKIK0Z9smxhUelEgwzfj_jxUcUpUow683B19mMJoIBmNZBvjwzIyltDK4t0iAjMi5xRLoQo5CUX8ArZ5DtF1u0TtTkEJnEJ4Hk0QnK1M3UEl9AD1x05hJ0UxiJa968Vt1Tr1Mk706jaZH0Ckkti1UtgF0twdcgHwHAtZ_BSY4xLNlFWpl0xZRc2NcsI0whZq3B5rAptJdIpqZq5rDQxUVxTpUZtpSw9gn8fEmVWVsUn4jrMETqFEoJlqgF9MvR1qDlNrwNjrdr1IThNIDqIqbKXrAajRmRzrih7hBMroywHQ7q747pAdOUMk6I8xirukO5HzAVypXyU0hstF8q7dZJvFaM0460Ox_ArDCLbD7C4BGcNgYAzBrLpqEh_BFiWa2a8tpqRZ2CbqkaiVngeJ3LwLZYkhNcTAyhNNIkrBHypioBrdvRb8rBEIMV290UwAOLY1JhpgEZostYAhgQAghU3ATbmp7Q3ckhNJ9BYJQ8I8o8QAadVA7sXBYBU949E9pAXasA3asAPaYBU8WA2AuAaBXb3bPac9tAq989JBfbi9S91BNA09K9RAZAa8YqARvNDBXEAh1hDxiADc8prBm9Hd5tJw9wggU4ujyhAg059AMINjn4h9Dayp0zlMygKgmpfA6ggLCTZhp5boucOwcQ3RhCO4WtkypL-45CKTBjxiSzeQjgPFITfzKzFytjVQ9jVyOCWyMSsTOzJ6HE6QZFO7bSPB7TKQnTKR5hvJtz9IhE4CfzoTWx0DUohirBMgmz971zagoB6ghFBt4zbR9AEjiDX75yqylzDiGzGC97zj0TnggGWTpla9iAZaZEJKOwwADxrlud4gch2lLR7zcaNdnzCaBs5xQE8YRMOxlhThZ62FxEx5Ji6SRMlwEhhgWtaj3BdJs1bQ-GHBiFzKpraGJZF4YGiEz45rCBOzZJ2a3pRFcI0E_73V051ari7lfhYbMduG0B17yDI1iAloiNLJM0G48DIGEC5zjYTGzGosJwG4-wPBqQLAEVnYkUFp4dbkkdvANpBlBHyQuHscZs8QfrxcoUIAjH5zWb2aJHWCPSVHvT4m-blH2ERZbitdu6n4vIwAMnAh76wB0I2JSgUAUUjUWCAmTAN9RME4hxT1aGnBGGlxpy-hmnWnlxLHmpippFpErBHbI9nba1VAYATB2A0A3b4AkAABtAAXXDyAA&runFile=main.py&filesystemSize=20&error_messages=TigerPython">
        Ouvrir dans une nouvelle fenêtre
        </a>    
        
    ..  
        code-block:: python
            
        class NotEqual():
            """
            Constraint representing x != y + offset.

            >>> x = Variable(range(5, 10))
            >>> y = Variable(range(3, 8))
            >>> x
            Variable(dom={5, 6, 7, 8, 9}, name='Var0')
            >>> y
            Variable(dom={3, 4, 5, 6, 7}, name='Var1')
            >>> c1 = NotEqual(x, y)     # x != y
            >>> c2 = NotEqual(x, y, 2)  # x != y + 2
            >>> c3 = NotEqual(x, y, -1) # x != y - 1
            >>> c1
            NotEqual(x=Variable(dom={5, 6, 7, 8, 9}, name='Var0'), y=Variable(dom={3, 4, 5, 6, 7}, name='Var1'), offset=0)
            >>> c1.propagate()
            False
            >>> x
            Variable(dom={5, 6, 7, 8, 9}, name='Var0')
            >>> y
            Variable(dom={3, 4, 5, 6, 7}, name='Var1')
            >>> x.dom.fix(6)
            >>> c1.propagate()
            True
            >>> x
            Variable(dom={6}, name='Var0')
            >>> y
            Variable(dom={3, 4, 5, 7}, name='Var1')
            >>> c2.propagate()
            True
            >>> x
            Variable(dom={6}, name='Var0')
            >>> y
            Variable(dom={3, 5, 7}, name='Var1')
            >>> c3.propagate()
            True
            >>> x
            Variable(dom={6}, name='Var0')
            >>> y
            Variable(dom={3, 5}, name='Var1')

            """

            def __init__(self, x: Variable, y: Variable, offset: int = 0) -> None:
                """
                Initializes the NotEqual constraint.

                Args:
                    x: The first variable.
                    y: The second variable.
                    offset: The offset value. Defaults to 0.
                """
                self.x = x
                self.y = y
                self.offset = offset

            def propagate(self) -> bool:
                """
                Propagates the NotEqual constraint.

                Returns:
                    True if any value was removed from a domain, False otherwise.
                """
                if self.x.dom.is_fixed():
                    return self.y.dom.remove(self.x.dom.min() - self.offset)
                elif self.y.dom.is_fixed():
                    return self.x.dom.remove(self.y.dom.min() + self.offset)
                return False

            def __repr__(self) -> str:
                return f'NotEqual(x={self.x}, y={self.y}, offset={self.offset})'

