TP_SIZE = 188
SYNC_BYTE = 0x47

class TransportPacket:
    def __init__(self, data):
        self.raw = data

    def display(self):
        readable = ''
        for byte in self.raw:
            print(hex(byte), end=' ')
        print()

    def is_sync(self):
        return self.raw[0] == SYNC_BYTE

    def size(self):
        return len(self.raw)

    def get_pid(self):
        return ( self.raw[1] << 8 | self.raw[2] ) & 0x1FFF

    def get_pusi(self):
        return ((self.raw[1] & 0x40) >> 6) == 1

    def get_continuity_count(self):
        return self.raw[3] & 0x0F
