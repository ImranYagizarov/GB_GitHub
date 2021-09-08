# Part 6.3 (Worker)

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(f'Total income:', sum(self._income.values()))


a = Position('Vasya', 'Pupkin', 'Driver', 40000, 25000)
a.get_full_name()
a.get_total_income()

