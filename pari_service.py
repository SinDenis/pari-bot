from model.Pari import PariState, Pari

pari_map = {}  # user_id -> List<pari_name> ----> user_name -> List<Pari>


def add_pari(challenger: str, pari_name: str, description: str, pari_taker: str):
    pari = Pari(pari_name=pari_name,
                description=description,
                challenger_login=challenger,
                state=PariState.NEW,
                taker_login=pari_taker)
    if challenger not in pari_map.keys():
        pari_map[challenger] = [pari]
    else:
        pari_map[challenger].append(pari)
    return pari


def get_pari(username):
    if username not in pari_map.keys():
        return []
    return pari_map[username]
