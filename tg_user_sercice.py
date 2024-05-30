tg_users_map = {}  # tg username to chat id


def register_user(username: str, tg_user_id: int):
    if (username not in tg_users_map.keys()):
        tg_users_map[username] = tg_user_id


def get_tg_user_chat_id(username: str) -> int:
    if username not in tg_users_map.keys():
        return None
    return tg_users_map[username]
