import math

from operator import itemgetter
from pprint import pprint as pp


def distance(goid_a, goid_n):
    x = goid_a[0] - goid_n[0]
    y = goid_a[1] - goid_n[1]
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

goids = [
    (1,21),
(1,2),
(1,15),
(10,1),
(12,21),
(1,31),
(1,11),
]

the_goid = (5,5)

print "before sort"
pp(goids)

new_goids = []
for goid in goids:
    new_goids.append((distance(the_goid, goid), goid))

print "new goids"
pp(new_goids)

print "sorting new goids"
new_goids.sort(key=itemgetter(0))
pp(new_goids)

sorted_goids = [goid[1] for goid in new_goids]

print "sorted goids"
pp(sorted_goids)


# TODO: Write algo to sort list items by nearest distance from selected point
