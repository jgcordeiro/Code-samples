import randomizer, params, io, data
import math, random

def go(player):
	if not player.seen('Canyon - L1'):
		player.remember('Canyon - L1')
		io.say('The road stops just short of the canyon edge. A dizzying web of stairs and scaffolding crawl down the stone face. Crates of clay and lime are moved from one side of the contruction site to the other, by a pulley system of questionable design. You should move carefully here.')
	else:
		io.say('You return to the canyon.')
	io.option(player,'Look around.')
	io.option(player,'Leave.')
	c = io.get(player)
	if c == 1:
		if not player.has('Torch'):
			io.say('You make your way down the nearby stairs. Just below the surface, a station full of planks, rope, and construction equipment looks over the rest of the site.')
			io.say('In a locker titled "DEMO," you find a torch with a black marble casing and bands of sterling silver.')
			io.option(player,'Pick up the torch.')
			io.option(player,'Nevermind.')
			c = io.get(player,False)
			if c == 1:
				io.say('You find a small latch on the side of the torch, set like the button of a flashlight. When you turn the latch, the sharp scent of brimstone heralds a brilliant flame.')
				io.say('Nervously, you hold the torch far away from you. It must be a great treasure for the miners here, as the light shows no signs of dying down. You decide to bring it with you; you can pay the workers back when the game remembers they exist.')
				addItem('Torch')
		else:
			io.say('There\'s nothing else to find here for now.')
	elif c == 2:
		leavePlace('Canyon')