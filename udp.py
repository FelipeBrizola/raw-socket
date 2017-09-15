from fm import *
from constants import *
from debug import *


###############################
########### DECODE ############
###############################
def decode(encodedPacket):
	return {
		"src_port": hi(encodedPacket[0:4]),
		"dest_port": hi(encodedPacket[4:8]),
		"length": hi(encodedPacket[8:12]),
		"checksum": encodedPacket[12:16],
		"data": encodedPacket[16:].decode("hex")
	}

	
	
###############################
########### ENCODE ############
###############################
def encode(message, src_port, dest_port, checksum = 0 ):

	hexMessage = message.encode("hex")
	udpSize = (len(hexMessage)/2) + UDP_HEADER_SIZE
	header = ih4(src_port) + ih4(dest_port) + ih4(udpSize) + ih4(checksum)
	
	if DEBUG_UDP_PACKET:
		print("\n## BUILD UDP PACKET ")
		print("## SRC PORT :"+str(src_port)+" | Hex="+ ih4(src_port))
		print("## DEST PORT :"+str(dest_port)+" | Hex="+ih4(dest_port))
		print("## UDP SIZE :"+str(udpSize) +" | Hex="+ih4(udpSize))  
		print("## CHECKSUM :"+str(checksum)+" | Hex="+ih4(checksum))
		print("\n ## MESSAGE\n"+message)
		print("\n## HEX HEADER UDP ("+str(len(header)/2)+" bytes)\n"+header)
		print("\n## MESSAGE HEX ("+str(len(hexMessage)/2)+" bytes)\n"+hexMessage+"\n")
	
	return header + hexMessage



###############################
########### TESTS #############
###############################
if __name__ == "__main__":
	print(encode("meu deus work after work", 16, 11423))
	

