import math

def divisor_sum(n):
    summ = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            summ += i
            summ += int(n/i)
    return summ

def find_amicable_number_under(n):
    list = []
    for i in range(1, n):
        if i == divisor_sum(divisor_sum(i)) and divisor_sum(i) != i:
            if not i in list:
                list.append(i)
                list.append(divisor_sum(i))
    return list

print(sum(find_amicable_number_under(10000)))