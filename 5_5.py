# Ввод данных пользователем
deposit = float(input("Введите сумму вклада: "))
end_deposit = deposit*2
interest_rate = float(input("Введите процентную ставку: "))
# Расчет времени удвоения вклада
years = 0
while deposit < end_deposit:
    deposit += deposit * (interest_rate / 100)
    years += 1
# Вывод результата
print("Сумма вклада удвоится через", years, "лет")
