save = {1:1}
def factorial(n):
    if not n in save:
        save[n] = factorial(n-1) * n
    return save[n]

print(factorial(10))