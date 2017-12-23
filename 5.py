def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a * b / gcd(a,b)

def smallest_multi(n):
    result = 1
    for i in range(1,n):
        result = lcm(result, i)
    return result

print(smallest_multi(20))