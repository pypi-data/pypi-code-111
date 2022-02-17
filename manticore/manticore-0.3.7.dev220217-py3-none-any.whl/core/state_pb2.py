# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="state.proto",
    package="mserialize",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0bstate.proto\x12\nmserialize"\x1d\n\nLogMessage\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t"\xb6\x01\n\x05State\x12\n\n\x02id\x18\x02 \x01(\x05\x12)\n\x04type\x18\x03 \x01(\x0e\x32\x1b.mserialize.State.StateType\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x15\n\rnum_executing\x18\x05 \x01(\x05\x12\x11\n\twait_time\x18\x06 \x01(\x05"<\n\tStateType\x12\t\n\x05READY\x10\x00\x12\x08\n\x04\x42USY\x10\x01\x12\n\n\x06KILLED\x10\x02\x12\x0e\n\nTERMINATED\x10\x03".\n\tStateList\x12!\n\x06states\x18\x07 \x03(\x0b\x32\x11.mserialize.State"7\n\x0bMessageList\x12(\n\x08messages\x18\x08 \x03(\x0b\x32\x16.mserialize.LogMessageb\x06proto3',
)


_STATE_STATETYPE = _descriptor.EnumDescriptor(
    name="StateType",
    full_name="mserialize.State.StateType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="READY",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BUSY",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="KILLED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TERMINATED",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=181,
    serialized_end=241,
)
_sym_db.RegisterEnumDescriptor(_STATE_STATETYPE)


_LOGMESSAGE = _descriptor.Descriptor(
    name="LogMessage",
    full_name="mserialize.LogMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="content",
            full_name="mserialize.LogMessage.content",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=27,
    serialized_end=56,
)


_STATE = _descriptor.Descriptor(
    name="State",
    full_name="mserialize.State",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="mserialize.State.id",
            index=0,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="type",
            full_name="mserialize.State.type",
            index=1,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reason",
            full_name="mserialize.State.reason",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="num_executing",
            full_name="mserialize.State.num_executing",
            index=3,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="wait_time",
            full_name="mserialize.State.wait_time",
            index=4,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _STATE_STATETYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=59,
    serialized_end=241,
)


_STATELIST = _descriptor.Descriptor(
    name="StateList",
    full_name="mserialize.StateList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="states",
            full_name="mserialize.StateList.states",
            index=0,
            number=7,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=243,
    serialized_end=289,
)


_MESSAGELIST = _descriptor.Descriptor(
    name="MessageList",
    full_name="mserialize.MessageList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="messages",
            full_name="mserialize.MessageList.messages",
            index=0,
            number=8,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=291,
    serialized_end=346,
)

_STATE.fields_by_name["type"].enum_type = _STATE_STATETYPE
_STATE_STATETYPE.containing_type = _STATE
_STATELIST.fields_by_name["states"].message_type = _STATE
_MESSAGELIST.fields_by_name["messages"].message_type = _LOGMESSAGE
DESCRIPTOR.message_types_by_name["LogMessage"] = _LOGMESSAGE
DESCRIPTOR.message_types_by_name["State"] = _STATE
DESCRIPTOR.message_types_by_name["StateList"] = _STATELIST
DESCRIPTOR.message_types_by_name["MessageList"] = _MESSAGELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogMessage = _reflection.GeneratedProtocolMessageType(
    "LogMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOGMESSAGE,
        "__module__": "state_pb2"
        # @@protoc_insertion_point(class_scope:mserialize.LogMessage)
    },
)
_sym_db.RegisterMessage(LogMessage)

State = _reflection.GeneratedProtocolMessageType(
    "State",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATE,
        "__module__": "state_pb2"
        # @@protoc_insertion_point(class_scope:mserialize.State)
    },
)
_sym_db.RegisterMessage(State)

StateList = _reflection.GeneratedProtocolMessageType(
    "StateList",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATELIST,
        "__module__": "state_pb2"
        # @@protoc_insertion_point(class_scope:mserialize.StateList)
    },
)
_sym_db.RegisterMessage(StateList)

MessageList = _reflection.GeneratedProtocolMessageType(
    "MessageList",
    (_message.Message,),
    {
        "DESCRIPTOR": _MESSAGELIST,
        "__module__": "state_pb2"
        # @@protoc_insertion_point(class_scope:mserialize.MessageList)
    },
)
_sym_db.RegisterMessage(MessageList)


# @@protoc_insertion_point(module_scope)
