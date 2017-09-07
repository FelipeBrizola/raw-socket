import socket
from struct import *
        
def buildPackage(ip_src_addr, ip_dest_addr, ip_proto=socket.IPPROTO_UDP, ip_ver=4, ip_ihl=5, ip_tos=0, ip_id=54321, ip_frag_off=0, ip_ttl=255, ip_opts=None, data=''):
    
    package = {
        'ip_ver'       : ip_ver,
        'ip_ihl'       : ip_ihl,
        'ip_tos'       : ip_tos,
        'ip_tlen'      : 0,
        'ip_id'        : ip_id,
        'ip_frag_off'  : ip_frag_off,
        'ip_ttl'       : ip_ttl,
        'ip_proto'     : ip_proto,
        'ip_hdr_cksum' : 0,
        'ip_src_addr'  : socket.inet_aton(ip_src_addr),
        'ip_dest_addr' : socket.inet_aton(ip_dest_addr),
        'ip_opts'      : ip_opts,
        'data'         : data
    }

    package['ip_tlen'] = 4 * package['ip_ihl'] + len(package['data'])

    return package

def format(package):
    ip_ihl_ver = (package['ip_ver'] << 4) + package['ip_ihl']

    header = pack('!BBHHHBBH4s4s' , ip_ihl_ver, package['ip_tos'], package['ip_tlen'], package['ip_id'], package['ip_frag_off'],
                                    package['ip_ttl'], package['ip_proto'], package['ip_hdr_cksum'], package['ip_src_addr'], package['ip_dest_addr'] )

    return header
