 
import grpc

# import the generated classes
from gRPC_service.proto import calculator_pb2
from gRPC_service.proto import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.AddStub(channel)

# create a valid request message
number = calculator_pb2.RequestAdd(num1=10,num2=20)

# make the call
response = stub.Addition(number)

# et voilà
print(response.result)