# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/protobuf/kiezbox_control.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)meshtastic/protobuf/kiezbox_control.proto\x12\x13meshtastic.protobuf\"\xb4\x03\n\x0eKiezboxMessage\x12\x46\n\x06status\x18\x04 \x01(\x0b\x32\x31.meshtastic.protobuf.KiezboxMessage.KiezboxStatusH\x00\x88\x01\x01\x1a\xce\x02\n\rKiezboxStatus\x12\x0e\n\x06\x62ox_id\x18\x01 \x01(\r\x12\x0f\n\x07\x64ist_id\x18\x02 \x01(\r\x12\x16\n\x0erouter_powered\x18\x03 \x01(\x08\x12\x11\n\tunix_time\x18\x04 \x01(\x03\x12\x17\n\x0ftemperature_out\x18\x05 \x01(\x05\x12\x16\n\x0etemperature_in\x18\x06 \x01(\x05\x12\x13\n\x0bhumidity_in\x18\x07 \x01(\x05\x12\x15\n\rsolar_voltage\x18\x08 \x01(\x05\x12\x13\n\x0bsolar_power\x18\t \x01(\x05\x12\x18\n\x10solar_energy_day\x18\n \x01(\x05\x12\x1a\n\x12solar_energy_total\x18\x0b \x01(\x05\x12\x17\n\x0f\x62\x61ttery_voltage\x18\x0c \x01(\x05\x12\x17\n\x0f\x62\x61ttery_current\x18\r \x01(\x05\x12\x17\n\x0ftemperature_rtc\x18\x0e \x01(\x05\x42\t\n\x07_statusBc\n\x13\x63om.geeksville.meshB\x0eKiezboxControlZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.protobuf.kiezbox_control_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\016KiezboxControlZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _globals['_KIEZBOXMESSAGE']._serialized_start=67
  _globals['_KIEZBOXMESSAGE']._serialized_end=503
  _globals['_KIEZBOXMESSAGE_KIEZBOXSTATUS']._serialized_start=158
  _globals['_KIEZBOXMESSAGE_KIEZBOXSTATUS']._serialized_end=492
# @@protoc_insertion_point(module_scope)
