import grpc
import cat_pb2
import cat_pb2_grpc

def call_cat(cat_name):
    channel = grpc.insecure_channel('localhost:50056')
    stub = cat_pb2_grpc.catStub(channel)
    req = cat_pb2.CatRequest(catName=cat_name)
    response = stub.CallCat(req)
    return response
