from api import API
from game import Game

my_api = API()
my_game = Game()
while True:
	my_api.listen(my_game,50000)
