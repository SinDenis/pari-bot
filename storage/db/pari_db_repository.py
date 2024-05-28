from psycopg2.extras import RealDictCursor
from storage.db.db_config.db_connection import connection
from storage.common.pari import Pari

cursor = connection.cursor(cursor_factory=RealDictCursor)


def add_pari(pari_name, challenger_name):
    cursor.execute("INSERT INTO pari(pari_name, challenger_name) VALUES (%s, %s)",
                   (pari_name, challenger_name))
    connection.commit()


def set_pari_taker(challenger_name, taker_name):
    cursor.execute(
        """
    UPDATE pari
       SET taker_name = %s
     WHERE challenger_name = %s
       AND taker_name IS NULL
     RETURNING *  
    """,
        (taker_name, challenger_name)
    )
    connection.commit()
    row = cursor.fetchone()
    return map_to_pari(row)


def get_pari_by_challenger(challenger_name):
    cursor.execute("SELECT * FROM pari WHERE challenger_name = %s", (challenger_name,))
    pari_rows = cursor.fetchall()
    return map(lambda row: map_to_pari(row), pari_rows)


def get_pari_by_taker(taker_name):
    cursor.execute("SELECT * FROM pari WHERE taker_name = %s", (taker_name,))
    pari_rows = cursor.fetchall()
    return map(lambda row: map_to_pari(row), pari_rows)


def map_to_pari(pari_dict):
    return Pari(id=pari_dict["id"], name=pari_dict["pari_name"],
                challenger_name=pari_dict["challenger_name"], taker_name=pari_dict["taker_name"])
