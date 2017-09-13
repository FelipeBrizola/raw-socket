def ih1(value):
	return format(value, '01x')

def ih2(value):
	return format(value, '02x')
	
def ih4(value):
	return format(value, '04x')
	
def ih8(value):
	return format(value, '08x')
	
def sh(value):
	return value.encode("hex")
	
def iptohex(IP):
	hexIP = ''
	for a in IP.split('.'):
		hexIP = hexIP + ih2(int(a))
	return hexIP
	
	
if __name__ == "__main__":
	print( iptohex('192.168.0.1') )
