"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class KiezboxMessage(google.protobuf.message.Message):
    """
    This message is used for
    KIEZBOX_CONTROL_APP PortNums.

    TODO: Add other message types/features
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class KiezboxStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KB_ID_FIELD_NUMBER: builtins.int
        UNIX_TIME_FIELD_NUMBER: builtins.int
        TEMPERATURE_OUT_FIELD_NUMBER: builtins.int
        TEMPERATURE_IN_FIELD_NUMBER: builtins.int
        HUMIDITY_IN_FIELD_NUMBER: builtins.int
        SOLAR_VOLTAGE_FIELD_NUMBER: builtins.int
        SOLAR_POWER_FIELD_NUMBER: builtins.int
        SOLAR_ENERGY_DAY_FIELD_NUMBER: builtins.int
        SOLAR_ENERGY_TOTAL_FIELD_NUMBER: builtins.int
        BATTERY_VOLTAGE_FIELD_NUMBER: builtins.int
        BATTERY_CURRENT_FIELD_NUMBER: builtins.int
        TEMPERATURE_RTC_FIELD_NUMBER: builtins.int
        kb_id: builtins.int
        """only 16 bit used"""
        unix_time: builtins.int
        """seconds since unix epoch"""
        temperature_out: builtins.int
        """in uCelsius"""
        temperature_in: builtins.int
        """in uCelsius"""
        humidity_in: builtins.int
        """in u%"""
        solar_voltage: builtins.int
        """in mV"""
        solar_power: builtins.int
        """in W"""
        solar_energy_day: builtins.int
        """in kWh/100"""
        solar_energy_total: builtins.int
        """in kWh/100"""
        battery_voltage: builtins.int
        """in mV"""
        battery_current: builtins.int
        """in mV"""
        temperature_rtc: builtins.int
        """in uClesius"""
        def __init__(
            self,
            *,
            kb_id: builtins.int = ...,
            unix_time: builtins.int = ...,
            temperature_out: builtins.int = ...,
            temperature_in: builtins.int = ...,
            humidity_in: builtins.int = ...,
            solar_voltage: builtins.int = ...,
            solar_power: builtins.int = ...,
            solar_energy_day: builtins.int = ...,
            solar_energy_total: builtins.int = ...,
            battery_voltage: builtins.int = ...,
            battery_current: builtins.int = ...,
            temperature_rtc: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["battery_current", b"battery_current", "battery_voltage", b"battery_voltage", "humidity_in", b"humidity_in", "kb_id", b"kb_id", "solar_energy_day", b"solar_energy_day", "solar_energy_total", b"solar_energy_total", "solar_power", b"solar_power", "solar_voltage", b"solar_voltage", "temperature_in", b"temperature_in", "temperature_out", b"temperature_out", "temperature_rtc", b"temperature_rtc", "unix_time", b"unix_time"]) -> None: ...

    STATUS_FIELD_NUMBER: builtins.int
    @property
    def status(self) -> global___KiezboxMessage.KiezboxStatus: ...
    def __init__(
        self,
        *,
        status: global___KiezboxMessage.KiezboxStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_status", b"_status", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_status", b"_status", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_status", b"_status"]) -> typing.Literal["status"] | None: ...

global___KiezboxMessage = KiezboxMessage
