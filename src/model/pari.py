class Pari:
    name: str  # unique name
    challenger_id: int  # telegram user_id of the one, who challenged a pari
    taker_id: int  # telegram user_id of the one, who took and started to execute a pari

    #  settings
    check_frequency_days: int  # check if taker passed a pari every N days
    total_checks_to_pass: int  # check N times to taker pass the pari

    def __init__(self, name: str) -> None:
        self.name = name
        self.check_frequency_days = 0
        self.total_checks_to_pass = 0

    def __str__(self) -> str:
        return f"""
        - Название пари: {self.name}
        - Регулярность проверки выполнения: {self.check_frequency_days} дней
        - Необходимое количество выполнения проверок для завершения: {self.total_checks_to_pass}
        """
