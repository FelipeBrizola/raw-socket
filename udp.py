from struct import *
import ipv4
from fm import *


def encode( message, port_src, ip_dest, port_dest  ):
   	udp_packet = buildUdpPacket(message, port_src, port_dest)
   	return ipv4.encode(udp_packet, ip_dest)


def decode
    if( dest_packet_port == src_port )
        app.receiveMessage(message)
def buildUdpPacket(message, port_src, port_dest, checksum = 0 ):

	hexMessage = message.encode("hex")
	udpHeaderSize=8
	udpSize = udpHeaderSize + (len(hexMessage)/2)
	
	print("\n## BUILD UDP PACKET ")
	print("## SRC PORT :"+str(port_src)+" | Hex="+ ih4(port_src))
	print("## DEST PORT :"+str(port_dest)+" | Hex="+ih4(port_dest))
	print("## UDP SIZE :"+str(udpSize) +" | Hex="+ih4(udpSize))  
	print("## CHECKSUM :"+str(checksum)+" | Hex="+ih4(checksum))
	print("\n ## MESSAGE\n"+message)
	
	#header =  pack('!HHHH', port_src, port_dest, ), checksum)
	#header = '00100010001e0000'
	header = ih4(port_src) + ih4(port_dest) + ih4(udpSize) + ih4(checksum)
	
	print("\n## HEX HEADER UDP ("+str(len(header)/2)+" bytes)\n"+header)
	
	print("\n## MESSAGE HEX ("+str(len(hexMessage)/2)+" bytes)\n"+hexMessage+"\n")
	
	
	return header + hexMessage
	

if __name__ == "__main__":
	#buildUdpPacket("meu deus work after work", 16, 11423)
	print(encode("meu deus work after work", 16,"192.168.1.100", 11423))
	

