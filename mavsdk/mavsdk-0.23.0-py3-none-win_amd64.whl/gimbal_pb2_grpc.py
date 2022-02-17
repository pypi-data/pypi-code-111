# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import gimbal_pb2 as gimbal_dot_gimbal__pb2


class GimbalServiceStub(object):
    """Provide control over a gimbal.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetPitchAndYaw = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/SetPitchAndYaw',
                request_serializer=gimbal_dot_gimbal__pb2.SetPitchAndYawRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.SetPitchAndYawResponse.FromString,
                )
        self.SetPitchRateAndYawRate = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/SetPitchRateAndYawRate',
                request_serializer=gimbal_dot_gimbal__pb2.SetPitchRateAndYawRateRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.SetPitchRateAndYawRateResponse.FromString,
                )
        self.SetMode = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/SetMode',
                request_serializer=gimbal_dot_gimbal__pb2.SetModeRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.SetModeResponse.FromString,
                )
        self.SetRoiLocation = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/SetRoiLocation',
                request_serializer=gimbal_dot_gimbal__pb2.SetRoiLocationRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.SetRoiLocationResponse.FromString,
                )
        self.TakeControl = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/TakeControl',
                request_serializer=gimbal_dot_gimbal__pb2.TakeControlRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.TakeControlResponse.FromString,
                )
        self.ReleaseControl = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/ReleaseControl',
                request_serializer=gimbal_dot_gimbal__pb2.ReleaseControlRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.ReleaseControlResponse.FromString,
                )
        self.SubscribeControl = channel.unary_stream(
                '/mavsdk.rpc.gimbal.GimbalService/SubscribeControl',
                request_serializer=gimbal_dot_gimbal__pb2.SubscribeControlRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.ControlResponse.FromString,
                )


class GimbalServiceServicer(object):
    """Provide control over a gimbal.
    """

    def SetPitchAndYaw(self, request, context):
        """

        Set gimbal pitch and yaw angles.

        This sets the desired pitch and yaw angles of a gimbal.
        Will return when the command is accepted, however, it might
        take the gimbal longer to actually be set to the new angles.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPitchRateAndYawRate(self, request, context):
        """

        Set gimbal angular rates around pitch and yaw axes.

        This sets the desired angular rates around pitch and yaw axes of a gimbal.
        Will return when the command is accepted, however, it might
        take the gimbal longer to actually reach the angular rate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMode(self, request, context):
        """
        Set gimbal mode.

        This sets the desired yaw mode of a gimbal.
        Will return when the command is accepted. However, it might
        take the gimbal longer to actually be set to the new angles.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRoiLocation(self, request, context):
        """
        Set gimbal region of interest (ROI).

        This sets a region of interest that the gimbal will point to.
        The gimbal will continue to point to the specified region until it
        receives a new command.
        The function will return when the command is accepted, however, it might
        take the gimbal longer to actually rotate to the ROI.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TakeControl(self, request, context):
        """
        Take control.

        There can be only two components in control of a gimbal at any given time.
        One with "primary" control, and one with "secondary" control. The way the
        secondary control is implemented is not specified and hence depends on the
        vehicle.

        Components are expected to be cooperative, which means that they can
        override each other and should therefore do it carefully.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReleaseControl(self, request, context):
        """
        Release control.

        Release control, such that other components can control the gimbal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeControl(self, request, context):
        """
        Subscribe to control status updates.

        This allows a component to know if it has primary, secondary or
        no control over the gimbal. Also, it gives the system and component ids
        of the other components in control (if any).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GimbalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetPitchAndYaw': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPitchAndYaw,
                    request_deserializer=gimbal_dot_gimbal__pb2.SetPitchAndYawRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.SetPitchAndYawResponse.SerializeToString,
            ),
            'SetPitchRateAndYawRate': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPitchRateAndYawRate,
                    request_deserializer=gimbal_dot_gimbal__pb2.SetPitchRateAndYawRateRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.SetPitchRateAndYawRateResponse.SerializeToString,
            ),
            'SetMode': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMode,
                    request_deserializer=gimbal_dot_gimbal__pb2.SetModeRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.SetModeResponse.SerializeToString,
            ),
            'SetRoiLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRoiLocation,
                    request_deserializer=gimbal_dot_gimbal__pb2.SetRoiLocationRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.SetRoiLocationResponse.SerializeToString,
            ),
            'TakeControl': grpc.unary_unary_rpc_method_handler(
                    servicer.TakeControl,
                    request_deserializer=gimbal_dot_gimbal__pb2.TakeControlRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.TakeControlResponse.SerializeToString,
            ),
            'ReleaseControl': grpc.unary_unary_rpc_method_handler(
                    servicer.ReleaseControl,
                    request_deserializer=gimbal_dot_gimbal__pb2.ReleaseControlRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.ReleaseControlResponse.SerializeToString,
            ),
            'SubscribeControl': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeControl,
                    request_deserializer=gimbal_dot_gimbal__pb2.SubscribeControlRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.ControlResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.gimbal.GimbalService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GimbalService(object):
    """Provide control over a gimbal.
    """

    @staticmethod
    def SetPitchAndYaw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.gimbal.GimbalService/SetPitchAndYaw',
            gimbal_dot_gimbal__pb2.SetPitchAndYawRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.SetPitchAndYawResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPitchRateAndYawRate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.gimbal.GimbalService/SetPitchRateAndYawRate',
            gimbal_dot_gimbal__pb2.SetPitchRateAndYawRateRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.SetPitchRateAndYawRateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.gimbal.GimbalService/SetMode',
            gimbal_dot_gimbal__pb2.SetModeRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.SetModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetRoiLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.gimbal.GimbalService/SetRoiLocation',
            gimbal_dot_gimbal__pb2.SetRoiLocationRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.SetRoiLocationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TakeControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.gimbal.GimbalService/TakeControl',
            gimbal_dot_gimbal__pb2.TakeControlRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.TakeControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReleaseControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.gimbal.GimbalService/ReleaseControl',
            gimbal_dot_gimbal__pb2.ReleaseControlRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.ReleaseControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.gimbal.GimbalService/SubscribeControl',
            gimbal_dot_gimbal__pb2.SubscribeControlRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.ControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
