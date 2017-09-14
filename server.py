import app

if __name__ == "__main__":
	(status, result) = app.receiveUdpPackage(50000)
	print(status, result)
	#app.sendUdpPackage("FUCK YOU CLIENT PEACE OF SHIT|1", result['from_ip'], result['from_port'], 50000)
	
