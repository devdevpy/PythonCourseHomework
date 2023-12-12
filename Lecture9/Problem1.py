from operator import itemgetter

list_ = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sorted(list_, key=itemgetter(1)))
