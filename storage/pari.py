class Pari:
    name: str  # unique name
    challenger_id: str  # telegram user_id of the one, who challenged a pari
    taker_id: str  # telegram user_id of the one, who took and started to execute a pari

    #  settings
    check_frequency_days: int  # check if taker passed a pari every N days
    total_checks_to_pass: int  # check N times to taker pass the pari

    def __init__(self, name: str, challenger_name: str) -> None:
        self.challenger_id = challenger_name
        self.name = name
        self.check_frequency_days = 0
        self.total_checks_to_pass = 0

    def get_challenger_id(self):
        return self.challenger_id

    def get_taker_id(self):
        return self.taker_id

    def set_taker_id(self, taker_id):
        self.taker_id = taker_id

    def __str__(self) -> str:
        return f"""
        - Название пари: {self.name}
        - Кто заключил пари: {self.challenger_id}
        - Выполняющий: {self.taker_id}
        """