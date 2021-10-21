# Part 6.5 (Stationery)

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
         super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def __init__(self, title):
         super().__init__(title)

    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def __init__(self, title):
         super().__init__(title)

    def draw(self):
        print('Запуск отрисовки фломастером')


p = Pen(Stationery)
pn = Pencil(Stationery)
hl = Handle(Stationery)
p.draw()
pn.draw()
hl.draw()
