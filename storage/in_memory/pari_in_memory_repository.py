from storage.common.pari import Pari

paris = []


def add_pari(pari_name, challenger_name):
    paris.append(Pari(name=pari_name, challenger_name=challenger_name))


def set_pari_taker(challenger_name, taker_name):
    for pari in paris:
        if pari.challenger_name == challenger_name and not hasattr(pari, taker_name):
            pari.set_taker_name(taker_name)
            return pari


def get_pari_by_challenger(challenger_name):
    challenger_paris = []
    for pari in paris:
        if pari.challenger_name == challenger_name:
            challenger_paris.append(pari)
    return challenger_paris


def get_pari_by_taker(taker_name):
    challenger_paris = []
    for pari in paris:
        if pari.taker_name == taker_name:
            challenger_paris.append(pari)
    return challenger_paris
