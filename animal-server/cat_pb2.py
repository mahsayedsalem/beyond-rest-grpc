# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cat.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tcat.proto\x12\x05proto\"\x1d\n\nCatRequest\x12\x0f\n\x07\x63\x61tName\x18\x01 \x01(\t\"\x1e\n\x0b\x43\x61tResponse\x12\x0f\n\x07\x63\x61tMeaw\x18\x01 \x01(\t\")\n\x16\x41nalyzeCatSoundRequest\x12\x0f\n\x07\x63\x61tName\x18\x01 \x01(\t\")\n\x17\x41nalyzeCatSoundResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\x8d\x01\n\x03\x63\x61t\x12\x30\n\x07\x43\x61llCat\x12\x11.proto.CatRequest\x1a\x12.proto.CatResponse\x12T\n\x0f\x41nalyzeCatSound\x12\x1d.proto.AnalyzeCatSoundRequest\x1a\x1e.proto.AnalyzeCatSoundResponse\"\x00\x30\x01\x62\x06proto3'
)




_CATREQUEST = _descriptor.Descriptor(
  name='CatRequest',
  full_name='proto.CatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='catName', full_name='proto.CatRequest.catName', index=0,
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
  serialized_start=20,
  serialized_end=49,
)


_CATRESPONSE = _descriptor.Descriptor(
  name='CatResponse',
  full_name='proto.CatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='catMeaw', full_name='proto.CatResponse.catMeaw', index=0,
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
  serialized_start=51,
  serialized_end=81,
)


_ANALYZECATSOUNDREQUEST = _descriptor.Descriptor(
  name='AnalyzeCatSoundRequest',
  full_name='proto.AnalyzeCatSoundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='catName', full_name='proto.AnalyzeCatSoundRequest.catName', index=0,
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
  serialized_start=83,
  serialized_end=124,
)


_ANALYZECATSOUNDRESPONSE = _descriptor.Descriptor(
  name='AnalyzeCatSoundResponse',
  full_name='proto.AnalyzeCatSoundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='proto.AnalyzeCatSoundResponse.result', index=0,
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
  serialized_start=126,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['CatRequest'] = _CATREQUEST
DESCRIPTOR.message_types_by_name['CatResponse'] = _CATRESPONSE
DESCRIPTOR.message_types_by_name['AnalyzeCatSoundRequest'] = _ANALYZECATSOUNDREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeCatSoundResponse'] = _ANALYZECATSOUNDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CatRequest = _reflection.GeneratedProtocolMessageType('CatRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATREQUEST,
  '__module__' : 'cat_pb2'
  # @@protoc_insertion_point(class_scope:proto.CatRequest)
  })
_sym_db.RegisterMessage(CatRequest)

CatResponse = _reflection.GeneratedProtocolMessageType('CatResponse', (_message.Message,), {
  'DESCRIPTOR' : _CATRESPONSE,
  '__module__' : 'cat_pb2'
  # @@protoc_insertion_point(class_scope:proto.CatResponse)
  })
_sym_db.RegisterMessage(CatResponse)

AnalyzeCatSoundRequest = _reflection.GeneratedProtocolMessageType('AnalyzeCatSoundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZECATSOUNDREQUEST,
  '__module__' : 'cat_pb2'
  # @@protoc_insertion_point(class_scope:proto.AnalyzeCatSoundRequest)
  })
_sym_db.RegisterMessage(AnalyzeCatSoundRequest)

AnalyzeCatSoundResponse = _reflection.GeneratedProtocolMessageType('AnalyzeCatSoundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZECATSOUNDRESPONSE,
  '__module__' : 'cat_pb2'
  # @@protoc_insertion_point(class_scope:proto.AnalyzeCatSoundResponse)
  })
_sym_db.RegisterMessage(AnalyzeCatSoundResponse)



_CAT = _descriptor.ServiceDescriptor(
  name='cat',
  full_name='proto.cat',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=170,
  serialized_end=311,
  methods=[
  _descriptor.MethodDescriptor(
    name='CallCat',
    full_name='proto.cat.CallCat',
    index=0,
    containing_service=None,
    input_type=_CATREQUEST,
    output_type=_CATRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AnalyzeCatSound',
    full_name='proto.cat.AnalyzeCatSound',
    index=1,
    containing_service=None,
    input_type=_ANALYZECATSOUNDREQUEST,
    output_type=_ANALYZECATSOUNDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAT)

DESCRIPTOR.services_by_name['cat'] = _CAT

# @@protoc_insertion_point(module_scope)
