list_ = [{5: 4}, {3: 2}, {1: 1}, {2: 6}]

print(sorted(list_, key=lambda x: sorted(list_[1])))

