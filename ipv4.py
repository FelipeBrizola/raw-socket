import socket
from struct import *
        
def buildPackage(ip_src_addr, ip_dest_addr, ip_proto=socket.IPPROTO_UDP, ip_ver=4, ip_ihl=5, ip_tos=0, ip_id=4321, ip_frag_off=0, ip_ttl=64, udpLen=26):
    
    package = {
        'ip_ver'       : ip_ver, # 4 bits .5
        'ip_ihl'       : ip_ihl, # 4 bits .5
        'ip_tos'       : ip_tos, # 8 bits 1
        'ip_tot_len'   : udpLen + 20, # 16 bits 2 
        'ip_id'        : ip_id, # 16 bits 2
        'ip_frag_off'  : ip_frag_off, # 16 bits 2
        'ip_ttl'       : ip_ttl, # 8 bits 1
        'ip_proto'     : ip_proto, # 8 bits 1
        'ip_check'     : 0, # 16 bits 2
        'ip_src_addr'  : socket.inet_aton(ip_src_addr), # 32 bits 4
        'ip_dest_addr' : socket.inet_aton(ip_dest_addr) # 32 bits 4
    }

    return package

def format(package):
    
    ip_ihl_ver = (package['ip_ver'] << 4) + package['ip_ihl']

    header = pack("BBHHHBBH4s4s", ip_ihl_ver,
                                package['ip_tos'], package['ip_tot_len'],
                                package['ip_id'], package['ip_frag_off'],
                                package['ip_ttl'], package['ip_proto'], package['ip_check'],
                                package['ip_src_addr'], package['ip_dest_addr'])
                                
    #header = '4'+'5'+'00'+'002e' + '1111'+ '0000' + '40'+ '11'+   '0000'+ 'c0a8000e' +'c0a8000be'
    header = '450000321111000040110000c0a8000ec0a8000b'

    return header
