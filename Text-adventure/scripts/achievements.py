import randomizer, params, io, data
import math, random

def go(player):
	io.clear()
	if destination() == 'Tutorial':
		io.say('Once you have some recurring objectives, you can mark them on the calendar. Most of this can be done automatically.')
	else:
		io.say('Your calendar reads:')
		for item in player.schedule():
			print " " + player.timeToStr(item(1)) + " - " + \
			player.timeToStr(item(2)) + ": " + item(3)