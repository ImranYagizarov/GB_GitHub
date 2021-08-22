# Part 2.1 (type of elements in list)

list = ["hello", {'one': 1}, [5, 6, 7], "teacher", 6.7, "say", "Hi back"]
for num, elem in enumerate(list, 1):
        print(f'element №{num}-{type(elem)}')

