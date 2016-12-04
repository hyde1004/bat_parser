import pytest

class TransportPacket:
    def __init__(self, data):
        self.raw = data

    def display(self):
        readable = ''
        for byte in self.raw:
            print(hex(byte), end=' ')
        print()

    def is_sync(self):
        return self.raw[0] == 0x47
