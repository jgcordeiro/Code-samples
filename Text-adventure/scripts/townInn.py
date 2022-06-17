import randomizer, params, io, data
import math, random

def go(player):
	if player.is_morning():
		if player.seen('Lucas'):
			io.say('Lucas is writing urgently on a little blue notepad.')
		else:
			io.say('There\'s almost nobody here--only a bored-looking innkeeper, and a man in a brown cap sitting by the fire.')
	else:
		io.say('There\'s almost nobody here--only a bored-looking innkeeper.')
	io.option(player,'Leave.')
	io.option(player,'Rent.')
	if player.is_morning():
		if player.seen('Lucas'):
			io.option(player,'Approach Lucas.')
		else:
			io.option(player,'Approach the man in the brown cap.')
	c = io.get(player)
	if c == 1:
		io.say('You exit the inn.')
		player.setDestination('Town - Inner Ring')
	elif c == 2:
		io.say('"Welcome! 50 G for a room?" the innkeeper adjusts a clipboard and a scrutinous pair of glasses, not looking up.')
		io.option(player,'Stay until 8:00 AM.')
		io.option(player,'Stay until 12:00 PM.')
		io.option(player,'Stay until 5:00 PM.')
		io.option(player,'Stay until 8:00 PM.')
		io.option(player,'Nevermind.')
		c = io.get(player,False)
		if c == 5:
			io.say('You leave the desk and look around the inn lounge.')
		else:
			if player.seen('Gold'):
				if gold() >= 50:
					changeGold(-50)
					io.say('You rest for a while...')
					io.option(player,'Continue.')
					io.get(player,False)
					if c == 1:
						sleepUntil(480)
					elif c == 2:
						sleepUntil(720)
					elif c == 3:
						sleepUntil(1020)
					elif c == 4:
						sleepUntil(1200)
				else:
					io.say('You\'re unable to pay...')
			else:
				io.say('You\'re not sure how to pay...')
			io.say('You return to the lounge.')
	elif c == 3:
		if player.has('Automaton'):
			io.say('"Best of luck on your journey," says Lucas. He\'s working on a new article now.')
		elif player.seen('Lucas'):
			io.say('"Thanks again for your help," says Lucas. "Do you know how much to spend?"')
			io.option(player,'Yes!')
			io.option(player,'Not yet...')
			io.option(player,'Could you repeat the instructions?')
			c = io.get(player,False)
			# TODO
			if c == 1:
				io.say('"I can\'t thank you enough for what you\'ve done," says Lucas. "Just wait--soon the paper will be better than ever before. We can hire new writers, design better printing...maybe even get some fact-checkers!')
				io.say('"But until then, please accept this gift." He holds out the automaton. It looks like a little golden rabbit, with eyes of silver bolts and ears of copper wire. Inside is a little mechanical engine which silently ticks along. There is no way to wind it, no battery, no fuel...yet it doesn\'t seem to slow down. It turns to face you, tilting its head one click of a gear.')
				io.say('The automaton reminds you of...something. It twitches its ears, and suddenly you begin to think about clocks. Even more suddenly, you begin to think about home. The automaton, such a simple-looking machine, seems like it wants to help you. It knows something.')
				io.say('You thank Lucas. Taking a wild guess, you hold out your hand, and the automaton jumps over to you. You have a rabbit now! You still aren\'t sure how to get home, but somehow, you feel like you have a start.')
				addItem('Automaton')
			elif c == 2:
				io.say('"Okay, let me know when you\'re sure."')
			elif c == 3:
				TOWN_explainquest()
		else:
			io.say('He\'s poring over a map of the town, visibly anxious. He\'s marking up the map with notes, but you can\'t make out his handwriting. One of his eyes follows a little automaton in his other hand.')
			io.say('You sit at the opposite end of the table, but it take him a while to speak. "Oh, hello. If you don\'t mind, I\'m very busy right now...oh, I\'m in so much trouble...')
			io.option(player,'"What\'s wrong?"')
			io.option(player,'"Nevermind."')
			c = io.get(player,False)
			if c == 1:
				io.say('"Have you heard about the town paper? ...No, of course you haven\'t, because we\'re going out of business. We can\'t even afford to pay our employees...')
				io.say('"I want to start asking for donations, but, well...I\'m not sure exactly how much money I need to raise. I just need to find that, and then...I guess I\'ll figure something out."')
				io.option(player,'Donate.')
				io.option(player,'Leave.')
				c = io.get(player,False)
				if c == 1:
					if player.seen('Gold'):
						io.say('You present the gold you have and ask if it\'s enough.')
						io.say('"What--yes! More than enough, I\'d say! I don\'t know how you became so wealthy, but I\'m honored you\'d help out the newspaper like this.')
						io.say('"In fact, what do you say about an investment? I know I can get the paper in business again if I just manage to pay one more week...I have some ideas to turn things around. So, how about this: you pay my workers\' weekly salary, and I return with interest once everything\'s up and running again?"')
						io.option(player,'Okay.')
						io.option(player,'No.')
						c = io.get(player,False)
						if c == 1:
							io.say('"Really? That\'s great! I\'m Lucas, by the way.')
							io.say('"So, here\'s the complicated part:')
							TOWN_explainquest()
							player.remember('Lucas')
							io.option(player,'Quest accepted!')
							io.get(player,False)
						elif c == 2:
							io.say('"Alright...I guess it was a long shot anyway. See you."')
					else:
						io.say('You consider donating, but you realize you have no money!')
				elif c == 2:
					io.say('You wish him luck and exit the lounge.')
			elif c == 2:
				io.say('You decide to leave him be.')