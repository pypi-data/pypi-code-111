# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event/Event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event/Event.proto',
  package='skywalking.v3',
  syntax='proto3',
  serialized_options=b'\n*org.apache.skywalking.apm.network.event.v3P\001Z1skywalking.apache.org/repo/goapi/collect/event/v3\252\002\035SkyWalking.NetworkProtocol.V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x65vent/Event.proto\x12\rskywalking.v3\x1a\x13\x63ommon/Common.proto\"\x8f\x02\n\x05\x45vent\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12%\n\x06source\x18\x02 \x01(\x0b\x32\x15.skywalking.v3.Source\x12\x0c\n\x04name\x18\x03 \x01(\t\x12!\n\x04type\x18\x04 \x01(\x0e\x32\x13.skywalking.v3.Type\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x38\n\nparameters\x18\x06 \x03(\x0b\x32$.skywalking.v3.Event.ParametersEntry\x12\x11\n\tstartTime\x18\x07 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x08 \x01(\x03\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"D\n\x06Source\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x02 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x03 \x01(\t*\x1d\n\x04Type\x12\n\n\x06Normal\x10\x00\x12\t\n\x05\x45rror\x10\x01\x32L\n\x0c\x45ventService\x12<\n\x07\x63ollect\x12\x14.skywalking.v3.Event\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x42\x81\x01\n*org.apache.skywalking.apm.network.event.v3P\x01Z1skywalking.apache.org/repo/goapi/collect/event/v3\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,])

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='skywalking.v3.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Normal', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Error', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=401,
  serialized_end=430,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
Normal = 0
Error = 1



_EVENT_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='skywalking.v3.Event.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='skywalking.v3.Event.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='skywalking.v3.Event.ParametersEntry.value', index=1,
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
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=329,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='skywalking.v3.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='skywalking.v3.Event.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='skywalking.v3.Event.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='skywalking.v3.Event.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='skywalking.v3.Event.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='skywalking.v3.Event.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='skywalking.v3.Event.parameters', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='skywalking.v3.Event.startTime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='skywalking.v3.Event.endTime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_PARAMETERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=329,
)


_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='skywalking.v3.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='skywalking.v3.Source.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceInstance', full_name='skywalking.v3.Source.serviceInstance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='skywalking.v3.Source.endpoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=331,
  serialized_end=399,
)

_EVENT_PARAMETERSENTRY.containing_type = _EVENT
_EVENT.fields_by_name['source'].message_type = _SOURCE
_EVENT.fields_by_name['type'].enum_type = _TYPE
_EVENT.fields_by_name['parameters'].message_type = _EVENT_PARAMETERSENTRY
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_PARAMETERSENTRY,
    '__module__' : 'event.Event_pb2'
    # @@protoc_insertion_point(class_scope:skywalking.v3.Event.ParametersEntry)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'event.Event_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.ParametersEntry)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'event.Event_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.Source)
  })
_sym_db.RegisterMessage(Source)


DESCRIPTOR._options = None
_EVENT_PARAMETERSENTRY._options = None

_EVENTSERVICE = _descriptor.ServiceDescriptor(
  name='EventService',
  full_name='skywalking.v3.EventService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=432,
  serialized_end=508,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='skywalking.v3.EventService.collect',
    index=0,
    containing_service=None,
    input_type=_EVENT,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTSERVICE)

DESCRIPTOR.services_by_name['EventService'] = _EVENTSERVICE

# @@protoc_insertion_point(module_scope)
