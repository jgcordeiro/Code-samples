import randomizer, params, io, data
import math, random

def go(player):
	io.say('From atop the clocktower, you can see more of this world than you ever have or will. You can see all the places you\'ve been, and all the people who\'ve lifted you to where you are now. The wind screams and the floor sways, but you block it out. Your attention is drawn to a figure at the other side of the tower, blurry though in plain view.')
	io.say('The magician sleeps on the slanted edge of the roof, feet rested on a couple of crooked shingles. A sketchbook sits nearby, along with a bounty of pencils and twice as many erasers. The magician\'s ragged boots match a hundred thousand prints over the surface of the roof. Of all the floors, this is clearly the one most visited. And yet, there\'s nothing here--just the view of the world you\'re leaving.')
	io.option(player,'Approach.')
	io.get(player,False)
	io.say('Aah! Who are--uh...hi. Nice to meet you.')
	io.option(player,'Introduce yourself.')
	io.option(player,'"Who are you?"')
	c = io.get(player,False)
	if c == 1:
		io.say('Okay...')
		io.say('...so, uh...')
		io.say('...how did you get here?')
		io.option(player,'"I took the elevator."')
		io.option(player,'"I worked out the locks, got the elevator working, started the furnace..."')
		io.option(player,'"I was just helping people, and came across five treasures..."')
		io.option(player,'"I don\'t know. One moment I was strolling down the sidewalk..."')
		c = io.get(player,False)
		if c == 1:
			io.say('The elevator...that\'s right, there\'s an elevator. Wasn\'t it broken?')
			io.option(player,'"Not anymore."')
			io.option(player,'"I had some help along the way."')
			c = io.get(player,False)
			c += 1
		if c == 2:
			io.say('Well, thank you kindly for the help. I\'m no good at maintenance.')
			io.option(player,'"Who are you?"')
			io.option(player,'"I had some help along the way."')
			io.option(player,'"Are you the reason I\'m here? In this world?"')
			c = io.get(player,False)
			c += 1
		if c == 3:
			io.say('You mean--oh, I get it. You couldn\'t have even approached this tower without all five treasures. And you managed to find them all...?')
			io.option(player,'"I wanted to help people; they helped me get here."')
			io.option(player,'"I wanted to go home; there are people waiting for me."')
			c = io.get(player)
			if c == 1:
				io.say('Clever, calculating, and kind...I\'ll admit, I\'m envious three times over.')
				io.option(player,'"Who are you?"')
				io.option(player,'"Are you the reason I\'m here? In this world?"')
				io.get(player,False)
			elif c == 2:
				c = 4
		if c == 4:
			io.say('What do you mean--')
			io.say('--oh.')
			io.say('Oh, no...')
			io.option(player,'"What\'s wrong?"')
			io.option(player,'"Who are you?"')
			c = io.get(player,False)
			if c == 1:
				io.say('I\'m sorry...I might have made an awful mistake.')
	io.say('I\'m...let\'s see, what am I...? I\'m a magician who\'s lived out here for a little while. I\'m a little surprised you showed up--I didn\'t know anyone could even come near this tower, much less reach the top.')
	while True:
		io.option(player,'"What is this place?"')
		io.option(player,'"Why are you here?"')
		io.option(player,'"Can you help me get home?"')
		c = io.get(player)
		if c == 1:
			io.say('It was supposed to be a community center of some sort, but no one else has come here in...ever, really.')
			while True:
				io.option(player,'"I see."')
				io.option(player,'"Why has no one come here?"')
				io.option(player,'"You know that only \'Rex\' can pass the first door, right?"')
				io.option(player,'"What are the tins on the third floor meant to be?"')
				io.option(player,'"Do you know about all the gremlins on the fourth floor?"')
				io.option(player,'"The elevator was broken--how do you reach the lower floors?"')
				io.option(player,'"How long has the furnace been broken? Haven\'t you needed it?"')
				if player.seen('Catalogues'):
					io.option(player,'"You created everything in the Catalogues, right?"')
				c = io.get(player,False)
				if c == 1:
					break
				elif c == 2:
					io.say('The grand opening flopped, and things went downhill from there.')
				elif c == 3:
					io.say('I haven\'t bothered to make this place walkable for a long time. I\'m sorry about any danger you encountered.')
				elif c == 4:
					io.say('Third...floor? Oh, right, I moved them up from the kitchen. Didn\'t you read the labels?')
				elif c == 5:
					io.say('They escaped a while ago. I managed to distract them with little games, but I can never seem to catch them for good. I\'m surprised you were able to get past them.')
				elif c == 6:
					io.say('There\'s, uh...this is embarassing...there\'s window cleaning equipment attached to this roof. Hey, easier than fixing the elevator.')
				elif c == 7:
					io.say('I was going to try fixing it before winter; I wasn\'t looking forward to it.')
				elif c == 8:
					io.say('Yes. I still visit once in a while, but they haven\'t left the Catalogues in a long time. I hope they\'re okay.')
					io.option(player,'"They seemed fine."')
					io.option(player,'"They seemed a little down."')
					io.option(player,'"So...what exactly are your powers?"')
					c = io.get(player,False)
					if c == 1:
						io.say('That\'s good. I\'m afraid they won\'t tell me if they\'re not.')
					elif c == 2:
						io.say('Oh. Well...thanks for talking to them, anyway.')
					elif c == 3:
						io.say('I\'ve heard people describe them as "a monkey\'s paw." At best, I can do pretty much anything--but it can\'t conflict with something I did earlier. So if I create or change something, it becomes totally immune to my powers. It\'s trickier than it sounds.')
			io.say('...anyway...')
		elif c == 2:
			io.say('What do you mean? I live here.')
			io.option(player,'"So you\'re...a prisoner?"')
			io.option(player,'"So you\'re...a recluse?"')
			c = io.get(player,False)
			if c == 1:
				io.say('What? No, no! I\'m here by my own choice.')
			elif c == 2:
				io.say('No, there are plenty of others staying here. They\'re on the previous floor.')
		elif c == 3:
			break
	io.say('I\'ll try. After all...I think I caused all of this.')
	io.say('Something went wrong while I was working. I opened some sort of trapdoor, through which you apparently fell. I didn\'t want any of this to happen, and I didn\'t realize you\'d end up here...but now that you are, I\'ll try to set things right.')
	io.option(player,'Okay. Thank you.')
	io.option(player,'Okay. I\'ll help however I can.')
	io.get(player,False)
	io.say('So, let\'s see...where did you come from? In fact, on that note, how did you get here? Because that shouldn\'t be...at all possible.')
	io.option(player,'Explain everything. Who you are, your whole adventure...')
	io.get(player,False)
	io.say('...I...I understand...')
	io.option(player,'...')
	io.get(player,False)
	io.say('...I suspected that\'s what I was doing wrong...')
	io.option(player,'...')
	io.get(player,False)
	io.say('Whenever I used my powers, I considered them a vector of "greatness" and "goodness." I had the power to make a "great" impact, and the goodwill to pursue a "good" direction. So how did everything go so wrong? How was I so vilified?')
	io.say('Because there was a third dimension I neglected. Something I never realized all this time. Something by which you accomplished what I never could.')
	io.say('I had the body and the heart, but not the Mind.')
	io.option(player,'...')
	io.get(player,False)
	io.say('You traveled to a whole new world. No friends, no powers but the wits you brought with you. With nothing but your humanity, you helped yourself and others far more than I could in years.')
	io.say('I hope you know how inspiring that is. Cherish your mind. Remember how powerful you are. Take it from me: all the strength in the world is nothing without cleverness and carefulness to guide it.')
	io.option(player,'Final Results?')
	io.get(player,False)
	showFinalResults()
	io.hline()
	io.say('EPILOGUE')
	io.hline()
	io.option(player,'Continue.')
	io.get(player,False)
	playEpilogues()
	ending = self.ending
	if ending == '* * * * *':
		io.say('Thank you.')
		io.say('Thank you for all you\'ve taught me.')
		io.say('I think...if I leave this tower, if I give myself one more chance...I could change the world for the better.')
		unlockAchievement('Teachable Moments')
	elif ending == ' * * * * ':
		io.say('Thank you...you\'ve helped this world a great deal on your path home.')
		io.say('I\'ll do everything I can to learn those same abilities, now that you\'ve proven...that it can be done.')
	elif ending == '  * * *  ':
		io.say('Thank you for relating your story...your wit and success are inspiring.')
		io.say('Maybe I can learn to accomplish the same, someday.')
	elif ending == '   * *   ':
		io.say('Thank you for all you\'ve done. I\'m glad you can return home with a healthy conscience.')
	elif ending == '    *    ':
		io.say('Thank you for your admirable efforts, and for helping so many people on your way home.')
	else:
		io.say('Thank you for finding your way here. To be perfectly truthful, I haven\'t talked to a person in quite a while.')
	io.say('')
	io.say('I wish you the best in your own world.')
	io.option(player,'End.')
	io.get(player,False)
	print '----------------------------------------'
	print '| _____ __ __ _____  _____ __ __ ____  |'
	print '| |_ _| ||_|| | __|  | __| | \\|| | _ \\ |'
	print '|  | |  | _ | | _|   | _|  |   | | / | |'
	print '|  |_|  || || |___|  |___| ||\\_| |___/ |'
	print '|                                      |'
	print '----------------------------------------'
	raw_input()