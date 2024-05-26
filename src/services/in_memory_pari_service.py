pari_by_user_id = {}

def get_pari_by_user_id(user_id):
    if user_id in pari_by_user_id:
        return pari_by_user_id[user_id]
    else:
        return []

def add_pari_by_user_id(user_id, pari_name):
    if user_id in pari_by_user_id:
        pari_by_user_id[user_id].append(pari_name)
    else:
        pari_by_user_id[user_id] = [pari_name]