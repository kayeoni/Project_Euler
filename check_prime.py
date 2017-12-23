import math

def check_prime(n):
    i = 2
    if n == i:
        return 1
    while i < int(math.sqrt(n)) + 1:
        if n % i == 0:
            return 0
        i += 1
    return 1