# Вывести первые N чисел кратные M и больше K
# Запросим у пользователя значения N, M и K
N = int(input("Введите значение N: "))
M = int(input("Введите значение M: "))
K = int(input("Введите значение K: "))


count = 0  # счетчик текущего количества подходящих чисел
current_number = K  # текущее число

# Пока не достигнуто необходимое количество чисел - выводится текущее число, если оно кратно M
while count < N:
    if current_number % M == 0:
        print(current_number)
        count += 1
    current_number += 1