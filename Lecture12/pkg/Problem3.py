def recursive_fibonacci(n: int):
    if n <= 2:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


print(recursive_fibonacci(8))
