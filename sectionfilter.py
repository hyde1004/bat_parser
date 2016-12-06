import pytest
import filter
import transportpacket

class SectionFilter(filter.Filter)
    def __init__(self, pid, table_id):
        self.pid = pid
        self.table_id = table_id

    def do_filter(self, packet):
        pass
