# opt 1
print("Please, input your name", end=': ')
name = input()
print("Please, input your age", end=': ')
age = input(str())
print("Please, input your city", end=': ')
city = input()
print('Hello ' + name + ' ' + age + ' y.o. from ' + city)
# opt 2
print('Hi, are you %s %s y.o. from %s ?' % (name, age, city))
# opt 3
print('Hello {fname} {} y.o. from {}'.format(fname = name, uage = age, ucity = city))

