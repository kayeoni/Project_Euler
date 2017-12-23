from time import time

def get_number_of_divisors(n):
    powers = {}
    f = 2
    while n > 1:
        if n % f == 0:
            powers[f] = powers.get(f, 0) + 1
            n /= f
        else:
            f += 1

    if powers:
        return reduce(lambda a,b: a*b, [p+1 for p in powers.values()])
    return 1

start = time()

i, n = 0, 0
while True:
    i += 1
    n += i
    divisors = get_number_of_divisors(n)
    if divisors > 500:
        print(n, divisors)
        break

print(time() - start)

# sec = 3.655