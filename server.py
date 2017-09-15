import app
import time

if __name__ == "__main__":
	while(True):
		(status, result) = app.receiveUdpPackage(50000)
		print result['message'].decode("hex")
		time.sleep(1)
		app.sendUdpPackage("FUCK YOU CLIENT PEACE OF SHIT|1", result['from_ip'], result['from_port'], 50000)
	
