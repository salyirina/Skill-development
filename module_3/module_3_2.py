#Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение),
# recipient(получатель) и 1 обязательно именованный аргумент со значением по
# умолчанию sender = "university.help@gmail.com".
def send_email(message, recipient, sender):

# 2. Если строки recipient и sender не содержат "@" или не оканчиваются на ".com"/".ru"/".net",
# то вывести на экран строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>."
    if "@" not in recipient or not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

# 3. Если sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

# 4. Если отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
# "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

# 5. В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено
# с адреса <sender> на адрес <recipient>."
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Примеры вызова
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', 'university.help@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')
