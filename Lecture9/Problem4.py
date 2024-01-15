a = {1, 2}
b = {2, 3}
c = {}

sum_1 = (a | b)  #: {1, 2, 3},
sum_2 = (a & b)  #: {2},
sum_3 = (a - b)  #: {1}

d = c[f"{a} | {b}"] = sum_1
e = c[f"{a} & {b}"] = sum_2
f = c[f"{a} - {b}"] = sum_3


print(c)
