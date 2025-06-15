import time
from typing import Callable

import serial

from hal.Common import ErrorCode, PortResponse


class Port:
    port: serial.Serial
    write_terminator: bytes
    write_pause: int = 10
    read_timeout: int = None
    write_timeout: int = 5000
    open_pause: int = 3000
    validate_response: Callable[[bytes], bool]

    def __init__(self, port: str = "COM1", baudrate: int = 9600):
        self.port = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=8,
            parity=serial.PARITY_NONE,
            stopbits=1,
            timeout=self.read_timeout,
            write_timeout=self.write_timeout,
        )

    def open(self):
        if self.port is None:
            print("[Port] port is not initialized")
            return False

        if self.port.is_open:
            print("[Port] port is already open")
            return True

        try:
            self.port.open()
            self.port.timeout = self.read_timeout / 1000  # convert ms to seconds
            self.port.write_timeout = self.write_timeout / 1000  # convert ms to seconds
            self.port.rts = True  # enable RTS (Request to Send)
            self.port.dtr = True  # enable DTR (Data Terminal Ready)
            time.sleep(self.open_pause / 1000)  # convert ms to seconds
            print(f"[Port] port {self.port.name} opened successfully")
        except serial.SerialException as e:
            print(f"[Port] error opening port: {e}")
            return False

        if self.reset_port_buffers(True):
            return True

        self.close()
        return False

    def close(self):
        if self.port is None or not self.port.is_open:
            print("[Port] port is not open")
            return False

        try:
            self.port.rts = True
            self.port.dtr = False
            self.port.close()
            print(f"[Port] port {self.port.name} closed successfully")
        except serial.SerialException as e:
            print(f"[Port] error closing port: {e}")
            return False

        return True

    def reset_port_buffers(self, reset_out: bool = False) -> bool:
        if self.port is None or not self.port.is_open:
            print("[Port] port is not open")
            return False

        # clear input and output buffers
        self.port.reset_input_buffer()
        if reset_out:
            self.port.reset_output_buffer()
        print("[Port] port buffers reset")
        return True

    def read_inner(self, response: PortResponse, read_timeout: int = 5000) -> bytes:
        # read until validate_response passes, timeout in ms
        self.port.timeout = read_timeout / 1000  # convert ms to seconds
        data = b""
        while True:
            data += self.port.read(1)
            if self.validate_response(data):
                response.raw_response = data
                response.response = data.decode()
                response.response_valid = True
                break

    def on_send_recv(self, command: bytes, read_timeout: int = 5000) -> PortResponse:
        response = PortResponse()

        # first we write the command selector
        try:
            self.port.write(command)
            if self.write_terminator != None:
                self.port.write(self.write_terminator)
            # wait for write_pause
            time.sleep(self.write_pause / 1000)  # convert ms to seconds
        except Exception as e:
            print(f"[Port] error sending command: {e}")
            response.error = ErrorCode.COMMUNICATION_ERROR
            return response

        self.read_inner(response, read_timeout)
        print(f"[Port] command response: {response.response}")

        return response

    def send_recv(self, data: str, read_timeout: int = 5000) -> PortResponse:
        self.reset_port_buffers()
        if not self.port.is_open:
            print("[Port] send/recv: port is not open")
            response = PortResponse()
            response.error = ErrorCode.COMMUNICATION_ERROR
            return response

        response = self.on_send_recv(data.encode(), read_timeout)
        print(f"[Port] Read {('ok' if not response.comm_error else 'timed out')}, bytes {len(response.response)}")
        print(response.response)

        return response
