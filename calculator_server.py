from concurrent import futures
import time

import grpc

import calculator_pb2_grpc
import calculator_pb2
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(calculator_pb2_grpc.CalculatorServicer):

    def Add(self, request, context):
        sum = request.num1 + request.num2;
        return calculator_pb2.CalculateReply(result=sum)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()