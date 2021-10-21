# Part 6.4 (Car)

class Car:

# АТРИБУТЫ КЛАССА
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

# МЕТОДЫ ДВИЖЕНИЯ
    def go(self):
        print('Car is moving')

    def stop(self):
        print('Car has stopped')

    def turn(self, direction):
        if direction == 'r':
            print('Car is turning right')
        if direction == 'l':
            print('Car is turning left')

    def show_speed(self):
        print('Car is driving', self.speed, 'km/h.')



class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Overspeeding of {self.name}')

class SportCar(Car):
    None

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if show_speed > 40:
            print(f'Speed of {self.name} is higher than allow for town car')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
        print('Car is from police department')



town = TownCar(63, "white", "Kia")
town.turn('r')
town.show_speed()
sport = SportCar(200, 'Black', 'Batmobile')
sport.show_speed()
work = WorkCar(38, 'gray', 'Shuttle')
police = PoliceCar(80, 'blue', 'Cops')
