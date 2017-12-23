alphabets = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def value_of_name(name):
    summ = 0
    for i in range(len(name)):
        summ += alphabets[name[i]]
    return summ

def make_list_in_file(file_name):
    f = open(file_name, 'r')
    data = f.read().split('","')
    f.close()
    for i in range(len(data)):
        if '"' in data[i]:
            temp = ''
            for j in range(len(data[i])):
                if data[i][j] != '"':
                    temp += data[i][j]
            data[i] = temp
    return data

def names_scores(file_name):
    data = sorted(make_list_in_file(file_name))
    score = []
    for i in range(len(data)):
        score.append( (i+1) * value_of_name(data[i]) )
    return score

print(sum(names_scores("p022_names.txt")))