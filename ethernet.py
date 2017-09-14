from constants import *
from fm import *
import utils

###############################
########### DECODE ############
###############################
def decode(encodedPackage):
	return  {
		'dest_mac': encodedPackage[0:12], 
		'src_mac': encodedPackage[12:24], 
		'protocol': encodedPackage[24:28] 
	}

###############################
########### ENCODE ############
###############################
def encode(ip_package, src_mac, dest_mac):
	print("\n## BUILDING ETHERNET PACKET SOURCE ")
	print("## Src Mac  = " + src_mac  )
	print("## Dest Mac = " + dest_mac  )
	print("## Network Protocol = " + ETHERNET_PROT_IPV4  )
	
	header = dest_mac + src_mac + ETHERNET_PROT_IPV4
	print("\n## HEX HEADER ETHERNET ("+ str(len(header)/2)+" bytes)\n" + header + "\n")
	return header + ip_package

###############################
########### TESTS #############
###############################
if __name__ == "__main__":
	src_mac = utils.getLocalMac()
	dest_mac = utils.getArpByIP("192.168.1.103")
	encode("abcb53a12a3512a35bc2acb513b75a25bc17a32c5b733abc1b3c5a", src_mac, dest_mac)

