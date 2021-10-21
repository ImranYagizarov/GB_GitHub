# Part 1.6 (Chasing kilometers)

a = float(input("Старт от ... км:"))
b = float(input("Необходимое расстояние ... км:"))
d = 1 #день

while a < b:
    a *= 1.1
    d += 1
print(f'Необходимое количество дней - {d}')

