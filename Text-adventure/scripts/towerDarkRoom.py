import randomizer, params, io, data
import math, random

def go(player):
	player.remember('Tower - L7')
	io.say('It is pitch black.')
	while True:
		io.option(player,'...what\'s that?')
		io.option(player,'Take the elevator down.')
		if player.seen('Catalogues'):
			io.option(player,'Open the second door.')
		c = io.get(player)
		if c == 1:
			io.say('You turn around. As your eyes adjust to the darkness, a sliver of light reveals itself at the edge of the room. It outlines a door to the outside of the tower. But as you approach it, you feel that familiar shiver, the same as when you first arrived...')
			io.option(player,'Open the door.')
			io.option(player,'One last thing...')
			c = io.get(player,False)
			if c == 1:
				if player.is_sundown():
					s = 'the sky, turned pink from the sunset on the other side of the tower.'
				elif player.is_night():
					s = 'the beautiful night sky'
				elif player.is_sunrise():
					s = 'the brilliant sunrise'
				else:
					s = 'the blinding sunlight'
				io.say('You step outside, and at last you see ' + s + '. You\'re on the eastern side of the tower: there is no clock face, only a stairwell leading to the very top. Below, you can see the tall grass around the base of the tower, weaving with the strong wind. Braving the terrible height, you begin to climb.')
				io.option(player,'Finish this journey.')
				io.get(player,False)
				player.setDestination('The End')
				break
			elif c == 2:
				io.say('Well...?')
		elif c == 2:
			io.say('Guided by a sudden panic, you return to the elevator and fall back to the previous floor.')
			player.setDestination('Tower - L6')
			break
		elif c == 3:
			player.setDestination('Tower - Catalogues')
			break