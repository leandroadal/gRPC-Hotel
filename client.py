import grpc
import ReservationService_pb2
import ReservationService_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ReservationService_pb2_grpc.ReservationServiceStub(channel)
        request = ReservationService_pb2.ReservationRequest(
            type='solteiro',
            category='luxo',
            quantity=2,
            start_date='2023-04-11',
            end_date='2023-12-10'
        )
        response = stub.MakeReservation(request)
        print('Availability:', response.availability)
        print('Dailyrate:', response.daily_rate)
        print('Total:', response.total_amount)

        request2 = ReservationService_pb2.ReservationRequest(
            type='casal',
            category='executivo',
            quantity=1,
            start_date='2023-05-05',
            end_date='2023-05-10'
        )
        response2 = stub.MakeReservation(request2)

        print('Availability:', response2.availability)
        print('Dailyrate:', response2.daily_rate)
        print('Total:', response2.total_amount)

        request3 = ReservationService_pb2.ReservationRequest(
            type='solteiro',
            category='luxo',
            quantity=2,
            start_date='2023-04-11',
            end_date='2023-12-10'
        )
        response3 = stub.MakeReservation(request3)
        print('Availability:', response3.availability)
        print('Dailyrate:', response3.daily_rate)
        print('Total:', response3.total_amount)

        request3 = ReservationService_pb2.ReservationRequest(
            type='solteiro',
            category='standard',
            quantity=1,
            start_date='2023-04-11',
            end_date='2023-12-10'
        )
        response3 = stub.MakeReservation(request3)
        print('Availability:', response3.availability)
        print('Dailyrate:', response3.daily_rate)
        print('Total:', response3.total_amount)

        request3 = ReservationService_pb2.ReservationRequest(
            type='solteiro',
            category='standard',
            quantity=1,
            start_date='2024-04-11',
            end_date='2024-12-10'
        )
        response3 = stub.MakeReservation(request3)
        print('Availability:', response3.availability)
        print('Dailyrate:', response3.daily_rate)
        print('Total:', response3.total_amount)

        request3 = ReservationService_pb2.ReservationRequest(
            type='solteiro',
            category='executivo',
            quantity=2,
            start_date='2025-04-11',
            end_date='2025-12-10'
        )
        response3 = stub.MakeReservation(request3)
        print('Availability:', response3.availability)
        print('Dailyrate:', response3.daily_rate)
        print('Total:', response3.total_amount)


if __name__ == '__main__':
    run()
