domen = [".com", ".ru", ".net"]     # Список в котором определяются разрешенные домены
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    recipient_ok = False
    sender_ok = False

    for i in range(0, len(domen)):  # Цикл для проверки соотвествия домена отправителя\получателя разрешенному
        if recipient.endswith(domen[i]) == recipient.endswith(recipient):  # Проверка соответствия домена получателя
            recipient_ok = True
        if sender.endswith(domen[i]) == sender.endswith(sender):    # Проверка соответствия домена отправителя
            sender_ok = True
        if recipient_ok and sender_ok:  #
            if sender != recipient:     # Проверка на отправку сообщения самому себе
                if sender == "university.help@gmail.com":   # Проверка на отправителя по умолчанию
                    print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
                    break
                else:
                    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
                    break
            else:
                print("Нельзя отправить письмо самому себе!")
                break

    if "@" not in recipient or "@" not in sender or recipient_ok == False or sender_ok == False:    #
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)

# Примеры выполнения кода
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')