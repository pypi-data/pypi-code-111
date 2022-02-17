# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from github.com.metaprov.modelaapi.services.license.v1 import license_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2


class LicenseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListLicenses = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/ListLicenses',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.ListLicensesRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.ListLicensesResponse.FromString,
                )
        self.CreateLicense = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/CreateLicense',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseResponse.FromString,
                )
        self.CreateLicenseFromKey = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/CreateLicenseFromKey',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseFromKeyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseResponse.FromString,
                )
        self.GetLicense = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/GetLicense',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.GetLicenseRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.GetLicenseResponse.FromString,
                )
        self.UpdateLicense = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/UpdateLicense',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.UpdateLicenseRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.UpdateLicenseResponse.FromString,
                )
        self.DeleteLicense = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/DeleteLicense',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.DeleteLicenseRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.DeleteLicenseResponse.FromString,
                )


class LicenseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListLicenses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateLicense(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateLicenseFromKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLicense(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateLicense(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteLicense(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LicenseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListLicenses': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLicenses,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.ListLicensesRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.ListLicensesResponse.SerializeToString,
            ),
            'CreateLicense': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateLicense,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseResponse.SerializeToString,
            ),
            'CreateLicenseFromKey': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateLicenseFromKey,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseFromKeyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseResponse.SerializeToString,
            ),
            'GetLicense': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLicense,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.GetLicenseRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.GetLicenseResponse.SerializeToString,
            ),
            'UpdateLicense': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateLicense,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.UpdateLicenseRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.UpdateLicenseResponse.SerializeToString,
            ),
            'DeleteLicense': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteLicense,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.DeleteLicenseRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.DeleteLicenseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'github.com.metaprov.modelaapi.services.license.v1.LicenseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LicenseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListLicenses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/ListLicenses',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.ListLicensesRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.ListLicensesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateLicense(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/CreateLicense',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateLicenseFromKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/CreateLicenseFromKey',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseFromKeyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.CreateLicenseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLicense(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/GetLicense',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.GetLicenseRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.GetLicenseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateLicense(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/UpdateLicense',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.UpdateLicenseRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.UpdateLicenseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteLicense(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.license.v1.LicenseService/DeleteLicense',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.DeleteLicenseRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_license_dot_v1_dot_license__pb2.DeleteLicenseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
