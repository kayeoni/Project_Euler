def power_digit_sum(x,n):
    a = pow(x,n)
    summ = 0
    while True:
        summ += a % 10
        a = int(a / 10)
        if a == 0:
            break
    return summ

print(power_digit_sum(2,1000))