import grpc
from .generated import owner_pb2, owner_pb2_grpc


class GrpcOwnerClient:
    def __init__(self):
        self._channel = grpc.insecure_channel('localhost:50051')
        self._stub = owner_pb2_grpc.OwnerStub(self._channel)
    
    def notify_owner(self, dog_name):
        req = owner_pb2.NotifyRequest(animalName=dog_name, animalType="Dog")
        res = self._stub.Notify(req)
        return res

    def close(self):
        self._channel.close()
