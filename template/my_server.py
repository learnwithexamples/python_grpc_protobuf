from concurrent import futures
import logging

import grpc
import template_pb2
import template_pb2_grpc


class Template(template_pb2_grpc.TemplateServicer):
    def SendRequest(self, request, context):
        return template_pb2.MyInfo(duration="The time delta is, %s!" % (request.stop.hour - request.start.hour))


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    template_pb2_grpc.add_TemplateServicer_to_server(Template(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
