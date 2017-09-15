import json
from random import randint
from functions import *
class Game:

	def process_request(self, message):
		request = json.loads(message)
		
		if request[FUNCTION] == QUESTIONS_REQUEST:
			return self.handleQuestionsRequest(request['level'])
		
		return -1

	def handleQuestionsRequest(self, level):
		with open('questions.json') as json_data:
			questions = json.load(json_data)
		indexOfQuestion = randint(0, 1)
		questionsOfLevel = questions[level]
		question = questionsOfLevel[indexOfQuestion]
		#print ' {"'+FUNCTION+'":'+QUESTIONS_RESPONSE+'} '
		json_response = json.loads( ' {"'+FUNCTION+'":"'+QUESTIONS_RESPONSE+'"} ')
		#print json_response
		json_response['question'] = question
		return json.dumps(json_response)


if __name__ == "__main__":
	g = Game()
	print g.process_request('{ "function":"QUESTIONS_REQUEST", "level":1 }')
