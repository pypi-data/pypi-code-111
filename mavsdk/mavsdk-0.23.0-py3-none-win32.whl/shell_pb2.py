# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shell/shell.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='shell/shell.proto',
  package='mavsdk.rpc.shell',
  syntax='proto3',
  serialized_options=b'\n\017io.mavsdk.shellB\nShellProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11shell/shell.proto\x12\x10mavsdk.rpc.shell\x1a\x14mavsdk_options.proto\"\x1e\n\x0bSendRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\"C\n\x0cSendResponse\x12\x33\n\x0cshell_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.shell.ShellResult\"\x19\n\x17SubscribeReceiveRequest\"\x1f\n\x0fReceiveResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\xe6\x01\n\x0bShellResult\x12\x34\n\x06result\x18\x01 \x01(\x0e\x32$.mavsdk.rpc.shell.ShellResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x8c\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x16\n\x12RESULT_NO_RESPONSE\x10\x04\x12\x0f\n\x0bRESULT_BUSY\x10\x05\x32\xc5\x01\n\x0cShellService\x12K\n\x04Send\x12\x1d.mavsdk.rpc.shell.SendRequest\x1a\x1e.mavsdk.rpc.shell.SendResponse\"\x04\x80\xb5\x18\x01\x12h\n\x10SubscribeReceive\x12).mavsdk.rpc.shell.SubscribeReceiveRequest\x1a!.mavsdk.rpc.shell.ReceiveResponse\"\x04\x80\xb5\x18\x00\x30\x01\x42\x1d\n\x0fio.mavsdk.shellB\nShellProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])



_SHELLRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.shell.ShellResult.Result',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_SYSTEM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_CONNECTION_ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_RESPONSE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_BUSY', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=313,
  serialized_end=453,
)
_sym_db.RegisterEnumDescriptor(_SHELLRESULT_RESULT)


_SENDREQUEST = _descriptor.Descriptor(
  name='SendRequest',
  full_name='mavsdk.rpc.shell.SendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='mavsdk.rpc.shell.SendRequest.command', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=91,
)


_SENDRESPONSE = _descriptor.Descriptor(
  name='SendResponse',
  full_name='mavsdk.rpc.shell.SendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shell_result', full_name='mavsdk.rpc.shell.SendResponse.shell_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=160,
)


_SUBSCRIBERECEIVEREQUEST = _descriptor.Descriptor(
  name='SubscribeReceiveRequest',
  full_name='mavsdk.rpc.shell.SubscribeReceiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=187,
)


_RECEIVERESPONSE = _descriptor.Descriptor(
  name='ReceiveResponse',
  full_name='mavsdk.rpc.shell.ReceiveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='mavsdk.rpc.shell.ReceiveResponse.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=220,
)


_SHELLRESULT = _descriptor.Descriptor(
  name='ShellResult',
  full_name='mavsdk.rpc.shell.ShellResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.shell.ShellResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.shell.ShellResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHELLRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=453,
)

_SENDRESPONSE.fields_by_name['shell_result'].message_type = _SHELLRESULT
_SHELLRESULT.fields_by_name['result'].enum_type = _SHELLRESULT_RESULT
_SHELLRESULT_RESULT.containing_type = _SHELLRESULT
DESCRIPTOR.message_types_by_name['SendRequest'] = _SENDREQUEST
DESCRIPTOR.message_types_by_name['SendResponse'] = _SENDRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeReceiveRequest'] = _SUBSCRIBERECEIVEREQUEST
DESCRIPTOR.message_types_by_name['ReceiveResponse'] = _RECEIVERESPONSE
DESCRIPTOR.message_types_by_name['ShellResult'] = _SHELLRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendRequest = _reflection.GeneratedProtocolMessageType('SendRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDREQUEST,
  '__module__' : 'shell.shell_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.shell.SendRequest)
  })
_sym_db.RegisterMessage(SendRequest)

SendResponse = _reflection.GeneratedProtocolMessageType('SendResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDRESPONSE,
  '__module__' : 'shell.shell_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.shell.SendResponse)
  })
_sym_db.RegisterMessage(SendResponse)

SubscribeReceiveRequest = _reflection.GeneratedProtocolMessageType('SubscribeReceiveRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBERECEIVEREQUEST,
  '__module__' : 'shell.shell_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.shell.SubscribeReceiveRequest)
  })
_sym_db.RegisterMessage(SubscribeReceiveRequest)

ReceiveResponse = _reflection.GeneratedProtocolMessageType('ReceiveResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVERESPONSE,
  '__module__' : 'shell.shell_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.shell.ReceiveResponse)
  })
_sym_db.RegisterMessage(ReceiveResponse)

ShellResult = _reflection.GeneratedProtocolMessageType('ShellResult', (_message.Message,), {
  'DESCRIPTOR' : _SHELLRESULT,
  '__module__' : 'shell.shell_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.shell.ShellResult)
  })
_sym_db.RegisterMessage(ShellResult)


DESCRIPTOR._options = None

_SHELLSERVICE = _descriptor.ServiceDescriptor(
  name='ShellService',
  full_name='mavsdk.rpc.shell.ShellService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=456,
  serialized_end=653,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='mavsdk.rpc.shell.ShellService.Send',
    index=0,
    containing_service=None,
    input_type=_SENDREQUEST,
    output_type=_SENDRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeReceive',
    full_name='mavsdk.rpc.shell.ShellService.SubscribeReceive',
    index=1,
    containing_service=None,
    input_type=_SUBSCRIBERECEIVEREQUEST,
    output_type=_RECEIVERESPONSE,
    serialized_options=b'\200\265\030\000',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHELLSERVICE)

DESCRIPTOR.services_by_name['ShellService'] = _SHELLSERVICE

# @@protoc_insertion_point(module_scope)
