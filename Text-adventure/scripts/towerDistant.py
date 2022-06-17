import randomizer, params, io, data
import math, random

def go(player):
	if player.haveAllTreasures():
		io.option(player,'Go.')
		io.option(player,'Take some time to say goodbye.')
		c = io.get(player,False)
		if c == 1:
			player.setDestination('???')
		elif c == 2:
			io.say('You pull your gaze from the tower, catch your breath, and run back to the crossroads. Just over that hill is the point of no return--you\'re not sure if you\'re ready just yet.')
			player.setDestination('Crossroads')
	else:
		io.option(player,'Turn back.')
		io.option(player,'Turn back.')
		c = io.get(player)
		if c == 1 or c == 2:
			player.setDestination('Crossroads')