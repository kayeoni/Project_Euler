def check_palindrome(n):
    string = str(n)
    for i in range(len(string)//2):
        if string[i] != string[len(string) -1 -i]:
            return 0
    return 1

def largest_palindromic_num(n):
    list = []
    i = pow(10, n) - 1
    
    while i > pow(10, n)/2:
        j = pow(10, n) - 1
        while j > pow(10, n)/2:
            if check_palindrome(i * j) == 1:
                list.append(i*j)
            j -= 1
        i -= 1
    if len(list) == 0:
        return "None!!"
    return max(list)

print(largest_palindromic_num(3))