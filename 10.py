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

def sum_of_primes(n):
    list = []
    if n < 2:
        return 0
    if n == 2:
        return 2
    if n > 2:
        list.append(2)
    i = 3
    while i <= n:
        if check_prime(i) == 1:
            list.append(i)
        i += 2
    return sum(list)

print(sum_of_primes(2000000))