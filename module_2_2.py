number1 = int(input('Введите число: '))
number2 = int(input('и еще одно: '))
number3 = int(input('и последнее: '))
if number1 == number2 and number1 == number3 :
    print(3)
elif number1 == number2 or number1 == number3 or number2 == number3 :
    print(2)
else:
    print(0)