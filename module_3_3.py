def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()              # 1 строка True
print_params(5)             # 5 строка True
print_params(2, c='Hi')  # 2 строка Hi
print_params([1, 2, 3])     # [1, 2, 3] строка True
print_params(b = 25)        # 1 25 True
print_params(c = [1,2,3])   # 1 строка [1, 2, 3]


values_list = [5, True, 'Hello']
values_dict = {'a': 8.2, 'b': 'Yes', 'c': 3}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'No']
print_params(values_list_2)          # [2, 'No'] строка True
print_params(*values_list_2, 42)  # 2 No 42