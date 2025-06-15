import time

import serial

from hal.CommandType import CommandType, CommandTypeBase
from hal.Common import CommandResponse, string_index


class FMEController:
    port: serial.Serial
    write_terminator: bytes

    def __init__(self, port: str = "COM1"):
        self.port = serial.Serial(port=port, baudrate=9600, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=1)
        print(f"[FMEController] opened port: {self.port.name}")
        self.write_terminator = bytes([13])

    def validate_response(self, response: bytes) -> bool:
        string = response.decode()
        return string != None and string != "" and (string_index(string, "OK") != -1 or string_index(string, "ERR") != -1)

    def read_inner(self, response: CommandResponse, timeout: int = 5000) -> bytes:
        # read until validate_response passes, timeout in ms
        self.port.timeout = timeout / 1000  # convert ms to seconds
        data = b""
        while True:
            data += self.port.read(1)
            if self.validate_response(data):
                response.response = data.decode()
                response.response_valid = True
                break

    def send_command(self, command: CommandType):
        command: CommandTypeBase = command.value if isinstance(command, CommandType) else command
        if command is None or command.address.is_none:
            print("[FMEController] invalid command")
            raise Exception("Invalid Command")

        if self.port is None or (not self.port.is_open and not self.port.open()):
            print("[FMEController] unable to open port")
            raise Exception("Comm Error")

        response = CommandResponse()
        print(f"[FMEController] sending command: {command.address.name}:{command.command}")

        try:
            # send selector
            self.port.write(command.address.value.encode() + self.write_terminator)

            # read response
            self.read_inner(response, 5000)
            print(f"[FMEController] selector response: {response.response}")
        except Exception as e:
            print(f"[FMEController] error sending selector: {e}")
            return response

        try:
            # send command
            self.port.write(command.command.encode() + self.write_terminator)

            # read response
            self.read_inner(response, 5000)
            print(f"[FMEController] command response: {response.response}")
        except Exception as e:
            print(f"[FMEController] error sending command: {e}")
            return response

        return response
