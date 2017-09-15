import json
from random import randint
from functions import *
class Game:

	def process_request(self, message):
		request = json.loads(message)
		
		if request[FUNCTION] == QUESTIONS_REQUEST:
			return self.sortQuestionByLevel(request['level'])
		
		return -1

	def sortQuestionByLevel(self, level):
		with open('questions.json') as json_data:
			questions = json.load(json_data)
		indexOfQuestion = randint(0, 1)
		questionsOfLevel = questions[level]
		
		json_response = json.loads( ' {"'+FUNCTION+'":'+QUESTIONS_RESPONSE+'} ')
		json_response['question'] = questionsOfLevel[indexOfQuestion]
		return json.dumps(json_response)
		



if __name__ == "__main__":
	g = Game()
	print g.process_request('{ "function":"QUESTIONS_REQUEST", "level":1 }')
