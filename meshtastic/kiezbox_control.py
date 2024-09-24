"""Kiezbox Control
"""
import logging

from pubsub import pub # type: ignore[import-untyped]

from meshtastic.protobuf import portnums_pb2, kiezbox_control_pb2
from meshtastic.util import our_exit


def onreceive(packet, interface):
    """Callback for received GPIO responses"""
    logging.debug(f"packet:{packet} interface:{interface}")
    print(
        f'Received KiezboxControl'
    )
    interface.gotResponse = True


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

    def _sendHardware(self, nodeid, r, wantResponse=False, onResponse=None):
        if not nodeid:
            our_exit(
                r"Warning: Must use a destination node ID for this operation (use --dest \!xxxxxxxxx)"
            )
        return self.iface.sendData(
            r,
            nodeid,
            portnums_pb2.KIEZBOX_CONTROL_APP,
            wantAck=True,
            channelIndex=self.channelIndex,
            wantResponse=wantResponse,
            onResponse=onResponse,
        )

    def watchstatus(self, nodeid):
        """Watch the specified bits from GPIO inputs on the device for changes"""
        logging.debug(f"watchstatus nodeid:{nodeid}")
        r = kiezbox_control_pb2.KiezboxMessage()
        return self._sendHardware(nodeid, r)
