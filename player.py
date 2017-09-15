from api import API

if __name__ == "__main__":
	my_api = API()

	print "Show do milhaoo"
	
	win = False
	loose = False
	
	print my_api.request('{ "function":"QUESTIONS_REQUEST", "level":1 }', "192.168.1.106", 50000, 25000)
	#while( !win && !loose ):
