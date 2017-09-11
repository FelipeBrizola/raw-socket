
import socket, sys
from struct import *
import ipv4
import udp
import ethernet

SRC_PORT = 60000
DST_PORT = 54321

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

    message = 'abcdefghijklmnopqrstuvxz'

    # ETHERNET
    headerEthernet = ethernet.buildPackage()
    headerEthernetFormatted = ethernet.format(headerEthernet)

    # UDP
    headerUdp = udp.buildPackage(SRC_PORT, portDestination, len(message), 0)
    headerUdpFormatted = udp.format(headerUdp)

    # IP
    headerIp = ipv4.buildPackage('192.168.0.14', ipDestination, len(headerUdpFormatted))
    headerIpFormatted = ipv4.format(headerIp)    
    

    package = headerEthernetFormatted + headerIpFormatted + headerUdpFormatted + message

    print str(package)

    sock = rawsocket()
    sock.sendto(package, (ipDestination, portDestination))