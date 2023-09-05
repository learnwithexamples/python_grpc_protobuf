#import grpc

from my_service_pb2 import MyRequest
from my_service_pb2_grpc import MyServiceStub

channel = grpc.insecure_channel('localhost:50051')
stub = MyServiceStub(channel)

request = MyRequest(name='Bard')
response = stub.SayHello(request)

print(response.message)
