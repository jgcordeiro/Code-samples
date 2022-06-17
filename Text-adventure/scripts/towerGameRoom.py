import randomizer, params, io, data
import math, random

def go(player):
	if not player.seen('Tower - L3'):
		player.remember('Tower - L3')
		io.say('You arrive at the third floor. It appears to be a game room, but it\'s fallen to terrible disarray. The tables, chairs, counters, and cabinets are untended at best, in ruins at worst. At the other end of the room, there\'s a door with a very small window.')
	io.option(player,'Look around the room.')
	if player.seen('Tower - L4'):
		io.option(player,'Go upstairs.')
	else:
		io.option(player,'Look through the window.')
		io.option(player,'Examine the door.')
	c = io.get(player)
	if c == 1:
		io.say('You find some unopened tins on one of the countertops. You read a few of the labels:')
		io.say('"Hyperigneous Urglwobbits..."')
		io.say('"Cantankerous Urgeloodans..."')
		io.say('"Hyperloquacious Drivelwobbits..."')
		if player.has('Idol'):
			io.say('With the idol\'s help, you might be able to decipher this nonsense; you suspect that these strange words hide some sort of quantitative information. But this puzzle isn\'t included in the demo, and you avoid this linguistic disaster.')
		else:
			io.say('You\'re not sure what to make of this.')
	elif c == 2:
		if player.seen('Tower - L4'):
			io.say('The instant you reach the fourth floor, an inexplicably sparkling pie tin goes sailing over your head. This place, a living room full of cabinets whose contents have been scattered across the floor, is beset by a pack of strange gremlins.')
			io.say('With a terrible cackle, the shoulder-height gremlins dance around the room while casting strange spells. Some run circles around you, while others leap over your head--they seem ecstatic to have a new visitor.')
			io.say('At the other end of the room, there\'s a reinforced steel door. It says, "LOCKDOWN - This door must remain closed unless the gremlins are in their kennels." Judging by the layer of dust, the door hasn\'t been opened in some time...that doesn\'t bode well.')
			player.setDestination('Tower - L4')
		else:
			io.say('A lantern, fixed tightly to the wall, makes this room much brighter than the one through the window. You can\'t see what\'s on the other side, but they can see you.')
	elif c == 3:
		io.say('The door is locked from the other side. Beneath the window, you see an inscription in large print.')
		print('   Remember:')
		print('')
		print('   GREATNESS THROUGH POWER')
		print('               BUT')
		print('    GOODNESS THROUGH _______ION')
		print('')
		print('                      Thank you\n')
		io.say('The first letters of "_______ion" are covered by a large keyhole. It seems to fit some sort of disc-shaped object.')
		io.option(player,'Knock on the door.')
		io.option(player,'Try something else.')
		c = io.get(player)
		if c == 1:
			player.remember('Tower - L4')
			io.say('After a few seconds, you hear a click: someone has unlocked the door. Well, that was easy...maybe the rest of the puzzles are in "demo" mode as well? You doubt it.')
			io.say('When you open the door, you see no one on the other side. There\'s only a stairwell leading to the next floor. Above, you hear arhythmic crashing, stomping, and noise you can\'t even describe. Much closer, you hear the faint scuttle of something climbing the stairs ahead of you. Here we go...')
		if c == 2:
			io.say('The door is too heavy to break open--maybe the key is somewhere here? You consider your inventory...')