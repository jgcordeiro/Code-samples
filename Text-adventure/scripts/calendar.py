import randomizer, params, io, data
import math, random

def go(player):
	io.clear()
	if player.destination == 'Tutorial':
		io.say('Once you have some recurring objectives, you can mark them on the calendar. Most of this can be done automatically.')
	else:
		if player.schedule:
			io.say('You check your daily schedule.')
			for item in player.schedule:
				print " " + player.timeToString(item[0]) + " - " + \
				player.timeToString(item[1]) + ": " + item[2] + "\n"
			io.option(player,'Okay.')
			io.option(player,'Remove something from the schedule.')
			c = io.get(player,False)
			if c == 2:
				io.say('What do you want to erase?')
				io.say('(This action cannot be undone!)')
				io.option(player,'Nevermind.')
				for i in range(len(player.schedule)):
					io.option(player,'"' + player.schedule[i][2] + '"')
				c = io.get(player,False)
				if c > 1:
					del player.schedule[c-2]
					io.say('Item removed.')
		else:
			io.say('You don\'t have anything on your schedule.')
