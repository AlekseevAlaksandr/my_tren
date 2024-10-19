values_list = [1, 'str', True]
values_dict = {'a': 2, 'b': 'int', 'c': False}
values_list_2 = [54.32, 'Строка' ]
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params() # Вызов без аргументов

print_params(a = 12, b = False) # Вызов без аргументов

print_params(b = 25) # Вызов без аргументов

print_params(c = [1,2,3])

print_params(*values_list)

print_params(**values_dict)

print_params(*values_list_2, 42)
