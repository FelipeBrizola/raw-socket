FUNCTION = 'function'


QUESTIONS_REQUEST = "QUESTIONS_REQUEST"
WELCOME_MESSAGE = "WELCOME_MESSAGE"
CONGRATULATIONS_MESSAGE = "CONGRATULATIONS_MESSAGE"
GAME_OVER_MESSAGE = "GAME_OVER_MESSAGE"

def requestWelcomeMessage():
    return '{ "'+FUNCTION+'":"'+WELCOME_MESSAGE+'" }'

def requestQuestion(level):
    return '{ "'+FUNCTION+'":"'+QUESTIONS_REQUEST+'", "level":'+str(level)+' }'

def requestCongratulationsMessage():
    return '{ "'+FUNCTION+'":"'+CONGRATULATIONS_MESSAGE+'" }'

def requestGameOverMessage():
    return '{ "'+FUNCTION+'":"'+GAME_OVER_MESSAGE+'" }'

	
	
###############################
########### TESTS #############
###############################
if __name__ == "__main__":
    print requestQuestion(1)
    print requestWelcomeMessage()
    print requestCongratulationsMessage()