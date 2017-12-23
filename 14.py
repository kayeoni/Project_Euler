def collatz_seq(n):
    list = []
    while n != 1:
        list.append(n)
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    list.append(1)
    return list

def longest_length_of_collartz_seq_under(n):
    i = 1
    length = len(collatz_seq(i))
    check = 0
    while i < n:
        i += 1
        if length <= len(collatz_seq(i)):
            length = len(collatz_seq(i))
            check = i
    return check

print(longest_length_of_collartz_seq_under(1000000))