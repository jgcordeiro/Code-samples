import randomizer, params, io, data
import math, random

def go(player):
	io.say('Which path will you choose?')
	io.option(player,'Take the off road.')
	io.option(player,'Continue to the garden.')
	io.option(player,'Return to the crossroads.')
	c = io.get(player)
	if c == 1:
		player.travel(120)
		io.say('You duck under the branches and around the trees, following a series of dim lanterns. Eventually you reach a little clearing, tucked away in the forest.')
		player.setDestination('Shrine - Vestibule')
		if not player.seen('Gargoyle'):
			player.remember('Gargoyle')
			io.say('Stacks of cobblestones, broken archways, and unlit strings of lights frame this abandoned but cozy shrine. In the center, a huge statue curls its talons around a leafy pedestal. The gargoyle carries a stone pole along its shoulders, holding a big stone urn on each end. You nervously approach and read the inscriptions on the urns:')
			print('   314.1  K  |  298.2  K')
			print('   271.8  L  |    0.0  L')
			print('   161.8 kg  |    0.0 kg\n')
		else:
			io.say('You return to the shrine, greeting the gargoyle respectfully.')
	elif c == 2:
		if not player.haveCarriage():
			player.travel(2000)
			io.say('You don\'t make it far before realizing how tired you\'ve become. Maybe 43 kilometers is a bit much to cover on foot.')
			io.option(player,'Return to the intersection.')
			io.get(player,False)
			player.travel(2000)
		else:
			player.travel(GARDEN_distance_from_crossroads - SHRINE_distance_from_crossroads)
			player.setDestination('Garden - Entrance')
	elif c == 3:
		player.travel(SHRINE_distance_from_crossroads)
		player.setDestination('Crossroads')