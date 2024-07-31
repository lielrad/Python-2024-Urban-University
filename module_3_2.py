def send_email(message, recipient, *, sender = 'university.help@gmail.com'):

    is_at = False
    is_domain = False
    correct_recipient = True
    if '@' in recipient:
        is_at = True
    if '.com' in recipient:
        is_domain = True
    elif '.ru' in recipient:
        is_domain = True
    elif '.net' in recipient:
        is_domain = True
    if is_at == False and is_domain == False:
        correct_recipient = False

    is_at = False
    is_domain = False
    correct_sender = True
    if '@' in sender:
        is_at = True
    if '.com' in sender:
        is_domain = True
    elif '.ru' in sender:
        is_domain = True
    elif '.net' in sender:
        is_domain = True
    if is_at == False or is_domain == False:
        correct_sender = False

    if correct_recipient == False or correct_sender == False:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

    if sender == recipient:
        return print('Нельзя отправить письмо самому себе!')

    if sender == 'university.help@gmail.com':
        return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')