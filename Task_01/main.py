n = int(input('введите количество монеток\n'))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input(f'введи 0 или 1 для {i+1}-й монеты\n'))
    if x == 0:
        count_zero += 1
    if x == 1:
        count_one += 1
    else: print('нужно вводить 1 или 0!')
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)