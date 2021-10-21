# Part 5.2 (str & words count in doc)

with open('text4task2.txt') as file:
    content = file.readlines()
    for num, line in enumerate(content):
        count = len(line.split())
        print(f'В {num + 1} строке {count} слова.')

file.close()

