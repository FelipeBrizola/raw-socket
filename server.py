# Echo server program
import socket
import sys
import ethernet

def rawsocket():
    try:
        return socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    

if __name__ == "__main__":
    sock = rawsocket()

    while True:
        network_data = sock.recv(2048)
        encoded = network_data.encode('hex')
        print encoded
        print '\n'
                

        