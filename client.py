from api import API
from functions import *
import sys


def printWelcomeMessage():
	welcome_message = my_api.request(requestWelcomeMessage(), server_ip, server_port, my_port)['message']
	print '\n' + welcome_message + '\n'

def printCongratulationsMessage():
	congratulations_message = my_api.request(requestCongratulationsMessage(), server_ip, server_port, my_port)['message']
	print '\n' + congratulations_message + '\n'

def printGameOverMessage():
	game_over_message = my_api.request(requestGameOverMessage(), server_ip, server_port, my_port)['message']
	print '\n' + game_over_message + '\n'

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


def play():

	printWelcomeMessage()

	correct, reward = askQuestion(0)

	if correct:
		print "\nResposta CORRETA"
		print "Parabens voce esta com "+str(reward)+" reais\n"
	else:
		print "\nResposta ERRADA"
		printGameOverMessage()
		return


	correct, reward = askQuestion(1)

	if correct:
		print "\nResposta CORRETA"
		print "Parabens voce esta com "+str(reward)+" reais\n"
	else:
		print "\nResposta ERRADA"
		printGameOverMessage()
		return

	correct, reward = askQuestion(2)

	if correct:
		print "\nResposta CORRETA\n"
	else:
		print "\nResposta ERRADA"
		printGameOverMessage()
		return

	printCongratulationsMessage()
	print "Sua recompensa foi de "+str(reward)+" reais\n"

if __name__ == "__main__":
	my_api = API()
	server_ip = sys.argv[1]
	server_port = int(sys.argv[2])
	my_port = int(sys.argv[3])
	play()