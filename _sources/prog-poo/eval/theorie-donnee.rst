..  header::

    OCI 3, Notions liées au projet "Moteur de recherche", examen écrit           Prénom : ....................... / Note : ...........


***************************************
Projet 1 : Examen écrit sur les notions
***************************************

..  admonition:: Consignes générales

    *   Barème : ...... / 50 points
    *   Les temps indicatifs pour chaque question sont indiqués
    *   Respecter la syntaxe Python au mieux
    *   Si vous ne parvenez pas à voir comment coder quelque chose en Python, expliquez au mieux les étapes de résolution en pseudo-code et/ou en français.

Question 1 (... / 5 points)
==========

Compléter le code de la fonction ``supprime_ponctuation(texte) ==> str :
texte`` qui enlève la ponctuation du texte ``texte`` à l'aide des
substitutions suivantes

**Indication**

    Utiliser la méthode ``chaine.replace(pattern, subst)`` qui retourne la
    chaine ``chaine`` dans laquelle toutes les occurrences de ``pattern`` sont
    remplacées par ``subst``.

    **Exemple d'utilisation**

    ::

        >>> "salut".replace('ut', 'utation')
        "salutation"


**Code Python**

..  only:: not corrige

    ::

        def supprime_ponctuation(texte):
            ponctuation = ',.!?;:'

            # compléter le code ici















            return texte

..  only:: corrige

    ..  code-block:: python
        :linenos:
        :include: supprime_ponctuation.py

    ..  literalinclude:: scripts/supprime_ponctuation.py
        :linenos:

..  _sec-exo-keyword-freq:

Question 2 ( ... / 9 points)
==========

Rédiger le code d'une fonction ``keyword_freq(text) ==> dict`` qui retourne un
dictionnaire indiquant tous les mots clés apparaissant dans la chaine de
caractères ``content`` et le nombre d'apparition de chaque mot clé dans la
chaine en question. 

**Indications**

*   La casse ne doit pas être respectée (il ne faut pas faire la différence entre
    les majuscules et les minuscules). Tous les caractères doivent donc être mis
    en minuscules.

*   Utiliser la fonction ``supprime_ponctuation`` de la question précédente
    pour supprimer la ponctuation avant d'extraire les mots de ``text``.

*   Utiliser la méthode ``str.lower()`` qui permet de mettre le texte en minuscules :
        
    ::

        >>> 'SaLuT'.lower()
        'salut'

Exemples d'utilisation
----------------------

::  

    >>> content = '''Si six scies scient six cyprès, six cent six scies scient six cent six cyprès'''
    >>> keyword_freq(content)
    {'cyprès': 2, 'scient': 2, 'cent': 2, 'six': 6, 'si': 1, 'scies': 2}
    >>> keyword_freq('')
    {}

Code Python
-----------

..  only:: not corrige

    ..  raw:: pdf

        Spacer 0 200


..  only:: corrige

    ..  literalinclude:: scripts/keyword_freq.py
        :linenos:

..  raw:: pdf

    PageBreak        

Question 3 ( ... / 6 points)
==========

On donne la fonction ``mystery`` définie par

::

    def mystery(c, k):
        w = []
        for a,b in c.items():
            if b == k and a not in w:
                w += [a]
        return w

Expliquer ce que fait la fonction ``mystery`` et déterminer la valeur de ``A``
et ``B`` après l'exécution des instructions suivantes :

::

    f = {'cyprès': 2, 'scient': 2, 'cent': 2, 'six': 6, 'si': 1, 'scies': 2}
    A = mystery(f, 2)
    B = mystery(f, 3)

..  raw:: pdf

    Spacer 0 30

..  only:: corrige
    
    Solution
    --------

    La fonction ``mystery(c,k)`` retourne une liste contenant tous les mots
    apparaissant exactemement ``k`` fois dans le dictionnaire ``c``. Ainsi, on
    aura les valeurs suivantes pour ``A`` et ``B`` : 

    ::

        >>> print(sorted(A))
        ['cent', 'scient', 'scies', 'cyprès']
        >>> print(sorted(B))
        []

Question 4 ( ... / 2 points)
==========

Qu'affiche le programme suivant :

::

    nombres = [1,2,3,4,5]
    copie = nombres
    copie[0] = 10
    print(nombres)
    print(copie)

**Affichage**

..  raw:: pdf
    
    Spacer 0 80
    PageBreak

..  only:: corrige

    Puisque la liste ``copie`` est un alias et non une véritable copie de
    ``nombres``, ces deux identifiants pointent vers la même liste en mémoire,
    ce qui engendre la sortie suivante :

    ::

        [10, 2, 3, 4, 5]
        [10, 2, 3, 4, 5]


Question 5 ( ... / 4 points)
==========

Compléter le code de la fonction ``copy`` pour qu'elle retourne une
véritable copie de la liste ``original``.

**Exemple d'utilisation**

::

    >>> fibonacci = [1,1,2,3,5,8,11]
    >>> copie = copy(fibonacci)
    >>> copie[0] = 2
    >>> print(fibonacci)
    [1,1,2,3,5,8,11]
    >>> print(copie)
    [2,1,2,3,5,8,11]

..  only:: not corrige

    ::

        def copy(original):

            # compléter le code














            ##########

..  only:: corrige

    Solution 1
    ----------

    ..  code-block:: python
        :linenos:

        def copy(original):

            copie = []

            for element in original:
                copie += [element]

            return copie


    Solution 2
    ----------

    ..  code-block:: python
        :linenos:

        def copy(original):

            return original[:]



Question 6 ( ... / 6 points)
==========

Indiquer la valeur de chaque variable du code ci-dessous après l'exécution du
programme. Signaler toute erreur éventuelle du programme


..  code-block:: python

    >>> notes = dict([("A", 5.6),
                      ("B", 5.37),
                      ("C", 3.97)])

    >>> a = notes["A"]

    >>> b = notes[5.37]

    >>> c = notes[B]

    >>> d = list(notes.keys())

    >>> e = list(notes.values())

    >>> f = list(notes.items())

..  only:: corrige

    Valeurs des variables
    ---------------------

    Voici la valeur des variables après l'exécution de chaque instruction

    *   ``notes`` : ``{'C': 3.97, 'B': 5.37, 'A': 5.6}``. Attention, il se peut que les éléments n'apparaissent pas dans cet ordre
    
    *   ``a`` : ``5.6``
    
    *   ``b`` : Produit une erreur
    
    *   ``c`` : Produit une erreur
    
    *   ``d`` : ``['C', 'B', 'A']``
    
    *   ``e`` : ``[3.97, 5.37, 5.6]``
    
    *   ``f`` : ``[('C', 3.97), ('B', 5.37), ('A', 5.6)]``


Question 7 : analyse de code ( ... / 8 points)
============================

Questions de compréhension de code
----------------------------------

Les questions suivantes se rapportent au code distribué en annexe à la fin de l'examen.

a)  Indiquer une ligne qui définit une variable globale
    
    ..  only:: not corrige
        
        ::

            # variable globale : 

    ..  only:: corrige

        ..  admonition:: Réponse

            Dans ``crawler.py``, la variable ``index`` définie à la ligne 9
            est une variable globale

b)  Indiquer une ligne qui définit une variable locale

    ..  only:: not corrige
        
        ::

            # variable locale : 

    ..  only:: corrige

        ..  admonition:: Réponse

            Toutes les variables définies dans le corps d'une fonction est une
            variable **locale**, par exemple la variable ``start`` définie à
            la ligne 38 dans la fonction ``get_all_links`` dans le fichier
            ``crawler.py``.

c)  À quoi sert le module ``urllib.request`` et préciser dans quel cas le code se trouvant dans le bloc ``except`` est exécuté.
    
    ..  raw:: pdf

        Spacer 0 65

    ..  only:: corrige

        ..  admonition:: Réponse

            a)  Ce module sert à télécharger des pages depuis Internet à l'aide d'une
                URL grâce à la méthode ``urlib.request.urlopen(<url>)``. De manière
                plus précise, ce module permet d'envoyer des requêtes **GET** à un
                serveur HTTP pour recevoir le document spécifié par l'URL ``<url>``.

            b)  La ligne de code 

                ::

                    fd = urllib.request.urlopen(url)

                lève une exception et causera l'exécution du bloc ``except`` si
                l'url spécifiée dans ``url`` n'existe pas (mauvaise URL) ou si la
                page en question n'est pas accessible pour des raisons de
                connexion Internet ou de problèmes du serveur HTTP.



d)  À quoi servent les instructions ``try ... except ...`` dans le fichier ``crawler.py`` aux lignes 12 à 18.
    :

    ..  raw:: pdf

        Spacer 0 65

    ..  only:: corrige

        ..  admonition:: Réponse

            L'instruction ``try ... except ...`` permet de gérer les
            exceptions (*Exception handling* en anglais). Ainsi, si l'une des
            instructions contenues dans le bloc ``try`` lèvent une exception,
            le programme ne va pas planter avec un message d'erreur, mais ce
            seront les instructions présentes dans le bloc ``except`` qui vont
            prendre en charge la gestion de l'exception et permettre au
            programme de réagir de manière adaptée.

Question 8 ( ... / 8 points)
==========

Le patron de ProSearch vous demande d'améliorer l'index pour
pouvoir tenir compte du nombre d'occurrences des mots-clés sur la page web correspondant à l'URL. Les
développeurs novices que vous avez sous vous ordres vous proposent les
structures de données suivantes pour implémenter l'index et n'arrivent pas à choisir la bonne alternative :

::

    index1 = [[kw1, [url11, url12, ...], n1],
              [kw2, [url21, url22, url23], n2],
               ...]

    index2 = [[kw1, [[url11, n11], [url12, n12], ...]],
              [kw2, [[url21, n21], [url22, n22], ...]],
              ...]

    index3 = {kw1 : [n1, [urls]],
              kw2 : [n2, [urls]],
              ...}

    index4 = {kw1 : [[url11, n11], [url12, n12], ...],
              kw2 : [[url21, n21], [url22, n22], ...],
              ...}

Consignes
---------

Déterminer quelles sont les structures de données possibles pour implémenter
la fonctionnalité souhaitée dans l'index et déterminer laquelle est la meilleure.

a)  Souligner les structures utilisables mais pas nécessairement optimales.


b)  Entourner la meilleure structure de données et justifier votre choix

    ..  raw:: pdf

        Spacer 0 120

c)  Faites une représentation de chaque structure de données ``index2`` selon
    la nomenclature vue au cours

..  raw:: pdf

    Spacer 0 500

Question 9 (6 points)
==========

a)  Modifier le fichier ``crawler.py`` pour implémenter la fonctionnalité demandée
    à l'exercice 8 avec la structure de données choisie dans la partie 8.b)

b)  Modifier la fonction ``lookup(kw)`` dans ``index.py`` pour tenir compte du nombre de
    recherches impliquant le mot-clé ``kw``.

c)  Définir une fonction ``count_kw(url, kw)`` qui retourne le nombre
    d'occurrences du mot-clé ``kw`` dans la page Web indiquée par ``url`` sur la base
    de ce qui est stocké dans l'index avec l'aternative choisie.

Annexes : code source à analyser
================================

``index.py``
------------

..  code-block:: python
    :linenos:

    ##############################################################
    ### Structure de données à utiliser pour l'index
    ##############################################################

    index4 = [['Python', ['http://www.python.org', 'http://www.donner-onlinech/oci']],
              ['Informatique', ['http://www.soi.ch', 'http://concours.castor-informatique.ch/']]
             ]

    # indiquer l'implémentation utilisée
    index = index4

    ##############################################################
    ### Fonctions auxiliaires
    ##############################################################

    def get_kw(entry):
        return entry[0]

    def get_urls(entry):
        return entry[1]

    def add_entry_to_index(index, keyword, url):
        index.append([keyword, [url]])

    def add_url_to_entry(entry, url):
        entry[1].append(url)

    def get_kw_position(index, keyword):
        i = 0
        while i < len(index):
            if get_kw(index[i]) == keyword:
                position = i
                break            
            i += 1

        return position

    ##############################################################
    ### Fonctions principales
    ##############################################################

    def lookup(index, keyword):

        for entry in index:
            if get_kw(entry) == keyword:
                urls = get_urls(entry)
                break

        return urls

    def add_to_index(index, keyword, url):

        position = get_kw_position(index, keyword) 
        if position == -1:
            add_entry_to_index(index, keyword, url)

        else:
            add_url_to_entry(index[position], url)



``crawler.py``
--------------

..  code-block:: python
    :linenos:

    ############################################################################################
    ## Moteur d'indexation
    ############################################################################################

    import urllib.request

    from index import *

    index = []

    def get_page(url):
        try:
            fd = urllib.request.urlopen(url)
            html = fd.read()

            return str(html)
        except:
            return ''

    def get_next_target(page, start=0):
        
        url = None
        pattern = '<a href="'
        start_tag = page.find(pattern, start)
        
        if start_tag == -1:
            return (None, -1)
        
        start_url = start_tag + len(pattern)
        end_url = page.find('"', start_url)
        
        url = page[start_url:end_url]
        
        return (url, end_url+1)
        
    def get_all_links(html):
        
        start = 0
        urls = []
        
        if len(html) == 0:
            return []
            
        while start != -1:
            url, end = get_next_target(html, start)
            start = end
            
            if url is not None:
                urls.append(url)
        
        return urls
        
    def get_keywords(html):
        mots = html.split(' ')
        return mots
        
    def crawl_web(seed): 
        tocrawl = [seed]
        crawled = [] 

        while tocrawl:
            
            page = tocrawl.pop() 
            
            if page not in crawled:
                html = get_page(page)
                newpages = get_all_links(html)
                
                keywords = get_keywords(html)
                for kw in keywords:
                    add_to_index(index, kw, page)
                    
                
                for url in newpages:
                    if url not in tocrawl:
                        tocrawl = tocrawl + [url]

                crawled.append(page)
                
        return crawled    
        
