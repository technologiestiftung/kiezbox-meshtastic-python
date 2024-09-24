"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PortNum:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PortNumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PortNum.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_APP: _PortNum.ValueType  # 0
    """
    Deprecated: do not use in new code (formerly called OPAQUE)
    A message sent from a device outside of the mesh, in a form the mesh does not understand
    NOTE: This must be 0, because it is documented in IMeshService.aidl to be so
    ENCODING: binary undefined
    """
    TEXT_MESSAGE_APP: _PortNum.ValueType  # 1
    """
    A simple UTF-8 text message, which even the little micros in the mesh
    can understand and show on their screen eventually in some circumstances
    even signal might send messages in this form (see below)
    ENCODING: UTF-8 Plaintext (?)
    """
    REMOTE_HARDWARE_APP: _PortNum.ValueType  # 2
    """
    Reserved for built-in GPIO/example app.
    See remote_hardware.proto/HardwareMessage for details on the message sent/received to this port number
    ENCODING: Protobuf
    """
    POSITION_APP: _PortNum.ValueType  # 3
    """
    The built-in position messaging app.
    Payload is a Position message.
    ENCODING: Protobuf
    """
    NODEINFO_APP: _PortNum.ValueType  # 4
    """
    The built-in user info app.
    Payload is a User message.
    ENCODING: Protobuf
    """
    ROUTING_APP: _PortNum.ValueType  # 5
    """
    Protocol control packets for mesh protocol use.
    Payload is a Routing message.
    ENCODING: Protobuf
    """
    ADMIN_APP: _PortNum.ValueType  # 6
    """
    Admin control packets.
    Payload is a AdminMessage message.
    ENCODING: Protobuf
    """
    TEXT_MESSAGE_COMPRESSED_APP: _PortNum.ValueType  # 7
    """
    Compressed TEXT_MESSAGE payloads.
    ENCODING: UTF-8 Plaintext (?) with Unishox2 Compression
    NOTE: The Device Firmware converts a TEXT_MESSAGE_APP to TEXT_MESSAGE_COMPRESSED_APP if the compressed
    payload is shorter. There's no need for app developers to do this themselves. Also the firmware will decompress
    any incoming TEXT_MESSAGE_COMPRESSED_APP payload and convert to TEXT_MESSAGE_APP.
    """
    WAYPOINT_APP: _PortNum.ValueType  # 8
    """
    Waypoint payloads.
    Payload is a Waypoint message.
    ENCODING: Protobuf
    """
    AUDIO_APP: _PortNum.ValueType  # 9
    """
    Audio Payloads.
    Encapsulated codec2 packets. On 2.4 GHZ Bandwidths only for now
    ENCODING: codec2 audio frames
    NOTE: audio frames contain a 3 byte header (0xc0 0xde 0xc2) and a one byte marker for the decompressed bitrate.
    This marker comes from the 'moduleConfig.audio.bitrate' enum minus one.
    """
    DETECTION_SENSOR_APP: _PortNum.ValueType  # 10
    """
    Same as Text Message but originating from Detection Sensor Module.
    NOTE: This portnum traffic is not sent to the public MQTT starting at firmware version 2.2.9
    """
    REPLY_APP: _PortNum.ValueType  # 32
    """
    Provides a 'ping' service that replies to any packet it receives.
    Also serves as a small example module.
    ENCODING: ASCII Plaintext
    """
    IP_TUNNEL_APP: _PortNum.ValueType  # 33
    """
    Used for the python IP tunnel feature
    ENCODING: IP Packet. Handled by the python API, firmware ignores this one and pases on.
    """
    PAXCOUNTER_APP: _PortNum.ValueType  # 34
    """
    Paxcounter lib included in the firmware
    ENCODING: protobuf
    """
    SERIAL_APP: _PortNum.ValueType  # 64
    """
    Provides a hardware serial interface to send and receive from the Meshtastic network.
    Connect to the RX/TX pins of a device with 38400 8N1. Packets received from the Meshtastic
    network is forwarded to the RX pin while sending a packet to TX will go out to the Mesh network.
    Maximum packet size of 240 bytes.
    Module is disabled by default can be turned on by setting SERIAL_MODULE_ENABLED = 1 in SerialPlugh.cpp.
    ENCODING: binary undefined
    """
    STORE_FORWARD_APP: _PortNum.ValueType  # 65
    """
    STORE_FORWARD_APP (Work in Progress)
    Maintained by Jm Casler (MC Hamster) : jm@casler.org
    ENCODING: Protobuf
    """
    RANGE_TEST_APP: _PortNum.ValueType  # 66
    """
    Optional port for messages for the range test module.
    ENCODING: ASCII Plaintext
    NOTE: This portnum traffic is not sent to the public MQTT starting at firmware version 2.2.9
    """
    TELEMETRY_APP: _PortNum.ValueType  # 67
    """
    Provides a format to send and receive telemetry data from the Meshtastic network.
    Maintained by Charles Crossan (crossan007) : crossan007@gmail.com
    ENCODING: Protobuf
    """
    ZPS_APP: _PortNum.ValueType  # 68
    """
    Experimental tools for estimating node position without a GPS
    Maintained by Github user a-f-G-U-C (a Meshtastic contributor)
    Project files at https://github.com/a-f-G-U-C/Meshtastic-ZPS
    ENCODING: arrays of int64 fields
    """
    SIMULATOR_APP: _PortNum.ValueType  # 69
    """
    Used to let multiple instances of Linux native applications communicate
    as if they did using their LoRa chip.
    Maintained by GitHub user GUVWAF.
    Project files at https://github.com/GUVWAF/Meshtasticator
    ENCODING: Protobuf (?)
    """
    TRACEROUTE_APP: _PortNum.ValueType  # 70
    """
    Provides a traceroute functionality to show the route a packet towards
    a certain destination would take on the mesh. Contains a RouteDiscovery message as payload.
    ENCODING: Protobuf
    """
    NEIGHBORINFO_APP: _PortNum.ValueType  # 71
    """
    Aggregates edge info for the network by sending out a list of each node's neighbors
    ENCODING: Protobuf
    """
    ATAK_PLUGIN: _PortNum.ValueType  # 72
    """
    ATAK Plugin
    Portnum for payloads from the official Meshtastic ATAK plugin
    """
    MAP_REPORT_APP: _PortNum.ValueType  # 73
    """
    Provides unencrypted information about a node for consumption by a map via MQTT
    """
    POWERSTRESS_APP: _PortNum.ValueType  # 74
    """
    PowerStress based monitoring support (for automated power consumption testing)
    """
    PRIVATE_APP: _PortNum.ValueType  # 256
    """
    Private applications should use portnums >= 256.
    To simplify initial development and testing you can use "PRIVATE_APP"
    in your code without needing to rebuild protobuf files (via [regen-protos.sh](https://github.com/meshtastic/firmware/blob/master/bin/regen-protos.sh))
    """
    ATAK_FORWARDER: _PortNum.ValueType  # 257
    """
    ATAK Forwarder Module https://github.com/paulmandal/atak-forwarder
    ENCODING: libcotshrink
    """
    KIEZBOX_CONTROL_APP: _PortNum.ValueType  # 258
    """
    Reserved for built-in GPIO/example app.
    See remote_hardware.proto/HardwareMessage for details on the message sent/received to this port number
    ENCODING: Protobuf
    """
    MAX: _PortNum.ValueType  # 511
    """
    Currently we limit port nums to no higher than this value
    """

class PortNum(_PortNum, metaclass=_PortNumEnumTypeWrapper):
    """
    For any new 'apps' that run on the device or via sister apps on phones/PCs they should pick and use a
    unique 'portnum' for their application.
    If you are making a new app using meshtastic, please send in a pull request to add your 'portnum' to this
    master table.
    PortNums should be assigned in the following range:
    0-63   Core Meshtastic use, do not use for third party apps
    64-127 Registered 3rd party apps, send in a pull request that adds a new entry to portnums.proto to  register your application
    256-511 Use one of these portnums for your private applications that you don't want to register publically
    All other values are reserved.
    Note: This was formerly a Type enum named 'typ' with the same id #
    We have change to this 'portnum' based scheme for specifying app handlers for particular payloads.
    This change is backwards compatible by treating the legacy OPAQUE/CLEAR_TEXT values identically.
    """

UNKNOWN_APP: PortNum.ValueType  # 0
"""
Deprecated: do not use in new code (formerly called OPAQUE)
A message sent from a device outside of the mesh, in a form the mesh does not understand
NOTE: This must be 0, because it is documented in IMeshService.aidl to be so
ENCODING: binary undefined
"""
TEXT_MESSAGE_APP: PortNum.ValueType  # 1
"""
A simple UTF-8 text message, which even the little micros in the mesh
can understand and show on their screen eventually in some circumstances
even signal might send messages in this form (see below)
ENCODING: UTF-8 Plaintext (?)
"""
REMOTE_HARDWARE_APP: PortNum.ValueType  # 2
"""
Reserved for built-in GPIO/example app.
See remote_hardware.proto/HardwareMessage for details on the message sent/received to this port number
ENCODING: Protobuf
"""
POSITION_APP: PortNum.ValueType  # 3
"""
The built-in position messaging app.
Payload is a Position message.
ENCODING: Protobuf
"""
NODEINFO_APP: PortNum.ValueType  # 4
"""
The built-in user info app.
Payload is a User message.
ENCODING: Protobuf
"""
ROUTING_APP: PortNum.ValueType  # 5
"""
Protocol control packets for mesh protocol use.
Payload is a Routing message.
ENCODING: Protobuf
"""
ADMIN_APP: PortNum.ValueType  # 6
"""
Admin control packets.
Payload is a AdminMessage message.
ENCODING: Protobuf
"""
TEXT_MESSAGE_COMPRESSED_APP: PortNum.ValueType  # 7
"""
Compressed TEXT_MESSAGE payloads.
ENCODING: UTF-8 Plaintext (?) with Unishox2 Compression
NOTE: The Device Firmware converts a TEXT_MESSAGE_APP to TEXT_MESSAGE_COMPRESSED_APP if the compressed
payload is shorter. There's no need for app developers to do this themselves. Also the firmware will decompress
any incoming TEXT_MESSAGE_COMPRESSED_APP payload and convert to TEXT_MESSAGE_APP.
"""
WAYPOINT_APP: PortNum.ValueType  # 8
"""
Waypoint payloads.
Payload is a Waypoint message.
ENCODING: Protobuf
"""
AUDIO_APP: PortNum.ValueType  # 9
"""
Audio Payloads.
Encapsulated codec2 packets. On 2.4 GHZ Bandwidths only for now
ENCODING: codec2 audio frames
NOTE: audio frames contain a 3 byte header (0xc0 0xde 0xc2) and a one byte marker for the decompressed bitrate.
This marker comes from the 'moduleConfig.audio.bitrate' enum minus one.
"""
DETECTION_SENSOR_APP: PortNum.ValueType  # 10
"""
Same as Text Message but originating from Detection Sensor Module.
NOTE: This portnum traffic is not sent to the public MQTT starting at firmware version 2.2.9
"""
REPLY_APP: PortNum.ValueType  # 32
"""
Provides a 'ping' service that replies to any packet it receives.
Also serves as a small example module.
ENCODING: ASCII Plaintext
"""
IP_TUNNEL_APP: PortNum.ValueType  # 33
"""
Used for the python IP tunnel feature
ENCODING: IP Packet. Handled by the python API, firmware ignores this one and pases on.
"""
PAXCOUNTER_APP: PortNum.ValueType  # 34
"""
Paxcounter lib included in the firmware
ENCODING: protobuf
"""
SERIAL_APP: PortNum.ValueType  # 64
"""
Provides a hardware serial interface to send and receive from the Meshtastic network.
Connect to the RX/TX pins of a device with 38400 8N1. Packets received from the Meshtastic
network is forwarded to the RX pin while sending a packet to TX will go out to the Mesh network.
Maximum packet size of 240 bytes.
Module is disabled by default can be turned on by setting SERIAL_MODULE_ENABLED = 1 in SerialPlugh.cpp.
ENCODING: binary undefined
"""
STORE_FORWARD_APP: PortNum.ValueType  # 65
"""
STORE_FORWARD_APP (Work in Progress)
Maintained by Jm Casler (MC Hamster) : jm@casler.org
ENCODING: Protobuf
"""
RANGE_TEST_APP: PortNum.ValueType  # 66
"""
Optional port for messages for the range test module.
ENCODING: ASCII Plaintext
NOTE: This portnum traffic is not sent to the public MQTT starting at firmware version 2.2.9
"""
TELEMETRY_APP: PortNum.ValueType  # 67
"""
Provides a format to send and receive telemetry data from the Meshtastic network.
Maintained by Charles Crossan (crossan007) : crossan007@gmail.com
ENCODING: Protobuf
"""
ZPS_APP: PortNum.ValueType  # 68
"""
Experimental tools for estimating node position without a GPS
Maintained by Github user a-f-G-U-C (a Meshtastic contributor)
Project files at https://github.com/a-f-G-U-C/Meshtastic-ZPS
ENCODING: arrays of int64 fields
"""
SIMULATOR_APP: PortNum.ValueType  # 69
"""
Used to let multiple instances of Linux native applications communicate
as if they did using their LoRa chip.
Maintained by GitHub user GUVWAF.
Project files at https://github.com/GUVWAF/Meshtasticator
ENCODING: Protobuf (?)
"""
TRACEROUTE_APP: PortNum.ValueType  # 70
"""
Provides a traceroute functionality to show the route a packet towards
a certain destination would take on the mesh. Contains a RouteDiscovery message as payload.
ENCODING: Protobuf
"""
NEIGHBORINFO_APP: PortNum.ValueType  # 71
"""
Aggregates edge info for the network by sending out a list of each node's neighbors
ENCODING: Protobuf
"""
ATAK_PLUGIN: PortNum.ValueType  # 72
"""
ATAK Plugin
Portnum for payloads from the official Meshtastic ATAK plugin
"""
MAP_REPORT_APP: PortNum.ValueType  # 73
"""
Provides unencrypted information about a node for consumption by a map via MQTT
"""
POWERSTRESS_APP: PortNum.ValueType  # 74
"""
PowerStress based monitoring support (for automated power consumption testing)
"""
PRIVATE_APP: PortNum.ValueType  # 256
"""
Private applications should use portnums >= 256.
To simplify initial development and testing you can use "PRIVATE_APP"
in your code without needing to rebuild protobuf files (via [regen-protos.sh](https://github.com/meshtastic/firmware/blob/master/bin/regen-protos.sh))
"""
ATAK_FORWARDER: PortNum.ValueType  # 257
"""
ATAK Forwarder Module https://github.com/paulmandal/atak-forwarder
ENCODING: libcotshrink
"""
KIEZBOX_CONTROL_APP: PortNum.ValueType  # 258
"""
Reserved for built-in GPIO/example app.
See remote_hardware.proto/HardwareMessage for details on the message sent/received to this port number
ENCODING: Protobuf
"""
MAX: PortNum.ValueType  # 511
"""
Currently we limit port nums to no higher than this value
"""
global___PortNum = PortNum
