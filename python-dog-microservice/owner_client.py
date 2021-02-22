import grpc
import owner_pb2
import owner_pb2_grpc

def notify_owner(dog_name):
    channel = grpc.insecure_channel('localhost:50051')
    stub = owner_pb2_grpc.OwnerStub(channel)
    req = owner_pb2.NotifyRequest(animalName=dog_name, animalType="dog")
    response = stub.Notify(req)
    print(response.message)