# Part 5.1 (Creating txt file with str)

user_line_1 = input('Enter line 1: ')
user_line_2 = input('Enter line 2: ')
user_line_3 = input('Enter line 3: ')
user_string = [user_line_1,'\n', user_line_2,'\n', user_line_3, '\n',]

with open('user_text.txt', 'w') as file:
     file.writelines(user_string)

