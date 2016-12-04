import logging
import transportpacket

logging.basicConfig(level=logging.INFO)

STREAM_NAME = 'D:/Stream/Airtel/BizTrip(2016-08)/11640V_32700_20160901_partial.TRP'
TP_SYNC = 0x47
TP_BYTE = 188

def display_result():
    print('* filename : stream.ts')
    print('* BAT Info')
    print('     Version : 0x2')
    print('     Bouquet ID : 0x6070')
    print('         TSID : 0x0, ONID : 0x0, Service ID : 0x0, LCN : 100')
    print('     Bouquet ID : 0x6071')
    print('         TSID : 0x0, ONID : 0x0, Service ID : 0x0, LCN : 100')

def read_file(filename):
    packet_num = 0
    with open(filename, 'rb') as f:
        while packet_num < 10:
            data = f.read(TP_BYTE)
#            logging.info(hex(data[0]))
            tp = transportpacket.TransportPacket(data)
#            tp.display()
#            print('Packet {0} : {1}'.format(packet_num, tp.is_sync()))
            packet_num += 1

if __name__ == '__main__':

    read_file(STREAM_NAME)
    display_result()
