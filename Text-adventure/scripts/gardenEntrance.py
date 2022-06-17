import randomizer, params, io, data
import math, random

def go(player):
	if not player.seen('Garden - Entrance'):
		player.remember('Garden - Entrance')
		io.say('You finally reach the garden, and what a garden it is. The place is painted beautifully over a wide downhill slope. A web of paths winds around the various trees and hedges. Ledges and bridges sort the massive garden into layers, and a murmuring creek swivels throughout.')
	else:
		io.say('You return to the edge of the garden, looking over the brilliant fractal of green and blue.')	
	io.option(player,'Look around.')
	io.option(player,'Leave.')
	c = io.get(player)
	if c == 1:
		if not player.has('Mirror'):
			io.say('While admiring the colorful garden, you come across a cherry wood box on the ground. A note on the top says, "Thanks for visiting the Garden! We can\'t be here until the game\'s finished, but in the meantime, why not learn some history?"')
			io.say('Inside the box is a small handheld mirror. The iron frame is scratched and discolored, but the glass is crystal clear.')
			io.option(player,'Pick up the mirror.')
			io.option(player,'Nevermind.')
			c = io.get(player,False)
			if c == 1:
				io.say('You turn a small gauge at the top of the mirror, and something strange begins to happen. Your image in the mirror retreats and walks backward off the frame. Leaves fall upward. Rabbits and grasshoppers zip in reverse motion, and speed up the faster you turn the gauge.')
				io.say('It can look back in time.')
				io.say('While you ponder the many uses of such a mirror, the glass turns pure white at about the 3-month mark; it can\'t remember anything before then. Despite this limit, you gratefully accept the incredible item...maybe it can help you return home.')
				addItem('Mirror')
		else:
			io.say('You look for more treasures, but turn up nothing. Oh well; a time mirror is okay, you guess.')
	elif c == 2:
		leavePlace('Garden')