# Part 1.5 (Working with company's incomes)

income = input("Введите данные выручки: ") #income = выручка
expenses = input("Введите данные издержек: ") #expenses = издержки

if int(income) < int(expenses) :
    print("Похоже, что у фирмы непростые времена...")
else :
    print("Так держать, работаем в прибыль.")
    earning = int(income) - int(expenses) #earning = прибыль
    rent = int(earning) // int(expenses) #rent = рентабельность
    print("Рентабельность фирмы составляет : ", rent)
    employee_num = input("Введите количество работников: ")  # employee_num = количество работников
    print("Прибыль на одного сотрудника : ", int(earning) // int(employee_num))

