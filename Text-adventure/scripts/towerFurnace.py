import randomizer, params, io, data
import math, random

def go(player):
	for x in range(1,1024):
		digits = []
		while x:
			digits.append(str(x % 4))
			x /= 4
		s = ""
		for c in digits[::-1]:
			s += str(c)
		player.furnaceSwitches[s] = False
	io.say('This floor is small and exceptionally cold. It looks a bit like an attic; you watch your step as you look around. The light from the elevator flickers out--there is no power up here. In a nearby corner, there\'s a broken furnace.')
	while True:
		io.option(player,'Examine the furnace.')
		io.option(player,'Take the elevator down.')
		io.option(player,'Take the elevator up.')
		if player.seen('Furnace') and not player.seen('Tower - L7'):
			io.option(player,'Flip a random switch.')
			io.option(player,'Throw the reset lever.')
		c = io.get(player)
		if c == 1:
			if not player.seen('Tower - L7'):
				player.remember('Furnace')
				io.say('There\'s a control panel on the side, with thousands of tiny switches and absurdly unhelpful labels. The only one you can discern is a level marked "RESET." There\'s a chute on the front which leads directly to a bed of half-used charcoal; maybe if you had some source of heat...')
			else:
				io.say('The furnace glows brightly...but you should probably move on before it dies out again.')
		elif c == 2:
			if player.seen('Tower - L7'):
				player.wait(1)
				if player.seen('Tower - L6'):
					io.say('The elevator squeaks for a moment, then moves down to the fifth floor.')
					player.setDestination('Tower - L5')
					break
				else:
					io.say('The elevator crashes against the engine on the previous floor. No place to go but upward.')
			else:
				io.say('No response--the elevator is completely dead on this floor.')
		elif c == 3:
			if player.seen('Tower - L7'):
				io.say('The elevator begins to rise. The warm glow of the furnace falls away, and the walls fade into total darkness. You\'ve reached the seventh floor.')
				player.setDestination('Tower - L7')
				break
			else:
				io.say('No response--the elevator is completely dead on this floor.')
		elif c == 4:
			io.say('You try flipping some switches on the control board, but it\'s even more convoluted than it looks. For each switch you activate, hundreds more switch on, and hundreds more switch off. You try the reset lever, but it just sets all the switches back to zero. It would take decades to follow all the wires...')
			for switch in player.furnaceSwitches.keys():
				if player.furnaceSwitches[switch]:
					player.furnaceSwitches[switch] = False
		elif c == 5:
			for switch in player.furnaceSwitches.keys():
				if player.furnaceSwitches[switch]:
					player.furnaceSwitches[switch] = False
					print(' Reset switch #' + switch)
			io.say('You reset the system.')