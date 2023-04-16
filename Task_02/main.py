x = int(input("Введите X: "))
y = int(input("Введите Y: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)