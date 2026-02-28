class Fraction:
    
    '''
    Classe Fraction : représente une fraction 

    #Manières d'appeler le constructeur de fractions.
    >>> Fraction(4, -6)
    Fraction(-2, 3)
    >>> Fraction('-5/6')
    Fraction(-5, 6)
    >>> Fraction('4')
    Fraction(4, 1)
    >>> Fraction('4.2')
    Fraction(21, 5)
    >>> f1, f2 = Fraction(6, 3), Fraction(2, 5)
    >>> f1 + f2
    Fraction(12, 5)
    >>> f1 - f2
    Fraction(8, 5)
    >>> f1 * f2
    Fraction(4, 5)
    >>> f1 / f2
    Fraction(5, 1)
    >>> f2 < f1
    True
    >>> f2 > f1
    False
    >>> Fraction(1, 2) <= Fraction(2, 4)
    True
    >>> Fraction(1, 2) >= Fraction(2, 4)
    True
    >>> f1 == f2
    False
    >>> f1 <= f2
    False
    >>> f1 >= f2
    True
    >>> gcd(15, 21)
    3
    >>> gcd(15, 5)
    5
    '''

    def __init__(self, num, denom):

        self.num = num
        self.denom = denom
        

    def __str__(self):
        pass

    def __repr__(self):
        pass

    
                                          
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

if __name__ == '__main__':
    import doctest
    doctest.testmod()