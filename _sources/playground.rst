.. _playground-aaf1d75d-d0ce-423b-8972-6540929b39fd.rst:

Playground
##########

..  raw:: html

    <script>
    // change this to show exam to students
    const hide = true;
    
    $('.nav.navbar-nav').hide()
    if (hide && !eBookConfig.isInstructor) {
        $('div#main-content').hide()
    }
    </script>


..  contents:: Contenu de la page
    :depth: 3

Visualiser l'arbre de recherche avec ``gturtle``
================================================

..  activecode:: tree-visu
    :language: webtp

    from gturtle import *

    def node(x: int, y: int, size: float, text: str, color = "black", bg_color = "lightgray") -> None:
        setPos(x, y)
        setPenColor(color)
        dot(size)
        setPenColor(bg_color)
        dot(size - 2)
        penUp()
        lt(-90)
        fd(size // 2 + 5)
        rt(-90)
        bk(5)
        penDown()
        setPenColor("black")
        setFontSize(20)
        label(text)

    hideTurtle()
    node(0, 0, 50, "q[0] = .")



Visualiser la propagation des n dames
=====================================

..  activecode:: playground-visu-propagation
    :language: webtp

Events
======

..  activecode:: playground-csp-events
    :language: webtp


BitSetDomain
============

..  activecode:: playground-butset-domain
    :language: webtp

    
SparseSet
=========

..  activecode:: playground-sparseset
    :language: webtp


StateManager
============

..  activecode:: playground-statemanager
    :language: webtp

Runestonelib
============

..  activecode:: runestone-lib
    :language: webtp