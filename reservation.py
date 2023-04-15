class Reservation:
    def __init__(self, type, quantity, price, start_date, end_date):
        self.type = type
        self.quantity = quantity
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.room = None

    def overlaps(self, other_start_date, other_end_date):
        return not self.start_date > other_end_date and not self.end_date < other_start_date

    def set_room(self, room):
        self.room = room

    def get_room(self):
        return self.room
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

