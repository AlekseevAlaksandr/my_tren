calls = 0

def count_calls():  # Добавляем 1 в переменную Calls при каждом вызове функции
    global calls
    calls = calls + 1

def string_info(string):    # Считаем количество символов и переводим в верхний, нижний регистр слова
    count_calls()
    t = len(string), string.upper(), string.lower()
    return t

def is_contains(string, list_to_search):    # Проверяем налиции слова в списке
    count_calls()
    for i in range (len(list_to_search)):
       if string.upper() == list_to_search[i].upper():  #   Приводим слово в одинаковый регистр со словом из списка
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
