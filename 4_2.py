# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
txt = list((str((input("input your text here: ")).replace(' ', ''))).lower()) # ввод текста пользователем
numbers = [txt.count(txt[i]) for i in range(len(txt))]
print(numbers)
data = {txt[i]: numbers[i] for i in range(len(txt))}
print(data)
