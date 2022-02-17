# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..common import Common_pb2 as common_dot_Common__pb2
from ..language_agent import Tracing_pb2 as language__agent_dot_Tracing__pb2


class TraceSegmentReportServiceStub(object):
    """Define a trace segment report service.
    All language agents or any trace collecting component, could use this service to send span collection to the SkyWalking OAP backend.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.collect = channel.stream_unary(
                '/skywalking.v3.TraceSegmentReportService/collect',
                request_serializer=language__agent_dot_Tracing__pb2.SegmentObject.SerializeToString,
                response_deserializer=common_dot_Common__pb2.Commands.FromString,
                )
        self.collectInSync = channel.unary_unary(
                '/skywalking.v3.TraceSegmentReportService/collectInSync',
                request_serializer=language__agent_dot_Tracing__pb2.SegmentCollection.SerializeToString,
                response_deserializer=common_dot_Common__pb2.Commands.FromString,
                )


class TraceSegmentReportServiceServicer(object):
    """Define a trace segment report service.
    All language agents or any trace collecting component, could use this service to send span collection to the SkyWalking OAP backend.
    """

    def collect(self, request_iterator, context):
        """Recommended trace segment report channel.
        gRPC streaming provides better performance.
        All language agents should choose this.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def collectInSync(self, request, context):
        """An alternative for trace report by using gRPC unary
        This is provided for some 3rd-party integration, if and only if they prefer the unary mode somehow.
        The performance of SkyWalking OAP server would be very similar with streaming report,
        the performance of the network and client side are affected
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TraceSegmentReportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'collect': grpc.stream_unary_rpc_method_handler(
                    servicer.collect,
                    request_deserializer=language__agent_dot_Tracing__pb2.SegmentObject.FromString,
                    response_serializer=common_dot_Common__pb2.Commands.SerializeToString,
            ),
            'collectInSync': grpc.unary_unary_rpc_method_handler(
                    servicer.collectInSync,
                    request_deserializer=language__agent_dot_Tracing__pb2.SegmentCollection.FromString,
                    response_serializer=common_dot_Common__pb2.Commands.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'skywalking.v3.TraceSegmentReportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TraceSegmentReportService(object):
    """Define a trace segment report service.
    All language agents or any trace collecting component, could use this service to send span collection to the SkyWalking OAP backend.
    """

    @staticmethod
    def collect(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/skywalking.v3.TraceSegmentReportService/collect',
            language__agent_dot_Tracing__pb2.SegmentObject.SerializeToString,
            common_dot_Common__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def collectInSync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/skywalking.v3.TraceSegmentReportService/collectInSync',
            language__agent_dot_Tracing__pb2.SegmentCollection.SerializeToString,
            common_dot_Common__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
