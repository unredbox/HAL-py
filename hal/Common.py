from enum import Enum


class ControlBoard(Enum):
    NONE = 0
    PICKER = 1
    AUX = 2
    SERIAL = 3


class AddressSelector(Enum):
    NONE = "NONE"
    PICKER = "H001"
    AUX = "H002"
    SERIAL = "H101"
    QR = "H555"

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


def string_index(string: str, substring: str) -> int:
    """
    Returns the index of the first occurrence of substring in string, or -1 if not found.
    """
    try:
        return string.index(substring)
    except ValueError:
        return -1


class ErrorCode(Enum):
    TIMEOUT = 0
    COMMUNICATION_ERROR = 1
    MOTOR_NOT_HOMED = 2
    HOME_X_TIMEOUT = 3
    DOOR_OPEN = 4
    SENSOR_ERROR = 5
    ROLLER_TO_POS_1_TIMEOUT = 6
    ROLLER_TO_POS_2_TIMEOUT = 7
    ROLLER_TO_POS_3_TIMEOUT = 8
    ROLLER_TO_POS_4_TIMEOUT = 9
    ROLLER_TO_POS_5_TIMEOUT = 10
    ROLLER_TO_POS_6_TIMEOUT = 11
    GRIPPER_EXTEND_TIMEOUT = 12
    GRIPPER_RETRACT_TIMEOUT = 13
    TRACK_OPEN_TIMEOUT = 14
    TRACK_CLOSE_TIMEOUT = 15
    GRIPPER_OPEN_TIMEOUT = 16
    GRIPPER_CLOSE_TIMEOUT = 17
    GRIPPER_RENT_TIMEOUT = 18
    VEND_DOOR_RENT_TIMEOUT = 19
    VEND_DOOR_CLOSE_TIMEOUT = 20
    CAMERA_CAPTURE = 21
    PICKER_FULL = 22
    SLOT_EMPTY = 23
    LOCATION_OUT_OF_RANGE = 24
    ITEM_STUCK = 25
    PICKER_OBSTRUCTED = 26
    PICKER_EMPTY = 27
    SLOT_IN_USE = 28
    SENSOR_READ_ERROR = 29
    MOTOR_ERROR = 30
    DECK_OUT_OF_RANGE = 31
    INVALID_LOCATION = 32
    ARCUS_UNRESPONSIVE = 33
    QLM_NOT_ENGAGED = 34
    QLM_BAY_EMPTY = 35
    SLOT_OUT_OF_RANGE = 36
    VEND_DOOR_OPEN = 37
    OBSTRUCTION_DETECTED = 38
    INVALID_MOVE_TO_SECURE_LOCATION = 39
    DISK_NOT_FILED = 40
    MACHINE_FULL = 41
    DEVICE_NOT_CONFIGURED = 42
    FRAUD_POST_FAILURE = 43
    INVALID_DEVICE_STATE = 44
    LOWER_LIMIT_ERROR = 45
    UPPER_LIMIT_ERROR = 46
    SERVICE_CHANNEL_ERROR = 47
    STORE_ERROR = 48


class PortResponse:
    response_valid: bool = False
    response: str = None
    raw_response: bytes = None
    error: ErrorCode = None

    def is_bit_set(self, bit: int) -> bool:
        """
        Check if the specified bit is set in the response.
        """
        if self.error is not None:
            return False

        if len(self.response) < bit + 1:
            print(f"[PortResponse] is_bit_set: response is {self.response}; too short")
            return False

        return self.response[bit] == "1"

    # getter
    @property
    def comm_error(self) -> bool:
        return self.error == ErrorCode.COMMUNICATION_ERROR

    @property
    def timeout(self) -> bool:
        return self.error == ErrorCode.TIMEOUT

    @property
    def success(self) -> bool:
        return self.response_valid and self.error is None

    def __str__(self):
        return f"Response: {self.response}, Error: {self.error.name if self.error else 'None'}"


# create alias for PortResponse as CommandResponse
CommandResponse = PortResponse
