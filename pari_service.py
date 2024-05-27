def add_pari(user_id, pari):
    message ="Добавлено пари \"" + pari + "\" для пользователя " + str(user_id)
    return message

def set_pari_name():
    message = "Введите описание пари"
    return message

def set_pari_taker():
    message = "С кем вы хотите заключить пари?"
    return message

def get_paris(paris):
    str_list = [str(pari) for pari in paris]
    return ''.join(str_list)