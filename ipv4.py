import socket
from struct import *
from fm import *
import utils
import ethernet

def encode(transport_packet, dest_ip):
	src_ip = utils.getLocalIP()
	ip_packet = buildIPv4Packet(transport_packet, src_ip, dest_ip)
	return ethernet.encode(ip_packet, dest_ip)
        
def decode(encodedPacket):
	myIp = "192.168.0.13" # funcao de bucar meu ip retorna 127.0.0.1
	udpProtocol = 11

	decodedPacket = {
    	"srcIp": encodedPacket[24:32], 
        "dstIp": encodedPacket[32:40], 
        "protocol": encodedPacket[18:20] 
    }

	print decodedPacket

	if (decodedPacket['srcIp'] == myIp) and (decodedPacket['protocol'] == updProtocol):
        return udp.decode(encodedPacket[40:])

def buildIPv4Packet(transport_packet, ip_src_addr, ip_dest_addr, ip_proto=socket.IPPROTO_UDP, ip_ver=4, ip_ihl=5, ip_tos=0, ip_id=4321, ip_frag_off=0, ip_ttl=64):
    
	headerIpSize = 20
  	totalSize = len(transport_packet) /2 + headerIpSize
  	
	package = {
		'ip_ver'       : ip_ver, # 4 bits .5
		'ip_ihl'       : ip_ihl, # 4 bits .5
		'ip_tos'       : ip_tos, # 8 bits 1
		'ip_tot_len'   : 0, # 16 bits 2 
		'ip_id'        : ip_id, # 16 bits 2
		'ip_frag_off'  : ip_frag_off, # 16 bits 2
		'ip_ttl'       : ip_ttl, # 8 bits 1
		'ip_proto'     : ip_proto, # 8 bits 1
		'ip_check'     : 0, # 16 bits 2
		'ip_src_addr'  : socket.inet_aton(ip_src_addr), # 32 bits 4
		'ip_dest_addr' : socket.inet_aton(ip_dest_addr) # 32 bits 4
	}
		                
	print("\n## BUILDING IP PACKET")
	print("## SRC IP= " + ip_src_addr + " | Hex:" + iptohex(ip_src_addr) )
	print("## DST IP= " + ip_dest_addr + " | Hex:" + iptohex(ip_dest_addr) )
	print("## TOTAL LENGTH " + str(totalSize) + " | Hex:" + ih4(totalSize) )

	header = '4500' + ih4(totalSize) + '1111000040110000' + iptohex(ip_src_addr) + iptohex(ip_dest_addr) 
	print("\n## HEX HEADER IP ("+ str(len(header)/2)+" bytes)\n"+header+"\n")

	return header + transport_packet


if __name__ == "__main__":
	#buildIPv4Packet("baba35126ab12653ba612531a6645126b3512635b", "192.168.1.100", "192.168.1.101")
	decode('45000048827e0000401175cdc0a8000ac0a800ffe115e11500341c4453706f7455647030503afd3139d9eef3000100044895c2034cd2c3964c5e21cbb49e8e15371c943163aea528')
