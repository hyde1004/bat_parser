import transportpacket

class TsFilter:
    pass


class PidFilter(TsFilter):
    def __init__(self, pid):
        self.pid = pid

    def do_filter(self, packet):
        if packet.get_pid() == self.pid:
            return packet
        else:
            return None
