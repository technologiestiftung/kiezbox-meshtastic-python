"""Kiezbox Control
"""
import logging

from pubsub import pub # type: ignore[import-untyped]

from meshtastic.protobuf import portnums_pb2, kiezbox_control_pb2
from meshtastic.util import our_exit

def onreceive(packet, interface) -> None:
    """Callback for received GPIO responses"""
    logging.debug(f"packet:{packet} interface:{interface}")
    hw = packet["decoded"]["kiezboxctrl"]
    print(
        f'Received Kiezbox Message'
    )
    if "update" in hw:
        update = hw["update"]
        print(
            f'Received Kiezbox Update ({update})'
        )
    interface.gotResponse = True

def convert_str_to_field_type(message_cls, field_name, value_str):
    field = message_cls.DESCRIPTOR.fields_by_name[field_name]
    field_type = field.type

    from google.protobuf.descriptor import FieldDescriptor

    type_map = {
        FieldDescriptor.TYPE_INT32: int,
        FieldDescriptor.TYPE_INT64: int,
        FieldDescriptor.TYPE_UINT32: int,
        FieldDescriptor.TYPE_UINT64: int,
        FieldDescriptor.TYPE_FLOAT: float,
        FieldDescriptor.TYPE_DOUBLE: float,
        FieldDescriptor.TYPE_BOOL: lambda v: v.lower() in ("true", "1", "yes", "on"),
        FieldDescriptor.TYPE_STRING: str,
    }

    # Handle enums
    if field_type == FieldDescriptor.TYPE_ENUM:
        enum_desc = field.enum_type
        # Try to parse as a name first
        enum_value = enum_desc.values_by_name.get(value_str)
        if enum_value is not None:
            return enum_value.number
        # Fallback: maybe it's a stringified number
        try:
            return int(value_str)
        except ValueError:
            raise ValueError(f"Invalid enum value: {value_str} (expected one of {[k for k in enum_desc.values_by_name]})")

    # Handle primitives
    converter = type_map.get(field_type)
    if converter is None:
        raise TypeError(f"Unsupported field type: {field_name} (type {field_type})")
    
    try:
        return converter(value_str)
    except Exception as e:
        raise ValueError(f"Could not convert value {value_str!r} to {field_type}: {e}")

class KiezboxControlClient:
    """
    This is the client code to control/monitor simple hardware built into the
    meshtastic devices.  It is intended to be both a useful API/service and example
    code for how you can connect to your own custom meshtastic services
    """

    def __init__(self, iface):
        """
        Constructor

        iface is the already open MeshInterface instance
        """
        self.iface = iface
        ch = iface.localNode.getChannelByName("kiezbox")
        if not ch:
            our_exit(
                "Warning: No channel named 'kiezbox' was found.\n"
                "On the sending and receive nodes create a channel named 'kiezbox'.\n"
                "For example, run '--ch-add kiezbox' on one device, then '--seturl' on\n"
                "the other devices using the url from the device where the channel was added."
            )
        self.channelIndex = ch.index

        pub.subscribe(onreceive, "meshtastic.receive.kiezboxctrl")

    def _sendKiezbox(self, nodenum, r, wantResponse=False, onResponse=None):
        return self.iface.sendData(
            r,
            nodenum,
            portnums_pb2.KIEZBOX_CONTROL_APP,
            wantAck=True,
            channelIndex=self.channelIndex,
            wantResponse=wantResponse,
            onResponse=onResponse,
        )

    def set_value(self, nodenum, key, value, meta):
        """set a specific key to value in for a set of kiezboxes filtered by id or type"""
        logging.debug(f"kiezbox value target nodenum:{nodenum}")
        r = kiezbox_control_pb2.KiezboxMessage()
        c = kiezbox_control_pb2.KiezboxMessage.Control()
        if meta:
            m = kiezbox_control_pb2.KiezboxMessage.Meta()
            for k,v in meta.items():
                if hasattr(m, k):
                    print(f"{k} is a valid metadata field")
                    typed_value = convert_str_to_field_type(kiezbox_control_pb2.KiezboxMessage.Meta, k, v)
                    setattr(m, k, typed_value)
                else:
                    print(f"{k} is not a valid metadata field")
                    return
            c.meta.CopyFrom(m)
        #TODO: this only checks if 'key' is anywhere in the message,
        # we need to restrict this to a member of the oneof 'set' field later
        if hasattr(c, key):
            print(f"{key} is a valid field")
            typed_value = convert_str_to_field_type(kiezbox_control_pb2.KiezboxMessage.Control, key, value)
            setattr(c, key, typed_value)
        else:
            print(f"{key} is not a valid field")
            return
        r.control.CopyFrom(c)
        
        return self._sendKiezbox(nodenum, r)
