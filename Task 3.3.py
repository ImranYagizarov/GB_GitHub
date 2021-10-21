#Part 3.3 (max num sum)

def my_func(num1, num2, num3):
    num = [num1, num2, num3]
    num.sort()
    result = num[1] + num[2]
    return print(result)

a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))
my_func(a, b, c)

