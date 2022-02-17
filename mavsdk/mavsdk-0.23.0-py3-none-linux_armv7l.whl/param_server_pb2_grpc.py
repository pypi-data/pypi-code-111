# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import param_server_pb2 as param__server_dot_param__server__pb2


class ParamServerServiceStub(object):
    """Provide raw access to retrieve and provide server parameters.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RetrieveParamInt = channel.unary_unary(
                '/mavsdk.rpc.param_server.ParamServerService/RetrieveParamInt',
                request_serializer=param__server_dot_param__server__pb2.RetrieveParamIntRequest.SerializeToString,
                response_deserializer=param__server_dot_param__server__pb2.RetrieveParamIntResponse.FromString,
                )
        self.ProvideParamInt = channel.unary_unary(
                '/mavsdk.rpc.param_server.ParamServerService/ProvideParamInt',
                request_serializer=param__server_dot_param__server__pb2.ProvideParamIntRequest.SerializeToString,
                response_deserializer=param__server_dot_param__server__pb2.ProvideParamIntResponse.FromString,
                )
        self.RetrieveParamFloat = channel.unary_unary(
                '/mavsdk.rpc.param_server.ParamServerService/RetrieveParamFloat',
                request_serializer=param__server_dot_param__server__pb2.RetrieveParamFloatRequest.SerializeToString,
                response_deserializer=param__server_dot_param__server__pb2.RetrieveParamFloatResponse.FromString,
                )
        self.ProvideParamFloat = channel.unary_unary(
                '/mavsdk.rpc.param_server.ParamServerService/ProvideParamFloat',
                request_serializer=param__server_dot_param__server__pb2.ProvideParamFloatRequest.SerializeToString,
                response_deserializer=param__server_dot_param__server__pb2.ProvideParamFloatResponse.FromString,
                )
        self.RetrieveAllParams = channel.unary_unary(
                '/mavsdk.rpc.param_server.ParamServerService/RetrieveAllParams',
                request_serializer=param__server_dot_param__server__pb2.RetrieveAllParamsRequest.SerializeToString,
                response_deserializer=param__server_dot_param__server__pb2.RetrieveAllParamsResponse.FromString,
                )


class ParamServerServiceServicer(object):
    """Provide raw access to retrieve and provide server parameters.
    """

    def RetrieveParamInt(self, request, context):
        """
        Retrieve an int parameter.

        If the type is wrong, the result will be `WRONG_TYPE`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvideParamInt(self, request, context):
        """
        Provide an int parameter.

        If the type is wrong, the result will be `WRONG_TYPE`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveParamFloat(self, request, context):
        """
        Retrieve a float parameter.

        If the type is wrong, the result will be `WRONG_TYPE`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvideParamFloat(self, request, context):
        """
        Provide a float parameter.

        If the type is wrong, the result will be `WRONG_TYPE`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveAllParams(self, request, context):
        """
        Retrieve all parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ParamServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RetrieveParamInt': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveParamInt,
                    request_deserializer=param__server_dot_param__server__pb2.RetrieveParamIntRequest.FromString,
                    response_serializer=param__server_dot_param__server__pb2.RetrieveParamIntResponse.SerializeToString,
            ),
            'ProvideParamInt': grpc.unary_unary_rpc_method_handler(
                    servicer.ProvideParamInt,
                    request_deserializer=param__server_dot_param__server__pb2.ProvideParamIntRequest.FromString,
                    response_serializer=param__server_dot_param__server__pb2.ProvideParamIntResponse.SerializeToString,
            ),
            'RetrieveParamFloat': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveParamFloat,
                    request_deserializer=param__server_dot_param__server__pb2.RetrieveParamFloatRequest.FromString,
                    response_serializer=param__server_dot_param__server__pb2.RetrieveParamFloatResponse.SerializeToString,
            ),
            'ProvideParamFloat': grpc.unary_unary_rpc_method_handler(
                    servicer.ProvideParamFloat,
                    request_deserializer=param__server_dot_param__server__pb2.ProvideParamFloatRequest.FromString,
                    response_serializer=param__server_dot_param__server__pb2.ProvideParamFloatResponse.SerializeToString,
            ),
            'RetrieveAllParams': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveAllParams,
                    request_deserializer=param__server_dot_param__server__pb2.RetrieveAllParamsRequest.FromString,
                    response_serializer=param__server_dot_param__server__pb2.RetrieveAllParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.param_server.ParamServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ParamServerService(object):
    """Provide raw access to retrieve and provide server parameters.
    """

    @staticmethod
    def RetrieveParamInt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.param_server.ParamServerService/RetrieveParamInt',
            param__server_dot_param__server__pb2.RetrieveParamIntRequest.SerializeToString,
            param__server_dot_param__server__pb2.RetrieveParamIntResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProvideParamInt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.param_server.ParamServerService/ProvideParamInt',
            param__server_dot_param__server__pb2.ProvideParamIntRequest.SerializeToString,
            param__server_dot_param__server__pb2.ProvideParamIntResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveParamFloat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.param_server.ParamServerService/RetrieveParamFloat',
            param__server_dot_param__server__pb2.RetrieveParamFloatRequest.SerializeToString,
            param__server_dot_param__server__pb2.RetrieveParamFloatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProvideParamFloat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.param_server.ParamServerService/ProvideParamFloat',
            param__server_dot_param__server__pb2.ProvideParamFloatRequest.SerializeToString,
            param__server_dot_param__server__pb2.ProvideParamFloatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveAllParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.param_server.ParamServerService/RetrieveAllParams',
            param__server_dot_param__server__pb2.RetrieveAllParamsRequest.SerializeToString,
            param__server_dot_param__server__pb2.RetrieveAllParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
