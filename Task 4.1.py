# Part 4.1 (Salary counter)

from sys import argv


def salary_count(hrs, money_per_hr, extra): #a = hrs, b = $ per hour, c = extra payments
    total = hrs * money_per_hr + extra
    return total

a = float(input('Hours of work: '))
b = float(input('Hour cost: '))
c = float(input('Extra $$$: '))

x = salary_count(a, b, c)
print(x)

