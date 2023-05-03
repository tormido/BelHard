# Заполнить список степенями числа 2 (от 2^1 до 2^n).
n = 1
result_list = []
max_n = int(input('Введите максимальную желаемую степень двойки '))
while n <= max_n:
    result_list.append(2**n)
    n = n + 1
print('Степени двойки от 1 до ' + str(max_n) + ' :')
print(result_list)
