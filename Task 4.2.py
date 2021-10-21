# Part 4.2 (Bigger num generator)

my_list = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 300]
print(my_list)
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)

