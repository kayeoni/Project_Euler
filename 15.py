def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def lattice_path(m,n):
    return factorial(m+n)/(factorial(m) * factorial(n))

print(lattice_path(20,20))