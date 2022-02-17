# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.compute.v1 import zone_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_zone__pb2
from yandex.cloud.compute.v1 import zone_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2


class ZoneServiceStub(object):
    """A set of methods to retrieve information about availability zones.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.compute.v1.ZoneService/Get',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.GetZoneRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_zone__pb2.Zone.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.compute.v1.ZoneService/List',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.ListZonesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.ListZonesResponse.FromString,
                )


class ZoneServiceServicer(object):
    """A set of methods to retrieve information about availability zones.
    """

    def Get(self, request, context):
        """Returns the information about the specified availability zone.

        To get the list of availability zones, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of availability zones.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ZoneServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.GetZoneRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_zone__pb2.Zone.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.ListZonesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.ListZonesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.compute.v1.ZoneService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ZoneService(object):
    """A set of methods to retrieve information about availability zones.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.ZoneService/Get',
            yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.GetZoneRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_zone__pb2.Zone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.ZoneService/List',
            yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.ListZonesRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_zone__service__pb2.ListZonesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
