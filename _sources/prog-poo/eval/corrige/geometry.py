from random import random
from math import sqrt

class Point(object):

    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # lors de la création de chaque nouvelle instance, le compteur sera
        # automatiquement mis à jour
        Point.count += 1

    def distance(self, other):
        return sqrt((self.x - other.x)** 2 + (self.y - other.y)**2)

    @classmethod
    def count(cls):
        return cls.count

    def __str__(self):
        return 'Point ({x} ; {y})'.format(x=self.x, y=self.y)

    def __repr__(self):
        return self.__str__()


class Rect(object):

    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rect):

    def __init__(self, side):
        Rect.__init__(self, origin, side, side)


class EuclidianPlane(object):

    #todo 1 point
    origin = Point(0,0)

    def __init__(self):
        self.points = []

    def generate(self, n=10):
        self.points = []

        for i in range(n):
            self.points += [Point(random(), random())]

        return self.points

    def get_num_points(self):
        #todo 1 point
        return len(self.points)

    def get_max_dist_from(self, ref_point):
        result = ref_point
        max_dist = 0

        for p in self.points:
            cur_dist = p.distance(ref_point)
            if cur_dist > max_dist:
                max_dist = cur_dist
                result = p


        return max_dist


def test():
    p1 = Point(3, 4)
    p2 = Point(0, 0)
    assert(p1.distance(p2) == 5.0)
    assert(p2.distance(p1) == 5.0)
    assert(str(p1) == 'Point (3 ; 4)')

    points = EuclidianPlane()
    points.generate(n=5)
    print(points.points)
    assert(points.get_num_points() == 5)
    points.generate(n=5)
    assert(points.get_num_points() == 5)
    print(points.points)
    print('Max distance : ', points.get_max_dist_from(EuclidianPlane.origin))


test()
