import pytest
import ts_filter
import transportpacket

class SectionFilter(ts_filter.TsFilter):
    def __init__(self, pid, table_id):
        self.pid = pid
        self.table_id = table_id

    def do_filter(self, packet):
        if self.pid == packet.get_pid() and self.pid == packet.get_pid():
            return packet
        else:
            return None
