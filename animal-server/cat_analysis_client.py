import grpc
import catAnalysis_pb2
import catAnalysis_pb2_grpc

def analyze_cat(cat_name):
    channel = grpc.insecure_channel('localhost:50057')
    stub = catAnalysis_pb2_grpc.catAnalysisStub(channel)
    req = catAnalysis_pb2.AnalysisRequest(catName=cat_name)
    response = stub.AnalyzeSound(req)
    return response