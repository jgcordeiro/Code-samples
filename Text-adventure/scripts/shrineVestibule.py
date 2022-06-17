import randomizer, params, io, data
import math, random

def go(player):
	io.option(player,'Look around.')
	io.option(player,'Leave.')
	c = io.get(player)
	if c == 1:
		if not player.has('Idol'):
			io.say('While examining a strange ceramic basin, you suddenly see an idol standing next to you. The meter-tall statue has short tusks adorned with laurels, a little upturned nose, and eyes as expressive as the gargoyle\'s, albeit a little kinder. It carries a cup in its paws, with the familiar engraving:')
			readIdol(298.15,0.00,0.00)
			io.say('You\'re sure the idol wasn\'t there before. Sure enough, it seems to move of its own will, and seems to lumber next to you as you walk.')
			io.option(player,'Take the idol with you.')
			io.option(player,'Tell the idol to stay here.')
			c = io.get(player,False)
			if c == 1:
				io.say('The idol remains at your side, and even seems willing to help you find your way home. You get the feeling that, if the game were finished, the idol would not be found so easily.')
				addItem('Idol')
			elif c == 2:
				io.say('The idol doesn\'t seem to respond, or to move. It obeys your command and happily embraces its origin as an inanimate rock.')
		else:
			io.say('There is nothing more to find here at the moment. The gargoyle tolerates your presence, but seems uninterested in helping you.')
	elif c == 2:
		player.travel(120)
		io.say('You return to the intersection.')
		player.setDestination('The Off Road')