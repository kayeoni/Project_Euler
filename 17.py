wordlist_under_10 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
wordlist_under_20 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
'eighteen', 'nineteen']
wordlist_multiple_10 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
wordlist_power_10 = ['hundred']
wordlist_connect = ['and']

def count_alphabet_in_num(n):
    if int(n/10) == 0:
        if n == 0:
            return 4
        return len(wordlist_under_10[n])
    if int(n/10) == 1:
        return len(wordlist_under_20[n % 10])
    if int(n/10) > 1 and int(n/10) < 10:
        return len(wordlist_multiple_10[int(n/10) - 2] + wordlist_under_10[n % 10])
    if int(n/10) >= 10 and int(n/10) < 100:
        if n % 100 == 0:
            return len(wordlist_under_10[n/100] + wordlist_power_10[0])
        count = 0
        count += len(wordlist_under_10[int(n/100)] + wordlist_power_10[0] + wordlist_connect[0])
        j = n % 100
        if int(j/10) == 0:
            count += len(wordlist_under_10[j])
            return count
        if int(j/10) == 1:
            count += len(wordlist_under_20[j % 10])
            return count
        if int(j/10) > 1 and int(j/10) < 10:
            count += len(wordlist_multiple_10[int(j/10) - 2] + wordlist_under_10[j % 10])
            return count
    if n == 1000:
        return 11

def count_alphabet_sum(n):
    count = 0
    for i in range(1,n+1):
        count += count_alphabet_in_num(i)
        if i % 10 == 1:
            print('(' + str(i) + ')')
        print(count_alphabet_in_num(i))
        if i % 5 == 0:
            print("="*10)
    return count

print(count_alphabet_sum(1000))