import re

dir_ = (dir(re))
list_ = []

for i in dir_:
    if "find" in i:
        list_.append(i)
        print(i)

print(dir_)
print(list_)

# list_ = [i for i in dir_ if "find" in i]
