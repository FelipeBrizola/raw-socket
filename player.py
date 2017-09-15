from api import API
from functions import *

def printWelcomeMessage():
	welcome_message = my_api.request(requestWelcomeMessage(), server_ip, server_port, my_port)['message']
	print '\n' + welcome_message + '\n'

def printCongratulationsMessage():
	congratulations_message = my_api.request(requestCongratulationsMessage(), server_ip, server_port, my_port)['message']
	print '\n' + congratulations_message + '\n'

def askQuestion(level):
	response = my_api.request(requestQuestion(level), server_ip, server_port, my_port)
	string_positions = ["primeira", "segunda", "terceira"]
	print "Vamos a "+string_positions[level]+" pergunta, valendo " + response['reward'] + " reais:\n"
	print response['question'] + "\n"
	print "Alternativas:"
	for x in range(0,4):
		print str(x+1) + ") "+response['answers'][x]
	res = input("Qual sua resposta? ")
	return (res-1) == response['correctAnswerIndex'], response['reward']


def play(server_ip, server_port, my_port):

	printWelcomeMessage()

	correct, reward = askQuestion(0)

	if correct:
		print "\nResposta CORRETA"
		print "Parabens voce esta com "+str(reward)+" reais\n"
	else:
		print "\nResposta ERRADA\nGAME OVER MY FRIEND\n"
		return


	correct, reward = askQuestion(1)

	if correct:
		print "\nResposta CORRETA"
		print "Parabens voce esta com "+str(reward)+" reais\n"
	else:
		print "\nResposta ERRADA\nGAME OVER MY FRIEND\n"
		return

	correct, reward = askQuestion(2)

	if correct:
		print "\nResposta CORRETA\n"
	else:
		print "\nResposta ERRADA\nGAME OVER MY FRIEND\n"
		return

	printCongratulationsMessage()
	print "Sua recompensa é de "+str(reward)+" reais\n"

if __name__ == "__main__":
	my_api = API()
	my_port = 25000
	server_port = 50000
	server_ip = "192.168.1.106"

	play(server_ip, server_port, my_port)