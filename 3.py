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

def largest_prime_factor(n):
    list = []
    rootn = int(math.sqrt(n))
    for i in range(2, rootn):
        if n % i == 0 and check_prime(i) == 1:
            list.append(i)
    
    return max(list)

print(largest_prime_factor(600851475143))