import ts_filter

class PidFilter(ts_filter.TsFilter):
    def __init__(self, pid):
        self.pid = pid

    def do_filter(self, packet):
        if packet.get_pid() == self.pid:
            return packet
        else:
            return None
