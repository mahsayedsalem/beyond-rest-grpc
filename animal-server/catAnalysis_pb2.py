# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: catAnalysis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='catAnalysis.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x63\x61tAnalysis.proto\x12\x05proto\"\"\n\x0f\x41nalysisRequest\x12\x0f\n\x07\x63\x61tName\x18\x01 \x01(\t\"\"\n\x10\x41nalysisResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2P\n\x0b\x63\x61tAnalysis\x12\x41\n\x0c\x41nalyzeSound\x12\x16.proto.AnalysisRequest\x1a\x17.proto.AnalysisResponse\"\x00\x62\x06proto3'
)




_ANALYSISREQUEST = _descriptor.Descriptor(
  name='AnalysisRequest',
  full_name='proto.AnalysisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='catName', full_name='proto.AnalysisRequest.catName', index=0,
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
  serialized_start=28,
  serialized_end=62,
)


_ANALYSISRESPONSE = _descriptor.Descriptor(
  name='AnalysisResponse',
  full_name='proto.AnalysisResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='proto.AnalysisResponse.result', index=0,
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
  serialized_start=64,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['AnalysisRequest'] = _ANALYSISREQUEST
DESCRIPTOR.message_types_by_name['AnalysisResponse'] = _ANALYSISRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalysisRequest = _reflection.GeneratedProtocolMessageType('AnalysisRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYSISREQUEST,
  '__module__' : 'catAnalysis_pb2'
  # @@protoc_insertion_point(class_scope:proto.AnalysisRequest)
  })
_sym_db.RegisterMessage(AnalysisRequest)

AnalysisResponse = _reflection.GeneratedProtocolMessageType('AnalysisResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANALYSISRESPONSE,
  '__module__' : 'catAnalysis_pb2'
  # @@protoc_insertion_point(class_scope:proto.AnalysisResponse)
  })
_sym_db.RegisterMessage(AnalysisResponse)



_CATANALYSIS = _descriptor.ServiceDescriptor(
  name='catAnalysis',
  full_name='proto.catAnalysis',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=100,
  serialized_end=180,
  methods=[
  _descriptor.MethodDescriptor(
    name='AnalyzeSound',
    full_name='proto.catAnalysis.AnalyzeSound',
    index=0,
    containing_service=None,
    input_type=_ANALYSISREQUEST,
    output_type=_ANALYSISRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CATANALYSIS)

DESCRIPTOR.services_by_name['catAnalysis'] = _CATANALYSIS

# @@protoc_insertion_point(module_scope)
