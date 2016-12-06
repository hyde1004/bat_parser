import pytest
import ts_filter
import transportpacket

class SectionFilter(ts_filter.Filter)
    def __init__(self, pid, table_id):
        self.pid = pid
        self.table_id = table_id

    def do_filter(self, packet):
        pass
