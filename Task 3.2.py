# Part 3.2 (User Data function)

def user_data_fun (name=None, surname=None, year=None, city=None, email=None, mobile=None):
    data = name, surname, year, city, email, mobile
    return print("User Data: ", data)

name = input("Имя: ")
surname = input("Фамилия: ")
year = input("Год рождения: ")
city = input("Город проживания: ")
email = input("Email: ")
mobile = input("Телефон: ")

user_data_fun(name= name, surname= surname, year= year, city= city, email= email, mobile= mobile)

