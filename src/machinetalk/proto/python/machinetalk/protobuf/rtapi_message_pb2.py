# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: machinetalk/protobuf/rtapi_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from machinetalk.protobuf import nanopb_pb2 as machinetalk_dot_protobuf_dot_nanopb__pb2
from machinetalk.protobuf import value_pb2 as machinetalk_dot_protobuf_dot_value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='machinetalk/protobuf/rtapi_message.proto',
  package='machinetalk',
  syntax='proto2',
  serialized_pb=_b('\n(machinetalk/protobuf/rtapi_message.proto\x12\x0bmachinetalk\x1a!machinetalk/protobuf/nanopb.proto\x1a machinetalk/protobuf/value.proto\"\x7f\n\rRTAPI_Message\x12\x10\n\x08msglevel\x18\n \x02(\x05\x12,\n\x06\x66ormat\x18\x14 \x02(\t:\x15*** uninitialized ***B\x05\x92?\x02\x08\x64\x12&\n\x03\x61rg\x18\x1e \x03(\x0b\x32\x12.machinetalk.ValueB\x05\x92?\x02\x10\n:\x06\x92?\x03H\xe8\x07')
  ,
  dependencies=[machinetalk_dot_protobuf_dot_nanopb__pb2.DESCRIPTOR,machinetalk_dot_protobuf_dot_value__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RTAPI_MESSAGE = _descriptor.Descriptor(
  name='RTAPI_Message',
  full_name='machinetalk.RTAPI_Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msglevel', full_name='machinetalk.RTAPI_Message.msglevel', index=0,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format', full_name='machinetalk.RTAPI_Message.format', index=1,
      number=20, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("*** uninitialized ***").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010d'))),
    _descriptor.FieldDescriptor(
      name='arg', full_name='machinetalk.RTAPI_Message.arg', index=2,
      number=30, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\020\n'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\350\007')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=253,
)

_RTAPI_MESSAGE.fields_by_name['arg'].message_type = machinetalk_dot_protobuf_dot_value__pb2._VALUE
DESCRIPTOR.message_types_by_name['RTAPI_Message'] = _RTAPI_MESSAGE

RTAPI_Message = _reflection.GeneratedProtocolMessageType('RTAPI_Message', (_message.Message,), dict(
  DESCRIPTOR = _RTAPI_MESSAGE,
  __module__ = 'machinetalk.protobuf.rtapi_message_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.RTAPI_Message)
  ))
_sym_db.RegisterMessage(RTAPI_Message)


_RTAPI_MESSAGE.fields_by_name['format'].has_options = True
_RTAPI_MESSAGE.fields_by_name['format']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010d'))
_RTAPI_MESSAGE.fields_by_name['arg'].has_options = True
_RTAPI_MESSAGE.fields_by_name['arg']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\020\n'))
_RTAPI_MESSAGE.has_options = True
_RTAPI_MESSAGE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\350\007'))
# @@protoc_insertion_point(module_scope)
