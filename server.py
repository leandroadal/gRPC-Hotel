from concurrent import futures
import grpc
import ReservationService_pb2_grpc
from reservation_service import ReservationService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    ReservationService_pb2_grpc.add_ReservationServiceServicer_to_server(ReservationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()