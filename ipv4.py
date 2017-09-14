from fm import *
from constants import *

###############################
########### DECODE ############
###############################

def decode(encodedPacket):
    return {
        "src_ip": encodedPacket[24:32],
        "dest_ip": encodedPacket[32:40],
        "protocol": encodedPacket[18:20]
    }




###############################
########### ENCODE ############
###############################
#ip_proto=socket.IPPROTO_UDP, ip_ver=4, ip_ihl=5, ip_tos=0, ip_id=4321, ip_frag_off=0, ip_ttl=64

def encode(transport_packet, src_ip, dest_ip):
    totalSize = len(transport_packet) /2 + IP_HEADER_SIZE
    print("\n## BUILDING IP PACKET")
    print("## SRC IP= " + src_ip + " | Hex:" + iptohex(src_ip) )
    print("## DST IP= " + dest_ip + " | Hex:" + iptohex(dest_ip) )
    print("## TOTAL LENGTH " + str(totalSize) + " | Hex:" + ih4(totalSize) )

    header = '4500' + ih4(totalSize) + '1111000040110000' + iptohex(src_ip) + iptohex(dest_ip)
    print("\n## HEX HEADER IP ("+ str(len(header)/2)+" bytes)\n"+header+"\n")

    return header + transport_packet

###############################
########### TESTS #############
###############################
#if __name__ == "__main__":
    encode("baba35126ab12653ba612531a6645126b3512635b", "192.168.1.100", "192.168.1.101")
    #decode('45000048827e0000401175cdc0a8000ac0a8000de115e11500341c4453706f7455647030503afd3139d9eef3000100044895c2034cd2c3964c5e21cbb49e8e15371c943163aea528')
#ffffffffffff20c9d0d326d1080045000048827e0000401175cdc0a8000ac0a800ffe115e11500341c4453706f7455647030503afd3139d9eef3000100044895c2034cd2c3964c5e21cbb49e8e15371c943163aea528
