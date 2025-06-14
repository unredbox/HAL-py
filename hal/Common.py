from enum import Enum


class ControlBoard(Enum):
    NONE = 0
    PICKER = 1
    AUX = 2
    SERIAL = 3


class AddressSelector(Enum):
    NONE = 0
    PICKER = 1  # H001
    AUX = 2  # H002
    SERIAL = 3  # H101
    QR = 4  # H555

    def __str__(self):
        return self.name.lower()

    @property
    def is_none(self) -> bool:
        return self == AddressSelector.NONE

    @property
    def is_picker(self) -> bool:
        return self == AddressSelector.PICKER

    @property
    def is_aux(self) -> bool:
        return self == AddressSelector.AUX

    @property
    def is_serial(self) -> bool:
        return self == AddressSelector.SERIAL
