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


if __name__ == '__main__':
    run()
