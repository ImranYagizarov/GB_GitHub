#Part 4.6 (2 scripts)

from itertools import cycle, count

test_gen = count(3)
for i in test_gen:
    if i > 10:
        break
    print(i)


num_list = range(5)
test_gen_2 = cycle(num_list)
j = 0
for i in test_gen_2:
    if j > 12:
        break
    j += 1
    print(i)

