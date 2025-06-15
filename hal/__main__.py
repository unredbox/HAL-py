import argparse
import time

from hal.CommandType import CommandType
from hal.FMEController import FMEController


def call_test_command(controller: FMEController, command_type: CommandType):
    """
    Calls a command on the controller and prints the response.
    """
    print(f"Calling command: {command_type.value.address.name} {command_type.name}")
    response = controller.send_command(command_type)
    if response.response_valid:
        print(f"Response: {response.response}")
    else:
        print("No valid response received.")

    time.sleep(3)


def test():
    print("[HAL] Running test commands")
    controller = FMEController()
    call_test_command(controller, CommandType.RESET)
    call_test_command(controller, CommandType.SENSOR_BAR_ON)
    call_test_command(controller, CommandType.SENSOR_BAR_OFF)
    call_test_command(controller, CommandType.AUDIO_OFF)
    call_test_command(controller, CommandType.AUDIO_ON)
    call_test_command(controller, CommandType.ROLLER_IN)
    call_test_command(controller, CommandType.ROLLER_OUT)
    call_test_command(controller, CommandType.ROLLER_STOP)
    call_test_command(controller, CommandType.RINGLIGHT_ON)
    call_test_command(controller, CommandType.RINGLIGT_OFF)
    call_test_command(controller, CommandType.AUX_SENSORS_ON)
    call_test_command(controller, CommandType.AUX_SENSORS_READ)
    call_test_command(controller, CommandType.AUX_SENSORS_OFF)
    call_test_command(controller, CommandType.VEND_DOOR_OPEN)
    call_test_command(controller, CommandType.VEND_DOOR_CLOSE)
    call_test_command(controller, CommandType.VEND_DOOR_RENT)
    call_test_command(controller, CommandType.VEND_DOOR_CLOSE)
    call_test_command(controller, CommandType.READ_PICKER_INPUTS)
    call_test_command(controller, CommandType.GRIPPER_OPEN)
    call_test_command(controller, CommandType.GRIPPER_CLOSE)
    call_test_command(controller, CommandType.GRIPPER_RENT)
    call_test_command(controller, CommandType.GRIPPER_CLOSE)
    call_test_command(controller, CommandType.GRIPPER_EXTEND)
    call_test_command(controller, CommandType.GRIPPER_RETRACT)
    call_test_command(controller, CommandType.TRACK_OPEN)
    call_test_command(controller, CommandType.TRACK_CLOSE)
    call_test_command(controller, CommandType.VERSION_SERIAL)
    call_test_command(controller, CommandType.VERSION_PICKER)
    call_test_command(controller, CommandType.VERSION_AUX)
    call_test_command(controller, CommandType.STATUS_PICKER)
    call_test_command(controller, CommandType.STATUS_AUX)


def main():
    print("[HAL] Starting HAL")
    controller = FMEController()
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HAL")
    parser.add_argument("--port", type=str, default="COM1", help="Serial port to connect to")
    parser.add_argument("--baudrate", type=int, default=9600, help="Baud rate for serial communication")
    parser.add_argument("--test", action="store_true", help="Run test commands")

    args = parser.parse_args()

    if args.test:
        test()
    else:
        main()
