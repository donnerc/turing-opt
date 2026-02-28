class Vector:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, other: "Vector") -> "Vector":
        return self.x * other.x + self.y * other.y + self.z * other.z

    def norm_squared(self) -> float:
        return self.x**2 + self.y**2 + self.z**2

    def norm(self) -> float:
        return self.norm_squared() ** 0.5

    def __invert__(self) -> float:
        return self.norm()

    def __floordiv__(self, other: "Vector", epsilon: float = 0.00000001) -> bool:
        return self.norm() * other.norm() - self * other < epsilon

    def __eq__(self, other: "Vector") -> "Vector":
        return all([self.x == other.x, self.y == other.y, self.z == other.z])
    def __ne__(self, other: "Vector") -> "Vector":
        return not self == other

    def __lt__(self, other: "Vector") -> "Vector":
        return self.norm() < other.norm()
    def __le__(self, other: "Vector") -> "Vector":
        return self.norm() <= other.norm()
    def __gt__(self, other: "Vector") -> "Vector":
        return self.norm() > other.norm()
    def __ge__(self, other: "Vector") -> "Vector":
        return self.norm() >= other.norm()

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"


def test():
        v1 = Vector(1, 1, 1)
        v2 = Vector(2, 2, 2)
        v3 = Vector(0, -2, 4)
        epsilon = 0.00000001

        # Addition vectorielle
        v = v1 + v2
        # Tester l'égalité de deux vecteurs
        assert v == Vector(3, 3, 3)
        # Différence entre deux vecteurs
        v = v - v2
        assert v == v1
        # Opposé du vecteur v1
        assert -v1 == Vector(-1, -1, -1)
        # Produit scalaire
        assert v1 * v2 == 6
        # Tester si deux vecteurs sont parallèles
        assert v1 // v2 == True
        assert v1 // v3 == False
        # Calculer la norme d'un vecteur
        assert ~v1 - v1 * v1 < epsilon
        assert ~(v1 + v2) - 27 ** .5 < epsilon
        # Comparaison de vecteurs
        assert v1 < v2
        assert v1 <= v1
        assert v1 <= v2
        assert v1 != v2
        assert v2 > v1
        assert v2 >= v1 


test()
