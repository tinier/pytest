from random import randint

def randint_list(n, no_ext = 300):
    return [randint(0, no_ext) for i in range(n)]