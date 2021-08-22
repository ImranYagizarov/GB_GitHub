# Part 2.2 (replacing elements in list by index)

list = list(input('Add numbers in list:').split())
n = 0
for i in range(int(len(list) / 2)):
    list[n], list[n + 1] = list[n + 1], list[n]
    n += 2
print(list)

