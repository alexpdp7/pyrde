# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reviewdog.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='reviewdog.proto',
  package='reviewdog.rdf',
  syntax='proto3',
  serialized_pb=_b('\n\x0freviewdog.proto\x12\rreviewdog.rdf\"\x94\x01\n\x10\x44iagnosticResult\x12.\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x19.reviewdog.rdf.Diagnostic\x12%\n\x06source\x18\x02 \x01(\x0b\x32\x15.reviewdog.rdf.Source\x12)\n\x08severity\x18\x03 \x01(\x0e\x32\x17.reviewdog.rdf.Severity\"\x86\x02\n\nDiagnostic\x12\x0f\n\x07message\x18\x01 \x01(\t\x12)\n\x08location\x18\x02 \x01(\x0b\x32\x17.reviewdog.rdf.Location\x12)\n\x08severity\x18\x03 \x01(\x0e\x32\x17.reviewdog.rdf.Severity\x12%\n\x06source\x18\x04 \x01(\x0b\x32\x15.reviewdog.rdf.Source\x12!\n\x04\x63ode\x18\x05 \x01(\x0b\x32\x13.reviewdog.rdf.Code\x12.\n\x0bsuggestions\x18\x06 \x03(\x0b\x32\x19.reviewdog.rdf.Suggestion\x12\x17\n\x0foriginal_output\x18\x07 \x01(\t\"=\n\x08Location\x12\x0c\n\x04path\x18\x02 \x01(\t\x12#\n\x05range\x18\x03 \x01(\x0b\x32\x14.reviewdog.rdf.Range\"U\n\x05Range\x12&\n\x05start\x18\x01 \x01(\x0b\x32\x17.reviewdog.rdf.Position\x12$\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x17.reviewdog.rdf.Position\"(\n\x08Position\x12\x0c\n\x04line\x18\x01 \x01(\x05\x12\x0e\n\x06\x63olumn\x18\x02 \x01(\x05\"?\n\nSuggestion\x12#\n\x05range\x18\x01 \x01(\x0b\x32\x14.reviewdog.rdf.Range\x12\x0c\n\x04text\x18\x02 \x01(\t\"#\n\x06Source\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\"\n\x04\x43ode\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t*B\n\x08Severity\x12\x14\n\x10UNKNOWN_SEVERITY\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x08\n\x04INFO\x10\x03\x42*Z(github.com/reviewdog/reviewdog/proto/rdfb\x06proto3')
)

_SEVERITY = _descriptor.EnumDescriptor(
  name='Severity',
  full_name='reviewdog.rdf.Severity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SEVERITY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=780,
  serialized_end=846,
)
_sym_db.RegisterEnumDescriptor(_SEVERITY)

Severity = enum_type_wrapper.EnumTypeWrapper(_SEVERITY)
UNKNOWN_SEVERITY = 0
ERROR = 1
WARNING = 2
INFO = 3



_DIAGNOSTICRESULT = _descriptor.Descriptor(
  name='DiagnosticResult',
  full_name='reviewdog.rdf.DiagnosticResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diagnostics', full_name='reviewdog.rdf.DiagnosticResult.diagnostics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='reviewdog.rdf.DiagnosticResult.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='severity', full_name='reviewdog.rdf.DiagnosticResult.severity', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=183,
)


_DIAGNOSTIC = _descriptor.Descriptor(
  name='Diagnostic',
  full_name='reviewdog.rdf.Diagnostic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='reviewdog.rdf.Diagnostic.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='reviewdog.rdf.Diagnostic.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='severity', full_name='reviewdog.rdf.Diagnostic.severity', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='reviewdog.rdf.Diagnostic.source', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='reviewdog.rdf.Diagnostic.code', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suggestions', full_name='reviewdog.rdf.Diagnostic.suggestions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_output', full_name='reviewdog.rdf.Diagnostic.original_output', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=448,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='reviewdog.rdf.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='reviewdog.rdf.Location.path', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='reviewdog.rdf.Location.range', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=511,
)


_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='reviewdog.rdf.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='reviewdog.rdf.Range.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='reviewdog.rdf.Range.end', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=513,
  serialized_end=598,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='reviewdog.rdf.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line', full_name='reviewdog.rdf.Position.line', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column', full_name='reviewdog.rdf.Position.column', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=600,
  serialized_end=640,
)


_SUGGESTION = _descriptor.Descriptor(
  name='Suggestion',
  full_name='reviewdog.rdf.Suggestion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='reviewdog.rdf.Suggestion.range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='reviewdog.rdf.Suggestion.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=642,
  serialized_end=705,
)


_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='reviewdog.rdf.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='reviewdog.rdf.Source.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='reviewdog.rdf.Source.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=707,
  serialized_end=742,
)


_CODE = _descriptor.Descriptor(
  name='Code',
  full_name='reviewdog.rdf.Code',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='reviewdog.rdf.Code.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='reviewdog.rdf.Code.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=744,
  serialized_end=778,
)

_DIAGNOSTICRESULT.fields_by_name['diagnostics'].message_type = _DIAGNOSTIC
_DIAGNOSTICRESULT.fields_by_name['source'].message_type = _SOURCE
_DIAGNOSTICRESULT.fields_by_name['severity'].enum_type = _SEVERITY
_DIAGNOSTIC.fields_by_name['location'].message_type = _LOCATION
_DIAGNOSTIC.fields_by_name['severity'].enum_type = _SEVERITY
_DIAGNOSTIC.fields_by_name['source'].message_type = _SOURCE
_DIAGNOSTIC.fields_by_name['code'].message_type = _CODE
_DIAGNOSTIC.fields_by_name['suggestions'].message_type = _SUGGESTION
_LOCATION.fields_by_name['range'].message_type = _RANGE
_RANGE.fields_by_name['start'].message_type = _POSITION
_RANGE.fields_by_name['end'].message_type = _POSITION
_SUGGESTION.fields_by_name['range'].message_type = _RANGE
DESCRIPTOR.message_types_by_name['DiagnosticResult'] = _DIAGNOSTICRESULT
DESCRIPTOR.message_types_by_name['Diagnostic'] = _DIAGNOSTIC
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Range'] = _RANGE
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Suggestion'] = _SUGGESTION
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['Code'] = _CODE
DESCRIPTOR.enum_types_by_name['Severity'] = _SEVERITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DiagnosticResult = _reflection.GeneratedProtocolMessageType('DiagnosticResult', (_message.Message,), dict(
  DESCRIPTOR = _DIAGNOSTICRESULT,
  __module__ = 'reviewdog_pb2'
  # @@protoc_insertion_point(class_scope:reviewdog.rdf.DiagnosticResult)
  ))
_sym_db.RegisterMessage(DiagnosticResult)

Diagnostic = _reflection.GeneratedProtocolMessageType('Diagnostic', (_message.Message,), dict(
  DESCRIPTOR = _DIAGNOSTIC,
  __module__ = 'reviewdog_pb2'
  # @@protoc_insertion_point(class_scope:reviewdog.rdf.Diagnostic)
  ))
_sym_db.RegisterMessage(Diagnostic)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'reviewdog_pb2'
  # @@protoc_insertion_point(class_scope:reviewdog.rdf.Location)
  ))
_sym_db.RegisterMessage(Location)

Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), dict(
  DESCRIPTOR = _RANGE,
  __module__ = 'reviewdog_pb2'
  # @@protoc_insertion_point(class_scope:reviewdog.rdf.Range)
  ))
_sym_db.RegisterMessage(Range)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'reviewdog_pb2'
  # @@protoc_insertion_point(class_scope:reviewdog.rdf.Position)
  ))
_sym_db.RegisterMessage(Position)

Suggestion = _reflection.GeneratedProtocolMessageType('Suggestion', (_message.Message,), dict(
  DESCRIPTOR = _SUGGESTION,
  __module__ = 'reviewdog_pb2'
  # @@protoc_insertion_point(class_scope:reviewdog.rdf.Suggestion)
  ))
_sym_db.RegisterMessage(Suggestion)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), dict(
  DESCRIPTOR = _SOURCE,
  __module__ = 'reviewdog_pb2'
  # @@protoc_insertion_point(class_scope:reviewdog.rdf.Source)
  ))
_sym_db.RegisterMessage(Source)

Code = _reflection.GeneratedProtocolMessageType('Code', (_message.Message,), dict(
  DESCRIPTOR = _CODE,
  __module__ = 'reviewdog_pb2'
  # @@protoc_insertion_point(class_scope:reviewdog.rdf.Code)
  ))
_sym_db.RegisterMessage(Code)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z(github.com/reviewdog/reviewdog/proto/rdf'))
# @@protoc_insertion_point(module_scope)
