from struct import *
from uuid import getnode
import utils
from fm import *
import ipv4


def encode(ip_package, ip_dest):
	src_mac = ih8(getnode())
	dest_mac = utils.getArpByIP(ip_dest)
	ethernet_packet = buildEthernetPacket(ip_package, src_mac, dest_mac)
	# my_sock.send(ethernet_packet)

def decode(encodedPackage):
    
    decodedPackage = {
        'dstMac': encodedPackage[0:12], 
        'srcMac': encodedPackage[12:24], 
        'ethertype': encodedPackage[24:28] 
    }

    if decodedPackage['dstMac'] == ih8(getnode()):
        ipv4.decode(encodedPackage[28:])



def buildEthernetPacket(ip_package, src_mac, dest_mac, network_protocol ='0800' ): #IPv4
	
	print("\n## BUILDING ETHERNET PACKET SOURCE ")
	print("## Src Mac  = " + src_mac  )
	print("## Dest Mac = " + dest_mac  )
	print("## Network Protocol = " + network_protocol  )
	
	header = dest_mac + src_mac + network_protocol
	print("\n## HEX HEADER ETHERNET ("+ str(len(header)/2)+" bytes)\n" + header + "\n")
	return header + ip_package
	
	
if __name__ == "__main__":
	src_mac = ih8(getnode())
	dest_mac = utils.getArpByIP("192.168.1.100")
	buildEthernetPacket("abcb53a12a3512a35bc2acb513b75a25bc17a32c5b733abc1b3c5a", src_mac, dest_mac)



