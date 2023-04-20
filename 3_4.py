pos = 0
neg = 0
zero = 0
while True:
    try:
        a = int(input("Please, input first number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
if a > 0:
    pos += 1
elif a == 0:
    zero += 1
else:
    neg += 1
while True:
    try:
        b = int(input("Please, input second number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
if b > 0:
    pos += 1
elif b == 0:
    zero += 1
else:
    neg += 1
while True:
    try:
        c = int(input("Please, input third number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
if c > 0:
    pos += 1
elif c == 0:
    zero += 1
else:
    neg += 1
print('negative value counter: ' + str(neg))
print('positive value counter: ' + str(pos))
print('zero value counter: ' + str(zero))
