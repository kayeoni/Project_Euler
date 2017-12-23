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

def nth_prime(n):
    list = []
    i = 2
    while True:
        if check_prime(i) == 1:
            list.append(i)
        if len(list) == n:
            break
        i += 1
    if len(list) == 0:
        return "None!!"
    return list[-1]

print(nth_prime(10001))