class Pari:
    id: int
    name: str
    challenger_name: str
    taker_name: str

    #  settings
    check_frequency_days: int  # check if taker passed a pari every N days
    total_checks_to_pass: int  # check N times to taker pass the pari

    def __init__(self, name: str, challenger_name: str, id: int = None, taker_name: str = None):
        self.id = id
        self.name = name
        self.challenger_name = challenger_name
        self.taker_name = taker_name

    def get_challenger_id(self):
        return self.challenger_name

    def get_taker_id(self):
        return self.taker_name

    def set_taker_name(self, taker_name):
        self.taker_name = taker_name

    def __str__(self) -> str:
        return f"""
        - Название пари: {self.name}
        - Кто заключил пари: {self.challenger_name}
        - Выполняющий: {self.taker_name}
        """
