# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/compat/proto/cpp_shape_inference.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorboard.compat.proto import full_type_pb2 as tensorboard_dot_compat_dot_proto_dot_full__type__pb2
from tensorboard.compat.proto import tensor_shape_pb2 as tensorboard_dot_compat_dot_proto_dot_tensor__shape__pb2
from tensorboard.compat.proto import types_pb2 as tensorboard_dot_compat_dot_proto_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/compat/proto/cpp_shape_inference.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_options=_b('Z\\github.com/tensorflow/tensorflow/tensorflow/go/python/framework/cpp_shape_inference_go_proto\370\001\001'),
  serialized_pb=_b('\n2tensorboard/compat/proto/cpp_shape_inference.proto\x12\x0btensorboard\x1a(tensorboard/compat/proto/full_type.proto\x1a+tensorboard/compat/proto/tensor_shape.proto\x1a$tensorboard/compat/proto/types.proto\"\xa1\x03\n\x17\x43ppShapeInferenceResult\x12,\n\x05shape\x18\x01 \x01(\x0b\x32\x1d.tensorboard.TensorShapeProto\x12\x44\n\x0bhandle_data\x18\x04 \x01(\x0b\x32/.tensorboard.CppShapeInferenceResult.HandleData\x1a\x96\x01\n\x12HandleShapeAndType\x12,\n\x05shape\x18\x01 \x01(\x0b\x32\x1d.tensorboard.TensorShapeProto\x12$\n\x05\x64type\x18\x02 \x01(\x0e\x32\x15.tensorboard.DataType\x12&\n\x04type\x18\x04 \x01(\x0b\x32\x18.tensorboard.FullTypeDefJ\x04\x08\x03\x10\x04\x1am\n\nHandleData\x12\x0e\n\x06is_set\x18\x01 \x01(\x08\x12O\n\x0eshape_and_type\x18\x02 \x03(\x0b\x32\x37.tensorboard.CppShapeInferenceResult.HandleShapeAndTypeJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"e\n\x1d\x43ppShapeInferenceInputsNeeded\x12\x1c\n\x14input_tensors_needed\x18\x01 \x03(\x05\x12&\n\x1einput_tensors_as_shapes_needed\x18\x02 \x03(\x05\x42\x61Z\\github.com/tensorflow/tensorflow/tensorflow/go/python/framework/cpp_shape_inference_go_proto\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorboard_dot_compat_dot_proto_dot_full__type__pb2.DESCRIPTOR,tensorboard_dot_compat_dot_proto_dot_tensor__shape__pb2.DESCRIPTOR,tensorboard_dot_compat_dot_proto_dot_types__pb2.DESCRIPTOR,])




_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE = _descriptor.Descriptor(
  name='HandleShapeAndType',
  full_name='tensorboard.CppShapeInferenceResult.HandleShapeAndType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorboard.CppShapeInferenceResult.HandleShapeAndType.shape', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorboard.CppShapeInferenceResult.HandleShapeAndType.dtype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorboard.CppShapeInferenceResult.HandleShapeAndType.type', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=337,
  serialized_end=487,
)

_CPPSHAPEINFERENCERESULT_HANDLEDATA = _descriptor.Descriptor(
  name='HandleData',
  full_name='tensorboard.CppShapeInferenceResult.HandleData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_set', full_name='tensorboard.CppShapeInferenceResult.HandleData.is_set', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape_and_type', full_name='tensorboard.CppShapeInferenceResult.HandleData.shape_and_type', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=489,
  serialized_end=598,
)

_CPPSHAPEINFERENCERESULT = _descriptor.Descriptor(
  name='CppShapeInferenceResult',
  full_name='tensorboard.CppShapeInferenceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorboard.CppShapeInferenceResult.shape', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='handle_data', full_name='tensorboard.CppShapeInferenceResult.handle_data', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE, _CPPSHAPEINFERENCERESULT_HANDLEDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=610,
)


_CPPSHAPEINFERENCEINPUTSNEEDED = _descriptor.Descriptor(
  name='CppShapeInferenceInputsNeeded',
  full_name='tensorboard.CppShapeInferenceInputsNeeded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_tensors_needed', full_name='tensorboard.CppShapeInferenceInputsNeeded.input_tensors_needed', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_tensors_as_shapes_needed', full_name='tensorboard.CppShapeInferenceInputsNeeded.input_tensors_as_shapes_needed', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=713,
)

_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE.fields_by_name['shape'].message_type = tensorboard_dot_compat_dot_proto_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE.fields_by_name['dtype'].enum_type = tensorboard_dot_compat_dot_proto_dot_types__pb2._DATATYPE
_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE.fields_by_name['type'].message_type = tensorboard_dot_compat_dot_proto_dot_full__type__pb2._FULLTYPEDEF
_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE.containing_type = _CPPSHAPEINFERENCERESULT
_CPPSHAPEINFERENCERESULT_HANDLEDATA.fields_by_name['shape_and_type'].message_type = _CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE
_CPPSHAPEINFERENCERESULT_HANDLEDATA.containing_type = _CPPSHAPEINFERENCERESULT
_CPPSHAPEINFERENCERESULT.fields_by_name['shape'].message_type = tensorboard_dot_compat_dot_proto_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_CPPSHAPEINFERENCERESULT.fields_by_name['handle_data'].message_type = _CPPSHAPEINFERENCERESULT_HANDLEDATA
DESCRIPTOR.message_types_by_name['CppShapeInferenceResult'] = _CPPSHAPEINFERENCERESULT
DESCRIPTOR.message_types_by_name['CppShapeInferenceInputsNeeded'] = _CPPSHAPEINFERENCEINPUTSNEEDED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CppShapeInferenceResult = _reflection.GeneratedProtocolMessageType('CppShapeInferenceResult', (_message.Message,), {

  'HandleShapeAndType' : _reflection.GeneratedProtocolMessageType('HandleShapeAndType', (_message.Message,), {
    'DESCRIPTOR' : _CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE,
    '__module__' : 'tensorboard.compat.proto.cpp_shape_inference_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.CppShapeInferenceResult.HandleShapeAndType)
    })
  ,

  'HandleData' : _reflection.GeneratedProtocolMessageType('HandleData', (_message.Message,), {
    'DESCRIPTOR' : _CPPSHAPEINFERENCERESULT_HANDLEDATA,
    '__module__' : 'tensorboard.compat.proto.cpp_shape_inference_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.CppShapeInferenceResult.HandleData)
    })
  ,
  'DESCRIPTOR' : _CPPSHAPEINFERENCERESULT,
  '__module__' : 'tensorboard.compat.proto.cpp_shape_inference_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.CppShapeInferenceResult)
  })
_sym_db.RegisterMessage(CppShapeInferenceResult)
_sym_db.RegisterMessage(CppShapeInferenceResult.HandleShapeAndType)
_sym_db.RegisterMessage(CppShapeInferenceResult.HandleData)

CppShapeInferenceInputsNeeded = _reflection.GeneratedProtocolMessageType('CppShapeInferenceInputsNeeded', (_message.Message,), {
  'DESCRIPTOR' : _CPPSHAPEINFERENCEINPUTSNEEDED,
  '__module__' : 'tensorboard.compat.proto.cpp_shape_inference_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.CppShapeInferenceInputsNeeded)
  })
_sym_db.RegisterMessage(CppShapeInferenceInputsNeeded)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
