import randomizer, params, io, data
import math, random

def go(player):
	io.clear()
	place = player.destination
	if player.destination == 'Tutorial':
		io.say('Hi there! I see you\'ve found the Talk command. It\'s prudent not to begin an adventure alone.')
	elif player.destination == 'Town - Outer Gate':
		if player.is_night():
			if player.verbose():
				io.say('[this place is usually much busier. maybe we should head to the inn...]')
			else:
				io.say('No one seems to pass by at this time of night.')
		else:
			io.say('"Excuse me--do you have the time?" says a passing civilian.')
			io.option(player,'"No."')
			if player.has('Clock'):
				io.option(player,'Check your Clock.')
			c = io.get(player,False)
			if c == 1:
				io.say('"Ah, foolish of me to ask." The civilian shuffles away.')
			elif c == 2:
				io.say('"So it\'s ' + timeStr() + '! Thank you," says the civilian. "So it took me...' + str(params.TOWN_distance_from_crossroads * 60 / 2000) + ' minutes to get from the crossroads to here! Yikes...I\'m not a very quick walker."')
				io.say('He begins to leave. "Thanks again! So many people have forgotten the importance of telling time..."')
	elif player.destination == 'Town - Outer Ring':
		if player.is_night():
			io.say('Tired people quietly shuffle around; none seem interested in talking. Maybe you should wait until daytime.')
		else:
			io.say('You converse with a short man walking near the gate. "I heard that Pheme lost a valuable necklace near the river, when she was just a child. I work at the riverbank, so I went searching for the necklace once--to return it, of course--but I couldn\'t find it before sundown."')
	elif player.destination == 'Town - Pheme\'s Shop':
		io.say('"Well," Pheme\'s cheer turns genuine for a moment. "This is the town\'s information network! Pheme\'s my name, like my father and grandmother.')
		io.say('"There\'s information here from all over the world. Ask about someplace and we\'ve got an answer!"')
	elif player.destination == 'Town - The Stables':
		io.say('"Wha--?" You count the seconds it takes for Ronald to form a sentence. "Oh, sorry...we\'ve been terribly understaffed here. Just like everywhere else, it seems." The whole sentence is one long sigh. "If you\'re staying here for a while, you should get a carriage as soon as possible--I couldn\'t be awake right now if I had to walk everywhere."')
		if not player.seen('Gold'):
			io.say('Makes sense--you should come back if you find any money.')
	elif player.destination == 'Town - Inner Ring':
		if player.is_night():
			io.say('Tired people quietly shuffle around; none seem interested in talking. Maybe you should wait until daytime.')
		else:
			io.say('"Excuse me," a woman with short red hair approaches you. "Do you have time for a quick question?"')
			io.option(player,'"Yes."')
			io.option(player,'"No."')
			c = io.get(player,False)
			if c == 1:
				io.say('"I have to meet someone on the opposite side of town. I would go straight there, by walking through the center of town, but I\'d rather avoid that weird palace. Do you know how much longer it would take to walk along the ring instead of through it? Travel half the circumference instead of the diameter?"')
				io.option(player,'"Yes."')
				io.option(player,'"No."')
				c = io.get(player,False)
				if c == 1:
					io.say('How much longer will it take? (Enter a percentage, as an integer from 0 to 100.)')
					i = getInt(100) - 57
					if i < -1:
						io.say('"Hmm...really? I thought it would be a longer journey than that..."')
					elif i > 1:
						io.say('"I would lose THAT much time? ...are you sure that\'s right?"')
					else:
						io.say('"Sounds about right. Thanks for your help!')
						io.say('"By the way, were you looking for something? If you want my advice...')
						io.say('"Some things are easier to see at night than during the day. If you have a light source, like a lantern or torch, you can discover things which would usually be undetectable."')
			if c == 2:
				io.say('"No problem--I\'ll ask someone else."')
	elif player.destination == 'Town - General Store':
		io.say('"Slow day? I haven\'t had a busy day in weeks. Nobody travels anymore, nobody builds...')
		io.say('"Not that I\'m complaining, since that means more traveling and building for me. I get a lot of time for engineering, so things are going okay, all things considered.')
		io.say('"I hope you don\'t need to buy any differential gears, though. They\'re a part of my Alkahest Drive now, and it\'ll take me a while to figure out how to disassemble it."')
	elif player.destination == 'Town - The Inn':
		if player.has('Automaton'):
			io.say('"No, there haven\'t been a lot of visitors lately," says the innkeeper. "This town isn\'t exactly a tourist favorite. Maybe I should buy some board games for the lounge?"')
		else:
			io.say('"I hear the newspaper\'s going out of business," says the innkeeper. "One of the writers works in the lounge every morning--he\'s worrying through the roof. If only he were better with numbers..."')
	elif player.destination == '???':
		io.say('...')
	elif player.destination == 'Tower - L4':
		if player.seen('Gremlin Trick'):
			io.say('The gremlins run and cackle as usual, but they seem interested in your attempts to solve their little puzzle.')
			io.option(player,'Approach a blue gremlin.')
			io.option(player,'Approach an indigo gremlin.')
			io.option(player,'Approach a pink gremlin.')
			io.option(player,'Approach a purple gremlin.')
			c = io.get(player,False)
			if c == 1:
				io.say('You play fetch with a blue gremlin, deciding not to clarify the fact that "teleportation" is technically a subset of "cheating."')
				s = 'upper-right'
			elif c == 2:
				io.say('You comfort a lonely indigo gremlin, whom the others had ignored for an entire six seconds.')
				s = 'middle-left'
			elif c == 3:
				io.say('You watch a pink gremlin demonstrate a new magic trick. It\'s clearly new at this, as it drops the playing cards from its sleeve; strange, considering it has neither.')
				s = 'lower-right'
			elif c == 4:
				io.say('A purple gremlin carries a poetry book in its mouth; it seems upset at its lack of arms. You carefully take the book and read a few pages aloud.')
				s = 'upper-left'
			if player.seen('Gremlin Hint'):
				io.say('Unfortunately, it isn\'t interested in providing another hint, and soon goes back to its usual self.')
			else:
				player.remember('Gremlin Hint')
				io.say('It seems to appreciate your company, but it abruptly leaves for the other side of the room. When you follow, it indicates the ' + s + ' kennel, then looks back at you. Is this a hint to the puzzle...?')
		else:
			io.say('You try to approach the gremlins, but can\'t seem to hold their attention. None of them are interested in talking, at least for the moment.')
	elif player.destination == 'Tower - Catalogues':
		i = player.getChecks('Catalogues')
		if i < 5:
			io.say('Strange...every hallway seems empty.')
		elif i < 10:
			io.say('Nobody here but that weird spider; you wouldn\'t have noticed it if it hadn\'t bumped its head on a nearby chandelier.')
			io.say('It seems preoccupied by a length of webbing held between its legs. It appears to be a new design for a 24-point truss.')
		elif i < 15:
			io.say('The spider can\'t talk; neither can the fish. They\'re underwater, after all. I mean, they are in spirit, I guess.')
		elif i < 20:
			io.say('You say hello. Some of them smile in acknowledgement, but nothing is spoken in response.')
		elif i < 24:
			io.say('The hallways are actually sort of crowded now, but still no one is capable of talking. They are, however, capable of jumping out of the way when the behemoth comes charging through.')
		else:
			io.say('A few of the creatures request your attention. They seem to be worried about room 17.')
	elif player.destination == 'The End':
		io.say('"Er...there\'s no one else here," the magician says awkwardly.')
	else:
		if player.verbose() and player.seen('Tock'):
			if player.destination == 'Copse':
				io.say('[oh, yeah--this is where you first showed up, right?]')
			elif player.destination == 'Crossroads':
				if not player.has('Automaton'):
					if not player.seen('Lucas'):
						io.say('[i have a friend in town named lucas--you might like him. he\'s been having trouble at work, though...maybe you could help him, if you have the time?]')
					else:
						io.say('[if you\'re not sure what to do in the town, maybe try taking some data, like with a clock or meterstick? i\'m not sure how to tell whether data are useful, but i bet you could figure it out.]')
				elif player.haveAllTreasures():
					io.say('[should we head for the tower? i don\'t know what else to try.]')
				elif player.seen('Clocktower'):
					io.say('[you think the automaton wants to help you find your way home? that...makes a lot of sense. well, i\'ve heard of a few similar treasures around the world--maybe we can try finding them too?]')
				else:
					io.say('[we should head for the tower. something tells me it\'s your best shot at getting home.]')
					io.say('Tock doesn\'t elaborate on what the "something" is.')
			elif player.destination == 'Canyon - L1':
				io.say('[woah...i\'ve never seen this place so quiet.]')
			elif player.destination == 'Garden - Entrance':
				io.say('[woah...i\'ve never seen this place so quiet.]')
			elif player.destination == 'River - Northern Bank':
				io.say('[normally people live here. i wonder where they went?]')
			elif player.destination == 'The Off Road':
				io.say('[this place used to look a lot nicer,] says Tock, looking down the road into the forest. [it wasn\'t really well-visited then, either.]')
			elif player.destination == 'Shrine - Vestibule':
				io.say('Tock looks at the gargoyle and shrugs. [the big guy never talked to me either.]')
			elif player.destination == 'Before the Clocktower':
				if player.haveAllTreasures():
					io.say('[wow...this is it, huh?]')
				else:
					io.say('[that\'s it--the tower! we should go there as soon as possible--i know someone there who might help you get home.]')
					io.say('[uh...are you doing okay?]')
		else:
			io.say('There\'s no response.')