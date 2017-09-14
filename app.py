import socket
import packet


def send_sock():
    try:
        #return socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        #return socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        return socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    
    
def recv_socket():
    try:
        #return socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        return socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        #return socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    

def receiveUdpPackage(port):
    sock = recv_socket()
    receiving = True
    while receiving:
        network_data = sock.recv(2048)
        encoded = network_data.encode('hex')
        #print encoded
        result = packet.recv(encoded,port)
        if result != -1:
            receiving = False
            return ("OK", result)


def sendUdpPackage(message, dest_ip, dest_port, src_port):
    
    ethernet_packet = packet.build(message, dest_ip, dest_port, src_port)
    
    sock = send_sock()
    sock.sendto(ethernet_packet, ("enp0s3", 0))
    #sock.shutdown(socket.SHUT_RDWR)
    #sock.close()

