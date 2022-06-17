import randomizer, params, io, data
import math, random

def go(player):
	player.setVar('Town Street',5)
	io.option(player,'Enter.')
	io.option(player,'Leave.')
	c = io.get(player)
	if c == 1:
		player.setDestination('Town - Outer Ring')
		io.say('Hundreds of buildings stand post around the circular road which encloses the rest of the town. Each one has a wide patio beneath a colorful linen roof and wooden beams carved into spirals. They\'re packed close together, fighting for elbow room on either side of the road.')
		io.say('Looks like there\'s plenty to do. What now?')
		if player.verbose():
			io.say('Tock\'s tinny voice quickly chimes in:')
			if not player.seen('Pheme'):
				io.say('[see that building over there? the one with the wings? there\'s a lady named pheme who might help us. she knows everything!!]')
			elif not player.seen('Lucas'):
				io.say('[hey, uh...i know you\'ve got your own problems, but do you think you could take a bit of time to help me? i have a friend named lucas who lives further into town, and he\'s having a lot of trouble. i really want to help him keep his job, but...]')
			elif not player.seen('Ronald'):
				io.say('[you know, it seems really boring to walk everywhere. why not try that building with a wheel on it? maybe you can find a faster way to travel.]')
			elif not player.has('Automaton'):
				io.say('[remember to talk to lucas when you\'ve got an answer ready. i\'m sure he\'d be glad to repeat the instructions, too.]')
			else:
				io.say('[if you\'ve bought everything you need, maybe we should head out? there are a lot more places to explore.]')
	elif c == 2:
		io.say('You leave the town.')
		player.leavePlace('Town')