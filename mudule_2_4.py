numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in range(0, len(numbers)):  # Перебираем числа из списка

    if numbers[i] < 2:  # Пропускаем единицы
        continue

    for s in range(1, numbers[i]):  # Перебираем делители

        if numbers[i] % s != 0:  # Проверяем делится ли число
            if numbers[i] - 1 == s:  # Проверяем все ли делители испробованы,
                is_prime = True  # если все, то ставим флаг и прерываем проверку
                break
            else:  # Иначе, продолжаем выполнение цикла
                continue
        else:
            if s > 1:  # Отсекаем если делитель был единицей
                is_prime = False
                break
            else:
                continue

    if is_prime:
        primes.append(numbers[i])

    else:
        not_primes.append(numbers[i])

print("primes", primes)
print("not_primes", not_primes)
