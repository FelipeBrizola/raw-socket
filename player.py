from api import API
from functions import *

if __name__ == "__main__":
	my_api = API()
	my_port = 25000
	server_port = 50000
	server_ip = "192.168.1.106"

	print my_api.request(requestGameIntroduction(), server_ip, server_port, my_port)
	print my_api.request(requestQuestion(0), server_ip, server_port, my_port)
