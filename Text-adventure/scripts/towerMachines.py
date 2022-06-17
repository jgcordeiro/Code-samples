import randomizer, params, io, data
import math, random

def go(player):
	io.say('This floor is half as loud as the one below, but the sound still rattles your bones. A wall of gears and pendulums surrounds you, and you can glimpse a few scraps of outdoor light between their teeth. You must be inside the clock.')
	if not player.seen('Tower - L6'):
		io.say('You examine the elevator; the pulley seems to be tangled with a huge, lifeless engine. Strange machines are piled around the engine--someone was trying to fix it.')
	while destination() == "Tower - L5":
		io.option(player,'Take the elevator down.')
		io.option(player,'Take the elevator up.')
		if not player.seen('Tower - L6'):
			io.option(player,'Examine the engine.')
			io.option(player,'Examine the little machines.')
		c = io.get(player)
		if c == 1:
			player.wait(6)
			io.say('The elevator makes the long journey back down; fortunately, it has momentum on its side this time. Less fortunately, when you return to the fourth floor, you find the door tightly shut.')
			io.option(player,'Knock on the door.')
			io.option(player,'Take the elevator up.')
			c = io.get(player,False)
			if c == 1:
				io.say('You try knocking on the door--figures, it\'s soundproof.')
				io.option(player,'Take the elevator up.')
				io.get(player,False)
			player.wait(12)
			io.say('With no other direction to go, you return to the fifth floor.')
		elif c == 2:
			if player.seen('Tower - L6'):
				player.wait(2)
				io.say('The elevator lurches its way to the next floor. So close to the roof...')
				player.setDestination('Tower - L6')
			else:
				io.say('The elevator bounces barely an inch above the fifth floor. A rotor of the engine prevents the pulley from going any higher.')
		elif c == 3:
			io.say('Hmm...the engine seems broken. Maybe it wouldn\'t be blocking the elevator if it worked. A note on the broken piece says:')
			io.say('"The stolen part should activate if the left or right wires are powered, but not both."')
			io.say('You try to fix the engine, but most of the components are out of your reach--only someone the size of a rabbit could navigate them...')
		elif c == 4:
			io.say('They seem to come in two sorts, TRUE and FALSE. Each has two input sockets and one output. They almost look like building blocks, and you find you can link them together.')
			io.say('However, one of them seems different from the others. Labeled "DEMO," it seems to match the missing part of the engine perfectly.')
			io.option(player,'Fix the engine.')
			io.option(player,'Try something else.')
			c = io.get(player,False)
			if c == 1:
				io.say('The engine is fixed and the elevator works!')
				player.remember('Tower - L6')
			else:
				io.say('Okay...what else?')