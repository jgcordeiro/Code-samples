import randomizer, params, io, data
import math, random

def go(player):
	io.option(player,'Look around.')
	io.option(player,'Climb the stairs.')
	c = io.get(player)
	if c == 1:
		io.say('The place is beautifully designed, but deathly quiet. In the dining room, there isn\'t much to find but a petrified loaf of bread. You consider exploring the kitchen as well...but whatever\'s in there, the smell causes you to slam the door and stay far away. This floor has been abandoned for quite a while.')
		addItem('Loaf of Bread')
	elif c == 2:
		io.say('You climb the stairs to the gallery. Many more stairs await you, spiraling from the back wall. You advance to the second floor.')
		player.setDestination('Tower - L2')