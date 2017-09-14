import app

if __name__ == "__main__":
	app.sendUdpPackage("RETRIEVE_QUESTION_FOR_LEVEL|1", "192.168.1.100", 50000, 25000)
	#app.receiveUdpPackage(25000)
