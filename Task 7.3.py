# Part 7.3 (Cell evolution)

class Cell:

    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        res = self.num + other.num
        return res

    def __sub__(self, other):
        res = self.num - other.num
        if res > 0:
            return res
        else:
            print(f'Operation unavailable')

    def __mul__(self, other):
        res = self.num * other.num
        return res

    def __truediv__(self, other):
        res = self.num // other.num
        return res

    def make_order(self, cells):
        line = ''
        for i in range(int(self.num / cells)):
            line += "*" * cells + '\n'
        line += "*" * (self.num % cells) + '\n'
        return line

cell = Cell(19)
cell2 = Cell(8)
print(cell2.make_order(7))
print(cell.make_order(13))
print(cell)
print(cell + cell2)
print(cell2 - cell)
print(cell / cell2)
