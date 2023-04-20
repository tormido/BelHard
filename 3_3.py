name = input("Please, input your name: ")
while True:
    try:
        age = int(input("Please, input your age: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
age = str(age)
city = input("Please, input your city: ")
# opt1
print('Hello ' + name + ' ' + age + ' y.o. from ' + city)
# opt 2
print('Hi, are you %s %s y.o. from %s ?' % (name, age, city))
# opt 3
print('Hello {fname} {uage} y.o. from {ucity}'.format(fname=name, uage=age, ucity=city))
