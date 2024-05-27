from src.model.pari import Pari

pari_by_user_id: dict[int, list[Pari]] = {}


def get_pari_by_user_id(user_id):
    if user_id in pari_by_user_id:
        return pari_by_user_id[user_id]
    else:
        return []


def get_pari_by_user_id_and_name(user_id, target_pari_name):
    user_paris = get_pari_by_user_id(user_id)
    for pari in user_paris:
        if pari.name == target_pari_name:
            return pari
    return None


def update_pari_by_user_id(user_id, pari):
    existing_pari = get_pari_by_user_id_and_name(user_id, pari.name)
    existing_pari.challenger_id = pari.challenger_id
    existing_pari.taker_id = pari.taker_id
    existing_pari.check_frequency_days = pari.check_frequency_days
    existing_pari.total_checks_to_pass = pari.total_checks_to_pass
    return existing_pari


def add_pari_by_user_id(user_id, pari_name):
    pari = Pari(name=pari_name)
    if user_id in pari_by_user_id:
        pari_by_user_id[user_id].append(pari)
    else:
        pari_by_user_id[user_id] = [pari]
