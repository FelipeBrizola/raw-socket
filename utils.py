from subprocess import Popen, PIPE
import re
import socket

def getLocalIP():
	return socket.gethostbyname(socket.gethostname())

def getArpByIP(IP):
	Popen(["ping", "-c 1", IP], stdout = PIPE)
	pid = Popen(["arp", "-n", IP], stdout = PIPE)
	s = pid.communicate()[0]
	search = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s)
	if( search == None ):
		return "NO MAC FOUND"
	mac = search.groups()[0]
	#return mac 		#hexstring formatada
	return mac.replace(':','') #hexstring pura
	

if __name__ == "__main__":
	print(	getArpByIP('192.168.0.100') )
