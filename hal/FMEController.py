import time

import serial

from hal.CommandType import CommandType, CommandTypeBase
from hal.Common import CommandResponse, ErrorCode, PortResponse, string_index
from hal.Port import Port


class FMEController:
    port: Port

    def __init__(self, port: str = "COM1", baudrate: int = 9600):
        self.port = Port(port=port, baudrate=baudrate)
        self.port.write_terminator = bytes([13])
        self.port.validate_response = self.validate_response

    def validate_response(self, response: bytes) -> bool:
        string = response.decode()
        return string != None and string != "" and (string_index(string, "OK") != -1 or string_index(string, "ERR") != -1)

    def send_command(self, command: CommandType):
        print(f"[FMEController] Sending command: {command.value.address.name} {command.name}")

        response = CommandResponse()

        command: CommandTypeBase = command.value
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
