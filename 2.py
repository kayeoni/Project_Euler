def fib_even_sum(n):
    list = [1,2]
    sum = 0
    
    while list[-1] < n:
        list.append(list[-2] + list[-1])
    
    for i in range(len(list)):
        if list[i] < n and i % 3 == 1:
            sum += list[i]
    
    return sum

print(fib_even_sum(4000000))