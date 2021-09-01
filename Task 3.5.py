# Part 3.5 (User sum_num & stop)

def sum_func(user_num, stop):
    nums = user_num.split (' ')
    sum_list = 0
    for i in nums:
        if i == stop:
            break
        sum_list += int(i)

    return sum_list

stop = '#'
finish = False
s = 0
while not finish:
    user_num = input("Enter numbers with space: ")
    s += sum_nums(user_num, stop)
    finish = stop in user_num
    print(f'Summary of announced numbers: {s}')

