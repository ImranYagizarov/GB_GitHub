#Part 4.5 (mult of num in range)

from functools import reduce

num_list = [i for i in range(99, 1001) if (i % 2 == 0)]
def mult_nums(a, b):
    return a * b

print(reduce(mult_nums, num_list))

