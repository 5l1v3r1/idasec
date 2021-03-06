# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import libcall_pb2 as libcall__pb2
import syscall_pb2 as syscall__pb2
import instruction_pb2 as instruction__pb2
import analysis_config_pb2 as analysis__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='configuration',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x63onfig.proto\x12\rconfiguration\x1a\x0c\x63ommon.proto\x1a\rlibcall.proto\x1a\rsyscall.proto\x1a\x11instruction.proto\x1a\x15\x61nalysis_config.proto\",\n\x0b\x63\x61ll_name_t\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\x04\x12\x0c\n\x04name\x18\x02 \x02(\t\"\x89\x07\n\rconfiguration\x12\r\n\x05start\x18\x01 \x01(\x04\x12\x0c\n\x04stop\x18\x02 \x01(\x04\x12\x12\n\ncall_skips\x18\x03 \x03(\x04\x12\x11\n\tfun_skips\x18\x04 \x03(\x04\x12,\n\x08libcalls\x18\x05 \x03(\x0b\x32\x1a.libcall_types.libcall_pol\x12,\n\x08syscalls\x18\x06 \x03(\x0b\x32\x1a.syscall_types.syscall_pol\x12*\n\x06instrs\x18\x07 \x03(\x0b\x32\x1a.instruction_pol.instr_pol\x12\x0e\n\x06policy\x18\x08 \x03(\t\x12&\n\x06inputs\x18\t \x03(\x0b\x32\x16.configuration.input_t\x12,\n\x08\x63\x61ll_map\x18\n \x03(\x0b\x32\x1a.configuration.call_name_t\x12\x13\n\x0b\x62reakpoints\x18\x0b \x03(\x04\x12\'\n\rinitial_state\x18\x0c \x03(\x0b\x32\x10.common.memory_t\x12\x38\n\tdirection\x18\r \x01(\x0e\x32\x1c.common.analysis_direction_t:\x07\x46ORWARD\x12\x11\n\x06ksteps\x18\x0e \x01(\r:\x01\x30\x12\x17\n\ranalysis_name\x18\x0f \x01(\t:\x00\x12$\n\x06solver\x18\x10 \x01(\x0e\x32\x10.common.solver_t:\x02Z3\x12\x1a\n\x0bincremental\x18\x11 \x01(\x08:\x05\x66\x61lse\x12\x12\n\x07timeout\x18\x12 \x01(\r:\x01\x30\x12\x1c\n\roptim_cstprop\x18\x13 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0coptim_rebase\x18\x14 \x01(\x08:\x05\x66\x61lse\x12\x18\n\toptim_row\x18\x15 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\roptim_rowplus\x18\x1a \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0coptim_eqprop\x18\x1b \x01(\x08:\x05\x66\x61lse\x12\x31\n\x07\x63\x61llcvt\x18\x16 \x01(\x0e\x32\x19.common.call_convention_t:\x05\x43\x44\x45\x43L\x12,\n\x0e\x64\x65\x66\x61ult_action\x18\x17 \x01(\x0e\x32\x0e.common.action:\x04SYMB\x12\x14\n\tverbosity\x18\x18 \x01(\r:\x01\x30\x12\x45\n\x15\x61\x64\x64itional_parameters\x18\x19 \x01(\x0b\x32&.analysis_config.specific_parameters_t\"\x81\x03\n\x07input_t\x12\x31\n\x06typeid\x18\x01 \x02(\x0e\x32!.configuration.input_t.input_kind\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\x04\x12+\n\x04when\x18\x03 \x02(\x0e\x32\x1d.configuration.input_t.when_t\x12\x1e\n\x06\x61\x63tion\x18\x04 \x02(\x0e\x32\x0e.common.action\x12\x14\n\titeration\x18\x64 \x01(\r:\x01\x30\x12!\n\x03reg\x18\x07 \x01(\x0b\x32\x12.common.register_tH\x00\x12\x1f\n\x03mem\x18\x08 \x01(\x0b\x32\x10.common.memory_tH\x00\x12/\n\x08indirect\x18\t \x01(\x0b\x32\x1b.common.indirect_register_tH\x00\",\n\ninput_kind\x12\x07\n\x03REG\x10\x00\x12\x07\n\x03MEM\x10\x01\x12\x0c\n\x08INDIRECT\x10\x02\"\x1f\n\x06when_t\x12\n\n\x06\x42\x45\x46ORE\x10\x00\x12\t\n\x05\x41\x46TER\x10\x01\x42\x0b\n\tinput_cnt')
  ,
  dependencies=[common__pb2.DESCRIPTOR,libcall__pb2.DESCRIPTOR,syscall__pb2.DESCRIPTOR,instruction__pb2.DESCRIPTOR,analysis__config__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_INPUT_T_INPUT_KIND = _descriptor.EnumDescriptor(
  name='input_kind',
  full_name='configuration.input_t.input_kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REG', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDIRECT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1367,
  serialized_end=1411,
)
_sym_db.RegisterEnumDescriptor(_INPUT_T_INPUT_KIND)

_INPUT_T_WHEN_T = _descriptor.EnumDescriptor(
  name='when_t',
  full_name='configuration.input_t.when_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BEFORE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AFTER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1413,
  serialized_end=1444,
)
_sym_db.RegisterEnumDescriptor(_INPUT_T_WHEN_T)


_CALL_NAME_T = _descriptor.Descriptor(
  name='call_name_t',
  full_name='configuration.call_name_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='configuration.call_name_t.address', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='configuration.call_name_t.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=161,
)


_CONFIGURATION = _descriptor.Descriptor(
  name='configuration',
  full_name='configuration.configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='configuration.configuration.start', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop', full_name='configuration.configuration.stop', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_skips', full_name='configuration.configuration.call_skips', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fun_skips', full_name='configuration.configuration.fun_skips', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='libcalls', full_name='configuration.configuration.libcalls', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='syscalls', full_name='configuration.configuration.syscalls', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrs', full_name='configuration.configuration.instrs', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy', full_name='configuration.configuration.policy', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='configuration.configuration.inputs', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_map', full_name='configuration.configuration.call_map', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='breakpoints', full_name='configuration.configuration.breakpoints', index=10,
      number=11, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_state', full_name='configuration.configuration.initial_state', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='configuration.configuration.direction', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ksteps', full_name='configuration.configuration.ksteps', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analysis_name', full_name='configuration.configuration.analysis_name', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solver', full_name='configuration.configuration.solver', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incremental', full_name='configuration.configuration.incremental', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='configuration.configuration.timeout', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optim_cstprop', full_name='configuration.configuration.optim_cstprop', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optim_rebase', full_name='configuration.configuration.optim_rebase', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optim_row', full_name='configuration.configuration.optim_row', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optim_rowplus', full_name='configuration.configuration.optim_rowplus', index=21,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optim_eqprop', full_name='configuration.configuration.optim_eqprop', index=22,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='callcvt', full_name='configuration.configuration.callcvt', index=23,
      number=22, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_action', full_name='configuration.configuration.default_action', index=24,
      number=23, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verbosity', full_name='configuration.configuration.verbosity', index=25,
      number=24, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_parameters', full_name='configuration.configuration.additional_parameters', index=26,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=1069,
)


_INPUT_T = _descriptor.Descriptor(
  name='input_t',
  full_name='configuration.input_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='typeid', full_name='configuration.input_t.typeid', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='configuration.input_t.address', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='when', full_name='configuration.input_t.when', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='configuration.input_t.action', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iteration', full_name='configuration.input_t.iteration', index=4,
      number=100, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reg', full_name='configuration.input_t.reg', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem', full_name='configuration.input_t.mem', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indirect', full_name='configuration.input_t.indirect', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INPUT_T_INPUT_KIND,
    _INPUT_T_WHEN_T,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='input_cnt', full_name='configuration.input_t.input_cnt',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1072,
  serialized_end=1457,
)

_CONFIGURATION.fields_by_name['libcalls'].message_type = libcall__pb2._LIBCALL_POL
_CONFIGURATION.fields_by_name['syscalls'].message_type = syscall__pb2._SYSCALL_POL
_CONFIGURATION.fields_by_name['instrs'].message_type = instruction__pb2._INSTR_POL
_CONFIGURATION.fields_by_name['inputs'].message_type = _INPUT_T
_CONFIGURATION.fields_by_name['call_map'].message_type = _CALL_NAME_T
_CONFIGURATION.fields_by_name['initial_state'].message_type = common__pb2._MEMORY_T
_CONFIGURATION.fields_by_name['direction'].enum_type = common__pb2._ANALYSIS_DIRECTION_T
_CONFIGURATION.fields_by_name['solver'].enum_type = common__pb2._SOLVER_T
_CONFIGURATION.fields_by_name['callcvt'].enum_type = common__pb2._CALL_CONVENTION_T
_CONFIGURATION.fields_by_name['default_action'].enum_type = common__pb2._ACTION
_CONFIGURATION.fields_by_name['additional_parameters'].message_type = analysis__config__pb2._SPECIFIC_PARAMETERS_T
_INPUT_T.fields_by_name['typeid'].enum_type = _INPUT_T_INPUT_KIND
_INPUT_T.fields_by_name['when'].enum_type = _INPUT_T_WHEN_T
_INPUT_T.fields_by_name['action'].enum_type = common__pb2._ACTION
_INPUT_T.fields_by_name['reg'].message_type = common__pb2._REGISTER_T
_INPUT_T.fields_by_name['mem'].message_type = common__pb2._MEMORY_T
_INPUT_T.fields_by_name['indirect'].message_type = common__pb2._INDIRECT_REGISTER_T
_INPUT_T_INPUT_KIND.containing_type = _INPUT_T
_INPUT_T_WHEN_T.containing_type = _INPUT_T
_INPUT_T.oneofs_by_name['input_cnt'].fields.append(
  _INPUT_T.fields_by_name['reg'])
_INPUT_T.fields_by_name['reg'].containing_oneof = _INPUT_T.oneofs_by_name['input_cnt']
_INPUT_T.oneofs_by_name['input_cnt'].fields.append(
  _INPUT_T.fields_by_name['mem'])
_INPUT_T.fields_by_name['mem'].containing_oneof = _INPUT_T.oneofs_by_name['input_cnt']
_INPUT_T.oneofs_by_name['input_cnt'].fields.append(
  _INPUT_T.fields_by_name['indirect'])
_INPUT_T.fields_by_name['indirect'].containing_oneof = _INPUT_T.oneofs_by_name['input_cnt']
DESCRIPTOR.message_types_by_name['call_name_t'] = _CALL_NAME_T
DESCRIPTOR.message_types_by_name['configuration'] = _CONFIGURATION
DESCRIPTOR.message_types_by_name['input_t'] = _INPUT_T

call_name_t = _reflection.GeneratedProtocolMessageType('call_name_t', (_message.Message,), dict(
  DESCRIPTOR = _CALL_NAME_T,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:configuration.call_name_t)
  ))
_sym_db.RegisterMessage(call_name_t)

configuration = _reflection.GeneratedProtocolMessageType('configuration', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATION,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:configuration.configuration)
  ))
_sym_db.RegisterMessage(configuration)

input_t = _reflection.GeneratedProtocolMessageType('input_t', (_message.Message,), dict(
  DESCRIPTOR = _INPUT_T,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:configuration.input_t)
  ))
_sym_db.RegisterMessage(input_t)


# @@protoc_insertion_point(module_scope)
