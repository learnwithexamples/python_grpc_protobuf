#import grpc
from concurrent import futures

from my_service_pb2 import MyRequest, MyResponse, MyServiceServicer

class MyService(MyServiceServicer):
    def SayHello(self, request, context):
        return MyResponse(message=f'Hello, {request.name}!')

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
my_service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    server.stop(0)