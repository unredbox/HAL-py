import serial


class FMEController:
    port: serial.Serial
    write_terminator: bytes

    def __init__(self):
        self.port = serial.Serial("COM1", baudrate=9600, bytesize=8, parity=serial.PARITY_NONE, stopbits=1)
        self.write_terminator = bytes([13])

    def validate_response(self, response: bytes) -> bool:
        string = response.decode()
        return string != None and string != "" and (string.index("OK") != -1 or string.index("ERR") != -1)

    def send_command(self, command):
        if self.port is None or (not self.port.is_open and not self.port.open()):
            print("[FMEController] unable to open port")
            raise Exception("Comm Error")

        try:
            self.port.write(command.encode())
            if self.write_terminator:
                self.port.write(self.write_terminator)

            response = self.port.readline()
            print(f"[FMEController] response: {response}")
        except Exception as e:
            print(f"[FMEController] error sending command: {e}")
            raise Exception("Comm Error")
