# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import simple_pb2 as simple__pb2


class TestServiceStub(object):
  """Define Greeter services
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.test = channel.unary_unary(
        '/simple.TestService/test',
        request_serializer=simple__pb2.TestMsg.SerializeToString,
        response_deserializer=simple__pb2.TestMsg.FromString,
        )


class TestServiceServicer(object):
  """Define Greeter services
  """

  def test(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'test': grpc.unary_unary_rpc_method_handler(
          servicer.test,
          request_deserializer=simple__pb2.TestMsg.FromString,
          response_serializer=simple__pb2.TestMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'simple.TestService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
