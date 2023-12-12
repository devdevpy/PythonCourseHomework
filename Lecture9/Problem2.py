A = set([1, 2, 3])
B = set([2, 3, 4])

set_ = set()

set_.add(frozenset(A - B))
set_.add(frozenset(B))
set_.add(frozenset(B - A))
set_.add(frozenset(A - B).union(frozenset(B - A)))
set_.add(frozenset(A & B))
set_.add(frozenset(A | B))

print(set_)
