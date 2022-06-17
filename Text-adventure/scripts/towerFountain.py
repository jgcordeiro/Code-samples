import randomizer, params, io, data
import math, random

def go(player):
	bottles = [0.,0.,0.,0.]
	hexagon = 41.3488
	petals = 19.5504
	volumes = [33.2357,3*hexagon,hexagon+petals,hexagon-petals]
	player.remember('Tower - L2')
	io.say('There\'s a bit more sound on this floor--a delicate fountain swirls in the middle of the room.')
	io.say('There\'s a huge door blocking the stairwell, which seems to be locked; a placard says "Closed until --/--/----." There seems to be no way through, but you do find a smaller side door. There\'s a pile of discarded ceramic bottles next to it.')
	while destination() == "Tower - L2":
		io.option(player,'Open the side door.')
		io.option(player,'Return downstairs.')
		if not player.seen('Tower - L3'):
			io.option(player,'Examine the fountain.')
			io.option(player,'Examine the bottles.')
		c = io.get(player)
		if c == 1:
			if player.seen('Tower - L3'):
				io.say('You open the door and ascend to floor 3.')
			else:
				io.say('This one\'s locked too, but the posted sign is a bit more promising:')
				print('   Rex,\n')
				print('     If you ever want to come back,')
				print('     add exactly 100 mL of water to')
				print('     the nearby vase.\n')
				print('     Sorry for the inconvenience...')
				print('     I can\'t afford anyone else to')
				print('     come here.\n')
				print('   Hope you\'re safe!\n')
				io.say('Hmm...it looks like this door was only made for one visitor. Someone who\'s really good at measuring volume.')
				io.option(player,'Call for the idol.')
				io.option(player,'Nevermind.')
				c = io.get(player,False)
				if c == 1:
					io.say('Suddenly you reconsider. The idol--"Rex," apparently--is at the other end of the room, immobile as ever. Only one visitor is allowed to pass here...you wonder if this is the last time you\'ll see the idol.')
					io.option(player,'Call for the idol now.')
					io.option(player,'Not yet.')
					c = io.get(player,False)
					if c == 1:
						io.say('The idol reads the note on the door, and a strange expression crosses its face. It goes to the fountain, fills the stone cup to a hundred milliliters exactly, and moves back toward the door. You try suggesting another way, but it\'s as stubborn as stone--the idol knows you\'ll have to continue by yourself.')
						io.say('The door opens at a snail\'s pace, but the instant you cross the doorframe, it slams shut, trapping you without your stalwart friend. Just before the door closed, you could have sworn you saw the idol waving goodbye...')
						io.say('Oh, well. There are more stairs to climb.')
						loseItem('Idol')
						io.option(player,'Continue to the next floor.')
						io.get(player,False)
						player.setDestination('Tower - L3')
					elif c == 2:
						io.say('Maybe later...')
				elif c == 2:
					io.say('Maybe later...')
		elif c == 2:
			io.say('You return to the base of the tower.')
			player.setDestination('Tower - L1')
			break
		elif c == 3:
			io.say('Despite all the disuse, the fountain is crystal clear. The sounds of the splashing water are wonderfully melodic. But you must continue.')
		elif c == 4:
			io.say('There are bottles of all shapes and sizes, lying by the side door. All but four have been reduced to shards. Someone has been trying to open the door, and they\'ve clearly gotten frustrated.')
			io.say('The first bottle has a circular base. It also has a check mark drawn on the side, which seems to indicate it\'s the correct one to use...but part of the top is broken. That\'s not good...')
			io.say('The second bottle has a large hexagonal base. It\'s half as tall as the first bottle, and three times as tall as the other bottles.')
			io.say('The third bottle has a flower-shaped base: it looks like the hexagon, but its sides are curved outward to form six petals. Each petal matches the curvature of the first bottle, and all six petals intersect at the center.')
			io.say('The fourth bottle has a star-shaped base: it\'s just like the flower, but the sides are curved inward instead of outward.')
			io.option(player,'Try using these bottles.')
			io.option(player,'Nevermind.')
			c = io.get(player,False)
			if c == 1:
				io.say('What to do...?')
				while True:
					io.option(player,'Fill the partly broken cylinder.')
					io.option(player,'Fill the hexagonal bottle.')
					io.option(player,'Fill the flower-shaped bottle.')
					io.option(player,'Fill the star-shaped bottle.')
					print ''
					io.option(player,'Pour the partly broken cylinder.')
					io.option(player,'Pour the hexagonal bottle.')
					io.option(player,'Pour the flower-shaped bottle.')
					io.option(player,'Pour the star-shaped bottle.')
					print ''
					io.option(player,'Nevermind...none of these are useful.')
					c = io.get(player,False)
					if c in range(1,5):
						bottle = c - 1
						bottles[bottle] = volumes[bottle]
						if c == 1:
							io.say('There\'s a check mark drawn on this bottle, which seems to indicate it\'s the correct one to use...but part of the top is broken. You fill it with a modicum of water, but it can never reach the brim.')
						else:
							io.say('You carefully fill the bottle.')
					elif c in range(5,9):
						bottle = c - 5
						if bottles[bottle] == 0.:
							io.say('That\'s already empty!')
						else:
							io.say('Pour into what?')
							io.option(player,'Pour into the partly broken cylinder.')
							io.option(player,'Pour into the hexagonal bottle.')
							io.option(player,'Pour into the flower-shaped bottle.')
							io.option(player,'Pour into the star-shaped bottle.')
							io.option(player,'Pour back into the fountain.')
							io.option(player,'Pour into the vase by the side door.')
							c = io.get(player,False)
							if c in range(1,5):
								otherBottle = c - 1
								if bottle == otherBottle:
									io.say('This is a water bottle, not a Klein bottle!')
								else:
									emptySpace = volumes[otherBottle] - bottles[otherBottle]
									if bottles[bottle] > emptySpace:
										bottles[bottle] -= emptySpace
										bottles[otherBottle] = volumes[otherBottle]
										io.say('The other bottle becomes full; you stop pouring.')
									else:
										bottles[otherBottle] += bottles[bottle]
										bottles[bottle] = 0
										io.say('You pour all the water into the other bottle.')
							elif c == 5:
								bottles[bottle] = 0
								io.say('You dump out the bottle.')
							elif c == 6:
								if abs(bottles[bottle] - 100) < 0.001:
									io.say('That\'s it--the door slides open! You pass through the door, which slams shut behind you.')
									io.say('After a bit of waiting, the door opens again, and the idol rejoins you; it must have heard the crash and followed. You\'re trapped now, with only the stairs onward, but you aren\'t alone yet.')
									io.option(player,'Continue up the stairs.')
									io.get(player,False)
									player.setDestination('Tower - L3')
									break
								else:
									io.say('That doesn\'t seem like the right answer...')
					elif c == 9:
						io.say('Okay...looks like there\'s only one choice.')
						break
			elif c == 2:
				io.say('Okay...what to do instead?')