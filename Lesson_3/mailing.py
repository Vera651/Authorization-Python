class Mailing:
    to_address = "somewhere"
    from_address = "from somewhere"
    cost = 1000
    track = "track number"

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return f"Отправление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей."
        