# Part 2.4 (Numeration of str with words)

list = input('Announce any words (punctuate with space):')
list = list.split()

for num, word in enumerate(list,1):
    print(f'{num}-{word[:10]}')

