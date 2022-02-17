# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: param_server/param_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='param_server/param_server.proto',
  package='mavsdk.rpc.param_server',
  syntax='proto3',
  serialized_options=b'\n\026io.mavsdk.param_serverB\020ParamServerProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fparam_server/param_server.proto\x12\x17mavsdk.rpc.param_server\x1a\x14mavsdk_options.proto\"\'\n\x17RetrieveParamIntRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"r\n\x18RetrieveParamIntResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\x12\r\n\x05value\x18\x02 \x01(\x05\"5\n\x16ProvideParamIntRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"b\n\x17ProvideParamIntResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\")\n\x19RetrieveParamFloatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"t\n\x1aRetrieveParamFloatResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\x12\r\n\x05value\x18\x02 \x01(\x02\"7\n\x18ProvideParamFloatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"d\n\x19ProvideParamFloatResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\"\x1a\n\x18RetrieveAllParamsRequest\"O\n\x19RetrieveAllParamsResponse\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\".mavsdk.rpc.param_server.AllParams\"\'\n\x08IntParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\")\n\nFloatParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"}\n\tAllParams\x12\x35\n\nint_params\x18\x01 \x03(\x0b\x32!.mavsdk.rpc.param_server.IntParam\x12\x39\n\x0c\x66loat_params\x18\x02 \x03(\x0b\x32#.mavsdk.rpc.param_server.FloatParam\"\x80\x02\n\x11ParamServerResult\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.mavsdk.rpc.param_server.ParamServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x93\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NOT_FOUND\x10\x02\x12\x15\n\x11RESULT_WRONG_TYPE\x10\x03\x12\x1e\n\x1aRESULT_PARAM_NAME_TOO_LONG\x10\x04\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x05\x32\x9b\x05\n\x12ParamServerService\x12}\n\x10RetrieveParamInt\x12\x30.mavsdk.rpc.param_server.RetrieveParamIntRequest\x1a\x31.mavsdk.rpc.param_server.RetrieveParamIntResponse\"\x04\x80\xb5\x18\x01\x12z\n\x0fProvideParamInt\x12/.mavsdk.rpc.param_server.ProvideParamIntRequest\x1a\x30.mavsdk.rpc.param_server.ProvideParamIntResponse\"\x04\x80\xb5\x18\x01\x12\x83\x01\n\x12RetrieveParamFloat\x12\x32.mavsdk.rpc.param_server.RetrieveParamFloatRequest\x1a\x33.mavsdk.rpc.param_server.RetrieveParamFloatResponse\"\x04\x80\xb5\x18\x01\x12\x80\x01\n\x11ProvideParamFloat\x12\x31.mavsdk.rpc.param_server.ProvideParamFloatRequest\x1a\x32.mavsdk.rpc.param_server.ProvideParamFloatResponse\"\x04\x80\xb5\x18\x01\x12\x80\x01\n\x11RetrieveAllParams\x12\x31.mavsdk.rpc.param_server.RetrieveAllParamsRequest\x1a\x32.mavsdk.rpc.param_server.RetrieveAllParamsResponse\"\x04\x80\xb5\x18\x01\x42*\n\x16io.mavsdk.param_serverB\x10ParamServerProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])



_PARAMSERVERRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.param_server.ParamServerResult.Result',
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
      name='RESULT_NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_WRONG_TYPE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_PARAM_NAME_TOO_LONG', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_SYSTEM', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1144,
  serialized_end=1291,
)
_sym_db.RegisterEnumDescriptor(_PARAMSERVERRESULT_RESULT)


_RETRIEVEPARAMINTREQUEST = _descriptor.Descriptor(
  name='RetrieveParamIntRequest',
  full_name='mavsdk.rpc.param_server.RetrieveParamIntRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mavsdk.rpc.param_server.RetrieveParamIntRequest.name', index=0,
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
  serialized_start=82,
  serialized_end=121,
)


_RETRIEVEPARAMINTRESPONSE = _descriptor.Descriptor(
  name='RetrieveParamIntResponse',
  full_name='mavsdk.rpc.param_server.RetrieveParamIntResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_server_result', full_name='mavsdk.rpc.param_server.RetrieveParamIntResponse.param_server_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mavsdk.rpc.param_server.RetrieveParamIntResponse.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=123,
  serialized_end=237,
)


_PROVIDEPARAMINTREQUEST = _descriptor.Descriptor(
  name='ProvideParamIntRequest',
  full_name='mavsdk.rpc.param_server.ProvideParamIntRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mavsdk.rpc.param_server.ProvideParamIntRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mavsdk.rpc.param_server.ProvideParamIntRequest.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=239,
  serialized_end=292,
)


_PROVIDEPARAMINTRESPONSE = _descriptor.Descriptor(
  name='ProvideParamIntResponse',
  full_name='mavsdk.rpc.param_server.ProvideParamIntResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_server_result', full_name='mavsdk.rpc.param_server.ProvideParamIntResponse.param_server_result', index=0,
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
  serialized_start=294,
  serialized_end=392,
)


_RETRIEVEPARAMFLOATREQUEST = _descriptor.Descriptor(
  name='RetrieveParamFloatRequest',
  full_name='mavsdk.rpc.param_server.RetrieveParamFloatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mavsdk.rpc.param_server.RetrieveParamFloatRequest.name', index=0,
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
  serialized_start=394,
  serialized_end=435,
)


_RETRIEVEPARAMFLOATRESPONSE = _descriptor.Descriptor(
  name='RetrieveParamFloatResponse',
  full_name='mavsdk.rpc.param_server.RetrieveParamFloatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_server_result', full_name='mavsdk.rpc.param_server.RetrieveParamFloatResponse.param_server_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mavsdk.rpc.param_server.RetrieveParamFloatResponse.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=437,
  serialized_end=553,
)


_PROVIDEPARAMFLOATREQUEST = _descriptor.Descriptor(
  name='ProvideParamFloatRequest',
  full_name='mavsdk.rpc.param_server.ProvideParamFloatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mavsdk.rpc.param_server.ProvideParamFloatRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mavsdk.rpc.param_server.ProvideParamFloatRequest.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=555,
  serialized_end=610,
)


_PROVIDEPARAMFLOATRESPONSE = _descriptor.Descriptor(
  name='ProvideParamFloatResponse',
  full_name='mavsdk.rpc.param_server.ProvideParamFloatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_server_result', full_name='mavsdk.rpc.param_server.ProvideParamFloatResponse.param_server_result', index=0,
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
  serialized_start=612,
  serialized_end=712,
)


_RETRIEVEALLPARAMSREQUEST = _descriptor.Descriptor(
  name='RetrieveAllParamsRequest',
  full_name='mavsdk.rpc.param_server.RetrieveAllParamsRequest',
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
  serialized_start=714,
  serialized_end=740,
)


_RETRIEVEALLPARAMSRESPONSE = _descriptor.Descriptor(
  name='RetrieveAllParamsResponse',
  full_name='mavsdk.rpc.param_server.RetrieveAllParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='mavsdk.rpc.param_server.RetrieveAllParamsResponse.params', index=0,
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
  serialized_start=742,
  serialized_end=821,
)


_INTPARAM = _descriptor.Descriptor(
  name='IntParam',
  full_name='mavsdk.rpc.param_server.IntParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mavsdk.rpc.param_server.IntParam.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mavsdk.rpc.param_server.IntParam.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=823,
  serialized_end=862,
)


_FLOATPARAM = _descriptor.Descriptor(
  name='FloatParam',
  full_name='mavsdk.rpc.param_server.FloatParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mavsdk.rpc.param_server.FloatParam.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mavsdk.rpc.param_server.FloatParam.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=864,
  serialized_end=905,
)


_ALLPARAMS = _descriptor.Descriptor(
  name='AllParams',
  full_name='mavsdk.rpc.param_server.AllParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_params', full_name='mavsdk.rpc.param_server.AllParams.int_params', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_params', full_name='mavsdk.rpc.param_server.AllParams.float_params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=907,
  serialized_end=1032,
)


_PARAMSERVERRESULT = _descriptor.Descriptor(
  name='ParamServerResult',
  full_name='mavsdk.rpc.param_server.ParamServerResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.param_server.ParamServerResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.param_server.ParamServerResult.result_str', index=1,
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
    _PARAMSERVERRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1035,
  serialized_end=1291,
)

_RETRIEVEPARAMINTRESPONSE.fields_by_name['param_server_result'].message_type = _PARAMSERVERRESULT
_PROVIDEPARAMINTRESPONSE.fields_by_name['param_server_result'].message_type = _PARAMSERVERRESULT
_RETRIEVEPARAMFLOATRESPONSE.fields_by_name['param_server_result'].message_type = _PARAMSERVERRESULT
_PROVIDEPARAMFLOATRESPONSE.fields_by_name['param_server_result'].message_type = _PARAMSERVERRESULT
_RETRIEVEALLPARAMSRESPONSE.fields_by_name['params'].message_type = _ALLPARAMS
_ALLPARAMS.fields_by_name['int_params'].message_type = _INTPARAM
_ALLPARAMS.fields_by_name['float_params'].message_type = _FLOATPARAM
_PARAMSERVERRESULT.fields_by_name['result'].enum_type = _PARAMSERVERRESULT_RESULT
_PARAMSERVERRESULT_RESULT.containing_type = _PARAMSERVERRESULT
DESCRIPTOR.message_types_by_name['RetrieveParamIntRequest'] = _RETRIEVEPARAMINTREQUEST
DESCRIPTOR.message_types_by_name['RetrieveParamIntResponse'] = _RETRIEVEPARAMINTRESPONSE
DESCRIPTOR.message_types_by_name['ProvideParamIntRequest'] = _PROVIDEPARAMINTREQUEST
DESCRIPTOR.message_types_by_name['ProvideParamIntResponse'] = _PROVIDEPARAMINTRESPONSE
DESCRIPTOR.message_types_by_name['RetrieveParamFloatRequest'] = _RETRIEVEPARAMFLOATREQUEST
DESCRIPTOR.message_types_by_name['RetrieveParamFloatResponse'] = _RETRIEVEPARAMFLOATRESPONSE
DESCRIPTOR.message_types_by_name['ProvideParamFloatRequest'] = _PROVIDEPARAMFLOATREQUEST
DESCRIPTOR.message_types_by_name['ProvideParamFloatResponse'] = _PROVIDEPARAMFLOATRESPONSE
DESCRIPTOR.message_types_by_name['RetrieveAllParamsRequest'] = _RETRIEVEALLPARAMSREQUEST
DESCRIPTOR.message_types_by_name['RetrieveAllParamsResponse'] = _RETRIEVEALLPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['IntParam'] = _INTPARAM
DESCRIPTOR.message_types_by_name['FloatParam'] = _FLOATPARAM
DESCRIPTOR.message_types_by_name['AllParams'] = _ALLPARAMS
DESCRIPTOR.message_types_by_name['ParamServerResult'] = _PARAMSERVERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RetrieveParamIntRequest = _reflection.GeneratedProtocolMessageType('RetrieveParamIntRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMINTREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamIntRequest)
  })
_sym_db.RegisterMessage(RetrieveParamIntRequest)

RetrieveParamIntResponse = _reflection.GeneratedProtocolMessageType('RetrieveParamIntResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMINTRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamIntResponse)
  })
_sym_db.RegisterMessage(RetrieveParamIntResponse)

ProvideParamIntRequest = _reflection.GeneratedProtocolMessageType('ProvideParamIntRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMINTREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamIntRequest)
  })
_sym_db.RegisterMessage(ProvideParamIntRequest)

ProvideParamIntResponse = _reflection.GeneratedProtocolMessageType('ProvideParamIntResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMINTRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamIntResponse)
  })
_sym_db.RegisterMessage(ProvideParamIntResponse)

RetrieveParamFloatRequest = _reflection.GeneratedProtocolMessageType('RetrieveParamFloatRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMFLOATREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamFloatRequest)
  })
_sym_db.RegisterMessage(RetrieveParamFloatRequest)

RetrieveParamFloatResponse = _reflection.GeneratedProtocolMessageType('RetrieveParamFloatResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMFLOATRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamFloatResponse)
  })
_sym_db.RegisterMessage(RetrieveParamFloatResponse)

ProvideParamFloatRequest = _reflection.GeneratedProtocolMessageType('ProvideParamFloatRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMFLOATREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamFloatRequest)
  })
_sym_db.RegisterMessage(ProvideParamFloatRequest)

ProvideParamFloatResponse = _reflection.GeneratedProtocolMessageType('ProvideParamFloatResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMFLOATRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamFloatResponse)
  })
_sym_db.RegisterMessage(ProvideParamFloatResponse)

RetrieveAllParamsRequest = _reflection.GeneratedProtocolMessageType('RetrieveAllParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEALLPARAMSREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveAllParamsRequest)
  })
_sym_db.RegisterMessage(RetrieveAllParamsRequest)

RetrieveAllParamsResponse = _reflection.GeneratedProtocolMessageType('RetrieveAllParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEALLPARAMSRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveAllParamsResponse)
  })
_sym_db.RegisterMessage(RetrieveAllParamsResponse)

IntParam = _reflection.GeneratedProtocolMessageType('IntParam', (_message.Message,), {
  'DESCRIPTOR' : _INTPARAM,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.IntParam)
  })
_sym_db.RegisterMessage(IntParam)

FloatParam = _reflection.GeneratedProtocolMessageType('FloatParam', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAM,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.FloatParam)
  })
_sym_db.RegisterMessage(FloatParam)

AllParams = _reflection.GeneratedProtocolMessageType('AllParams', (_message.Message,), {
  'DESCRIPTOR' : _ALLPARAMS,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.AllParams)
  })
_sym_db.RegisterMessage(AllParams)

ParamServerResult = _reflection.GeneratedProtocolMessageType('ParamServerResult', (_message.Message,), {
  'DESCRIPTOR' : _PARAMSERVERRESULT,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ParamServerResult)
  })
_sym_db.RegisterMessage(ParamServerResult)


DESCRIPTOR._options = None

_PARAMSERVERSERVICE = _descriptor.ServiceDescriptor(
  name='ParamServerService',
  full_name='mavsdk.rpc.param_server.ParamServerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1294,
  serialized_end=1961,
  methods=[
  _descriptor.MethodDescriptor(
    name='RetrieveParamInt',
    full_name='mavsdk.rpc.param_server.ParamServerService.RetrieveParamInt',
    index=0,
    containing_service=None,
    input_type=_RETRIEVEPARAMINTREQUEST,
    output_type=_RETRIEVEPARAMINTRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ProvideParamInt',
    full_name='mavsdk.rpc.param_server.ParamServerService.ProvideParamInt',
    index=1,
    containing_service=None,
    input_type=_PROVIDEPARAMINTREQUEST,
    output_type=_PROVIDEPARAMINTRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RetrieveParamFloat',
    full_name='mavsdk.rpc.param_server.ParamServerService.RetrieveParamFloat',
    index=2,
    containing_service=None,
    input_type=_RETRIEVEPARAMFLOATREQUEST,
    output_type=_RETRIEVEPARAMFLOATRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ProvideParamFloat',
    full_name='mavsdk.rpc.param_server.ParamServerService.ProvideParamFloat',
    index=3,
    containing_service=None,
    input_type=_PROVIDEPARAMFLOATREQUEST,
    output_type=_PROVIDEPARAMFLOATRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RetrieveAllParams',
    full_name='mavsdk.rpc.param_server.ParamServerService.RetrieveAllParams',
    index=4,
    containing_service=None,
    input_type=_RETRIEVEALLPARAMSREQUEST,
    output_type=_RETRIEVEALLPARAMSRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PARAMSERVERSERVICE)

DESCRIPTOR.services_by_name['ParamServerService'] = _PARAMSERVERSERVICE

# @@protoc_insertion_point(module_scope)
