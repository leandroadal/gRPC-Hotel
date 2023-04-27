import ReservationService_pb2
import ReservationService_pb2_grpc
from Room import Room
from reservation import Reservation
import datetime


class ReservationService(ReservationService_pb2_grpc.ReservationServiceServicer):

    def __init__(self):
        self.reservations = []
        self.availableRooms = [
            Room("solteiro", "standard", 100, 10),
            Room("casal", "standard", 120, 20),
            Room("familia", "standard", 150, 5),
            Room("solteiro", "executivo", 1000, 10),
            Room("casal", "executivo", 1200, 20),
            Room("familia", "executivo", 1500, 5),
            Room("solteiro", "luxo", 10000, 10),
            Room("casal", "luxo", 12000, 20),
            Room("familia", "luxo", 15000, 5)]

    def calculatePrice(self, room, numberOfDays, type, quantity):
        price = 0
        if room.get_type() == type:
            price = room.get_price() * quantity * numberOfDays
        return price

    def findRoomByType(self, type, category):
        for room in self.availableRooms:
            if room.get_type() == type and room.get_category() == category and room.get_availability() > 0:
                return room
        return None

    def checkAvailability(self, type, category, quantity, startDate, endDate):
        room = self.findRoomByType(type, category)
        if room is not None and room.get_availability() >= quantity:
            for reservation in self.reservations:
                if reservation.get_room() == room and reservation.overlaps(startDate, endDate):
                    return False
            return True
        return False

    def MakeReservation(self, request, context):
        # Pegando os dados da requisição
        type = request.type
        category = request.category
        quantity = request.quantity
        start_date = request.start_date
        end_date = request.end_date

        if self.checkAvailability(type, category, quantity, start_date, end_date):
            room = self.findRoomByType(type, category)
            # Subtraindo as datas
            temp_end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            temp_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            number_of_days = (temp_end_date - temp_start_date).days
            price = self.calculatePrice(room, number_of_days, type, quantity)
            room.set_availability(room.get_availability() - quantity)
            reservation = Reservation(type, quantity, price, start_date, end_date)
            reservation.set_room(room)
            self.reservations.append(reservation)
            # Retornando a resposta para o cliente
            return ReservationService_pb2.ReservationResponse(availability=True,
                                                              daily_rate=room.get_price(),
                                                              total_amount=price)
        else:
            return ReservationService_pb2.ReservationResponse(availability=False,
                                                              daily_rate=0,
                                                              total_amount=0)
