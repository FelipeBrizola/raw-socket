from struct import *
        
def buildPackage(sourcePort, destinationPort, messageLength, checksum, udpHeaderSize=8):

    package = {
        'srcPort': sourcePort,
        'dstPort': destinationPort,
        'length': udpHeaderSize + messageLength,
        'checksum': checksum
    }

    return package

def format(package):
    
    header =  pack('!HHHH', package['srcPort'], package['dstPort'], package['length'], package['checksum'])

    header = '1770d431000b0000'

    return header

