# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: faucetconfrpc/faucetconfrpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!faucetconfrpc/faucetconfrpc.proto\x12\x10\x66\x61ucetconfserver\"/\n\x14GetConfigFileRequest\x12\x17\n\x0f\x63onfig_filename\x18\x01 \x01(\t\")\n\x12GetConfigFileReply\x12\x13\n\x0b\x63onfig_yaml\x18\x01 \x01(\t\"q\n\x14SetConfigFileRequest\x12\x17\n\x0f\x63onfig_filename\x18\x01 \x01(\t\x12\x13\n\x0b\x63onfig_yaml\x18\x02 \x01(\t\x12\r\n\x05merge\x18\x03 \x01(\x08\x12\x1c\n\x14\x64\x65l_config_yaml_keys\x18\x04 \x01(\t\"\x14\n\x12SetConfigFileReply\"M\n\x18\x44\x65lConfigFromFileRequest\x12\x17\n\x0f\x63onfig_filename\x18\x01 \x01(\t\x12\x18\n\x10\x63onfig_yaml_keys\x18\x02 \x01(\t\"\x18\n\x16\x44\x65lConfigFromFileReply\"\x82\x01\n\x1aSetRemoteMirrorPortRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x0f\n\x07port_no\x18\x02 \x01(\r\x12\x12\n\ntunnel_vid\x18\x03 \x01(\r\x12\x16\n\x0eremote_dp_name\x18\x04 \x01(\t\x12\x16\n\x0eremote_port_no\x18\x05 \x01(\r\"\x1a\n\x18SetRemoteMirrorPortReply\"P\n\x14\x41\x64\x64PortMirrorRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x0f\n\x07port_no\x18\x02 \x01(\r\x12\x16\n\x0emirror_port_no\x18\x03 \x01(\r\"\x14\n\x12\x41\x64\x64PortMirrorReply\"e\n\x1aMakeCoprocessorPortRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x0f\n\x07port_no\x18\x02 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08strategy\x18\x04 \x01(\t\"\x1a\n\x18MakeCoprocessorPortReply\"S\n\x17RemovePortMirrorRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x0f\n\x07port_no\x18\x02 \x01(\r\x12\x16\n\x0emirror_port_no\x18\x03 \x01(\r\"\x17\n\x15RemovePortMirrorReply\"A\n\x16\x43learPortMirrorRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x16\n\x0emirror_port_no\x18\x02 \x01(\r\"\x16\n\x14\x43learPortMirrorReply\":\n\x14SetVlanOutAclRequest\x12\x11\n\tvlan_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63l_out\x18\x02 \x01(\t\"\x14\n\x12SetVlanOutAclReply\"C\n\x11SetPortAclRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x0f\n\x07port_no\x18\x02 \x01(\r\x12\x0c\n\x04\x61\x63ls\x18\x03 \x01(\t\"\x11\n\x0fSetPortAclReply\"B\n\x11\x41\x64\x64PortAclRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x0f\n\x07port_no\x18\x02 \x01(\r\x12\x0b\n\x03\x61\x63l\x18\x03 \x01(\t\"\x11\n\x0f\x41\x64\x64PortAclReply\"E\n\x14RemovePortAclRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x0f\n\x07port_no\x18\x02 \x01(\r\x12\x0b\n\x03\x61\x63l\x18\x03 \x01(\t\"\x14\n\x12RemovePortAclReply\"4\n\x0cSetInterface\x12\x0f\n\x07port_no\x18\x01 \x01(\r\x12\x13\n\x0b\x63onfig_yaml\x18\x02 \x01(\t\"\\\n\x0fSetDpInterfaces\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x38\n\x10interface_config\x18\x02 \x03(\x0b\x32\x1e.faucetconfserver.SetInterface\"V\n\x16SetDpInterfacesRequest\x12<\n\x11interfaces_config\x18\x01 \x03(\x0b\x32!.faucetconfserver.SetDpInterfaces\"\x16\n\x14SetDpInterfacesReply\"<\n\x10GetDpInfoRequest\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63onfig_filename\x18\x02 \x01(\t\"C\n\rInterfaceInfo\x12\x0f\n\x07port_no\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"o\n\x06\x44pInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x64p_id\x18\x02 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x33\n\ninterfaces\x18\x04 \x03(\x0b\x32\x1f.faucetconfserver.InterfaceInfo\"7\n\x0eGetDpInfoReply\x12%\n\x03\x64ps\x18\x01 \x03(\x0b\x32\x18.faucetconfserver.DpInfo\"f\n\x16\x44\x65lDpInterfacesRequest\x12\x33\n\x11interfaces_config\x18\x01 \x03(\x0b\x32\x18.faucetconfserver.DpInfo\x12\x17\n\x0f\x64\x65lete_empty_dp\x18\x02 \x01(\x08\"\x16\n\x14\x44\x65lDpInterfacesReply\"D\n\rDelDpsRequest\x12\x33\n\x11interfaces_config\x18\x01 \x03(\x0b\x32\x18.faucetconfserver.DpInfo\"\r\n\x0b\x44\x65lDpsReply\"\x13\n\x11GetDpNamesRequest\"\"\n\x0fGetDpNamesReply\x12\x0f\n\x07\x64p_name\x18\x01 \x03(\t\"\x11\n\x0fGetDpIDsRequest\"\x1e\n\rGetDpIDsReply\x12\r\n\x05\x64p_id\x18\x01 \x03(\x04\"&\n\x12GetAclNamesRequest\x12\x10\n\x08\x61\x63l_name\x18\x01 \x03(\t\"$\n\x10GetAclNamesReply\x12\x10\n\x08\x61\x63l_name\x18\x01 \x03(\t\"-\n\x05SetDp\x12\x0f\n\x07\x64p_name\x18\x01 \x01(\t\x12\x13\n\x0b\x63onfig_yaml\x18\x02 \x01(\t\";\n\rSetDpsRequest\x12*\n\tdp_config\x18\x01 \x03(\x0b\x32\x17.faucetconfserver.SetDp\"\r\n\x0bSetDpsReply2\x8b\x0f\n\x10\x46\x61ucetConfServer\x12_\n\rGetConfigFile\x12&.faucetconfserver.GetConfigFileRequest\x1a$.faucetconfserver.GetConfigFileReply\"\x00\x12_\n\rSetConfigFile\x12&.faucetconfserver.SetConfigFileRequest\x1a$.faucetconfserver.SetConfigFileReply\"\x00\x12k\n\x11\x44\x65lConfigFromFile\x12*.faucetconfserver.DelConfigFromFileRequest\x1a(.faucetconfserver.DelConfigFromFileReply\"\x00\x12_\n\rAddPortMirror\x12&.faucetconfserver.AddPortMirrorRequest\x1a$.faucetconfserver.AddPortMirrorReply\"\x00\x12h\n\x10RemovePortMirror\x12).faucetconfserver.RemovePortMirrorRequest\x1a\'.faucetconfserver.RemovePortMirrorReply\"\x00\x12\x65\n\x0f\x43learPortMirror\x12(.faucetconfserver.ClearPortMirrorRequest\x1a&.faucetconfserver.ClearPortMirrorReply\"\x00\x12V\n\nAddPortAcl\x12#.faucetconfserver.AddPortAclRequest\x1a!.faucetconfserver.AddPortAclReply\"\x00\x12_\n\rRemovePortAcl\x12&.faucetconfserver.RemovePortAclRequest\x1a$.faucetconfserver.RemovePortAclReply\"\x00\x12V\n\nSetPortAcl\x12#.faucetconfserver.SetPortAclRequest\x1a!.faucetconfserver.SetPortAclReply\"\x00\x12\x65\n\x0fSetDpInterfaces\x12(.faucetconfserver.SetDpInterfacesRequest\x1a&.faucetconfserver.SetDpInterfacesReply\"\x00\x12S\n\tGetDpInfo\x12\".faucetconfserver.GetDpInfoRequest\x1a .faucetconfserver.GetDpInfoReply\"\x00\x12\x65\n\x0f\x44\x65lDpInterfaces\x12(.faucetconfserver.DelDpInterfacesRequest\x1a&.faucetconfserver.DelDpInterfacesReply\"\x00\x12J\n\x06\x44\x65lDps\x12\x1f.faucetconfserver.DelDpsRequest\x1a\x1d.faucetconfserver.DelDpsReply\"\x00\x12q\n\x13SetRemoteMirrorPort\x12,.faucetconfserver.SetRemoteMirrorPortRequest\x1a*.faucetconfserver.SetRemoteMirrorPortReply\"\x00\x12V\n\nGetDpNames\x12#.faucetconfserver.GetDpNamesRequest\x1a!.faucetconfserver.GetDpNamesReply\"\x00\x12P\n\x08GetDpIDs\x12!.faucetconfserver.GetDpIDsRequest\x1a\x1f.faucetconfserver.GetDpIDsReply\"\x00\x12Y\n\x0bGetAclNames\x12$.faucetconfserver.GetAclNamesRequest\x1a\".faucetconfserver.GetAclNamesReply\"\x00\x12J\n\x06SetDps\x12\x1f.faucetconfserver.SetDpsRequest\x1a\x1d.faucetconfserver.SetDpsReply\"\x00\x12q\n\x13MakeCoprocessorPort\x12,.faucetconfserver.MakeCoprocessorPortRequest\x1a*.faucetconfserver.MakeCoprocessorPortReply\"\x00\x12_\n\rSetVlanOutAcl\x12&.faucetconfserver.SetVlanOutAclRequest\x1a$.faucetconfserver.SetVlanOutAclReply\"\x00\x42\x13Z\x11\x66\x61ucetconfserver/b\x06proto3')



_GETCONFIGFILEREQUEST = DESCRIPTOR.message_types_by_name['GetConfigFileRequest']
_GETCONFIGFILEREPLY = DESCRIPTOR.message_types_by_name['GetConfigFileReply']
_SETCONFIGFILEREQUEST = DESCRIPTOR.message_types_by_name['SetConfigFileRequest']
_SETCONFIGFILEREPLY = DESCRIPTOR.message_types_by_name['SetConfigFileReply']
_DELCONFIGFROMFILEREQUEST = DESCRIPTOR.message_types_by_name['DelConfigFromFileRequest']
_DELCONFIGFROMFILEREPLY = DESCRIPTOR.message_types_by_name['DelConfigFromFileReply']
_SETREMOTEMIRRORPORTREQUEST = DESCRIPTOR.message_types_by_name['SetRemoteMirrorPortRequest']
_SETREMOTEMIRRORPORTREPLY = DESCRIPTOR.message_types_by_name['SetRemoteMirrorPortReply']
_ADDPORTMIRRORREQUEST = DESCRIPTOR.message_types_by_name['AddPortMirrorRequest']
_ADDPORTMIRRORREPLY = DESCRIPTOR.message_types_by_name['AddPortMirrorReply']
_MAKECOPROCESSORPORTREQUEST = DESCRIPTOR.message_types_by_name['MakeCoprocessorPortRequest']
_MAKECOPROCESSORPORTREPLY = DESCRIPTOR.message_types_by_name['MakeCoprocessorPortReply']
_REMOVEPORTMIRRORREQUEST = DESCRIPTOR.message_types_by_name['RemovePortMirrorRequest']
_REMOVEPORTMIRRORREPLY = DESCRIPTOR.message_types_by_name['RemovePortMirrorReply']
_CLEARPORTMIRRORREQUEST = DESCRIPTOR.message_types_by_name['ClearPortMirrorRequest']
_CLEARPORTMIRRORREPLY = DESCRIPTOR.message_types_by_name['ClearPortMirrorReply']
_SETVLANOUTACLREQUEST = DESCRIPTOR.message_types_by_name['SetVlanOutAclRequest']
_SETVLANOUTACLREPLY = DESCRIPTOR.message_types_by_name['SetVlanOutAclReply']
_SETPORTACLREQUEST = DESCRIPTOR.message_types_by_name['SetPortAclRequest']
_SETPORTACLREPLY = DESCRIPTOR.message_types_by_name['SetPortAclReply']
_ADDPORTACLREQUEST = DESCRIPTOR.message_types_by_name['AddPortAclRequest']
_ADDPORTACLREPLY = DESCRIPTOR.message_types_by_name['AddPortAclReply']
_REMOVEPORTACLREQUEST = DESCRIPTOR.message_types_by_name['RemovePortAclRequest']
_REMOVEPORTACLREPLY = DESCRIPTOR.message_types_by_name['RemovePortAclReply']
_SETINTERFACE = DESCRIPTOR.message_types_by_name['SetInterface']
_SETDPINTERFACES = DESCRIPTOR.message_types_by_name['SetDpInterfaces']
_SETDPINTERFACESREQUEST = DESCRIPTOR.message_types_by_name['SetDpInterfacesRequest']
_SETDPINTERFACESREPLY = DESCRIPTOR.message_types_by_name['SetDpInterfacesReply']
_GETDPINFOREQUEST = DESCRIPTOR.message_types_by_name['GetDpInfoRequest']
_INTERFACEINFO = DESCRIPTOR.message_types_by_name['InterfaceInfo']
_DPINFO = DESCRIPTOR.message_types_by_name['DpInfo']
_GETDPINFOREPLY = DESCRIPTOR.message_types_by_name['GetDpInfoReply']
_DELDPINTERFACESREQUEST = DESCRIPTOR.message_types_by_name['DelDpInterfacesRequest']
_DELDPINTERFACESREPLY = DESCRIPTOR.message_types_by_name['DelDpInterfacesReply']
_DELDPSREQUEST = DESCRIPTOR.message_types_by_name['DelDpsRequest']
_DELDPSREPLY = DESCRIPTOR.message_types_by_name['DelDpsReply']
_GETDPNAMESREQUEST = DESCRIPTOR.message_types_by_name['GetDpNamesRequest']
_GETDPNAMESREPLY = DESCRIPTOR.message_types_by_name['GetDpNamesReply']
_GETDPIDSREQUEST = DESCRIPTOR.message_types_by_name['GetDpIDsRequest']
_GETDPIDSREPLY = DESCRIPTOR.message_types_by_name['GetDpIDsReply']
_GETACLNAMESREQUEST = DESCRIPTOR.message_types_by_name['GetAclNamesRequest']
_GETACLNAMESREPLY = DESCRIPTOR.message_types_by_name['GetAclNamesReply']
_SETDP = DESCRIPTOR.message_types_by_name['SetDp']
_SETDPSREQUEST = DESCRIPTOR.message_types_by_name['SetDpsRequest']
_SETDPSREPLY = DESCRIPTOR.message_types_by_name['SetDpsReply']
GetConfigFileRequest = _reflection.GeneratedProtocolMessageType('GetConfigFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONFIGFILEREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetConfigFileRequest)
  })
_sym_db.RegisterMessage(GetConfigFileRequest)

GetConfigFileReply = _reflection.GeneratedProtocolMessageType('GetConfigFileReply', (_message.Message,), {
  'DESCRIPTOR' : _GETCONFIGFILEREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetConfigFileReply)
  })
_sym_db.RegisterMessage(GetConfigFileReply)

SetConfigFileRequest = _reflection.GeneratedProtocolMessageType('SetConfigFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETCONFIGFILEREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetConfigFileRequest)
  })
_sym_db.RegisterMessage(SetConfigFileRequest)

SetConfigFileReply = _reflection.GeneratedProtocolMessageType('SetConfigFileReply', (_message.Message,), {
  'DESCRIPTOR' : _SETCONFIGFILEREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetConfigFileReply)
  })
_sym_db.RegisterMessage(SetConfigFileReply)

DelConfigFromFileRequest = _reflection.GeneratedProtocolMessageType('DelConfigFromFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELCONFIGFROMFILEREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.DelConfigFromFileRequest)
  })
_sym_db.RegisterMessage(DelConfigFromFileRequest)

DelConfigFromFileReply = _reflection.GeneratedProtocolMessageType('DelConfigFromFileReply', (_message.Message,), {
  'DESCRIPTOR' : _DELCONFIGFROMFILEREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.DelConfigFromFileReply)
  })
_sym_db.RegisterMessage(DelConfigFromFileReply)

SetRemoteMirrorPortRequest = _reflection.GeneratedProtocolMessageType('SetRemoteMirrorPortRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETREMOTEMIRRORPORTREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetRemoteMirrorPortRequest)
  })
_sym_db.RegisterMessage(SetRemoteMirrorPortRequest)

SetRemoteMirrorPortReply = _reflection.GeneratedProtocolMessageType('SetRemoteMirrorPortReply', (_message.Message,), {
  'DESCRIPTOR' : _SETREMOTEMIRRORPORTREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetRemoteMirrorPortReply)
  })
_sym_db.RegisterMessage(SetRemoteMirrorPortReply)

AddPortMirrorRequest = _reflection.GeneratedProtocolMessageType('AddPortMirrorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDPORTMIRRORREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.AddPortMirrorRequest)
  })
_sym_db.RegisterMessage(AddPortMirrorRequest)

AddPortMirrorReply = _reflection.GeneratedProtocolMessageType('AddPortMirrorReply', (_message.Message,), {
  'DESCRIPTOR' : _ADDPORTMIRRORREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.AddPortMirrorReply)
  })
_sym_db.RegisterMessage(AddPortMirrorReply)

MakeCoprocessorPortRequest = _reflection.GeneratedProtocolMessageType('MakeCoprocessorPortRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAKECOPROCESSORPORTREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.MakeCoprocessorPortRequest)
  })
_sym_db.RegisterMessage(MakeCoprocessorPortRequest)

MakeCoprocessorPortReply = _reflection.GeneratedProtocolMessageType('MakeCoprocessorPortReply', (_message.Message,), {
  'DESCRIPTOR' : _MAKECOPROCESSORPORTREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.MakeCoprocessorPortReply)
  })
_sym_db.RegisterMessage(MakeCoprocessorPortReply)

RemovePortMirrorRequest = _reflection.GeneratedProtocolMessageType('RemovePortMirrorRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPORTMIRRORREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.RemovePortMirrorRequest)
  })
_sym_db.RegisterMessage(RemovePortMirrorRequest)

RemovePortMirrorReply = _reflection.GeneratedProtocolMessageType('RemovePortMirrorReply', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPORTMIRRORREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.RemovePortMirrorReply)
  })
_sym_db.RegisterMessage(RemovePortMirrorReply)

ClearPortMirrorRequest = _reflection.GeneratedProtocolMessageType('ClearPortMirrorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEARPORTMIRRORREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.ClearPortMirrorRequest)
  })
_sym_db.RegisterMessage(ClearPortMirrorRequest)

ClearPortMirrorReply = _reflection.GeneratedProtocolMessageType('ClearPortMirrorReply', (_message.Message,), {
  'DESCRIPTOR' : _CLEARPORTMIRRORREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.ClearPortMirrorReply)
  })
_sym_db.RegisterMessage(ClearPortMirrorReply)

SetVlanOutAclRequest = _reflection.GeneratedProtocolMessageType('SetVlanOutAclRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETVLANOUTACLREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetVlanOutAclRequest)
  })
_sym_db.RegisterMessage(SetVlanOutAclRequest)

SetVlanOutAclReply = _reflection.GeneratedProtocolMessageType('SetVlanOutAclReply', (_message.Message,), {
  'DESCRIPTOR' : _SETVLANOUTACLREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetVlanOutAclReply)
  })
_sym_db.RegisterMessage(SetVlanOutAclReply)

SetPortAclRequest = _reflection.GeneratedProtocolMessageType('SetPortAclRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPORTACLREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetPortAclRequest)
  })
_sym_db.RegisterMessage(SetPortAclRequest)

SetPortAclReply = _reflection.GeneratedProtocolMessageType('SetPortAclReply', (_message.Message,), {
  'DESCRIPTOR' : _SETPORTACLREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetPortAclReply)
  })
_sym_db.RegisterMessage(SetPortAclReply)

AddPortAclRequest = _reflection.GeneratedProtocolMessageType('AddPortAclRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDPORTACLREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.AddPortAclRequest)
  })
_sym_db.RegisterMessage(AddPortAclRequest)

AddPortAclReply = _reflection.GeneratedProtocolMessageType('AddPortAclReply', (_message.Message,), {
  'DESCRIPTOR' : _ADDPORTACLREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.AddPortAclReply)
  })
_sym_db.RegisterMessage(AddPortAclReply)

RemovePortAclRequest = _reflection.GeneratedProtocolMessageType('RemovePortAclRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPORTACLREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.RemovePortAclRequest)
  })
_sym_db.RegisterMessage(RemovePortAclRequest)

RemovePortAclReply = _reflection.GeneratedProtocolMessageType('RemovePortAclReply', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPORTACLREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.RemovePortAclReply)
  })
_sym_db.RegisterMessage(RemovePortAclReply)

SetInterface = _reflection.GeneratedProtocolMessageType('SetInterface', (_message.Message,), {
  'DESCRIPTOR' : _SETINTERFACE,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetInterface)
  })
_sym_db.RegisterMessage(SetInterface)

SetDpInterfaces = _reflection.GeneratedProtocolMessageType('SetDpInterfaces', (_message.Message,), {
  'DESCRIPTOR' : _SETDPINTERFACES,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetDpInterfaces)
  })
_sym_db.RegisterMessage(SetDpInterfaces)

SetDpInterfacesRequest = _reflection.GeneratedProtocolMessageType('SetDpInterfacesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETDPINTERFACESREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetDpInterfacesRequest)
  })
_sym_db.RegisterMessage(SetDpInterfacesRequest)

SetDpInterfacesReply = _reflection.GeneratedProtocolMessageType('SetDpInterfacesReply', (_message.Message,), {
  'DESCRIPTOR' : _SETDPINTERFACESREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetDpInterfacesReply)
  })
_sym_db.RegisterMessage(SetDpInterfacesReply)

GetDpInfoRequest = _reflection.GeneratedProtocolMessageType('GetDpInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDPINFOREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetDpInfoRequest)
  })
_sym_db.RegisterMessage(GetDpInfoRequest)

InterfaceInfo = _reflection.GeneratedProtocolMessageType('InterfaceInfo', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACEINFO,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.InterfaceInfo)
  })
_sym_db.RegisterMessage(InterfaceInfo)

DpInfo = _reflection.GeneratedProtocolMessageType('DpInfo', (_message.Message,), {
  'DESCRIPTOR' : _DPINFO,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.DpInfo)
  })
_sym_db.RegisterMessage(DpInfo)

GetDpInfoReply = _reflection.GeneratedProtocolMessageType('GetDpInfoReply', (_message.Message,), {
  'DESCRIPTOR' : _GETDPINFOREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetDpInfoReply)
  })
_sym_db.RegisterMessage(GetDpInfoReply)

DelDpInterfacesRequest = _reflection.GeneratedProtocolMessageType('DelDpInterfacesRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELDPINTERFACESREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.DelDpInterfacesRequest)
  })
_sym_db.RegisterMessage(DelDpInterfacesRequest)

DelDpInterfacesReply = _reflection.GeneratedProtocolMessageType('DelDpInterfacesReply', (_message.Message,), {
  'DESCRIPTOR' : _DELDPINTERFACESREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.DelDpInterfacesReply)
  })
_sym_db.RegisterMessage(DelDpInterfacesReply)

DelDpsRequest = _reflection.GeneratedProtocolMessageType('DelDpsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELDPSREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.DelDpsRequest)
  })
_sym_db.RegisterMessage(DelDpsRequest)

DelDpsReply = _reflection.GeneratedProtocolMessageType('DelDpsReply', (_message.Message,), {
  'DESCRIPTOR' : _DELDPSREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.DelDpsReply)
  })
_sym_db.RegisterMessage(DelDpsReply)

GetDpNamesRequest = _reflection.GeneratedProtocolMessageType('GetDpNamesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDPNAMESREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetDpNamesRequest)
  })
_sym_db.RegisterMessage(GetDpNamesRequest)

GetDpNamesReply = _reflection.GeneratedProtocolMessageType('GetDpNamesReply', (_message.Message,), {
  'DESCRIPTOR' : _GETDPNAMESREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetDpNamesReply)
  })
_sym_db.RegisterMessage(GetDpNamesReply)

GetDpIDsRequest = _reflection.GeneratedProtocolMessageType('GetDpIDsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDPIDSREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetDpIDsRequest)
  })
_sym_db.RegisterMessage(GetDpIDsRequest)

GetDpIDsReply = _reflection.GeneratedProtocolMessageType('GetDpIDsReply', (_message.Message,), {
  'DESCRIPTOR' : _GETDPIDSREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetDpIDsReply)
  })
_sym_db.RegisterMessage(GetDpIDsReply)

GetAclNamesRequest = _reflection.GeneratedProtocolMessageType('GetAclNamesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACLNAMESREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetAclNamesRequest)
  })
_sym_db.RegisterMessage(GetAclNamesRequest)

GetAclNamesReply = _reflection.GeneratedProtocolMessageType('GetAclNamesReply', (_message.Message,), {
  'DESCRIPTOR' : _GETACLNAMESREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.GetAclNamesReply)
  })
_sym_db.RegisterMessage(GetAclNamesReply)

SetDp = _reflection.GeneratedProtocolMessageType('SetDp', (_message.Message,), {
  'DESCRIPTOR' : _SETDP,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetDp)
  })
_sym_db.RegisterMessage(SetDp)

SetDpsRequest = _reflection.GeneratedProtocolMessageType('SetDpsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETDPSREQUEST,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetDpsRequest)
  })
_sym_db.RegisterMessage(SetDpsRequest)

SetDpsReply = _reflection.GeneratedProtocolMessageType('SetDpsReply', (_message.Message,), {
  'DESCRIPTOR' : _SETDPSREPLY,
  '__module__' : 'faucetconfrpc.faucetconfrpc_pb2'
  # @@protoc_insertion_point(class_scope:faucetconfserver.SetDpsReply)
  })
_sym_db.RegisterMessage(SetDpsReply)

_FAUCETCONFSERVER = DESCRIPTOR.services_by_name['FaucetConfServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\021faucetconfserver/'
  _GETCONFIGFILEREQUEST._serialized_start=55
  _GETCONFIGFILEREQUEST._serialized_end=102
  _GETCONFIGFILEREPLY._serialized_start=104
  _GETCONFIGFILEREPLY._serialized_end=145
  _SETCONFIGFILEREQUEST._serialized_start=147
  _SETCONFIGFILEREQUEST._serialized_end=260
  _SETCONFIGFILEREPLY._serialized_start=262
  _SETCONFIGFILEREPLY._serialized_end=282
  _DELCONFIGFROMFILEREQUEST._serialized_start=284
  _DELCONFIGFROMFILEREQUEST._serialized_end=361
  _DELCONFIGFROMFILEREPLY._serialized_start=363
  _DELCONFIGFROMFILEREPLY._serialized_end=387
  _SETREMOTEMIRRORPORTREQUEST._serialized_start=390
  _SETREMOTEMIRRORPORTREQUEST._serialized_end=520
  _SETREMOTEMIRRORPORTREPLY._serialized_start=522
  _SETREMOTEMIRRORPORTREPLY._serialized_end=548
  _ADDPORTMIRRORREQUEST._serialized_start=550
  _ADDPORTMIRRORREQUEST._serialized_end=630
  _ADDPORTMIRRORREPLY._serialized_start=632
  _ADDPORTMIRRORREPLY._serialized_end=652
  _MAKECOPROCESSORPORTREQUEST._serialized_start=654
  _MAKECOPROCESSORPORTREQUEST._serialized_end=755
  _MAKECOPROCESSORPORTREPLY._serialized_start=757
  _MAKECOPROCESSORPORTREPLY._serialized_end=783
  _REMOVEPORTMIRRORREQUEST._serialized_start=785
  _REMOVEPORTMIRRORREQUEST._serialized_end=868
  _REMOVEPORTMIRRORREPLY._serialized_start=870
  _REMOVEPORTMIRRORREPLY._serialized_end=893
  _CLEARPORTMIRRORREQUEST._serialized_start=895
  _CLEARPORTMIRRORREQUEST._serialized_end=960
  _CLEARPORTMIRRORREPLY._serialized_start=962
  _CLEARPORTMIRRORREPLY._serialized_end=984
  _SETVLANOUTACLREQUEST._serialized_start=986
  _SETVLANOUTACLREQUEST._serialized_end=1044
  _SETVLANOUTACLREPLY._serialized_start=1046
  _SETVLANOUTACLREPLY._serialized_end=1066
  _SETPORTACLREQUEST._serialized_start=1068
  _SETPORTACLREQUEST._serialized_end=1135
  _SETPORTACLREPLY._serialized_start=1137
  _SETPORTACLREPLY._serialized_end=1154
  _ADDPORTACLREQUEST._serialized_start=1156
  _ADDPORTACLREQUEST._serialized_end=1222
  _ADDPORTACLREPLY._serialized_start=1224
  _ADDPORTACLREPLY._serialized_end=1241
  _REMOVEPORTACLREQUEST._serialized_start=1243
  _REMOVEPORTACLREQUEST._serialized_end=1312
  _REMOVEPORTACLREPLY._serialized_start=1314
  _REMOVEPORTACLREPLY._serialized_end=1334
  _SETINTERFACE._serialized_start=1336
  _SETINTERFACE._serialized_end=1388
  _SETDPINTERFACES._serialized_start=1390
  _SETDPINTERFACES._serialized_end=1482
  _SETDPINTERFACESREQUEST._serialized_start=1484
  _SETDPINTERFACESREQUEST._serialized_end=1570
  _SETDPINTERFACESREPLY._serialized_start=1572
  _SETDPINTERFACESREPLY._serialized_end=1594
  _GETDPINFOREQUEST._serialized_start=1596
  _GETDPINFOREQUEST._serialized_end=1656
  _INTERFACEINFO._serialized_start=1658
  _INTERFACEINFO._serialized_end=1725
  _DPINFO._serialized_start=1727
  _DPINFO._serialized_end=1838
  _GETDPINFOREPLY._serialized_start=1840
  _GETDPINFOREPLY._serialized_end=1895
  _DELDPINTERFACESREQUEST._serialized_start=1897
  _DELDPINTERFACESREQUEST._serialized_end=1999
  _DELDPINTERFACESREPLY._serialized_start=2001
  _DELDPINTERFACESREPLY._serialized_end=2023
  _DELDPSREQUEST._serialized_start=2025
  _DELDPSREQUEST._serialized_end=2093
  _DELDPSREPLY._serialized_start=2095
  _DELDPSREPLY._serialized_end=2108
  _GETDPNAMESREQUEST._serialized_start=2110
  _GETDPNAMESREQUEST._serialized_end=2129
  _GETDPNAMESREPLY._serialized_start=2131
  _GETDPNAMESREPLY._serialized_end=2165
  _GETDPIDSREQUEST._serialized_start=2167
  _GETDPIDSREQUEST._serialized_end=2184
  _GETDPIDSREPLY._serialized_start=2186
  _GETDPIDSREPLY._serialized_end=2216
  _GETACLNAMESREQUEST._serialized_start=2218
  _GETACLNAMESREQUEST._serialized_end=2256
  _GETACLNAMESREPLY._serialized_start=2258
  _GETACLNAMESREPLY._serialized_end=2294
  _SETDP._serialized_start=2296
  _SETDP._serialized_end=2341
  _SETDPSREQUEST._serialized_start=2343
  _SETDPSREQUEST._serialized_end=2402
  _SETDPSREPLY._serialized_start=2404
  _SETDPSREPLY._serialized_end=2417
  _FAUCETCONFSERVER._serialized_start=2420
  _FAUCETCONFSERVER._serialized_end=4351
# @@protoc_insertion_point(module_scope)
