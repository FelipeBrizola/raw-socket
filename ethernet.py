from struct import *

# def buildPackage(dstMac='\xd4\xdc\xcd\xba\xfb\xf1', srcMac='\x20\xc9\xd0\xd3\x26\xd1', ethertype='\x80\x00'):
# def buildPackage(dstMac=0xd4dccdbafbf1, srcMac=0x20c9d0d326d1, ethertype=0x8000):


def buildPackage(dstMac='d4dccdbafbf1', srcMac='20c9d0d326d1', ethertype='0800'):

    package = {
        'dstMac': dstMac, 
        'srcMac': srcMac, 
        'ethertype': ethertype 
    }

    return package

def format(package):
    return package['dstMac'] + package['srcMac'] + package['ethertype']
