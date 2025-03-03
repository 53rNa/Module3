# Задача "Рассылка писем"

def send_email (message, recipient, *, sender="university.help@gmail.com"):

    index1 = sender.find("@")
    index2 = recipient.find("@")
    mail_self = 0

    if (index1 >= 0 and index2 >= 0) and ((sender.endswith(".com")
        or sender.endswith(".ru") or sender.endswith(".net")) and (recipient.endswith(".com")
        or recipient.endswith(".ru") or recipient.endswith(".net"))):

        if sender == recipient:
            print(f"Нельзя отправить письмо самому себе!")
            mail_self = 1

        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")

        elif mail_self == 0:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
