import randomizer, params, io, data
import math, random

def go(player):
	io.clear()
	place = player.destination
	if player.destination == 'Tutorial':
		io.say('Good, you can use the Wait command! But what reason is there to wait?')
	else:
		if self.has('Clock'):
			io.say('You watch as the hands of the clock stumble by.')
			io.say('How many minutes do you want to wait? (At most 60)')
			n = io.getInt(60)
			waitandwatch(n)
		elif player.destination == 'Before the Clocktower':
			io.say('You wait, keeping a close eye on the face of the clocktower.')
			io.say('How many minutes do you want to wait? (At most 60)')
			n = io.getInt(60)
			waitandwatch(n)
		else:
			io.say('You try counting things around you.')
			io.say('How many minutes do you want to wait? (At most 60)')
			io.say('Warning: it\'s difficult to estimate time!')
			n = io.getInt(60)
			n = int(randomize(n,n/2.0))

def waitandwatch(t,advanceTime = True):
	io.clear()
	if advanceTime:
		player.wait(t)
	if player.destination == 'Copse':
		if player.is_night():
			io.say('You watch the night sky. All stars, no satellites...that\'s odd.')
			io.say('A shiver of loneliness rings in your head.')
			io.option(player,'Look away.')
			io.option(player,'...')
			c = io.get(player,False)
			if c == 1:
				io.say('You pull your gaze back to the ground.')
			elif c == 2:
				io.say('There\'s still so much to discover. There\'s no need to be afraid. There\'s no TIME to be afraid.')
				io.say('With a new resolve, you continue on your way.')
				#TODO: Achievement get
		else:
			io.say('You rest, looking blankly at the sky. You observe ' + io.count(n,'petal') + ' falling from the frail blossoms overhead.')
	elif player.destination == 'Crossroads':
		n = countovertime(2,1,t)
		io.say('You sit at the edge of the crossroads, watching a nearby pond, with ' + io.count(n,'frog') + ' hopping into the water.')
	elif player.destination in ['Town - Outer Ring','Town - Inner Ring']:
		if player.destination == 'Town - Outer Ring':
			m = params.TOWN_outer_morning_walkers_per_minute
		else:
			m = params.TOWN_inner_morning_walkers_per_minute
		if player.is_night():
			n = countovertime(0.1*m,0.05*m,t)
		elif player.is_sundown():
			n = countovertime(1.5*m,0.1*m,t)
		elif player.is_sunrise():
			n = countovertime(1.5*m,0.15*m,t)
		elif player.is_morning():
			n = countovertime(m,0.03*m,t)
		else:
			n = countovertime(0.8*m,0.6*m,t)
		io.say('You sit on a bench and see ' + io.count(n,'citizen') + ' passing by.')
		if player.is_night():
			io.say('It seems like not many people walk around at night.')
		elif player.is_sundown():
			io.say('It seems like people are heading back from work about now.')
		elif player.is_sunrise():
			io.say('It seems like people are heading to work about now.')
	elif player.destination in ['Town - Pheme\'s Shop','Town - General Store','Town - The Stables']:
		io.say('That would be rude!')
	elif player.destination == 'Town - The Inn':
		n = countovertime(12,4,t)
		io.say('You rest on one of the lounge\'s comfortable armchairs, watching as the fire pops ' + io.count(n,'time') + '.')
	else:
		io.say('You wait, but nothing seems to change.')