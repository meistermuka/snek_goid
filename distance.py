import math

from pprint import pprint as pp

goids = [
    (1,21),
(1,2),
(1,15),
(10,1),
(12,21),
(1,31),
(1,11),
]

goid = (5,5)

print "before sort"
pp(goids)

sorted(goids, )


def distance(goid_a, goid_n):
    x = goid_a[0] - goid_n[0]
    y = goid_a[1] - goid_n[1]
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# TODO: Write algo to sort list items by nearest distance from selected point
