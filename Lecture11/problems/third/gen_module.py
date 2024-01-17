def even_num():
    for i in range(10):
        if i % 2 == 0:
            yield i


if __name__ == "__main__":
    for x in even_num():
        print(x, end=" ")

    gen = even_num()
    while True:
        try:
            print(next(gen), end=" ")
        except StopIteration:
            break
