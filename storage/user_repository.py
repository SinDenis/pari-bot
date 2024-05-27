
user_map = {}

def save_user(name, chatId):
    user_map[name] = chatId

def get_user(name):
    return user_map.get(name)