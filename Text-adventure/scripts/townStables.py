import randomizer, params, io, data
import math, random

def go(player):
	io.option(player,'Leave.')
	if player.inSchedule('Work at the stables'):
		io.option(player,'Help around the stables (until 5PM.)')
	else:
		io.option(player,'Ask for a job.')
	if not player.haveCarriage():
		io.option(player,'Rent a carriage.')
	c = io.get(player)
	if c == 1:
		io.say('"Bye," says Ronald, managing a wave.')
		player.setDestination('Town - Outer Ring')
	elif c == 2:
		if player.inSchedule('Work at the stables'):
			player.waitUntil(1020)
			player.wait(1)
			player.getItem('Gold',300)
			io.say('"Thanks for your help," says Ronald.')
			io.say('You obtain 300 G!')
		else:
			accept = True
			io.say('"Oh, did you see the listing? On the town bulletin?"')
			io.option(player,'"Yes."')
			io.option(player,'"No."')
			c = io.get(player,False)
			if c == 1:
				io.say('"Great, so you want the job? Remember, it\'s 1PM to 5PM, for 300 G every day you show up."')
			elif c == 2:
				io.say('"Oh--well, you should check there at least once. It\'s a great place to find work.')
				io.say('"Anyway, we\'re pretty understaffed here. If you want to work from 1PM to 5PM, the pay\'s 300 G for every day you show up."')
			io.option(player,'"Okay."')
			io.option(player,'"Nevermind."')
			c = io.get(player,False)
			if c == 1:
				conflict = player.scheduleOverlap(780,1020)
				if conflict != '':
					io.say('This conflicts with "' + conflict + '" on your schedule. Are you sure?')
					io.option(player,'Yes.')
					io.option(player,'No.')
					c = io.get(player,False)
					if c == 2:
						accept = False
				if accept:
					player.schedule += [(780,1020,'Work at the stables')]
	elif c == 3:
		io.say('Ronald hands you the pricing chart:')
		print '      Plan       Speed        Cost (G)'
		print ' ==========================================='
		print ' |   Horses   | ' + str(params.kmph_dict['horses']).rjust(2) + ' kmph | ' + str(params.cost_dict['horses']).rjust(5) + ' + ' + str(params.daycost_dict['horses']) + '/day |'
		print ' -------------------------------------------'
		print ' |    Oxen    | ' + str(params.kmph_dict['oxen']).rjust(2) + ' kmph | ' + str(params.cost_dict['oxen']).rjust(5) + ' + ' + str(params.daycost_dict['oxen']) + '/day |'
		print ' -------------------------------------------'
		print ' | Jabberwock | ' + str(params.kmph_dict['jabberwock']).rjust(2) + ' kmph | ' + str(params.cost_dict['jabberwock']).rjust(5) + ' + ' + str(params.daycost_dict['jabberwock']) + '/day |'
		print ' ===========================================\n'
		io.option(player,'Ask about "Horses."')
		io.option(player,'Ask about "Oxen."')
		io.option(player,'Ask about "Jabberwock."')
		io.option(player,'Nevermind.')
		c = io.get(player,False)
		if c == 1:
			io.say('Ronald leads you to a small outdoor field, where two brown horses are standing. "You\'ll be able to get where you\'re going, but make sure you can afford enough food."')
			io.option(player,'Buy!')
			io.option(player,'Maybe later.')
			c = io.get(player,False)
			if c == 1:
				if gold() < params.cost_dict['horses']:
					io.say('Oops--you don\'t have enough gold!')
				else:
					player.wait(45)
					setSteed('horses')
					io.say('Ronald explains all the necessary instructions. Soon you\'re sitting at the helm of a spacious carriage, with the center of town on your left and the vast unknown on your right. You feel ready to travel!')
					player.setDestination('Town - Outer Ring')
			else:
				io.say('Okay. What else?')
		elif c == 2:
			io.say('Ronald leads you to an outdoor pen, where two gray oxen pace about restlessly. "Oxen may not be as quick as the rest, but they\'re tough and willing to trek long distances."')
			io.option(player,'Buy!')
			io.option(player,'Maybe later.')
			c = io.get(player,False)
			if c == 1:
				if gold() < params.cost_dict['oxen']:
					io.say('Oops--you don\'t have enough gold!')
				else:
					player.wait(35)
					setSteed('oxen')
					io.say('Ronald explains all the necessary instructions. The oxen lumber onto the streets and walk stalwartly around the edge of town. There\'s no rush, you suppose--now you can reach any destination you want.')
					player.setDestination('Town - Outer Ring')
			else:
				io.say('Okay. What else?')
		elif c == 3:
			io.say('You honestly thought he was kidding. "It\'s the swiftest we\'ve got, but also the most expensive. Hope you know what you\'re doing."')
			io.option(player,'Buy!')
			io.option(player,'Maybe later.')
			c = io.get(player,False)
			if c == 1:
				if gold() < params.cost_dict['jabberwock']:
					io.say('Oops--you don\'t have enough gold!')
				else:
					player.wait(110)
					setSteed('jabberwock')
					io.say('Ronald explains the many instructions. Soon your carriage flies along the road, almost too fast for you to read the passing signs. You feel ready to travel, if only to stop dodging around pedestrians.')
					player.setDestination('Town - Outer Ring')
			else:
				io.say('Okay. What else?')
		elif c == 4:
			io.say('Okay, what else?')