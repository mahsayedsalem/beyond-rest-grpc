import grpc
import dog_pb2
import dog_pb2_grpc

def call_dog(dog_name):
    channel = grpc.insecure_channel('localhost:50055')
    stub = dog_pb2_grpc.dogStub(channel)
    req = dog_pb2.DogRequest(dogName=dog_name)
    response = stub.CallDog(req)
    return response
