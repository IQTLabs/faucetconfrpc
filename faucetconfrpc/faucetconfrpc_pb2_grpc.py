# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from faucetconfrpc import faucetconfrpc_pb2 as faucetconfrpc_dot_faucetconfrpc__pb2


class FaucetConfServerStub(object):
    """NOTE: currently some of these API calls allow specifying an optional config_file.
    This will be removed in future so the client does not need/have knowledge of the underlying YAML store.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConfigFile = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/GetConfigFile',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetConfigFileRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetConfigFileReply.FromString,
                )
        self.SetConfigFile = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/SetConfigFile',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetConfigFileRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetConfigFileReply.FromString,
                )
        self.DelConfigFromFile = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/DelConfigFromFile',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelConfigFromFileRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelConfigFromFileReply.FromString,
                )
        self.AddPortMirror = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/AddPortMirror',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.AddPortMirrorRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.AddPortMirrorReply.FromString,
                )
        self.RemovePortMirror = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/RemovePortMirror',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortMirrorRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortMirrorReply.FromString,
                )
        self.ClearPortMirror = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/ClearPortMirror',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.ClearPortMirrorRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.ClearPortMirrorReply.FromString,
                )
        self.AddPortAcl = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/AddPortAcl',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.AddPortAclRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.AddPortAclReply.FromString,
                )
        self.RemovePortAcl = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/RemovePortAcl',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortAclRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortAclReply.FromString,
                )
        self.SetPortAcl = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/SetPortAcl',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetPortAclRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetPortAclReply.FromString,
                )
        self.SetDpInterfaces = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/SetDpInterfaces',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetDpInterfacesRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetDpInterfacesReply.FromString,
                )
        self.GetDpInfo = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/GetDpInfo',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpInfoRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpInfoReply.FromString,
                )
        self.DelDpInterfaces = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/DelDpInterfaces',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelDpInterfacesRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelDpInterfacesReply.FromString,
                )
        self.DelDps = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/DelDps',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelDpsRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelDpsReply.FromString,
                )
        self.SetRemoteMirrorPort = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/SetRemoteMirrorPort',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetRemoteMirrorPortRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetRemoteMirrorPortReply.FromString,
                )
        self.GetDpNames = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/GetDpNames',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpNamesRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpNamesReply.FromString,
                )
        self.GetDpIDs = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/GetDpIDs',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpIDsRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpIDsReply.FromString,
                )
        self.GetAclNames = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/GetAclNames',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetAclNamesRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetAclNamesReply.FromString,
                )
        self.SetDps = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/SetDps',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetDpsRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetDpsReply.FromString,
                )
        self.MakeCoprocessorPort = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/MakeCoprocessorPort',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.MakeCoprocessorPortRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.MakeCoprocessorPortReply.FromString,
                )
        self.SetVlanOutAcl = channel.unary_unary(
                '/faucetconfserver.FaucetConfServer/SetVlanOutAcl',
                request_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetVlanOutAclRequest.SerializeToString,
                response_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetVlanOutAclReply.FromString,
                )


class FaucetConfServerServicer(object):
    """NOTE: currently some of these API calls allow specifying an optional config_file.
    This will be removed in future so the client does not need/have knowledge of the underlying YAML store.
    """

    def GetConfigFile(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConfigFile(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelConfigFromFile(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPortMirror(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemovePortMirror(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearPortMirror(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPortAcl(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemovePortAcl(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPortAcl(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDpInterfaces(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDpInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelDpInterfaces(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelDps(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRemoteMirrorPort(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDpNames(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDpIDs(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAclNames(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDps(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MakeCoprocessorPort(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetVlanOutAcl(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FaucetConfServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetConfigFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfigFile,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetConfigFileRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetConfigFileReply.SerializeToString,
            ),
            'SetConfigFile': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigFile,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetConfigFileRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetConfigFileReply.SerializeToString,
            ),
            'DelConfigFromFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DelConfigFromFile,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelConfigFromFileRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelConfigFromFileReply.SerializeToString,
            ),
            'AddPortMirror': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPortMirror,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.AddPortMirrorRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.AddPortMirrorReply.SerializeToString,
            ),
            'RemovePortMirror': grpc.unary_unary_rpc_method_handler(
                    servicer.RemovePortMirror,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortMirrorRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortMirrorReply.SerializeToString,
            ),
            'ClearPortMirror': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearPortMirror,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.ClearPortMirrorRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.ClearPortMirrorReply.SerializeToString,
            ),
            'AddPortAcl': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPortAcl,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.AddPortAclRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.AddPortAclReply.SerializeToString,
            ),
            'RemovePortAcl': grpc.unary_unary_rpc_method_handler(
                    servicer.RemovePortAcl,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortAclRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortAclReply.SerializeToString,
            ),
            'SetPortAcl': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPortAcl,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetPortAclRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetPortAclReply.SerializeToString,
            ),
            'SetDpInterfaces': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDpInterfaces,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetDpInterfacesRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetDpInterfacesReply.SerializeToString,
            ),
            'GetDpInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDpInfo,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpInfoRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpInfoReply.SerializeToString,
            ),
            'DelDpInterfaces': grpc.unary_unary_rpc_method_handler(
                    servicer.DelDpInterfaces,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelDpInterfacesRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelDpInterfacesReply.SerializeToString,
            ),
            'DelDps': grpc.unary_unary_rpc_method_handler(
                    servicer.DelDps,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelDpsRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.DelDpsReply.SerializeToString,
            ),
            'SetRemoteMirrorPort': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRemoteMirrorPort,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetRemoteMirrorPortRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetRemoteMirrorPortReply.SerializeToString,
            ),
            'GetDpNames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDpNames,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpNamesRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpNamesReply.SerializeToString,
            ),
            'GetDpIDs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDpIDs,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpIDsRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetDpIDsReply.SerializeToString,
            ),
            'GetAclNames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAclNames,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetAclNamesRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.GetAclNamesReply.SerializeToString,
            ),
            'SetDps': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDps,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetDpsRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetDpsReply.SerializeToString,
            ),
            'MakeCoprocessorPort': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeCoprocessorPort,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.MakeCoprocessorPortRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.MakeCoprocessorPortReply.SerializeToString,
            ),
            'SetVlanOutAcl': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVlanOutAcl,
                    request_deserializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetVlanOutAclRequest.FromString,
                    response_serializer=faucetconfrpc_dot_faucetconfrpc__pb2.SetVlanOutAclReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'faucetconfserver.FaucetConfServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FaucetConfServer(object):
    """NOTE: currently some of these API calls allow specifying an optional config_file.
    This will be removed in future so the client does not need/have knowledge of the underlying YAML store.
    """

    @staticmethod
    def GetConfigFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/GetConfigFile',
            faucetconfrpc_dot_faucetconfrpc__pb2.GetConfigFileRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.GetConfigFileReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetConfigFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/SetConfigFile',
            faucetconfrpc_dot_faucetconfrpc__pb2.SetConfigFileRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.SetConfigFileReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelConfigFromFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/DelConfigFromFile',
            faucetconfrpc_dot_faucetconfrpc__pb2.DelConfigFromFileRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.DelConfigFromFileReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPortMirror(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/AddPortMirror',
            faucetconfrpc_dot_faucetconfrpc__pb2.AddPortMirrorRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.AddPortMirrorReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemovePortMirror(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/RemovePortMirror',
            faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortMirrorRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortMirrorReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearPortMirror(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/ClearPortMirror',
            faucetconfrpc_dot_faucetconfrpc__pb2.ClearPortMirrorRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.ClearPortMirrorReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPortAcl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/AddPortAcl',
            faucetconfrpc_dot_faucetconfrpc__pb2.AddPortAclRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.AddPortAclReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemovePortAcl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/RemovePortAcl',
            faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortAclRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.RemovePortAclReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPortAcl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/SetPortAcl',
            faucetconfrpc_dot_faucetconfrpc__pb2.SetPortAclRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.SetPortAclReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDpInterfaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/SetDpInterfaces',
            faucetconfrpc_dot_faucetconfrpc__pb2.SetDpInterfacesRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.SetDpInterfacesReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDpInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/GetDpInfo',
            faucetconfrpc_dot_faucetconfrpc__pb2.GetDpInfoRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.GetDpInfoReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelDpInterfaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/DelDpInterfaces',
            faucetconfrpc_dot_faucetconfrpc__pb2.DelDpInterfacesRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.DelDpInterfacesReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelDps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/DelDps',
            faucetconfrpc_dot_faucetconfrpc__pb2.DelDpsRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.DelDpsReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetRemoteMirrorPort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/SetRemoteMirrorPort',
            faucetconfrpc_dot_faucetconfrpc__pb2.SetRemoteMirrorPortRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.SetRemoteMirrorPortReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDpNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/GetDpNames',
            faucetconfrpc_dot_faucetconfrpc__pb2.GetDpNamesRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.GetDpNamesReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDpIDs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/GetDpIDs',
            faucetconfrpc_dot_faucetconfrpc__pb2.GetDpIDsRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.GetDpIDsReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAclNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/GetAclNames',
            faucetconfrpc_dot_faucetconfrpc__pb2.GetAclNamesRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.GetAclNamesReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/SetDps',
            faucetconfrpc_dot_faucetconfrpc__pb2.SetDpsRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.SetDpsReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MakeCoprocessorPort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/MakeCoprocessorPort',
            faucetconfrpc_dot_faucetconfrpc__pb2.MakeCoprocessorPortRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.MakeCoprocessorPortReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetVlanOutAcl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faucetconfserver.FaucetConfServer/SetVlanOutAcl',
            faucetconfrpc_dot_faucetconfrpc__pb2.SetVlanOutAclRequest.SerializeToString,
            faucetconfrpc_dot_faucetconfrpc__pb2.SetVlanOutAclReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
