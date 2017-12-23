cdays = {1:3, 2:0, 3:3, 4:2, 5:3, 6:2, 7:3, 8:3, 9:2, 10:3, 11:2, 12:3}
# For common years, The keys of "days" are the number of each months,
# and the values are remains which divided by 7

ldays = {1:3, 2:1, 3:3, 4:2, 5:3, 6:2, 7:3, 8:3, 9:2, 10:3, 11:2, 12:3}
# For leap years, The keys of "days" are the number of each months,
# and the values are remains which divided by 7

def check_leap_year(n):         # common years = 0, leap years = 1
    if n % 4 != 0:
        return 0
    elif n % 100 != 0:
        return 1
    elif n % 400 != 0:
        return 0
    else:
        return 1

def adding_first_of_month(start, year):
    list = []
    list.append(start)
    if check_leap_year(year) == 0:
        for i in range(1, 12):
            list.append( (list[i-1] + cdays[i]) % 7 )
    else:
        for i in range(1, 12):
            list.append( (list[i-1] + ldays[i]) % 7 )
    return list

def counting_first_of_next_year(start, year):
    if check_leap_year(year) == 0:
        return (start + 1) % 7
    else:
        return (start + 2) % 7

def counting_sundays(start, start_year, last_year):
    main_list = []
    start_point = start
    for i in range(start_year, last_year + 1):
        main_list += adding_first_of_month(start_point, i)
        start_point = counting_first_of_next_year(start_point, i)
    return main_list.count(0)

print(counting_sundays(2, 1901, 2000))