import pytest
import transportpacket

STREAM_NAME = 'D:/Stream/Airtel/BizTrip(2016-08)/11640V_32700_20160901_partial.TRP'

class TestTransportPacket:
    def test_init(self):
        with open(STREAM_NAME, 'rb') as f:
            f.seek(0)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.is_sync() == True
            assert packet.size() == transportpacket.TP_SIZE

    def test_read(self):
        with open(STREAM_NAME, 'rb') as f:
            f.seek(transportpacket.TP_SIZE*(1614-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.raw[0] == transportpacket.SYNC_BYTE
            assert packet.raw[1] == 0x40
            assert packet.raw[2] == 0x00
            assert packet.raw[3] == 0x1F

    def test_pusi(self):
        with open(STREAM_NAME, 'rb') as f:
            f.seek(0)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_pusi() == False

            f.seek(transportpacket.TP_SIZE * 1)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_pusi() == False

            f.seek(transportpacket.TP_SIZE*(1614-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_pusi() == True

    def test_pid(self):
        with open(STREAM_NAME, 'rb') as f:
            f.seek(0)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_pid() == 0x15E1

            f.seek(transportpacket.TP_SIZE * 1)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_pid() == 0x7FA

            f.seek(transportpacket.TP_SIZE * 2)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_pid() == 0x1FA6

            f.seek(transportpacket.TP_SIZE*(1614-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_pid() == 0x0

    def test_continuity_counter(self):
        with open(STREAM_NAME, 'rb') as f:
            f.seek(0)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_continuity_count() == 0x4

            f.seek(transportpacket.TP_SIZE * 1)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_continuity_count() == 0x4

            f.seek(transportpacket.TP_SIZE * 2)
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_continuity_count() == 0xE

            f.seek(transportpacket.TP_SIZE*(1614-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_continuity_count() == 0xF

    def test_adpation_field(self):
        with open(STREAM_NAME, 'rb') as f:
            f.seek(transportpacket.TP_SIZE*(40-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_adpation_field_control() == transportpacket.ADAPTATION_PAYLOAD

            f.seek(transportpacket.TP_SIZE*(1614-1))
            data = f.read(transportpacket.TP_SIZE)
            packet = transportpacket.TransportPacket(data)
            assert packet.get_adpation_field_control() == transportpacket.PAYLOAD_ONLY
