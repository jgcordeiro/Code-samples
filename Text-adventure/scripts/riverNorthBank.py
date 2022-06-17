import randomizer, params, io, data
import math, random

def go(player):
	if not player.seen('River - Northern Bank'):
		player.remember('River - Northern Bank')
		io.say('You reach a vast network of fresh water. Rivers split, join, and bend all throughout the lightly forested hills. The rivers eventually lead to the town, but the rocky channels prohibit you from traveling along it.')
	else:
		io.say('You return to the intersection between the road and the riverbank.')
	io.option(player,'Look around.')
	io.option(player,'Leave.')
	c = io.get(player)
	if c == 1:
		if not player.has('Compass'):
			io.say('In a small cabin next to the riverbank, you find a pile of papers, pens, and work orders for the construction of dams and floodgates. On top there\'s a pretty brass compass with a ruby red needle facing north. A note is attached: "Feel free to take this compass; you\'ve earned it! I mean, you hypothetically would have if the game were finished."')
			io.option(player,'Pick up the compass.')
			io.option(player,'Nevermind.')
			c = io.get(player,False)
			if c == 1:
				io.say('You take the compass; it seems to work very well, and comes with a built-in protractor. It seems rather mundane, but obtaining it grants you a surge of hope--you\'re sure you can put it to good use.')
				addItem('Compass')
		else:
			io.say('The cabin is otherwise devoid of useful trinkets.')
	elif c == 2:
		leavePlace('River')