.. _generate-and-test.rst:

Visualisation de la recherche exhaustive naïve
##############################################

..  contents:: Contenu de la page
    :depth: 3

Exécutez le programme suivant pour visualiser la recherche exhaustive de
solutions pour les instances du problème représentées dans la docstring de la
fonction ``nqueens_solver``.

..  activecode:: 5e3f3147-eed0-4ab7-9f73-371b2af176a6
    :language: webtp

    from itertools import product
    from collections.abc import Iterable
    
    # Visualisation avec la tortue graphique de WebTP
    from gturtle import *

    def chess_board(solution: Iterable[int], x: int = 0, y: int = 0, size: int = 50, color="black") -> tuple[int, int]:
        def square(cx, cy) -> None:
            setPos(cx - size / 2, cy - size / 2)
            for _ in range(4):
                fd(size)
                rt(90)

        def queen(cx, cy):
            setPos(cx, cy)
            dot(size * 0.7)
            
        hideTurtle()
        setPenColor(color)
        setFontSize(size * 0.95)

        n = len(solution)

        for i in range(n):
            for j in range(n):
                cx = x + i * size - size / 2
                cy = y + j * size - size / 2
                square(cx, cy)
                if solution[i] == j:
                    queen(cx, cy)

        setPos(x - size, y - 2 * size)
        setHeading(0)
        label("  ".join(str(q) for q in solution))

        return n, size

    def generate_solutions(n: int) -> list[tuple[int, ...]]:
        '''
        >>> generate_solutions(n=0)
        [()]
        >>> generate_solutions(n=1)
        [(0,)]
        >>> generate_solutions(n=2)
        [(0, 0), (0, 1), (1, 0), (1, 1)]
        >>> n = 3
        >>> x = generate_solutions(n)
        >>> x[:6]
        [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2)]
        >>> x[-6:]
        [(2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]
        >>> len(x) == n ** n
        True
        '''
        domain = list(range(n))
        return list(product(domain, repeat=n))


    def check_constraints(q: Iterable[int]) -> bool:
        '''

        Vérifie que toutes les contraintes du problème soient satisfaites dans
        la solution ``q`` représentant la ligne sur laquelle est placée chaque
        dames ``q[i]``.

        >>> check_constraints([0])
        True
        >>> check_constraints([1, 3, 0, 2])
        True
        >>> check_constraints([1, 3, 5, 0, 2, 4])
        True

        >>> check_constraints([0, 1, 2, 3])
        False
        >>> check_constraints([3, 2, 1, 0])
        False
        >>> check_constraints([1, 3, 0, 0])
        False
        >>> check_constraints([1, 4, 5, 2, 0, 4])
        False

        '''
        n = len(q)

        for i in range(n):
            for j in range(i + 1, n):
                if q[i] == q[j]: return False
                if q[i] - q[j] == i - j: return False
                if q[j] - q[i] == i - j: return False

        return True

    def nqueens_solver(n: int) -> list[tuple[int, ...]]:
        '''
        >>> nqueens_solver(n=1)
        [(0,)]
        >>> nqueens_solver(n=2)
        []
        >>> nqueens_solver(n=3)
        []
        >>> nqueens_solver(n=4)
        [(1, 3, 0, 2), (2, 0, 3, 1)]
        >>> nqueens_solver(n=5)
        [(0, 2, 4, 1, 3), (0, 3, 1, 4, 2), (1, 3, 0, 2, 4), (1, 4, 2, 0, 3), (2, 0, 3, 1, 4), (2, 4, 1, 3, 0), (3, 0, 2, 4, 1), (3, 1, 4, 2, 0), (4, 1, 3, 0, 2), (4, 2, 0, 3, 1)]
        '''
        feasible_solutions = []
        for sol in generate_solutions(n):
            clear()
            if check_constraints(sol):
                chess_board(sol, color="green")
                delay(3000)
                feasible_solutions.append(sol)
            else:
                chess_board(sol, color="red")
                delay(10)
        return feasible_solutions

    if __name__ == '__main__':
        import doctest
        doctest.testmod()