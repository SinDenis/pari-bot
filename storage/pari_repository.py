from storage.pari import Pari

paris = []


def add_pari(comment, challenger_id):
    paris.append(Pari(comment, challenger_id))


def set_pari_taker(challenger_id, taker_id):
    for pari in paris:
        if pari.challenger_id == challenger_id and not hasattr(pari, taker_id):
            pari.set_taker_id(taker_id)
            return pari


def get_pari_by_challenger(challenger_name):
    challenger_paris = []
    for pari in paris:
        if pari.challenger_id == challenger_name:
            challenger_paris.append(pari)
    return challenger_paris


def get_pari_by_taker(taker_name):
    challenger_paris = []
    for pari in paris:
        if pari.taker_id == taker_name:
            challenger_paris.append(pari)
    return challenger_paris
