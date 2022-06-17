import randomizer, params, io, data
import math, random

def go(player):
	def printGremlins(g):
		s = ['Purple',' Blue ','Indigo',' Pink ','      ',' ???? ']
		print ' ----------------------------'
		print ' | ' + s[g[0]] + ' | ' + s[g[1]] + ' | ' + s[g[2]] + ' |'
		print ' ----------------------------'
		print ' | ' + s[g[3]] + ' | ' + s[g[4]] + ' | ' + s[g[5]] + ' |'
		print ' ----------------------------'
		print ' | ' + s[g[6]] + ' | ' + s[g[7]] + ' | ' + s[g[8]] + ' |'
		print ' ----------------------------\n'
	def transformGremlins(g):
		table = [
			g[0] + g[1] + g[3],
			g[1] + g[0] + g[2] + g[4],
			g[2] + g[1] + g[5],
			g[3] + g[0] + g[4] + g[6],
			g[4] + g[1] + g[3] + g[5] + g[7],
			g[5] + g[2] + g[4] + g[8],
			g[6] + g[3] + g[7],
			g[7] + g[4] + g[6] + g[8],
			g[8] + g[5] + g[7]
		]
		for i in range(9):
			table[i] %= 4
		return table
	io.option(player,'Return downstairs.')
	io.option(player,'Examine the kennels.')
	if player.seen('Gremlin Kennels'):
		io.option(player,'Count the gremlins.')
	if player.seen('Gremlin Trick'):
		io.option(player,'Place the gremlins in the kennels.')
	c = io.get(player)
	if c == 1:
		io.say('You descend the stairs; none of the gremlins seem to follow.')
		player.setDestination('Tower - L3')
	elif c == 2:
		io.say('You find a set of 9 kennels in a square arrangement. They\'re labeled in a particular order:')
		print(' Indigo  Pink  Purple')
		print('  Pink  Purple  Blue')
		print(' Indigo  Blue   Pink\n')
		player.remember('Gremlin Kennels')
		io.say('Each kennel seems to be designed only for a certain gremlin.')
	elif c == 3:
		io.say('Counting carefully, you notice there are 9 gremlins in total:')
		io.say('2 gremlins are BLUE, with the head of a fish and the body of a badger. Their breath is noxious...and somehow visible.')
		io.say('2 gremlins are INDIGO, with the skin of a coral and the eyes of a goat. They have prickly hair and six sticky feet.')
		io.say('3 gremlins are PINK, with the front of a gorilla, the back of a chicken, and the tail of a sauropod. They have jaws on the back of their necks.')
		io.say('2 gremlins are PURPLE, with the body of a slug and the face of a bug-eyed shrimp. You\'re not sure if they\'re even 3-dimensional; maybe 3.4?')
		if not player.seen('Gremlin Trick'):
			io.say('At least they seem to match the labels on the kennels.')
			io.option(player,'Place the gremlins in the corresponding kennels.')
			io.option(player,'Well...')
			c = io.get(player,False)
			if c == 1:
				kennels = [2,3,0,
						   3,0,1,
						   2,1,3]
				kennels = transformGremlins(kennels)
				io.say('Collecting the gremlins isn\'t as difficult as you expected. You manage to catch each one and haul it to the correct kennel, where it stays without a fuss. Eventually you\'ve gathered all of them.')
				io.say('Oh, no...the door is still closed.')
				io.say('The gremlins\' chattering grows steadily louder. When you turn around to see what they\'re laughing about, you find a completely different set of gremlins looking back at you. You\'re sure this wasn\'t how they were before.')
				printGremlins(kennels)
				io.option(player,'What happened...?')
				io.get(player,False)
				player.remember('Gremlin Trick')
				io.say('As the transformation spell wears off, the mismatched gremlins leap from their kennels, roaring with laughter at their prank. Back to square one.')
				io.say('They labels on the kennels were wrong--the gremlins must have fooled the record keeper with the same trick. There must be a way to find the correct arrangement--if only you could look back in time...')
			elif c == 2:
				io.say('You decide to deal with them later. Nearby, two gremlins throw a third one to the top of a bookcase, while a fourth one conjures paper birds to attack a fifth...you\'re not looking forward to chasing any of them.')
	elif c == 4:
		cancelled = False
		kennels = [4]*9
		for i in range(9):
			if cancelled:
				break
			while True:
				kennels[i] = 5
				io.say('Which gremlin should go here?')
				printGremlins(kennels)
				io.option(player,'Blue.')
				io.option(player,'Indigo.')
				io.option(player,'Pink.')
				io.option(player,'Purple.')
				io.option(player,'Nevermind.')
				c = io.get(player,False)
				if c == 5:
					io.say('Hmm, that doesn\'t seem like it\'ll work. If only you could look back in time...')
					cancelled = True
					break
				else:
					num = c % 4
					if kennels.count(num) < [2,2,2,3][num]:
						kennels[i] = num
						break
					else:
						s = ['purple','blue','indigo','pink'][num]
						io.say('Oops--there are no more ' + s + ' gremlins in the room!')
		if not cancelled:
			io.say('Sounds like a plan. You recapture the gremlins like before, but you\'re ready for their tricks this time. You turn away, turn back, and...')
			kennels = transformGremlins(kennels)
			printGremlins(kennels)
			if kennels == [2,3,0,
						   3,0,1,
						   2,1,3]:
				io.say('With a shower of dust and the crashing of half-dissolved gears, the door staggers open. You\'ve done it! The gremlins become louder, and you quickly slip through the door while the kennels still hold. But the noise seems somewhat different now. The cackling and stomping slowly fades into...cheers and applause?')
				io.say('With the door closed, there is nowhere to go but a little wooden elevator. It seems to be controlled by an old brass gauge; a green light faintly informs you that it\'s functioning properly.')
				io.option(player,'Take the elevator up.')
				io.get(player,False)
				io.say('The elevator shivers for a moment, and you hear a few pulleys turning just above...soon the elevator is crawling up the tower.')
				player.wait(12)
				io.say('After a long wait, the elevator crashes to a halt. It seems to be stuck.')
				io.option(player,'Step outside.')
				io.get(player,False)
				player.remember('Tower - L5')
				player.setDestination('Tower - L5')
			else:
				io.say('The door remains closed, and the gremlins leap out of their kennels. Back to square one.')