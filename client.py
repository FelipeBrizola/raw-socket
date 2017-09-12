
import socket, sys
from struct import *
import arp
import ipv4
import udp
import ethernet

SRC_PORT = 60000
DST_PORT = 54321

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
        #return socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        return socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    

if __name__ == "__main__":
    ipDestination = sys.argv[1]
    portDestination = int(sys.argv[2])

    message = '1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a'

    headerEthernet = ethernet.buildPackage()
    headerEthernetFormatted = ethernet.format(headerEthernet)

    headerUdp = udp.buildPackage(SRC_PORT, portDestination, len(message), 0)
    headerUdpFormatted = udp.format(headerUdp)

    headerIp = ipv4.buildPackage('192.168.0.14', ipDestination, len(headerUdpFormatted))
    headerIpFormatted = ipv4.format(headerIp)    
    

    package = headerEthernetFormatted + headerIpFormatted + headerUdpFormatted + message
   
    #package = headerIpFormatted + headerUdpFormatted + message

    print str(package)

    sock = rawsocket()
    #sock.sendto(package.decode('hex'), (ipDestination, portDestination))
    sock.bind(("wlp1s0", 0))
    sock.send(package.decode("hex"))
    sock.shutdown(socket.SHUT_RDWR)
