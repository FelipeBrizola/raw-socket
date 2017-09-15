from api import API
from game import Game
import sys

my_api = API()
my_game = Game()
while True:
	my_api.listen(my_game,int(sys.argv[1]))