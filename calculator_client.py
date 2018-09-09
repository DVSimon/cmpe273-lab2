from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.CalculateRequest(num1 = 10, num2 = 15))
    print("Result = " + str(response.result))


if __name__ == '__main__':
    run()