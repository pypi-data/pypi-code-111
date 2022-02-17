# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/entity/v1/entity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='github.com/metaprov/modelaapi/services/entity/v1/entity.proto',
  package='github.com.metaprov.modelaapi.services.entity.v1',
  syntax='proto3',
  serialized_options=b'Z0github.com/metaprov/modelaapi/services/entity/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=github.com/metaprov/modelaapi/services/entity/v1/entity.proto\x12\x30github.com.metaprov.modelaapi.services.entity.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/data/v1alpha1/generated.proto\"\xf3\x01\n\x13ListEntitiesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x61\n\x06labels\x18\x02 \x03(\x0b\x32Q.github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x83\x01\n\x14ListEntitiesResponse\x12R\n\x08\x65ntities\x18\x01 \x01(\x0b\x32@.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.EntityList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"c\n\x13\x43reateEntityRequest\x12L\n\x06\x65ntity\x18\x01 \x01(\x0b\x32<.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Entity\"\x16\n\x14\x43reateEntityResponse\"\x93\x01\n\x13UpdateEntityRequest\x12L\n\x06\x65ntity\x18\x01 \x01(\x0b\x32<.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Entity\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x16\n\x14UpdateEntityResponse\"c\n\x10GetEntityRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"o\n\x11GetEntityResponse\x12L\n\x06\x65ntity\x18\x01 \x01(\x0b\x32<.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Entity\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"6\n\x13\x44\x65leteEntityRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x16\n\x14\x44\x65leteEntityResponse2\xf3\x07\n\rEntityService\x12\xbf\x01\n\x0cListEntities\x12\x45.github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest\x1a\x46.github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/entities/{namespace}\x12\xb6\x01\n\x0c\x43reateEntity\x12\x45.github.com.metaprov.modelaapi.services.entity.v1.CreateEntityRequest\x1a\x46.github.com.metaprov.modelaapi.services.entity.v1.CreateEntityResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/entities:\x01*\x12\xb1\x01\n\tGetEntity\x12\x42.github.com.metaprov.modelaapi.services.entity.v1.GetEntityRequest\x1a\x43.github.com.metaprov.modelaapi.services.entity.v1.GetEntityResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/entities/{name}\x12\xe9\x01\n\x0cUpdateEntity\x12\x45.github.com.metaprov.modelaapi.services.entity.v1.UpdateEntityRequest\x1a\x46.github.com.metaprov.modelaapi.services.entity.v1.UpdateEntityResponse\"J\x82\xd3\xe4\x93\x02\x44\x1a?/v1/entities/{entity.metadata.namespace}/{entity.metadata.name}:\x01*\x12\xc6\x01\n\x0c\x44\x65leteEntity\x12\x45.github.com.metaprov.modelaapi.services.entity.v1.DeleteEntityRequest\x1a\x46.github.com.metaprov.modelaapi.services.entity.v1.DeleteEntityResponse\"\'\x82\xd3\xe4\x93\x02!*\x1f/v1/entities/{namespace}/{name}B2Z0github.com/metaprov/modelaapi/services/entity/v1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2.DESCRIPTOR,])




_LISTENTITIESREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.LabelsEntry.value', index=1,
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
  serialized_start=448,
  serialized_end=493,
)

_LISTENTITIESREQUEST = _descriptor.Descriptor(
  name='ListEntitiesRequest',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.order_by', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LISTENTITIESREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=493,
)


_LISTENTITIESRESPONSE = _descriptor.Descriptor(
  name='ListEntitiesResponse',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesResponse.entities', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesResponse.next_page_token', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=496,
  serialized_end=627,
)


_CREATEENTITYREQUEST = _descriptor.Descriptor(
  name='CreateEntityRequest',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.CreateEntityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='github.com.metaprov.modelaapi.services.entity.v1.CreateEntityRequest.entity', index=0,
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
  serialized_start=629,
  serialized_end=728,
)


_CREATEENTITYRESPONSE = _descriptor.Descriptor(
  name='CreateEntityResponse',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.CreateEntityResponse',
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
  serialized_start=730,
  serialized_end=752,
)


_UPDATEENTITYREQUEST = _descriptor.Descriptor(
  name='UpdateEntityRequest',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.UpdateEntityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='github.com.metaprov.modelaapi.services.entity.v1.UpdateEntityRequest.entity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_mask', full_name='github.com.metaprov.modelaapi.services.entity.v1.UpdateEntityRequest.field_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=755,
  serialized_end=902,
)


_UPDATEENTITYRESPONSE = _descriptor.Descriptor(
  name='UpdateEntityResponse',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.UpdateEntityResponse',
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
  serialized_start=904,
  serialized_end=926,
)


_GETENTITYREQUEST = _descriptor.Descriptor(
  name='GetEntityRequest',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.GetEntityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.entity.v1.GetEntityRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.entity.v1.GetEntityRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_mask', full_name='github.com.metaprov.modelaapi.services.entity.v1.GetEntityRequest.field_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=928,
  serialized_end=1027,
)


_GETENTITYRESPONSE = _descriptor.Descriptor(
  name='GetEntityResponse',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.GetEntityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='github.com.metaprov.modelaapi.services.entity.v1.GetEntityResponse.entity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaml', full_name='github.com.metaprov.modelaapi.services.entity.v1.GetEntityResponse.yaml', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1029,
  serialized_end=1140,
)


_DELETEENTITYREQUEST = _descriptor.Descriptor(
  name='DeleteEntityRequest',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.DeleteEntityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.entity.v1.DeleteEntityRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.entity.v1.DeleteEntityRequest.name', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1142,
  serialized_end=1196,
)


_DELETEENTITYRESPONSE = _descriptor.Descriptor(
  name='DeleteEntityResponse',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.DeleteEntityResponse',
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
  serialized_start=1198,
  serialized_end=1220,
)

_LISTENTITIESREQUEST_LABELSENTRY.containing_type = _LISTENTITIESREQUEST
_LISTENTITIESREQUEST.fields_by_name['labels'].message_type = _LISTENTITIESREQUEST_LABELSENTRY
_LISTENTITIESRESPONSE.fields_by_name['entities'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._ENTITYLIST
_CREATEENTITYREQUEST.fields_by_name['entity'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._ENTITY
_UPDATEENTITYREQUEST.fields_by_name['entity'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._ENTITY
_UPDATEENTITYREQUEST.fields_by_name['field_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_GETENTITYREQUEST.fields_by_name['field_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_GETENTITYRESPONSE.fields_by_name['entity'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._ENTITY
DESCRIPTOR.message_types_by_name['ListEntitiesRequest'] = _LISTENTITIESREQUEST
DESCRIPTOR.message_types_by_name['ListEntitiesResponse'] = _LISTENTITIESRESPONSE
DESCRIPTOR.message_types_by_name['CreateEntityRequest'] = _CREATEENTITYREQUEST
DESCRIPTOR.message_types_by_name['CreateEntityResponse'] = _CREATEENTITYRESPONSE
DESCRIPTOR.message_types_by_name['UpdateEntityRequest'] = _UPDATEENTITYREQUEST
DESCRIPTOR.message_types_by_name['UpdateEntityResponse'] = _UPDATEENTITYRESPONSE
DESCRIPTOR.message_types_by_name['GetEntityRequest'] = _GETENTITYREQUEST
DESCRIPTOR.message_types_by_name['GetEntityResponse'] = _GETENTITYRESPONSE
DESCRIPTOR.message_types_by_name['DeleteEntityRequest'] = _DELETEENTITYREQUEST
DESCRIPTOR.message_types_by_name['DeleteEntityResponse'] = _DELETEENTITYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListEntitiesRequest = _reflection.GeneratedProtocolMessageType('ListEntitiesRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTENTITIESREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTENTITIESREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesRequest)
  })
_sym_db.RegisterMessage(ListEntitiesRequest)
_sym_db.RegisterMessage(ListEntitiesRequest.LabelsEntry)

ListEntitiesResponse = _reflection.GeneratedProtocolMessageType('ListEntitiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTENTITIESRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.ListEntitiesResponse)
  })
_sym_db.RegisterMessage(ListEntitiesResponse)

CreateEntityRequest = _reflection.GeneratedProtocolMessageType('CreateEntityRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENTITYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.CreateEntityRequest)
  })
_sym_db.RegisterMessage(CreateEntityRequest)

CreateEntityResponse = _reflection.GeneratedProtocolMessageType('CreateEntityResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENTITYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.CreateEntityResponse)
  })
_sym_db.RegisterMessage(CreateEntityResponse)

UpdateEntityRequest = _reflection.GeneratedProtocolMessageType('UpdateEntityRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENTITYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.UpdateEntityRequest)
  })
_sym_db.RegisterMessage(UpdateEntityRequest)

UpdateEntityResponse = _reflection.GeneratedProtocolMessageType('UpdateEntityResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENTITYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.UpdateEntityResponse)
  })
_sym_db.RegisterMessage(UpdateEntityResponse)

GetEntityRequest = _reflection.GeneratedProtocolMessageType('GetEntityRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETENTITYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.GetEntityRequest)
  })
_sym_db.RegisterMessage(GetEntityRequest)

GetEntityResponse = _reflection.GeneratedProtocolMessageType('GetEntityResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETENTITYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.GetEntityResponse)
  })
_sym_db.RegisterMessage(GetEntityResponse)

DeleteEntityRequest = _reflection.GeneratedProtocolMessageType('DeleteEntityRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENTITYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.DeleteEntityRequest)
  })
_sym_db.RegisterMessage(DeleteEntityRequest)

DeleteEntityResponse = _reflection.GeneratedProtocolMessageType('DeleteEntityResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENTITYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.entity.v1.entity_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.entity.v1.DeleteEntityResponse)
  })
_sym_db.RegisterMessage(DeleteEntityResponse)


DESCRIPTOR._options = None
_LISTENTITIESREQUEST_LABELSENTRY._options = None

_ENTITYSERVICE = _descriptor.ServiceDescriptor(
  name='EntityService',
  full_name='github.com.metaprov.modelaapi.services.entity.v1.EntityService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1223,
  serialized_end=2234,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListEntities',
    full_name='github.com.metaprov.modelaapi.services.entity.v1.EntityService.ListEntities',
    index=0,
    containing_service=None,
    input_type=_LISTENTITIESREQUEST,
    output_type=_LISTENTITIESRESPONSE,
    serialized_options=b'\202\323\344\223\002\032\022\030/v1/entities/{namespace}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateEntity',
    full_name='github.com.metaprov.modelaapi.services.entity.v1.EntityService.CreateEntity',
    index=1,
    containing_service=None,
    input_type=_CREATEENTITYREQUEST,
    output_type=_CREATEENTITYRESPONSE,
    serialized_options=b'\202\323\344\223\002\021\"\014/v1/entities:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEntity',
    full_name='github.com.metaprov.modelaapi.services.entity.v1.EntityService.GetEntity',
    index=2,
    containing_service=None,
    input_type=_GETENTITYREQUEST,
    output_type=_GETENTITYRESPONSE,
    serialized_options=b'\202\323\344\223\002\025\022\023/v1/entities/{name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateEntity',
    full_name='github.com.metaprov.modelaapi.services.entity.v1.EntityService.UpdateEntity',
    index=3,
    containing_service=None,
    input_type=_UPDATEENTITYREQUEST,
    output_type=_UPDATEENTITYRESPONSE,
    serialized_options=b'\202\323\344\223\002D\032?/v1/entities/{entity.metadata.namespace}/{entity.metadata.name}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteEntity',
    full_name='github.com.metaprov.modelaapi.services.entity.v1.EntityService.DeleteEntity',
    index=4,
    containing_service=None,
    input_type=_DELETEENTITYREQUEST,
    output_type=_DELETEENTITYRESPONSE,
    serialized_options=b'\202\323\344\223\002!*\037/v1/entities/{namespace}/{name}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENTITYSERVICE)

DESCRIPTOR.services_by_name['EntityService'] = _ENTITYSERVICE

# @@protoc_insertion_point(module_scope)
