import pytest
import sectionfilter
import transportpacket

STREAM_NAME = 'D:/Stream/Airtel/BizTrip(2016-08)/11640V_32700_20160901_partial.TRP'

class TestSectionFilter:
    def test_init(self):
        section = sectionfilter.SectionFilter(0x0, 0x0)
        assert isinstance(section, sectionfilter.SectionFilter)

    def test_pat(self):
        with open(STREAM_NAME, 'rb') as f:
            f.seek(0)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            pat_filter = sectionfilter.SectionFilter(0x0, 0x0)
            filtered_packet = pat_filter.do_filter(packet)
            assert filtered_packet == None

            f.seek(transportpacket.TP_SIZE*(1614-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            pat_filter = sectionfilter.SectionFilter(0x0, 0x0)
            filtered_packet = pat_filter.do_filter(packet)
            assert filtered_packet.get_pid() == 0
