class Room:
    def __init__(self, type, category, price, availability):
        self.type = type
        self.category = category
        self.price = price
        self.availability = availability
        self.id = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_reservations(self):
        return self.reservations

    def set_reservations(self, reservations):
        self.reservations = reservations

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability
