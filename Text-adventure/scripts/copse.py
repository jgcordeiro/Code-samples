import randomizer, params, io, data
import math, random

def go(player):
	io.option(player,'Look around.')
	io.option(player,'Start moving.')
	c = io.get(player)
	if c == 1:
		if player.is_sunrise():
			io.say('You can\'t see very far, but an opening in the trees reveals the fiery sunrise. The forest has come back to life after the long night.')
		elif player.is_day():
			io.say('You can\'t see very far, but an opening in the trees reveals the wonderful daylight. You discover an overwhelming drive to travel.')
		elif player.is_sundown():
			io.say('You can\'t see very far, but an opening in the trees reveals the warm sunset. Shadows yawn across the ground and under your feet.')
		elif player.is_night():
			io.say('It is very dark. All you can see are the distant lanterns through a thin patch of trees.')
	elif c == 2:
		if player.seen('Crossroads'):
			io.say('You are pleased to find the footprints of your previous trip. You trace your way back to the road, where you find the familiar intersection.')
		else:
			io.say('You set off down the clearest path. After stumbling down a ridge, you find yourself on a wide gravel road.')
		player.wait(3)
		if player.verbose() and not player.seen('Tock'):
			player.remember('Tock')
			io.say('You look to the right, then to the left again--someone is there, floating before your eyes. The being looks manufactured...more alive than a quilt, but certainly not any person or animal.')
			io.option(player,'...')
			io.get(player,False)
			io.say('A gear turns, a tumbler clicks, and it speaks:')
			io.say('[hello!! are you alright?]')
			io.say('You\'re not sure.')
			io.say('[don\'t worry, i know the feeling. you\'re lost, huh? lucky for you, i can\'t sit around when someone\'s in trouble. tock is my name--i know this whole world forward and back, so you just ask whenever you need advice.]')
			io.say('The tinny voice abruptly disappears. Tock hovers in place at a distance, smiling like a puppy.')
			io.option(player,'Continue.')
			io.get(player,False)
		io.say('A stout, lonely signpost guards the crossroads. It\'s buried in a pall of leaves and faint white flowers. The wooden markers are still readable:')
		print " N  43.2 km: The Garden"
		print " NW  0.2 km: The Town"
		print " SE 21.6 km: The Canyon"
		print " S  32.4 km: The River"
		print " E  --.- km: The Tower?\n"
		player.setDestination('Crossroads')