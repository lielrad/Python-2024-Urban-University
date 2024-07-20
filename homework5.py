immutable_var = 1,2,True,4,'tuple',5,[6,8]
print(immutable_var)
# immutable_var[0] = 6  заменить\изменить элементы нельзя
# Почему в неизменяемом списке (tuple) нельзя изменить элементы? - Очевидно потому что он неизменяемый. Или нужен какой-то более умный ответ?
immutable_var[6][1] = 7  # если в tuple есть list, то внутри листа элементы изменить можно

mutable_var = [1,2,True,4,'tuple',5]
mutable_var[2] = False
print(mutable_var)
