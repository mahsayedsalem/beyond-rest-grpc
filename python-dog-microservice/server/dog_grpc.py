from .generated import dog_pb2, dog_pb2_grpc
from .owner_client import GrpcOwnerClient


class Dog(dog_pb2_grpc.dogServicer):
    def __init__(self):
        self.owner_client = GrpcOwnerClient()


    def CallDog(self, request, context):
        dog_name = request.dogName
        res = f"{dog_name} is going to bark!"
        print(self.owner_client.notify_owner(dog_name))
        print(res)
        return dog_pb2.DogResponse(dogBark=res)