from concurrent import futures
import grpc

from .generated import dog_pb2_grpc
from .dog_grpc import Dog


class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        dog_pb2_grpc.add_dogServicer_to_server(Dog(), server)
        server.add_insecure_port('[::]:50055')
        print("Dog Server is running")
        server.start()
        server.wait_for_termination()
