def lcm_3and5(n):
    sum = 0
    
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    
    return sum

print(lcm_3and5(1000))