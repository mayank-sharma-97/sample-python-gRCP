import grpc
from concurrent import futures
import time

# import the generated classes
import gRPC_service.proto.calculator_pb2 as calculator_pb2 
import gRPC_service.proto.calculator_pb2_grpc as calculator_pb2_grpc

# import the original calculator.py
import src.add as add

# create a class to define the server functions
# derived from calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.AddServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data types
    # generated as calculator_pb2.Number
    def Addition(self, request, context):
        response = calculator_pb2.ResponeAdd()
        response.result = add.add(request.num1,request.num2)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_AddServicer_to_server`
# to add the defined class to the created server
calculator_pb2_grpc.add_AddServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)