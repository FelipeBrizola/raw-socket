QUESTIONS_REQUEST = "QUESTIONS_REQUEST"
GAME_INTRODUCTION = "GAME_INTRODUCTION"
FUNCTION = 'function'

def requestGameIntroduction():
    return '{ "'+FUNCTION+'":"'+GAME_INTRODUCTION+'" }'

def requestQuestion(level):
    return '{ "'+FUNCTION+'":"'+QUESTIONS_REQUEST+'", "level":'+str(level)+' }'


	
	
###############################
########### TESTS #############
###############################
if __name__ == "__main__":
    print requestQuestion(1)
    print requestGameIntroduction()