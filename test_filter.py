import pytest
import filter
import transportpacket

STREAM_NAME = 'D:/Stream/Airtel/BizTrip(2016-08)/11640V_32700_20160901_partial.TRP'

class TestPidFilter:
    def test_init(self):
        tp = filter.PidFilter(0x0)
        assert isinstance(tp, filter.PidFilter)

    def test_pid_00(self):
        with open(STREAM_NAME, 'rb') as f:
            data = f.read(188)
            packet = transportpacket.TransportPacket(data)
            tp = filter.PidFilter(0x0)
            filtered_packet = tp.do_filter(packet)
            assert filter_packet.raw[0] == 0x47
            assert filter_packet.raw[1] == 0x0
