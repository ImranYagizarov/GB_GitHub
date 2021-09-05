# Part 5.5 (sum count in created file)

record_string = '5 4 3 4 5 6 7'

with open('sum_count.txt', 'w') as file:
     file.write(record_string)

with open('sum_count.txt') as file:
     spl_num = file.read().split()
     sum = 0
     for num in spl_num:
         sum += int(num)

print(sum)
file.close()
