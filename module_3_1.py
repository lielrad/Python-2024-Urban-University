calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(list_):
    count_calls()
    list_len = len(list_)
    list_upper = list_.upper()
    list_lower = list_.lower()
    return list_len, list_upper, list_lower

def is_contains(name, string_):
    count_calls()
    contains = False
    for i in range(0, len(string_)):
        if string_[i].casefold() == name.casefold():
            contains = True
            break
    return contains

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)