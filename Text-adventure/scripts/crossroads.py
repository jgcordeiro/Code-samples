import randomizer, params, io, data
import math, random

def go(player):
	if player.verbose() and not player.haveCarriage():
		io.say('[you won\'t be getting far on foot. why not head to the town?]')
	else:
		io.say('Where to?')
	io.option(player,'(N  43.2 km) Visit the Garden!')
	io.option(player,'(NW  0.2 km) Visit the Town!')
	io.option(player,'(SE 21.6 km) Visit the Canyon!')
	io.option(player,'(S  32.4 km) Visit the River!')
	io.option(player,'(E  --.- km) Visit the Tower?')
	io.option(player,'Return to the woods.')
	c = io.get(player)
	if c == 1:
		if player.haveCarriage():
			if steed() == 'horses':
				s = 'One of the horses glances at the little "43.2 km" etched into the marker you follow, and looks back at you with as much concern as it can show.'
			elif steed() == 'oxen':
				s = 'Staring down the long path, the oxen bray with confidence.'
			elif steed() == 'jabberwock':
				s = 'The jabberwock takes off running.'
			io.say(s + ' The carriage rattles on the road before settling into a steady pace. Trees and landmarks fall away from you, and soon you\'re surrounded by plains and the whooshing of long grass beside the carriage wheels.')
			player.travel(params.SHRINE_distance_from_crossroads)
			if not player.seen('The Off Road'):
				io.say('On your way to the garden, you find a dirt path leading into the dense trees. A thicket of vines and little white flowers looms over the path; it seems like people haven\'t visited in some time.')
				player.remember('The Off Road')
			else:
				io.say('You return to the intersection between the garden, the crossroads, and the mysterious off road.')
			player.setDestination('The Off Road')
		else:
			io.say('The Garden sounds pleasant. You decide to walk there. 43-and-something kilometers? How bad could it be?')
			io.option(player,'Yeah!')
			io.get(player,False)
			io.say('You walk and walk and walk. You observe the same scenery four hundred and sixty-something times, though you\'re not sure how you counted. Eventually you reach a little assembly of trees and hills, but nothing resembling a "garden"...')
			player.travel(params.SHRINE_distance_from_crossroads)
			io.say('As you strongly consider turning back, you discover a smaller road branching off into the forest.')
			player.setDestination('The Off Road')
	elif c == 2:
		if player.is_day():
			io.say('Houses and low buildings sprinkle the horizon. You make your way to the welcoming little hamlet.')
		elif player.is_sundown():
			io.say('You can smell the smoke of chimneys, and lampposts blink to life in the distance. The sky darkens and the air coldens, urging you to the safety of the town.')
		elif player.is_night():
			io.say('Among the blackened trees, there is only one road with a clearly visible end. The darkness chills you to the bone, and you set off deliberately for the softly shining town.')
		else:
			io.say('The sun warmly looks over your shoulder as you advance toward the blossoming horizon. You can faintly see carriages crossing the streets, as the town slowly returns to life after the long night.')
		io.option(player,'Continue to town.')
		io.option(player,'Actually...')
		c = io.get(player,False)
		if c == 1:
			player.travel(200)
			# TODO: River affects this
			io.say('You arrive at the edge of town. The entrance is a lowly bridge over a steam of blue-green freshwater.')
			if not player.seen('Town Gate'):
				player.remember('Town Gate')
				io.say('You can see a lot of houses, the roof of a distant palace, and a radio tower. The tower seems especially out of place: most of the buildings around it could have been built centuries ago.')
				io.say('Above the bridge, a gate grins down at you with rusty copper jaws. It seems to be fused open, and hasn\'t been maintained for some time.')
			player.setDestination('Town - Outer Gate')
		else:
			io.say('...well, maybe not. You stop and stand at the intersection.')
	elif c == 3:
		if player.haveCarriage():
			player.travel(params.CANYON_distance_from_crossroads)
			io.say('You ride along the trail, watching trees disappear nearby, then far away, until you\'re surrounded by nothing but golden-green plains. As usual, you watch the horizon as the hours tick by...until suddenly it seems much closer than before. You\'ve reached the canyon.')
			player.setDestination('Canyon - L1')
		else:
			io.say('The canyon seems like a good place to try. 21 kilometers? You can get there in 20!')
			io.option(player,'Yeah!')
			io.get(player,False)
			player.travel(3000)
			io.say('You walk, farther and farther. The scenery grows ever more blank, with no landmarks but the road forward and the road back. You can\'t see any hint of the canyon...it doesn\'t look like you can make it there.')
			io.option(player,'Return to the crossroads.')
			io.get(player,False)
			player.travel(3000)
	elif c == 4:
		if player.haveCarriage():
			player.travel(params.RIVER_distance_from_crossroads)
			io.say('This trail leads deeper into the forest, swaying slightly back and forth, like the gait of an explorer who hasn\'t slept in a week or two. The carriage crawls over roots and fallen branches, until you are thoroughly bored of trees. Finally, you hear rushing water ahead...')
			player.setDestination('River - Northern Bank')
		else:
			io.say('You\'re feeling a bit thirsty...the river seems like a smart decision. What did the sign say? 30-something kilometers? Eh, it\'s probably fine.')
			io.option(player,'Yeah!')
			io.get(player,False)
			player.travel(3000)
			io.say('You walk past enough trees that you lose count. You\'re feeling very tired, and you can\'t tell your place apart from where you were half an hour ago. This isn\'t going to work...you\'ll need a better form of transportation.')
			io.option(player,'Return to the crossroads.')
			io.get(player,False)
			player.travel(3000)
	elif c == 5:
		if player.haveAllTreasures():
			io.say('You\'ve scoured this entire world, and found amazing treasures in every other location. Seems like a good time to visit the tower.')
			io.option(player,'It\'s worth a shot...')
		else:
			io.say('The question mark in "Tower?" just screams mystery. You\'re not sure how far "dash-dashydash kilometers" is, but no distance will stop you.')
			io.option(player,'Yeah!')
		io.get(player,False)
		player.travel(80)
		io.say('You scale a little hill and find the horizon. Deep into the distance, nearly invisible, a clocktower stands. It\'s tall enough to watch over half the world. The road beneath you leads right up to it.')
		io.option(player,'Go.')
		io.option(player,'Turn back.')
		c = io.get(player,False)
		if c == 1:
			if player.haveAllTreasures():
				io.say('A sense of finality overwhelms you. You move toward the tower, and no force turns you away. You\'ve found everything you need. It\'s time to go home.')
			else:
				io.say('As you try to approach the clocktower, a terrible chill seizes you. For some reason, you can\'t go forward. Your heart heats up like a combustion engine...')
			player.setDestination('Before the Clocktower')
		elif c == 2:
			if player.haveAllTreasures():
				io.say('...maybe a little later.')
			else:
				io.say('Turning away provides a strange relief. You decide to head for a more...normal destination.')
	elif c == 6:
		io.say('You rediscover the little copse where you first awakened.')
		player.setDestination('Copse')