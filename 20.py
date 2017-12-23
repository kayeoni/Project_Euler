save = {1:1}

def factorial(n):
    if not n in save:
        save[n] = factorial(n-1) * n
    return save[n]

def factorial_digit_sum(n):
    digit = str(factorial(n))
    summ = 0
    for i in range(len(digit)):
        summ += int(digit[i])
    return summ

print(factorial_digit_sum(100))