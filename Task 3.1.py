# Part 3.1 (Division function)

div_func = lambda num1, num2: num1 / num2

a = int(input('Делимое: '))
b = int(input('Делитель: '))
while b == 0:
    print("Деление на ноль! Решение невозможно.")
    break
else:
    print(div_func(a, b))

