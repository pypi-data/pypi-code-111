# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/attachment/v1/attachment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.services.common.v1 import common_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_common_dot_v1_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='github.com/metaprov/modelaapi/services/attachment/v1/attachment.proto',
  package='github.com.metaprov.modelaapi.services.attachment.v1',
  syntax='proto3',
  serialized_options=b'Z4github.com/metaprov/modelaapi/services/attachment/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nEgithub.com/metaprov/modelaapi/services/attachment/v1/attachment.proto\x12\x34github.com.metaprov.modelaapi.services.attachment.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x45github.com/metaprov/modelaapi/pkg/apis/infra/v1alpha1/generated.proto\x1a=github.com/metaprov/modelaapi/services/common/v1/common.proto\x1a google/protobuf/field_mask.proto\"\xfd\x01\n\x16ListAttachmentsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12h\n\x06labels\x18\x02 \x03(\x0b\x32X.github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8e\x01\n\x17ListAttachmentsResponse\x12Z\n\x0b\x61ttachments\x18\x01 \x01(\x0b\x32\x45.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.AttachmentList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x14\n\x12\x41ttachmentResponse\"p\n\x17\x43reateAttachmentRequest\x12U\n\nattachment\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Attachment\"\x1a\n\x18\x43reateAttachmentResponse\"\xa0\x01\n\x17UpdateAttachmentRequest\x12U\n\nattachment\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Attachment\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x1a\n\x18UpdateAttachmentResponse\"7\n\x14GetAttachmentRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"|\n\x15GetAttachmentResponse\x12U\n\nattachment\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Attachment\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"A\n\x1eGetAttachmentNamespacesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"v\n\x1fGetAttachmentNamespacesResponse\x12S\n\nnamespaces\x18\x01 \x03(\x0b\x32?.github.com.metaprov.modelaapi.services.common.v1.NamespaceInfo\":\n\x17\x44\x65leteAttachmentRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1a\n\x18\x44\x65leteAttachmentResponse\"\x1a\n\x18\x41ttachmentCreateResponse2\xfb\x08\n\x11\x41ttachmentService\x12\xd3\x01\n\x0fListAttachments\x12L.github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest\x1aM.github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/attachments/{namespace}\x12\xcd\x01\n\x10\x43reateAttachment\x12M.github.com.metaprov.modelaapi.services.attachment.v1.CreateAttachmentRequest\x1aN.github.com.metaprov.modelaapi.services.attachment.v1.CreateAttachmentResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/attachments:\x01*\x12\xd4\x01\n\rGetAttachment\x12J.github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentRequest\x1aK.github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/attachments/{namespace}/{name}\x12\x88\x02\n\x10UpdateAttachment\x12M.github.com.metaprov.modelaapi.services.attachment.v1.UpdateAttachmentRequest\x1aN.github.com.metaprov.modelaapi.services.attachment.v1.UpdateAttachmentResponse\"U\x82\xd3\xe4\x93\x02O\x1aJ/v1/attachments/{attachment.metadata.namespace}/{attachment.metadata.name}:\x01*\x12\xdd\x01\n\x10\x44\x65leteAttachment\x12M.github.com.metaprov.modelaapi.services.attachment.v1.DeleteAttachmentRequest\x1aN.github.com.metaprov.modelaapi.services.attachment.v1.DeleteAttachmentResponse\"*\x82\xd3\xe4\x93\x02$*\"/v1/attachments/{namespace}/{name}B6Z4github.com/metaprov/modelaapi/services/attachment/v1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2.DESCRIPTOR,github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_common_dot_v1_dot_common__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_LISTATTACHMENTSREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.LabelsEntry.value', index=1,
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
  serialized_start=534,
  serialized_end=579,
)

_LISTATTACHMENTSREQUEST = _descriptor.Descriptor(
  name='ListAttachmentsRequest',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.order_by', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LISTATTACHMENTSREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=579,
)


_LISTATTACHMENTSRESPONSE = _descriptor.Descriptor(
  name='ListAttachmentsResponse',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attachments', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsResponse.attachments', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsResponse.next_page_token', index=1,
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
  serialized_start=582,
  serialized_end=724,
)


_ATTACHMENTRESPONSE = _descriptor.Descriptor(
  name='AttachmentResponse',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.AttachmentResponse',
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
  serialized_start=726,
  serialized_end=746,
)


_CREATEATTACHMENTREQUEST = _descriptor.Descriptor(
  name='CreateAttachmentRequest',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.CreateAttachmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attachment', full_name='github.com.metaprov.modelaapi.services.attachment.v1.CreateAttachmentRequest.attachment', index=0,
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
  serialized_start=748,
  serialized_end=860,
)


_CREATEATTACHMENTRESPONSE = _descriptor.Descriptor(
  name='CreateAttachmentResponse',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.CreateAttachmentResponse',
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
  serialized_start=862,
  serialized_end=888,
)


_UPDATEATTACHMENTREQUEST = _descriptor.Descriptor(
  name='UpdateAttachmentRequest',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.UpdateAttachmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attachment', full_name='github.com.metaprov.modelaapi.services.attachment.v1.UpdateAttachmentRequest.attachment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_mask', full_name='github.com.metaprov.modelaapi.services.attachment.v1.UpdateAttachmentRequest.field_mask', index=1,
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
  serialized_start=891,
  serialized_end=1051,
)


_UPDATEATTACHMENTRESPONSE = _descriptor.Descriptor(
  name='UpdateAttachmentResponse',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.UpdateAttachmentResponse',
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
  serialized_start=1053,
  serialized_end=1079,
)


_GETATTACHMENTREQUEST = _descriptor.Descriptor(
  name='GetAttachmentRequest',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentRequest.name', index=1,
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
  serialized_start=1081,
  serialized_end=1136,
)


_GETATTACHMENTRESPONSE = _descriptor.Descriptor(
  name='GetAttachmentResponse',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attachment', full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentResponse.attachment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaml', full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentResponse.yaml', index=1,
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
  serialized_start=1138,
  serialized_end=1262,
)


_GETATTACHMENTNAMESPACESREQUEST = _descriptor.Descriptor(
  name='GetAttachmentNamespacesRequest',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentNamespacesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentNamespacesRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentNamespacesRequest.name', index=1,
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
  serialized_start=1264,
  serialized_end=1329,
)


_GETATTACHMENTNAMESPACESRESPONSE = _descriptor.Descriptor(
  name='GetAttachmentNamespacesResponse',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentNamespacesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentNamespacesResponse.namespaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1331,
  serialized_end=1449,
)


_DELETEATTACHMENTREQUEST = _descriptor.Descriptor(
  name='DeleteAttachmentRequest',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.DeleteAttachmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.attachment.v1.DeleteAttachmentRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.attachment.v1.DeleteAttachmentRequest.name', index=1,
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
  serialized_start=1451,
  serialized_end=1509,
)


_DELETEATTACHMENTRESPONSE = _descriptor.Descriptor(
  name='DeleteAttachmentResponse',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.DeleteAttachmentResponse',
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
  serialized_start=1511,
  serialized_end=1537,
)


_ATTACHMENTCREATERESPONSE = _descriptor.Descriptor(
  name='AttachmentCreateResponse',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.AttachmentCreateResponse',
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
  serialized_start=1539,
  serialized_end=1565,
)

_LISTATTACHMENTSREQUEST_LABELSENTRY.containing_type = _LISTATTACHMENTSREQUEST
_LISTATTACHMENTSREQUEST.fields_by_name['labels'].message_type = _LISTATTACHMENTSREQUEST_LABELSENTRY
_LISTATTACHMENTSRESPONSE.fields_by_name['attachments'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2._ATTACHMENTLIST
_CREATEATTACHMENTREQUEST.fields_by_name['attachment'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2._ATTACHMENT
_UPDATEATTACHMENTREQUEST.fields_by_name['attachment'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2._ATTACHMENT
_UPDATEATTACHMENTREQUEST.fields_by_name['field_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_GETATTACHMENTRESPONSE.fields_by_name['attachment'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2._ATTACHMENT
_GETATTACHMENTNAMESPACESRESPONSE.fields_by_name['namespaces'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_common_dot_v1_dot_common__pb2._NAMESPACEINFO
DESCRIPTOR.message_types_by_name['ListAttachmentsRequest'] = _LISTATTACHMENTSREQUEST
DESCRIPTOR.message_types_by_name['ListAttachmentsResponse'] = _LISTATTACHMENTSRESPONSE
DESCRIPTOR.message_types_by_name['AttachmentResponse'] = _ATTACHMENTRESPONSE
DESCRIPTOR.message_types_by_name['CreateAttachmentRequest'] = _CREATEATTACHMENTREQUEST
DESCRIPTOR.message_types_by_name['CreateAttachmentResponse'] = _CREATEATTACHMENTRESPONSE
DESCRIPTOR.message_types_by_name['UpdateAttachmentRequest'] = _UPDATEATTACHMENTREQUEST
DESCRIPTOR.message_types_by_name['UpdateAttachmentResponse'] = _UPDATEATTACHMENTRESPONSE
DESCRIPTOR.message_types_by_name['GetAttachmentRequest'] = _GETATTACHMENTREQUEST
DESCRIPTOR.message_types_by_name['GetAttachmentResponse'] = _GETATTACHMENTRESPONSE
DESCRIPTOR.message_types_by_name['GetAttachmentNamespacesRequest'] = _GETATTACHMENTNAMESPACESREQUEST
DESCRIPTOR.message_types_by_name['GetAttachmentNamespacesResponse'] = _GETATTACHMENTNAMESPACESRESPONSE
DESCRIPTOR.message_types_by_name['DeleteAttachmentRequest'] = _DELETEATTACHMENTREQUEST
DESCRIPTOR.message_types_by_name['DeleteAttachmentResponse'] = _DELETEATTACHMENTRESPONSE
DESCRIPTOR.message_types_by_name['AttachmentCreateResponse'] = _ATTACHMENTCREATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAttachmentsRequest = _reflection.GeneratedProtocolMessageType('ListAttachmentsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTATTACHMENTSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTATTACHMENTSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsRequest)
  })
_sym_db.RegisterMessage(ListAttachmentsRequest)
_sym_db.RegisterMessage(ListAttachmentsRequest.LabelsEntry)

ListAttachmentsResponse = _reflection.GeneratedProtocolMessageType('ListAttachmentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTATTACHMENTSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.ListAttachmentsResponse)
  })
_sym_db.RegisterMessage(ListAttachmentsResponse)

AttachmentResponse = _reflection.GeneratedProtocolMessageType('AttachmentResponse', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHMENTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.AttachmentResponse)
  })
_sym_db.RegisterMessage(AttachmentResponse)

CreateAttachmentRequest = _reflection.GeneratedProtocolMessageType('CreateAttachmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEATTACHMENTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.CreateAttachmentRequest)
  })
_sym_db.RegisterMessage(CreateAttachmentRequest)

CreateAttachmentResponse = _reflection.GeneratedProtocolMessageType('CreateAttachmentResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEATTACHMENTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.CreateAttachmentResponse)
  })
_sym_db.RegisterMessage(CreateAttachmentResponse)

UpdateAttachmentRequest = _reflection.GeneratedProtocolMessageType('UpdateAttachmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEATTACHMENTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.UpdateAttachmentRequest)
  })
_sym_db.RegisterMessage(UpdateAttachmentRequest)

UpdateAttachmentResponse = _reflection.GeneratedProtocolMessageType('UpdateAttachmentResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEATTACHMENTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.UpdateAttachmentResponse)
  })
_sym_db.RegisterMessage(UpdateAttachmentResponse)

GetAttachmentRequest = _reflection.GeneratedProtocolMessageType('GetAttachmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETATTACHMENTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentRequest)
  })
_sym_db.RegisterMessage(GetAttachmentRequest)

GetAttachmentResponse = _reflection.GeneratedProtocolMessageType('GetAttachmentResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETATTACHMENTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentResponse)
  })
_sym_db.RegisterMessage(GetAttachmentResponse)

GetAttachmentNamespacesRequest = _reflection.GeneratedProtocolMessageType('GetAttachmentNamespacesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETATTACHMENTNAMESPACESREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentNamespacesRequest)
  })
_sym_db.RegisterMessage(GetAttachmentNamespacesRequest)

GetAttachmentNamespacesResponse = _reflection.GeneratedProtocolMessageType('GetAttachmentNamespacesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETATTACHMENTNAMESPACESRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.GetAttachmentNamespacesResponse)
  })
_sym_db.RegisterMessage(GetAttachmentNamespacesResponse)

DeleteAttachmentRequest = _reflection.GeneratedProtocolMessageType('DeleteAttachmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEATTACHMENTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.DeleteAttachmentRequest)
  })
_sym_db.RegisterMessage(DeleteAttachmentRequest)

DeleteAttachmentResponse = _reflection.GeneratedProtocolMessageType('DeleteAttachmentResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEATTACHMENTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.DeleteAttachmentResponse)
  })
_sym_db.RegisterMessage(DeleteAttachmentResponse)

AttachmentCreateResponse = _reflection.GeneratedProtocolMessageType('AttachmentCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHMENTCREATERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.attachment.v1.attachment_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.attachment.v1.AttachmentCreateResponse)
  })
_sym_db.RegisterMessage(AttachmentCreateResponse)


DESCRIPTOR._options = None
_LISTATTACHMENTSREQUEST_LABELSENTRY._options = None

_ATTACHMENTSERVICE = _descriptor.ServiceDescriptor(
  name='AttachmentService',
  full_name='github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1568,
  serialized_end=2715,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListAttachments',
    full_name='github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService.ListAttachments',
    index=0,
    containing_service=None,
    input_type=_LISTATTACHMENTSREQUEST,
    output_type=_LISTATTACHMENTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\022\033/v1/attachments/{namespace}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateAttachment',
    full_name='github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService.CreateAttachment',
    index=1,
    containing_service=None,
    input_type=_CREATEATTACHMENTREQUEST,
    output_type=_CREATEATTACHMENTRESPONSE,
    serialized_options=b'\202\323\344\223\002\024\"\017/v1/attachments:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttachment',
    full_name='github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService.GetAttachment',
    index=2,
    containing_service=None,
    input_type=_GETATTACHMENTREQUEST,
    output_type=_GETATTACHMENTRESPONSE,
    serialized_options=b'\202\323\344\223\002$\022\"/v1/attachments/{namespace}/{name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAttachment',
    full_name='github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService.UpdateAttachment',
    index=3,
    containing_service=None,
    input_type=_UPDATEATTACHMENTREQUEST,
    output_type=_UPDATEATTACHMENTRESPONSE,
    serialized_options=b'\202\323\344\223\002O\032J/v1/attachments/{attachment.metadata.namespace}/{attachment.metadata.name}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAttachment',
    full_name='github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService.DeleteAttachment',
    index=4,
    containing_service=None,
    input_type=_DELETEATTACHMENTREQUEST,
    output_type=_DELETEATTACHMENTRESPONSE,
    serialized_options=b'\202\323\344\223\002$*\"/v1/attachments/{namespace}/{name}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ATTACHMENTSERVICE)

DESCRIPTOR.services_by_name['AttachmentService'] = _ATTACHMENTSERVICE

# @@protoc_insertion_point(module_scope)
