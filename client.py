import app

if __name__ == "__main__":
	app.sendUdpPackage("RETRIEVE_QUESTION_FOR_LEVEL|1", "10.32.143.237", 50000, 25000)
	(status, response) = app.receiveUdpPackage(25000)
	print status, response
