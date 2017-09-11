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

    src = '1770'
    dst = 'd431'
    length = '001a'
    check = '0000'

    header = src + dst + length + check

    return header

