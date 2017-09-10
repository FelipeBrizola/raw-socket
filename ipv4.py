import socket
from struct import *
        
def buildPackage(ip_src_addr, ip_dest_addr, ip_proto=socket.IPPROTO_UDP, ip_ver=4, ip_ihl=5, ip_tos=0, ip_id=4321, ip_frag_off=0, ip_ttl=64, udpLen):
    
    package = {
        'ip_ver'       : ip_ver, # 4 bits
        'ip_ihl'       : ip_ihl, # 4 bits
        'ip_tos'       : ip_tos, # 8 bits
        'ip_tot_len'   : udpLen, # 16 bits
        'ip_id'        : ip_id, # 16 bits
        'ip_frag_off'  : ip_frag_off, # 16 bits
        'ip_ttl'       : ip_ttl, # 8 bits
        'ip_proto'     : ip_proto, # 8 bits
        'ip_check'     : 0, # 16 bits
        'ip_src_addr'  : socket.inet_aton(ip_src_addr), # 32 bits
        'ip_dest_addr' : socket.inet_aton(ip_dest_addr) # 32 bits
    }

    return package

def format(package):
    
    ip_ihl_ver = (package['ip_ver'] << 4) + package['ip_ihl']

    header = pack("BBHHHBBH4s4s", ip_ihl_ver,
                                package['ip_tos'], package['ip_tot_len'],
                                package['ip_id'], package['ip_frag_off'],
                                package['ip_ttl'], package['ip_proto'], package['ip_check'],
                                package['ip_src_addr'], package['ip_dest_addr'])

    header = '450000001111000040110000c0a8000ec0a8000bea'

    return header
