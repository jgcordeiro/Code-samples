import randomizer, params, io, data
import math, random

def go(player):
	if not player.finishedTutorial:
		io.hline()
		print ' Welcome!'
		io.hline()
		io.say('\n Explore, innovate, and quantify in your quest to return home. No one can tell you the formulas, or give you the steps to escape this strange world...what will you do?')

		io.hline()
		print ' How to Play:'
		io.hline()
		io.say('\n Every scene provides you with a list of choices. To select an option, type the corresponding number and press Enter.')
		io.say('INCREASE THE HEIGHT OF THE WINDOW until you can see the Welcome text.')
		io.option(player,'Enter 1 to begin.')
		io.get(player,False)

		io.hline()
		print ' Verbose'
		io.hline()
		io.say('\n Do you want to enable hints and advice for advancing through the game?')
		io.option(player,'Enable Verbose Mode.')
		io.option(player,'No thanks.')
		c = io.get(player,False)
		if c == 1:
			player.setVerbose(True)

		io.hline()
		print ' Seed'
		io.hline()
		io.say('\n Enter an integer; players who use the same seed will have the same answers to each puzzle.')
		io.say('Enter 0 for a random seed.')
		s = raw_input()
		if io.isInt(s):
			s = int(s)
			if s != 0:
				seed = s
				random.seed(seed)
		io.clear()
		player.finishedTutorial = True

		io.hline()
		print ' One more thing...'
		io.hline()
		io.say('\n You can sometimes use special commands which might apply to many situations. For example, enter a T to talk to people nearby. These commands are shown at the bottom of the screen.')
		
	io.option(player,'Ready to go!!')
	c = io.get(player)
	if c == 1:
		io.say('One day you found a golden trinket, lodged in the sidewalk. It seemed to follow your gaze, spinning and swirling as you walked around it. Every step you took, it adopted a new shape. The little jewel held a strange glow: it caught the sunlight in every possible direction, and a few impossible ones as well.')
		io.say('When you try to take the trinket, a shiver runs up your arm. As you lift it up, it drags you down...through the floor, through the world, in a direction you can\'t seem to comprehend. Before you realize it, there is a bed of soft grass beneath you. You ease your eyes open--nothing familiar is around.')
		io.say('You\'re lying against a gnarled stump, in a copse of lazy trees weighed down by swaying branches. The piece of gold is beside you.')
		player.setDestination('Copse')