def single_root_words(root_word, *other_words):
    same_words = [] # Саздаем пустой список
    r_w = root_word.lower() # Приводим первое слово в нижний регистр
    for i in  range (len(other_words)):
        o_w = other_words[i]    # Записываем каждое слово в временную переменную
        o_w = o_w.lower()   #   Приводим каждое слово в нижний регистр
        if r_w in o_w or o_w in r_w:    #   Проверка совпадений слов
            same_words.append(other_words[i])   #   Добавление совпавшего слова в список

    return same_words   #


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)