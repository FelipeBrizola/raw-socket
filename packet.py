from constants import *
import utils
from fm import *

import ethernet
import ipv4
import udp

import app

def recv(packet, my_port):
	my_mac = utils.getLocalMac()
	my_ip = utils.getLocalIP()	
	
	############################################
	## ETHERNET 
	############################################
	ethernet_decoded = ethernet.decode(packet)
	
	if ethernet_decoded['dest_mac'] != my_mac:
		#print "ETH: MAC Not Equal ", ethernet_decoded['dest_mac'], my_mac
		return -1
	
	if ethernet_decoded['protocol'] != ETHERNET_PROT_IPV4:
		#print("ETH: PROTOCOL NOT EQUAL")
		return -1
	
	#CUT UDP HEADER FROM PACKET
	packet = packet[ETHERNET_HEADER_SIZE*2:]
	

	
	############################################
	## IPV4 
	############################################
	ipv4_decoded = ipv4.decode(packet)	

	if hextoip(ipv4_decoded['dest_ip']) != my_ip:
		return -1
	
	if ipv4_decoded['protocol'] != IP_PROT_UDP:
		return -1
	
	#CUT IP HEADER FROM PACKET
	packet = packet[IP_HEADER_SIZE*2:]
	
	
	############################################
	## UDP 
	############################################
	udp_decoded = udp.decode(packet)
	
	if udp_decoded['dest_port'] != my_port:
		return -1

	return{
		'from_ip': hextoip(ipv4_decoded['src_ip']),
		'from_port': udp_decoded['src_port'],
		'to_port': udp_decoded['dest_port'],
		'message': udp_decoded['data']
	}
	
	

def build(message, dest_ip, dest_port, src_port ):
	udp_packet = udp.encode(message, src_port, dest_port )
	ip_packet = ipv4.encode(udp_packet, utils.getLocalIP(), dest_ip )
	ethernet_packet = ethernet.encode(ip_packet, utils.getLocalMac(), utils.getMacByIP(dest_ip)) #e894f6acea70  #24f5aa67cf7a
	
	return ethernet_packet
	
	
	
###############################
########### TESTS #############
###############################
if __name__ == "__main__":
	#build("29831298739812798371298371982213", "192.168.1.102", 15015)
	recv("985fd3613bfa24f5aa67cf7a08004500003c11110000401100007f000101c0a8016604d23aa7002800003239383331323938373339383132373938333731323938333731393832323133")
	
	
	
	
	
	
	
