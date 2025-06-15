from enum import Enum

from hal.Common import AddressSelector


class CommandTypeBase:
    """
    Base class for Command Types
    """

    def __init__(
        self,
        address: AddressSelector = AddressSelector.NONE,
        command: str = None,
        command_wait: int = -1,
        status_bit: int = -1,
        reset_command: str = None,
        wait_pause_time: int = -1,
    ):
        self.address = address
        self.command = command
        self.command_wait = command_wait
        self.status_bit = status_bit
        self.reset_command = reset_command
        self.wait_pause_time = wait_pause_time


class CommandType(Enum):
    """
    Enum for Command Types
    """

    RESET = CommandTypeBase(address=AddressSelector.SERIAL, command="X", command_wait=60000)
    QLM_ENGAGE = CommandTypeBase(address=AddressSelector.AUX, command="M1", status_bit=6, reset_command="K1", wait_pause_time=500)
    QLM_DISENGAGE = CommandTypeBase(address=AddressSelector.AUX, command="L1", status_bit=5, reset_command="K1", wait_pause_time=500)
    QLM_HALT = CommandTypeBase(address=AddressSelector.AUX, command="K1")
    QLM_DOOR_LOCK = CommandTypeBase(address=AddressSelector.AUX, command="P2")
    QLM_DOOR_UNLOCK = CommandTypeBase(address=AddressSelector.AUX, command="O2")
    SENSOR_BAR_ON = CommandTypeBase(address=AddressSelector.PICKER, command="O1")
    SENSOR_BAR_OFF = CommandTypeBase(address=AddressSelector.PICKER, command="P1")
    AUDIO_ON = CommandTypeBase(address=AddressSelector.SERIAL, command="I")
    AUDIO_OFF = CommandTypeBase(address=AddressSelector.SERIAL, command="J")
    ROLLER_IN = CommandTypeBase(address=AddressSelector.PICKER, command="J4")
    ROLLER_OUT = CommandTypeBase(address=AddressSelector.PICKER, command="I4")
    ROLLER_STOP = CommandTypeBase(address=AddressSelector.PICKER, command="K4")
    ROLLER_TO_POS_1 = CommandTypeBase(address=AddressSelector.PICKER, command="U1", status_bit=18, reset_command="K4,P1", wait_pause_time=20)
    ROLLER_TO_POS_2 = CommandTypeBase(address=AddressSelector.PICKER, command="U2", status_bit=19, reset_command="K4,P1", wait_pause_time=20)
    ROLLER_TO_POS_3 = CommandTypeBase(address=AddressSelector.PICKER, command="U3", status_bit=20, reset_command="K4,P1", wait_pause_time=20)
    ROLLER_TO_POS_4 = CommandTypeBase(address=AddressSelector.PICKER, command="T4", status_bit=15, reset_command="K4,P1", wait_pause_time=20)
    ROLLER_TO_POS_5 = CommandTypeBase(address=AddressSelector.PICKER, command="T5", status_bit=16, reset_command="K4,P1", wait_pause_time=20)
    ROLLER_TO_POS_6 = CommandTypeBase(address=AddressSelector.PICKER, command="T6", status_bit=17, reset_command="K4,P1", wait_pause_time=20)
    FRUAD_SENSOR_ENABLE_POWER_TRANSISTOR = CommandTypeBase(address=AddressSelector.PICKER, command="O4")
    FRUAD_SENSOR_DISABLE_POWER_TRANSISTOR = CommandTypeBase(address=AddressSelector.PICKER, command="P4")
    FRUAD_SENSOR_ENABLE_TRANSISTOR = CommandTypeBase(address=AddressSelector.PICKER, command="O3")
    FRUAD_SENSOR_DISABLE_TRANSISTOR = CommandTypeBase(address=AddressSelector.PICKER, command="P4")
    RINGLIGHT_ON = CommandTypeBase(address=AddressSelector.PICKER, command="O2")
    RINGLIGT_OFF = CommandTypeBase(address=AddressSelector.PICKER, command="P2")
    JUNCTION_4_ON = CommandTypeBase(address=AddressSelector.PICKER, command="O1")
    JUNCTION_4_OFF = CommandTypeBase(address=AddressSelector.PICKER, command="P1")
    AUX_SENSORS_ON = CommandTypeBase(address=AddressSelector.AUX, command="O1")
    AUX_SENSORS_OFF = CommandTypeBase(address=AddressSelector.AUX, command="P1")
    AUX_SENSORS_READ = CommandTypeBase(address=AddressSelector.AUX, command="R")
    VEND_DOOR_OPEN = CommandTypeBase(address=AddressSelector.AUX, command="M2", status_bit=8, reset_command="K2", wait_pause_time=60)
    VEND_DOOR_RENT = CommandTypeBase(address=AddressSelector.AUX, command="V", status_bit=10, reset_command="K2", wait_pause_time=60)
    VEND_DOOR_CLOSE = CommandTypeBase(address=AddressSelector.AUX, command="L2", status_bit=7, reset_command="K2", wait_pause_time=60)
    READ_PICKER_INPUTS = CommandTypeBase(address=AddressSelector.PICKER, command="R")
    GRIPPER_EXTEND_HALT = CommandTypeBase(address=AddressSelector.PICKER, command="K1")
    EXTEND_GRIPPER_ARM_FOR_TIME = CommandTypeBase(address=AddressSelector.PICKER, command="I1")
    GRIPPER_EXTEND = CommandTypeBase(address=AddressSelector.PICKER, command="L1", status_bit=5, reset_command="K1", wait_pause_time=50)
    GRIPPER_RETRACT = CommandTypeBase(address=AddressSelector.PICKER, command="M1", status_bit=6, reset_command="K1", wait_pause_time=50)
    GRIPPER_OPEN = CommandTypeBase(address=AddressSelector.PICKER, command="M3", status_bit=10, reset_command="K3", wait_pause_time=50)
    GRIPPER_RENT = CommandTypeBase(address=AddressSelector.PICKER, command="V", status_bit=12, reset_command="K3", wait_pause_time=50)
    GRIPPER_CLOSE = CommandTypeBase(address=AddressSelector.PICKER, command="L3", status_bit=9, reset_command="K3", wait_pause_time=50)
    TRACK_OPEN = CommandTypeBase(address=AddressSelector.PICKER, command="M2", status_bit=8, reset_command="K2", wait_pause_time=50)
    TRACK_CLOSE = CommandTypeBase(address=AddressSelector.PICKER, command="L2", status_bit=7, reset_command="K2", wait_pause_time=50)
    VERSION_SERIAL = CommandTypeBase(address=AddressSelector.SERIAL, command="Y")
    VERSION_PICKER = CommandTypeBase(address=AddressSelector.PICKER, command="W")
    VERSION_AUX = CommandTypeBase(address=AddressSelector.AUX, command="W")
    STATUS_PICKER = CommandTypeBase(address=AddressSelector.PICKER, command="S")
    STATUS_AUX = CommandTypeBase(address=AddressSelector.AUX, command="S")
    TURN_ON_GREEN_BUTTON_LED = CommandTypeBase(address=AddressSelector.QR, command="I1")
    TURN_OFF_GREEN_BUTTON_LED = CommandTypeBase(address=AddressSelector.QR, command="I3")
    BLINK_GREEN_BUTTON_LED = CommandTypeBase(address=AddressSelector.QR, command="I2")
    TURN_ON_RED_BUTTON_LED = CommandTypeBase(address=AddressSelector.QR, command="R1")
    TURN_OFF_RED_BUTTON_LED = CommandTypeBase(address=AddressSelector.QR, command="R3")
    BLINK_RED_BUTTON_LED = CommandTypeBase(address=AddressSelector.QR, command="R2")
    TURN_ON_GREEN_ARROW_LED = CommandTypeBase(address=AddressSelector.QR, command="T1")
    TURN_OFF_GREEN_ARROW_LED = CommandTypeBase(address=AddressSelector.QR, command="T3")
    BLINK_GREEN_ARROW_LED = CommandTypeBase(address=AddressSelector.QR, command="T2")
    TURN_ON_RED_ARROW_LED = CommandTypeBase(address=AddressSelector.QR, command="Z1")
    TURN_OFF_RED_ARROW_LED = CommandTypeBase(address=AddressSelector.QR, command="Z3")
    BLINK_RED_ARROW_LED = CommandTypeBase(address=AddressSelector.QR, command="Z2")
    TURN_ON_BACK_LIGHT = CommandTypeBase(address=AddressSelector.QR, command="W1")
    TURN_OFF_BACK_LIGHT = CommandTypeBase(address=AddressSelector.QR, command="W3")
    BLINK_BACK_LIGHT = CommandTypeBase(address=AddressSelector.QR, command="W2")
    SEND_TEXT = CommandTypeBase(address=AddressSelector.QR, command="S{0}")
    CLEAR_DISPLAY_MEMORY = CommandTypeBase(address=AddressSelector.QR, command="X{0}")
    SIDE_TERMINAL_VERSION = CommandTypeBase(address=AddressSelector.QR, command="Y")
    READ_QR_BUTTON = CommandTypeBase(address=AddressSelector.QR, command="J")
    CLEAR_QR_BUTTON_STATUS = CommandTypeBase(address=AddressSelector.QR, command="K")
    TURN_OFF_PIXELS = CommandTypeBase(address=AddressSelector.QR, command="U90")
    SET_TEXT_ONLY_DISPLAY_MODE = CommandTypeBase(address=AddressSelector.QR, command="U94")
    SET_GRAPHICS_ONLY_DISPLAY_MODE = CommandTypeBase(address=AddressSelector.QR, command="U98")
    DISPLAY_SETTING_QR = CommandTypeBase(address=AddressSelector.QR, command="U80")
    DISPLAY_SETTING_EXOR = CommandTypeBase(address=AddressSelector.QR, command="U81")
    DISPLAY_SETTING_AND = CommandTypeBase(address=AddressSelector.QR, command="U83")
    SET_START_TEXT_PAGE_POINTER = CommandTypeBase(address=AddressSelector.QR, command="M{0}")
    SET_START_GRAPHICS_PAGE_POINTER = CommandTypeBase(address=AddressSelector.QR, command="L{0}")
    SET_MEMORY_WRITE_POINTER = CommandTypeBase(address=AddressSelector.QR, command="V{0}")
    SET_TEXT_COLUMNS = CommandTypeBase(address=AddressSelector.QR, command="O{0}")
    SET_GRAPHICS_COLUMNS = CommandTypeBase(address=AddressSelector.QR, command="N{0}")
    WRITE_GRAPHIC_DATA = CommandTypeBase(address=AddressSelector.QR, command="g{0}")
    WRITE_GRAPHIC_DATA_TO_EEPROM = CommandTypeBase(address=AddressSelector.QR, command="l{0}")
    SET_EEPROM_POINTER = CommandTypeBase(address=AddressSelector.QR, command="d{0}")
    LOAD_FROM_EEPROM_TO_DISPLAY_MEMORY = CommandTypeBase(address=AddressSelector.QR, command="m")
    TERMINAL_REVISION = CommandTypeBase(address=AddressSelector.QR, command="c")
    UNKNOWN_VEND_DOOR_CLOSE = CommandTypeBase(address=AddressSelector.AUX, command="J2")
    UNKNOWN_VEND_DOOR_OPEN = CommandTypeBase(address=AddressSelector.AUX, command="I2")
    VEND_DOOR_KILL = CommandTypeBase(address=AddressSelector.AUX, command="K2")
    POWER_AUX_20 = CommandTypeBase(address=AddressSelector.AUX, command="O3")
    DISABLE_AUX_20 = CommandTypeBase(address=AddressSelector.AUX, command="P3")
    POWER_AUX_21 = CommandTypeBase(address=AddressSelector.AUX, command="O4")
    DISABLE_AUX_21 = CommandTypeBase(address=AddressSelector.AUX, command="P4")
    QLM_LIFT = CommandTypeBase(address=AddressSelector.AUX, command="M1")
    QLM_DROP = CommandTypeBase(address=AddressSelector.AUX, command="L1")
