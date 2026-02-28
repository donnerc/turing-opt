class Fraction:

    '''
    Classe Fraction : représente une fraction 

    #Manières d'appeler le constructeur de fractions.
    >>> Fraction(4, 0)
    Traceback (most recent call last):
    ValueError: Unable to define fraction with zero denominator
    >>> Fraction(4, -6)
    Fraction(-2, 3)
    >>> Fraction('-5/6')
    Fraction(-5, 6)
    >>> Fraction('4')
    Fraction(4, 1)
    >>> Fraction('5.0')
    Fraction(5, 1)
    >>> Fraction('4.2')
    Fraction(21, 5)
    >>> f1, f2 = Fraction(6, 3), Fraction(2, 5)
    >>> f3, f4 = Fraction(3, -2), Fraction(3, 2)
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
    >>> f3 < f4
    True
    >>> 
    >>> f4 > f3
    True
    >>> f1 >= f2
    True
    >>> gcd(15, 21)
    3
    >>> gcd(15, 5)
    5
    '''

    def __init__(self, num, denom=None):

        if denom is None:

            if isinstance(num, str) and "/" in num:
                num, denom = [int(x) for x in num.split("/")]
            else:
                # s'il n'y a qu'un seul argument passé à la fonction, considérer ce
                # nombre comme flottant et déterminer la fraction équivalente
                try:
                    num = float(num)
                except:
                    raise ValueError("Unable to transform number {num} to a fraction".format(num=num))

                # déterminer le nombre de décimales du nombre et multiplier 
                try:
                    n_decimals = len(str(num).split('.')[1])
                except:
                    n_decimals = 0

                num = num * 10 ** n_decimals
                denom = 10 ** n_decimals
        
        if denom == 0:
            raise ValueError("Unable to define fraction with zero denominator")

        # la fraction est automatiquement réduite lors de l'instanciation.
        self.num, self.denom = Fraction.reduce(int(num), int(denom))
        

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __repr__(self):
        return 'Fraction({num}, {denom})'.format(num=self.num, denom=self.denom)

    def show(self):
        print(self.num, "/", self.denom)

    @staticmethod
    def reduce(num, denom):
        common_divisor = gcd(num, denom)
        return num // common_divisor, denom // common_divisor
        

    def __add__(self, other):
        newnum = self.num * other.denom + self.denom * other.num
        newden = self.denom * other.denom
        
        return Fraction(newnum, newden) 
                    
    def __sub__(self, other):
        newnum = self.num * other.denom - self.denom * other.num
        newden = self.denom * other.denom
        return Fraction(newnum, newden) 
                    
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.denom * other.denom
        return Fraction(newnum, newden) 

    def __truediv__(self, other):
        newnum = self.num * other.denom
        newden = self.denom * other.num
        return Fraction(newnum, newden) 

    def __eq__(self, other):
        ab = self.num * other.denom
        cd = other.num * self.denom

        return ab == cd

    def __gt__(self, other):
        ab = self.num * other.denom
        cd = other.num * self.denom
        
        return ab > cd

    def __lt__(self, other):
        ab = self.num * other.denom
        cd = other.num * self.denom

        return ab < cd


    def __ge__(self, other):
        ab = self.num * other.denom
        cd = other.num * self.denom
        
        return ab >= cd

    def __le__(self, other):
        ab = self.num * other.denom
        cd = other.num * self.denom

        return ab <= cd
                                          
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