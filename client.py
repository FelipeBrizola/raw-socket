
import socket, sys
from struct import *
import ipv4
import udp

SRC_PORT = 60000
DST_PORT = 60000

def checksum(msg):
    s = 0
     
    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8 )
        s = s + w
     
    s = (s>>16) + (s & 0xffff);
    s = s + (s >> 16);
     
    #complement and mask to 4 byte short
    s = ~s & 0xffff
     
    return s

def rawsocket():
    # IPPROTO_UDP
    # IPPROTO_RAW
    try:
        return socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()


        



if __name__ == "__main__":
    ipDestination = sys.argv[1]
    portDestination = int(sys.argv[2])

    message = 'abc'

    headerIp = ipv4.buildPackage('127.0.0.1', ipDestination)
    headerIpFormatted = ipv4.format(headerIp)

    headerUdp = udp.buildPackage(SRC_PORT, DST_PORT, len(message), 0)
    headerUdpFormatted = udp.format(headerUdp)
    

    package = headerIpFormatted + headerUdpFormatted + message

    sock = rawsocket()
    sock.sendto(package, (ipDestination, portDestination))