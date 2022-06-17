import randomizer, params, io, data
import math, random

def go(player):
	if player.verbose():
		io.say('[you can reach the tower?] Tock floats bouncily in front of you. [then you can go home! i knew you could do it!]')
		io.option(player,'...')
		io.get(player,False)
		io.say('[go to the highest floor of the tower, and you\'ll be back in your own world. it was really nice meeting you--i hope you have a great life!]')
		io.option(player,'"I understand. Thanks, Tock."')
		io.option(player,'"Could you go to the tower with me?"')
		io.option(player,'"Wait..."')
		c = io.get(player,False)
		if c == 2:
			io.say('[i\'m sorry, but i can\'t. it would be better for everyone if i stay away from that tower.]')
			io.option(player,'"...okay?"')
			io.option(player,'"Why are you avoiding the tower?"')
			io.option(player,'"Why have you been avoiding everyone?"')
			c = io.get(player,False)
			if c == 1:
				io.say('[don\'t worry. you\'ve made it this far...i\'m sure you can do this.]')
				io.option(player,'"I will. Thanks, Tock."')
				io.option(player,'"Wait..."')
				c = io.get(player,False)
				if c == 2:
					c = 3
			else:
				io.say('Tock\'s face falls.')
				io.say('[...i shouldn\'t be talking about it. this is your moment, i don\'t want to ruin it.]')
				io.option(player,'"Alright, sorry I brought it up."')
				io.option(player,'"But if there\'s some way I can help..."')
				c = io.get(player,False)
				if c == 1:
					io.say('[it\'s fine.]')
					io.say('The brief moment of silence feels longer than the entire time you\'ve wandered this world.')
					io.option(player,'"You\'ve been a great help, Tock. It was nice to meet you too."')
					io.option(player,'"Wait..."')
					c = io.get(player,False)
					if c == 2:
						c = 3
				if c == 2:
					io.say('Tock\'s voice begins to shake. You\'re not sure what to say to defuse the situation.')
					io.say('[no, no, no, you shouldn\'t have to deal with this. i\'m sorry...i shouldn\'t have brought this up. i ruined it, didn\'t i? you were so happy to go home, and i ruined it.]')
					io.option(player,'"You didn\'t ruin anything."')
					io.option(player,'"Why do you say that?"')
					c = io.get(player,False)
					if c == 1:
						io.say('Tock calms down a bit.')
						io.say('[you\'re a good friend to say that. you\'ll do just as great in your world as you did in this one.]')
						io.option(player,'"Thanks, Tock."')
						io.option(player,'"Wait..."')
						c = io.get(player,False)
						if c == 2:
							c = 3
					elif c == 2:
						io.say('[BECAUSE THAT\'S WHAT I DO!]')
						io.say('A part of you saw it coming, but the distress in Tock\'s voice is painful. As you comfort the mysterious character, Tock finally begins to explain:')
						io.say('[when i first showed up, i caused a lot of trouble. the more i was around, the more damage and destruction followed. i was no better than a natural disaster, i\'ll never forget...then i met you, and i could talk to someone again, as long as you didn\'t find out who i am. please believe me when i say i only wanted to help people...]')
						io.option(player,'"It sounds like you\'ve been through a lot."')
						io.option(player,'"Whatever you were before, you\'re a good friend now."')
						io.option(player,'"You think none of those people will forgive you?"')
						c = io.get(player,False)
						if c == 1:
							io.say('[it doesn\'t matter, i\'m over it. you have a world to get back to, not me.]')
						elif c == 2:
							io.say('[really? ...thank you. i must have been really lucky.]')
						elif c == 3:
							io.say('[i\'d rather not find out.]')
						io.option(player,'"Thank you for telling me about this. I won\'t forget you."')
						io.option(player,'"Wait..."')
						c = io.get(player,False)
						if c == 2:
							c = 3
		if c == 3:
			while True:
				io.say('[...]')
				io.option(player,'"What\'s so strange about this tower?"')
				io.option(player,'"Are you sure you\'ll be okay?"')
				io.option(player,'"You should visit the town again, at least once."')
				io.option(player,'"...nevermind."')
				c = io.get(player,False)
				if c == 1:
					io.say('[the tower has oddities which i can\'t quite explain, but they mean no harm toward you. to be honest, they could really use your help.]')
				elif c == 2:
					io.say('Tock laughs quietly.')
					io.say('[hey, i\'m supposed to advise you, remember?]')
					io.say('[...yes, i think i\'ll be fine.]')
				elif c == 3:
					io.say('[but i--okay, i\'ll try. i promise.]')
					io.say('Tock is nervous as ever, but somehow seems a bit calmer than before. You feel like you said exactly what Tock needed to hear.')
					unlockEpilogue('Tock')
				elif c == 4:
					io.say('[don\'t worry--you don\'t have much farther to go. i\'m sure you\'ll do great.]')
				io.option(player,'"Thanks, Tock."')
				io.option(player,'"Wait..."')
				c = io.get(player,False)
				if c == 1:
					break
		setVerbose(False)
		io.say('Tock smiles sweetly for one moment, then disappears in the next.')
	io.say('Alright...here we go.')
	io.option(player,'Set off for the tower.')
	io.get(player,False)
	player.travel(14142)

	io.say('You set up the carriage and begin your journey. On your left, the garden sinks under the horizon. On your right, the canyon swerves away.')
	io.option(player,'Keep going.')
	io.get(player,False)
	player.travel(16180)

	io.say('Your stomach falls at the terrible distance.')
	io.option(player,'Keep going.')
	io.get(player,False)
	player.travel(27183)

	io.say('The worried whining of the ' + steed() + ' begins to rise. Thank goodness someone said it.')
	io.option(player,'Keep going.')
	io.get(player,False)
	player.travel(31416)

	io.say('You feel relieved of your burdens.')
	io.option(player,'Almost there.')
	io.get(player,False)
	player.travel(43210)

	io.say('The carriage slows to a halt.')
	io.say('You release the yolk, allowing the ' + steed() + ' to return home. As you turn to face the tower door, the idol stands guard nearby, and the automaton looks over your shoulder. You\'re ready for whatever this tower holds.')
	setSteed('none')
	loseItem('Sleeping Bag')
	while True:
		io.option(player,'Open the door.')
		c = io.get(player)
		if c == 1:
			io.say('The base of the clocktower is far grander than you expected. A remarkably clean carpet leads to a wide staircase, and at the top, a gallery which seems much greater than the diameter of the tower can hold. The tower has two wings connected by small gray doors, both open--one seems to lead to a kitchen, and the other to a dining hall. A banner clings by one end to the ceiling--it reads "Welcome to the Clocktower!" The place looks like an ancient surprise party which was never sprung.')
			player.setDestination('Tower - L1')
			break