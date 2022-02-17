# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ondewo.nlu import aiservices_pb2 as ondewo_dot_nlu_dot_aiservices__pb2


class AiServicesStub(object):
    """The Central class defining the ondewo ai services
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExtractEntities = channel.unary_unary(
                '/ondewo.nlu.AiServices/ExtractEntities',
                request_serializer=ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesRequest.SerializeToString,
                response_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesResponse.FromString,
                )
        self.GenerateUserSays = channel.unary_unary(
                '/ondewo.nlu.AiServices/GenerateUserSays',
                request_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GenerateUserSaysRequest.SerializeToString,
                response_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GenerateUserSaysResponse.FromString,
                )
        self.GenerateResponses = channel.unary_unary(
                '/ondewo.nlu.AiServices/GenerateResponses',
                request_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GenerateResponsesRequest.SerializeToString,
                response_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GenerateResponsesResponse.FromString,
                )
        self.GetAlternativeSentences = channel.unary_unary(
                '/ondewo.nlu.AiServices/GetAlternativeSentences',
                request_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeSentencesRequest.SerializeToString,
                response_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeSentencesResponse.FromString,
                )
        self.GetAlternativeTrainingPhrases = channel.unary_unary(
                '/ondewo.nlu.AiServices/GetAlternativeTrainingPhrases',
                request_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeTrainingPhrasesRequest.SerializeToString,
                response_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeTrainingPhrasesResponse.FromString,
                )
        self.GetSynonyms = channel.unary_unary(
                '/ondewo.nlu.AiServices/GetSynonyms',
                request_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GetSynonymsRequest.SerializeToString,
                response_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GetSynonymsResponse.FromString,
                )
        self.ExtractEntitiesFuzzy = channel.unary_unary(
                '/ondewo.nlu.AiServices/ExtractEntitiesFuzzy',
                request_serializer=ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesFuzzyRequest.SerializeToString,
                response_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesResponse.FromString,
                )


class AiServicesServicer(object):
    """The Central class defining the ondewo ai services
    """

    def ExtractEntities(self, request, context):
        """Processes a natural language query and returns detected entities
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateUserSays(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateResponses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAlternativeSentences(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAlternativeTrainingPhrases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSynonyms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExtractEntitiesFuzzy(self, request, context):
        """Processes a natural language query and returns detected entities
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AiServicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExtractEntities': grpc.unary_unary_rpc_method_handler(
                    servicer.ExtractEntities,
                    request_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesRequest.FromString,
                    response_serializer=ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesResponse.SerializeToString,
            ),
            'GenerateUserSays': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateUserSays,
                    request_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GenerateUserSaysRequest.FromString,
                    response_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GenerateUserSaysResponse.SerializeToString,
            ),
            'GenerateResponses': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateResponses,
                    request_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GenerateResponsesRequest.FromString,
                    response_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GenerateResponsesResponse.SerializeToString,
            ),
            'GetAlternativeSentences': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAlternativeSentences,
                    request_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeSentencesRequest.FromString,
                    response_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeSentencesResponse.SerializeToString,
            ),
            'GetAlternativeTrainingPhrases': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAlternativeTrainingPhrases,
                    request_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeTrainingPhrasesRequest.FromString,
                    response_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeTrainingPhrasesResponse.SerializeToString,
            ),
            'GetSynonyms': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSynonyms,
                    request_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.GetSynonymsRequest.FromString,
                    response_serializer=ondewo_dot_nlu_dot_aiservices__pb2.GetSynonymsResponse.SerializeToString,
            ),
            'ExtractEntitiesFuzzy': grpc.unary_unary_rpc_method_handler(
                    servicer.ExtractEntitiesFuzzy,
                    request_deserializer=ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesFuzzyRequest.FromString,
                    response_serializer=ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ondewo.nlu.AiServices', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AiServices(object):
    """The Central class defining the ondewo ai services
    """

    @staticmethod
    def ExtractEntities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.AiServices/ExtractEntities',
            ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesRequest.SerializeToString,
            ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateUserSays(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.AiServices/GenerateUserSays',
            ondewo_dot_nlu_dot_aiservices__pb2.GenerateUserSaysRequest.SerializeToString,
            ondewo_dot_nlu_dot_aiservices__pb2.GenerateUserSaysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateResponses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.AiServices/GenerateResponses',
            ondewo_dot_nlu_dot_aiservices__pb2.GenerateResponsesRequest.SerializeToString,
            ondewo_dot_nlu_dot_aiservices__pb2.GenerateResponsesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAlternativeSentences(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.AiServices/GetAlternativeSentences',
            ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeSentencesRequest.SerializeToString,
            ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeSentencesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAlternativeTrainingPhrases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.AiServices/GetAlternativeTrainingPhrases',
            ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeTrainingPhrasesRequest.SerializeToString,
            ondewo_dot_nlu_dot_aiservices__pb2.GetAlternativeTrainingPhrasesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSynonyms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.AiServices/GetSynonyms',
            ondewo_dot_nlu_dot_aiservices__pb2.GetSynonymsRequest.SerializeToString,
            ondewo_dot_nlu_dot_aiservices__pb2.GetSynonymsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExtractEntitiesFuzzy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.AiServices/ExtractEntitiesFuzzy',
            ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesFuzzyRequest.SerializeToString,
            ondewo_dot_nlu_dot_aiservices__pb2.ExtractEntitiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
