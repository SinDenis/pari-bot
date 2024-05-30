tg_users_map = {}


def register_user(username: str, tg_user_id: int):
    if (username not in tg_users_map.keys()):
        tg_users_map[username] = tg_user_id
