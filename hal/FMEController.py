import time

import serial

from hal.CommandType import CommandType, CommandTypeBase
from hal.Common import CommandResponse, ErrorCode, PortResponse, TrackState, string_index
from hal.Port import Port


class FMEController:
    port: Port

    def __init__(self, port: str = "COM1", baudrate: int = 9600):
        self.port = Port(port=port, baudrate=baudrate)
        self.port.write_terminator = bytes([13])
        self.port.validate_response = self.validate_response

    def set_track(self, track_state: TrackState) -> PortResponse:
        command = CommandType.TRACK_OPEN if track_state == TrackState.OPEN else CommandType.TRACK_CLOSE
        return self.retryable_command(command.value, retries=2, delay=5000)

    def validate_response(self, response: bytes) -> bool:
        string = response.decode()
        return string != None and string != "" and (string_index(string, "OK") != -1 or string_index(string, "ERR") != -1)

    def send_command(self, command: CommandTypeBase) -> CommandResponse:
        print(f"[FMEController] Sending command: {command.value.address.name} {command.name}")

        response = CommandResponse()

        if not self.port or not self.port.open():
            print("[FMEController] unable to open port")
            response.error = ErrorCode.COMMUNICATION_ERROR
            return response

        try:
            response = command.execute(self.port)
        except Exception as e:
            print(f"[FMEController] error sending command: {e}")
            response.error = ErrorCode.COMMUNICATION_ERROR

        return response

    def retryable_command(self, command: CommandTypeBase, retries: int, delay: int):
        response = CommandResponse()
        command.operation_timeout = delay

        for i in range(retries):
            response = self.send_command(command)
            if response.success or response.comm_error:
                return response

        return response
