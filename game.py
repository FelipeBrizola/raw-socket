import json
from random import randint
from functions import *
class Game:

	def process_request(self, request):
		
		if request[FUNCTION] == QUESTIONS_REQUEST:
			return self.handleQuestionsRequest(request['level'])

		if request[FUNCTION] == WELCOME_MESSAGE:
			return self.handleWelcomeMessageRequest()
		
		if request[FUNCTION] == CONGRATULATIONS_MESSAGE:
			return self.handleCongratulationsMessageRequest()
		
		if request[FUNCTION] == GAME_OVER_MESSAGE:
			return self.handleGameOverMessageRequest()
			
		return -1

	def handleQuestionsRequest(self, level):
		with open('questions.json') as json_data:
			questions = json.load(json_data)
		indexOfQuestion = randint(0, 1)
		questionsOfLevel = questions[level]
		question = questionsOfLevel[indexOfQuestion]
		return json.dumps(question)

	def handleWelcomeMessageRequest(self):
		return '{"messages":[ "Bem vindo ao show do milhao","Responda as perguntas corretamente"]}'

	def handleCongratulationsMessageRequest(self):
		return '{"message":"Parabens, voce ganhou no show do milhao!"}'

	def handleGameOverMessageRequest(self):
		return '{"message":"Voce PERDEU :( | GAME OVER | BYE"}'

if __name__ == "__main__":
	g = Game()
	print g.process_request('{ "function":"QUESTIONS_REQUEST", "level":1 }')
	print g.process_request('{ "function":"GAME_INTRODUCTION"}')
