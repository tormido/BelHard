# **Вывести четные числа от 2 до N по 5 в строчку

n = int(input("Введите число N: "))
count = 0
for i in range(2, n+1, 2):
    if count < 4:
        print(i, end=" ")
        count += 1
    else:
        print(i)
        count = 0
