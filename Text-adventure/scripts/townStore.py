import randomizer, params, io, data
import math, random

def go(player):
	if player.verbose():
		io.say('[i\'ll meet up with you later...i don\'t think she wants to see me.]')
	io.say('You enter the store. All around you, servos and joints weave back and forth, clicking a crude melody. Merchandise is stacked against every wall, but most of it is clearly meant for construction and other crafts.')
	if player.seen('Maria'):
		io.say('"Welcome back," says Maria, barely visible behind what looks like the skeleton of an old radio.')
	else:
		io.say('"Welcome," says a woman with short blonde hair and a relaxed smile. "My name is Maria. Do you need help finding anything?"')
		player.remember('Maria')
	while True:
		io.option(player,'Leave.')
		io.option(player,'Buy the Clock.')
		io.option(player,'Buy the Meterstick.')
		io.option(player,'Buy the Sleeping Bag.')
		io.option(player,'Ask about home.')
		c = io.get(player)
		if c == 1:
			io.say('"Come back anytime," says Maria halfmindedly, as she quickly returns to repairing the strange machine.')
			player.setDestination('Town - Inner Ring')
			break
		elif c == 2:
			if player.has('Clock'):
				io.say('You already have that!')
			else:
				io.say('"Oh...that\'s 4000 G."')
				if not player.has('Gold',4000):
					io.say('It doesn\'t look like you can pay.')
				else:
					io.option(player,'Buy!')
					io.option(player,'Nevermind.')
					c = io.get(player,False)
					if c == 1:
						io.say('"Here you are," says Maria. She hands you a little clock with a wooden frame--it\'s barely the size of a compass. The face reads ' + timeStr() + '.')
						io.say('A note is inscribed on the back: "This clock is accurate to the minute; manufacturer is not responsible for errors in measuring short lengths of time. Remember to press \'I\' to view your items!"')
						player.loseItem('Gold',4000)
						addItem('Clock')
						setTimeMemory(timeStr())
					elif c == 2:
						io.say('"Okay."')
		elif c == 3:
			if player.has('Meterstick'):
				io.say('You already have that!')
			else:
				io.say('"That\'s 3000 G." You somehow feel like you\'re being overcharged.')
				if not player.has('Gold',3000):
					io.say('You\'re not sure how to pay for even this.')
				else:
					io.option(player,'Buy!')
					io.option(player,'Nevermind.')
					c = io.get(player,False)
					if c == 1:
						io.say('"Here you are," says Maria. She hands you the meterstick, with a sturdy maple finish and markings delicately cut at each centimeter. Every tenth one is marked by a bronze rivet.')
						io.say('A note is inscribed on the back: "This meterstick is accurate to the centimeter; manufacturer is not responsible for errors in measuring long distances. Remember to press \'I\' to view your items!"')
						player.loseItem('Gold',3000)
						addItem('Meterstick')
					elif c == 2:
						io.say('"Okay, what else?"')
		elif c == 4:
			if player.has('Sleeping Bag'):
				io.say('You already have that!')
			else:
				io.say('"That\'s 6000 G. Traveling is so much easier when you don\'t have to return to town every night!"')
				if not player.has('Gold',6000):
					io.say('Sounds useful...but you\'re not sure how to pay.')
				elif not player.haveCarriage():
					io.say('Sounds useful...but you should find a way to carry it first.')
				else:
					io.option(player,'Buy!')
					io.option(player,'Nevermind.')
					c = io.get(player,False)
					if c == 1:
						io.say('"Here you are," says Maria. She takes a dark gray bag from the back shelf--it\'s nearly as tall as she is. "Safe travels!"')
						player.loseItem('Gold',6000)
						addItem('Sleeping Bag')
					elif c == 2:
						io.say('"Okay, what else?"')
		elif c == 5:
			io.say('"Where\'s that? North of here? South?" You don\'t have an answer.')
		elif c == 6:
			io.say('Maria laughs. "You don\'t know what it is? People these days...they don\'t even recognize 100000 G when they see it. That\'s a lot of money, my friend--you must\'ve had an incredible turn of luck. Don\'t waste it!"')
			player.remember('Gold')