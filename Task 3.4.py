# Part 3.4 ()

def get_pow(x, y):
    if x < 0:
        return 'X must nbe greater than 0'
    if y > 0:
        return 'Y must be less than 0'
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z

x = float(input('X positive num: '))
y = int(input('Y negative int: '))
print(get_pow(x, y))

