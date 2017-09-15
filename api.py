import socket
import packet
import utils
import time

class API:

	def __init__(self):
		try:
			self.my_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
		except socket.error , msg:
			print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	

	def receiveUdpPackage(self, port):
		receiving = True
		while receiving:
			network_data = self.my_socket.recv(2048)
			encoded = network_data.encode('hex')
			result = packet.decode(encoded,port)
			if result != -1:
				receiving = False
				return ("OK", result)


	def sendUdpPackage(self, message, dest_ip, dest_port, src_port):
		ethernet_packet = packet.build(message, dest_ip, dest_port, src_port)
		packet = ethernet_packet.decode("hex") # Decode from hexadecimal to bytes
		self.my_socket.sendto(packet, (utils.getMyInterfaceName(), 0))
	
	
	def request(self, message, dest_ip, dest_port, src_port):
		self.sendUdpPackage(message, dest_ip, dest_port, src_port)
		return self.receiveUdpPackage(src_port)
		
	def listen(self, request_processor, port):
		(status, packet_info) = self.receiveUdpPackage(port)
		response = request_processor.process_request(packet_info['message'])
		time.sleep(1)
		self.sendUdpPackage(response, packet_info['from_ip'], packet_info['from_port'], port)

