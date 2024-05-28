from psycopg2.extras import RealDictCursor
from storage.db.db_config.db_connection import connection

cursor = connection.cursor(cursor_factory=RealDictCursor)


def save_user(name, chat_id):
    cursor.execute("INSERT INTO tg_user(chat_id, username) VALUES(%s, %s) ON CONFLICT DO NOTHING", (chat_id, name))
    connection.commit()


def get_user(name):
    cursor.execute("SELECT chat_id FROM tg_user WHERE username = %s", (name,))
    row = cursor.fetchone()
    return None if row is None else row["chat_id"]
