from __future__ import print_function

import logging

import grpc
import template_pb2
import template_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to get info within timewindow ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = template_pb2_grpc.TemplateStub(channel)
        response = stub.SendRequest(template_pb2.TimeWindow(start=template_pb2.TimeStamp(day=1, hour=2, min=3), stop=template_pb2.TimeStamp(day=4, hour=5, min=6)))
    print("Template client received: " + response.duration)


if __name__ == "__main__":
    logging.basicConfig()
    run()
