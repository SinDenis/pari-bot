class PariState:
    NEW = 'Новое'
    IN_PROGRESS = 'В процессе'
    FINISHED = 'Завершено'
    DENIED = 'Отклонено'


class Pari:
    pari_name: str
    description: str

    challenger_login: str
    taker_login: str = None

    state: PariState
    winner: str = None

    def __init__(self,
                 pari_name: str,
                 description: str,
                 challenger_login: str,
                 taker_login: str,
                 state: PariState):
        self.pari_name = pari_name
        self.description = description
        self.challenger_login = challenger_login
        self.taker_login = taker_login
        self.state = state

    def __str__(self) -> str:
        return f"""
        Имя пари: {self.pari_name}
        Описание: {self.description}
        Кто вызвал: {self.challenger_login}
        Кого вызвали: {self.taker_login}
        Состояние пари: {str(self.state)}
        """
