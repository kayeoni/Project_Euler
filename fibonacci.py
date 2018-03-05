save = {0:0, 1:1}
def fibm(n):                # This is the faster method than the below
    if not n in save:
        save[n] = fibm(n-1) + fibm(n-2)
    return save[n]

def fibonacci(n):
    if n < 0:
        return "NO! Please enter the natural number"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibm(100))
