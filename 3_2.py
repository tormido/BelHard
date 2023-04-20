while True:
    try:
        a = int(input("Please, input first number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
while True:
    try:
        b = int(input("Please, input second number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
while True:
    try:
        c = int(input("Please, input third number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
print(round((a + b + c)/3, 3))
