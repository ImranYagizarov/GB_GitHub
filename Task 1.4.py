#Part 4 (Max digit in number)

n = int(input("Announce any number :"))
m = 0
while (n):
    if (n % 10 > m):
        m = n % 10
    n //= 10
print("Max digit in selected number is :", m)

