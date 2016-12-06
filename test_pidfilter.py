import pytest
import pidfilter
import transportpacket

STREAM_NAME = 'D:/Stream/Airtel/BizTrip(2016-08)/11640V_32700_20160901_partial.TRP'

class TestPidFilter:
    def test_init(self):
        tp = pidfilter.PidFilter(0x0)
        assert isinstance(tp, pidfilter.PidFilter)

    def test_pid_00(self):
        with open(STREAM_NAME, 'rb') as f:
            f.seek(0)
            data = f.read(188)
            packet = transportpacket.TransportPacket(data)
            pid_filter = pidfilter.PidFilter(0x0)
            filtered_packet = pid_filter.do_filter(packet)
            assert filtered_packet == None

            f.seek(transportpacket.TP_SIZE*(1614-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            pid_filter = pidfilter.PidFilter(0x0)
            filtered_packet = pid_filter.do_filter(packet)
            assert filtered_packet.get_pid() == 0

            f.seek(transportpacket.TP_SIZE*(8038-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            pid_filter = pidfilter.PidFilter(0x14)
            filtered_packet = pid_filter.do_filter(packet)
            assert filtered_packet.get_pid() == 0x14
