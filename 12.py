def nth_tri_num(n):
    if n % 2 == 0:
        return [n/2, n+1, n*(n+1)/2]
    return [n, (n+1)/2, n*(n+1)/2]

def count_divisor(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

def count_divisor_for_list(x):
    return count_divisor(x[0]) * count_divisor(x[1]) - 1

def tri_num_over_nth_div(n):
    i = 1
    while True:
        a = count_divisor_for_list(nth_tri_num(i))
        if a >= n:
            break
        i += 1
    return [nth_tri_num(i)[-1], i, count_divisor_for_list(nth_tri_num(i))]

from time import time

start = time()

print(tri_num_over_nth_div(500))
print(time() - start)


# when n=5, [28, 7, 5]
# when n=10, [120, 15, 15]
# when n=15, [120, 15, 15]
# when n=20, [630, 35, 23]
# when n=50, [25200, 224, 89]
# when n=100, [73920, 384, 111]
# when n=150, [749700, 1224, 161]
# when n=200, [2031120, 2015, 239]
# when n=300, [2162160, 2079, 319]
# when n=400, [17907120, 5984, 479]
# when n=500, [76576500, 12375, 575], sec = 11.598