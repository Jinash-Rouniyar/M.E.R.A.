# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import audio2face_pb2 as audio2face__pb2


class Audio2FaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PushAudio = channel.unary_unary(
            "/nvidia.audio2face.Audio2Face/PushAudio",
            request_serializer=audio2face__pb2.PushAudioRequest.SerializeToString,
            response_deserializer=audio2face__pb2.PushAudioResponse.FromString,
        )
        self.PushAudioStream = channel.stream_unary(
            "/nvidia.audio2face.Audio2Face/PushAudioStream",
            request_serializer=audio2face__pb2.PushAudioStreamRequest.SerializeToString,
            response_deserializer=audio2face__pb2.PushAudioStreamResponse.FromString,
        )


class Audio2FaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PushAudio(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PushAudioStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_Audio2FaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PushAudio": grpc.unary_unary_rpc_method_handler(
            servicer.PushAudio,
            request_deserializer=audio2face__pb2.PushAudioRequest.FromString,
            response_serializer=audio2face__pb2.PushAudioResponse.SerializeToString,
        ),
        "PushAudioStream": grpc.stream_unary_rpc_method_handler(
            servicer.PushAudioStream,
            request_deserializer=audio2face__pb2.PushAudioStreamRequest.FromString,
            response_serializer=audio2face__pb2.PushAudioStreamResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("nvidia.audio2face.Audio2Face", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Audio2Face(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PushAudio(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/nvidia.audio2face.Audio2Face/PushAudio",
            audio2face__pb2.PushAudioRequest.SerializeToString,
            audio2face__pb2.PushAudioResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def PushAudioStream(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            "/nvidia.audio2face.Audio2Face/PushAudioStream",
            audio2face__pb2.PushAudioStreamRequest.SerializeToString,
            audio2face__pb2.PushAudioStreamResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
