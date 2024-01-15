def prime_num():
    for i in range(3, 25):
        is_prime = True
        for num_ in range(2, i):
            if i % num_ == 0:
                is_prime = False
                break
        if is_prime:
            yield i


for x in prime_num():
    print(x, end=" ")