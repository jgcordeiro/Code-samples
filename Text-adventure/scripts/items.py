import randomizer, params, io, data
import math, random

def go(player):
	io.clear()
	inventory = player.inventory
	if player.destination == 'Tutorial':
		io.say('There\'s the Items command! Check back here when you find some items; they can come in handy during the game\'s challenges.')
	elif not inventory:
		io.say('You don\'t have any items yet. Find some!')
	else:
		numChoices = 0
		print 'Which item do you need?\n'
		for s in inventory:
			io.option(s)
		useItem(inventory[get(False) - 1])

def useItem(player):
	io.clear()
	useOnce = False
	if item == 'Clock':
		io.say('It\'s ' + timeStr() + ' right now.')
		if timeMemory():
			io.say('The last time you used the clock was ' + timeMemory() + '.')
		else:
			io.say('You record the time.')
		setTimeMemory(timeStr())
	elif item == 'Meterstick':
		io.say('You invoke the meterstick.')
		if destination() == 'Copse':
			player.wait(5)
			io.say('The nearest visible root is %.2f meters.' % randomize(5,2))
			io.say('The tree stump has a diameter of 2.03 meters, and a height of 1.52 meters.')
			io.say('The second-nearest visible root is...this place isn\'t very interesting, is it?')
		elif destination() == 'Crossroads':
			player.wait(8)
			io.say('The signpost is 2.36 meters tall.')
			io.say('Each marker is about 1.3 meters wide.')
			io.say('The cobblestones are about %.1f by %.1f centimeters.' % (randomize(16,6),randomize(20,8)))
			io.say('You consider finding a new hobby.')
		elif destination() == 'Town - Outer Ring':
			player.wait(12)
			io.say('The nearest storefront is about %.2f meters wide.' % randomize(params.TOWN_outer_building_width,2))
			io.say('The alley separating this store from the next is about %.2f meters wide.' % randomize(params.TOWN_outer_distance_between_buildings,0.2))
			io.say('You check a couple of lampposts lined up toward the center of town: they\'re %.2f meters apart.' % randomize(params.TOWN_distance_between_lampposts,0.2))
			io.say('You measure the circular road using a slight perpendicular curb. It\'s about %.2f meters wide here.' % randomize(params.TOWN_width_of_road,0.3))
			io.say('You consider checking the water barrels, flower beds, fences, benches, and sidewalk tiles, but if someone asked what you were doing, you\'re not sure you\'d be able to answer.')
		elif destination() == 'Town - Inner Ring':
			player.wait(16)
			io.say('The nearest building is about %.2f meters wide.' % randomize(params.TOWN_inner_building_width,2))
			io.say('The alley separating this building from the next is about %.2f meters wide.' % randomize(params.TOWN_inner_distance_between_buildings,0.2))
			io.say('You check a couple of lampposts lined up toward the edge of town: they\'re %.2f meters apart.' % randomize(params.TOWN_distance_between_lampposts,0.2))
			io.say('You measure the circular road using a slight perpendicular curb. It\'s about %.2f meters wide here.' % randomize(params.TOWN_width_of_road,0.3))
			io.say('Well, that was fun. Go and find more numbers!')
		else:
			io.say('But you don\'t find any useful information.')
	elif item == 'Automaton':
		io.say('The automaton hops away.')
		player.wait(2)
		if hasUsed('Automaton',destination()):
			io.say('It quickly returns, but it didn\'t find anything.')
		else:
			if destination() == 'Copse':
				io.say('When it comes back, it has a bough of orange berries around its neck.')
				addReagent('Orange Berry',10)
				useOnce = True
			elif destination() == 'Crossroads':
				io.say('It returns with 5 G in its front paws. It seems to have quite the talent for scavenging.')
				changeGold(5)
				useOnce = True
			elif destination() == 'Town - Outer Gate':
				io.say('After running back and forth along the town wall, it stops at your feet and mechanically shakes its head. Looks like there\'s nothing to do here.')
			elif destination() == 'Town - Outer Ring':
				io.say('It reappears behind a nearby bench, 100 G in tow. People lose a lot of money around here...')
				changeGold(100)
				useOnce = True
			elif destination() == 'Town - Pheme\'s Shop':
				io.say('After getting lost under a stack of papers, the automaton retrieves a fountain pen and presents it to you. You apologize to Pheme and return the pen to the desk.')
			elif destination() == 'Town - The Stables':
				io.say('You hear a distant clank, as the automaton tries and fails to lift an abandoned horseshoe. It returns emptyhanded, save a piece of lint caught on its ear.')
			elif destination() == 'Town - Inner Ring':
				io.say('It returns with a long blue ribbon around its foreleg. It looks like a discarded prop from some kind of play or celebration. You gather up the ribbon; maybe it will come in handy.')
				addItem('Ribbon')
				useOnce = True
			elif destination() == 'Town - General Store':
				io.say('It hops toward a very dangerous-looking stenograph, but Maria catches it and returns it to you. "Lucas gave you this?" she asked. "Sure brings back memories...I never did find out how it works. Take care of the little guy, alright?"')
			elif destination() == 'Town - The Inn':
				io.say('It runs around the inn for a while, then returns and hops impatiently around your feet. It seems restless to travel.')
			elif destination() == 'Canyon - L1':
				io.say('It proudly returns with 200 G, which it found stuck on a nearby cable.')
				changeGold(200)
				useOnce = True
			elif destination() == 'Garden - Entrance':
				io.say('It pops out of a nearby fern, carrying a little cluster of green berries.')
				addReagent('Green Berry',5)
				useOnce = True
			elif destination() == 'River - Northern Bank':
				io.say('It slips down the riverbank to an old mesh of stone and planks, left from a failed construction project. It recovers a fallen but watertight jar of oil, and returns it to you.')
				addReagent('Oil',40)
				useOnce = True
			elif destination() == 'The Off Road':
				io.say('It can\'t find anything nearby, but it seems intrigued by the off road.')
			elif destination() == 'Shrine - Vestibule':
				io.say('It searches all around the basin for fallen treasures. A few fresh berries are still lying in the grass.')
				addReagent('Orange Berry',4)
				addReagent('Green Berry',7)
				addReagent('Purple Berry',11)
				useOnce = True
			elif destination() == 'Before the Clocktower':
				io.say('It doesn\'t seem to find anything, and is reticent to go any closer to the tower.')
			elif destination() == '???':
				io.say('It sits near the entrance, transfixed by the height of the tower. You wait for it to move, but it\'s as still as can be--you give up and return the automaton to your pocket.')
			elif destination() == 'Tower - L1':
				io.say('It takes off toward the rightmost door, more determined than you\'ve ever seen it. Unfortunately, all it wanted was a shred of rotten lettuce abandoned beneath a dining room table. You want to be annoyed, but you appreciate the moment of levity...right?')
				useOnce = True
			elif destination() == 'Tower - L2':
				io.say('It surveys the room, giving the fountain a wide berth. Just before it seems to have given up, it finds a crumpled piece of paper stuck beneath the leg of the desk. You carefully retrieve the page.')
				addItem('Crumpled Page')
				useOnce = True
			elif destination() == 'Tower - L3':
				io.say('It carefully looks around, but despite the many items strewn across the room, it can\'t seem to find anything useful.')
			elif destination() == 'Tower - L4':
				io.say('It tries to search for items, but its head darts left and right, and it shivers until you recover it. The automaton seems terribly distracted by the nearby gremlins.')
			elif destination() == 'Tower - L5':
				if player.seen('Tower - L6'):
					io.say('But with the engine fixed, it can\'t think of anything else to do.')
				else:
					io.say('The automaton finds a couple of wires connected to nothing, and drags them to the other side of the engine. The rotor begins to shiver, and seems to untangle from the engine, but the automaton is keeping the wires in place with all its might. If it returns to you, the elevator will fail again.')
					io.option(player,'Call the automaton back.')
					io.option(player,'Say goodbye.')
					c = io.get(player,False)
					if c == 1:
						io.say('The automaton returns to you, and the engine crashes into the elevator, trapping you on this floor once again.')
					else:
						loseItem('Automaton')
						io.say('You step onto the elevator and set it to the next floor. As you clear the broken engine and begin to ascend, the automaton scurries to the edge of the rotor, and waves goodbye with one ear.')
						player.setDestination('Tower - L6')
			elif destination() == 'Tower - L6':
				if player.seen('Tower - L7'):
					io.say('But with the furnace working properly, it isn\'t sure how else to help.')
				elif player.seen('Furnace'):
					io.say('You set the automaton in front of the control panel; it will have better luck finding the switches. Which one do you want to toggle?')
					switch = raw_input()
					io.clear()
					if ['INVALID' for c in switch if c not in ['0','1','2','3']] == []:
						upSwitches = 0
						downSwitches = 0
						for s in furnaceSwitches().keys():
							if ['INVALID' for i in ['0','1','2','3'] if switch.count(i) > s.count(i)] == []:
								if furnaceSwitches()[s]:
									self.furnaceSwitches[s] = False
									print (' Deactivated switch #' + s)
									downSwitches += 1
								else:
									self.furnaceSwitches[s] = True
									print ('   Activated switch #' + s)
									upSwitches += 1
						print('')
						io.say(str(upSwitches) + ' switches turn on,')
						io.say('and ' + str(downSwitches) + ' turn off.')
						if ['OFF' for i in furnaceSwitches().values() if not i] == []:
							io.say('There\'s a sudden rumble and a puff of smoke, and the furnace is lit! The whole room glows and the chilling air disperses. As you look around the newly illuminated walls, your attention is drawn to a little green light beneath the elevator controls. You can reach the next floor.')
							player.remember('Tower - L7')
						else:
							io.say('The furnace remains silent.')
					else:
						io.say('The automaton can\'t find a switch with that name.')
				else:
					io.say('It isn\'t sure what to do just yet, but it seems intrigued by the furnace.')
			elif destination() == 'Tower - L7':
				io.say('It circles you a few times, then it stops and won\'t move. The automaton seems no better at navigating the darkness than you are.')
			elif destination() == 'Tower - Catalogues':
				player.wait(15)
				io.say('The automaton doesn\'t seem to return. Worriedly, you wander through the hallways in search of your lost friend. Eventually you find a mousehole on the door of room 12; you knock and the automaton returns.')
			elif destination() == 'The End':
				io.say('It immediately runs to the magician. "--Hello!" the magician says. "I was wondering where you\'d gone..."')
				io.say('After the reunion, the automaton returns to you. The magician guesses your first question: "Yes, I built this automaton a while back. You can keep it if you want; it seems happy to travel beside you."')
			else:
				io.say('You wait a couple minutes, and soon enough it returns. Whatever it was trying to find, its search turns up empty.')
	elif item == 'Mirror':
		io.say('You hold up the mirror of time and look around, slowly scrolling through history.')
		player.wait(3)
		if hasUsed('Mirror',destination()):
			io.say('But you don\'t discover anything else.')
		else:
			if destination() == 'Copse':
				io.say('As you change the time, you watch in awe as leaves fly upward and saplings sink toward the ground. Despite this, you don\'t learn much about your objective.')
			elif destination() == 'Crossroads':
				io.say('You look ten, twenty, thirty days back, watching people rush backward and moss retreat from the road. Eventually something catches your eye: a few pieces of gold fall from a traveler\'s pocket, sinking into the ground during a following rainstorm. You go to that spot and dig, unearthing 400 G from the ground!')
				changeGold(400)
				useOnce = True
			elif destination() == 'Town - Outer Gate':
				io.say('Nothing much seems to change over time, except for the cracks crawling along the town wall, and the rust creeping over the gate.')
			elif destination() == 'Town - Outer Ring':
				io.say('"What\'s your problem?" a tall man said eight days ago. The mirror can\'t indicate sound, but his frustrated demeanor is easy to read.')
				io.say('He seems to be a freelance announcer, speaking to a group of about twenty people on the side of the road. A few of them are nodding, but most are disappointed at best. The announcer doesn\'t seem to understand their outrage.')
				io.say('Behind the announcer, a sign reads: "Festival Tonight! Commemorating our defeat of the magician which threatened our town..."')
				io.say('You scroll the mirror forward. There was no festival that night.')
			elif destination() == 'Town - Pheme\'s Shop':
				io.say('Not much has changed in this building; a few new decorations added, a repaint...apparently Pheme used to favor glasses with heptagonal lenses. Stacks of papers change rapidly in height.')
				io.say('Pheme notices the frame of the mirror. "You know, I think I\'ve seen that mirror before. Is it the time one?" Pheme is surprisingly nonchalant about the concept. "Do you mind if I borrow that for a few minutes? I misplaced a paper about 40 minutes ago..."')
				player.wait(3)
				io.say('After recovering the lost document, Pheme returns the mirror. "Where did you find this, by the way? It\'s incredibly helpful if you know when to look."')
				useOnce = True
			elif destination() == 'Town - The Stables':
				io.say('The dirt and straw on the ground moves about constantly. Ronald wanders all around the stables, doing most of the work himself.')
				io.say('But you don\'t find anything else.')
			elif destination() == 'Town - Inner Ring':
				io.say('Not much seems to happen around this town, but as you scroll back to the 3-month mark, you seem to catch the aftermath of some strange event.')
				io.say('Everyone appears to be alright, but random damage is scattered throughout the buildings and roads. A lost horse runs alone down the empty road. Only a few people are around, repairing houses and streets.')
				io.say('You notice a mysterious figure near a broken lamppost. It\'s short, but extremely strong, as it slowly lifts the metal post, apparently trying to fix it. But the lamppost slips and falls, and the mysterious figure flies away in a panic.')
				if player.verbose():
					io.say('Before you can ask, Tock quickly explains.')
					io.say('[there was a really bad storm; i was there trying to clean up. i couldn\'t do much, though.]')
				else:
					io.say('You rewind again and draw a bit closer, but you can\'t seem to identify the mystery character. At first it seemed to be wrapped in a blanket, but no, the stitched cloth seems to move on its own...maybe the mirror is glitchy?')
			elif destination() == 'Town - General Store':
				io.say('"Oh--they gave you that mirror??" Maria asks, her voice doubling in volume. "Have you figured out how it works yet? It\'s amazing, I know...but it comes with a terrible curse: the more you use it, the less practiced you become in taking careful records."')
				io.say('She notes your expression. "No, there is no literal curse. It was a joke, alright?"')
				useOnce = True
			elif destination() == 'Town - The Inn':
				io.say('You see Lucas visiting the inn each morning, and a remodeling which occurred three weeks ago, but it seems like few others visit the inn.')
			elif destination() == 'Canyon - L1':
				io.say('The scaffolding throughout the canyon folds up and vanishes as you scroll back in time. As you examine the history of the site, you notice a counterweight fallen from a pile of supplies and marked off the inventory. You find the place where it fell; the weight could come in handy.')
				addItem('Weight')
				useOnce = True
			elif destination() == 'Garden - Entrance':
				io.say('You revisit the history of these trees and bushes, watching them sway along with time. You find nothing to help you progress, but you could watch the motion of this garden for a long time.')
			elif destination() == 'River - Northern Bank':
				io.say('After scrutinizing the river current, forward and backward, you discover a few coins drifting through the water. You chase them from past to present, finding their resting place in an emerald green thicket. You count up 210 G in total!')
				changeGold(210)
				useOnce = True
			elif destination() == 'The Off Road':
				io.say('A few weeks ago, the road into the woods was far more visible than it is now. There were a couple of lanterns to mark the way, which have since disappeared among the brush. You locate one of the lanterns, finding a shallow pool of lamp oil inside. It appears to still be usable.')
				addReagent('Oil',15)
				useOnce = True
			elif destination() == 'Shrine - Vestibule':
				io.say('It looks like this shrine has seen better days. Even just a couple months ago, the ivy and grass were far more tame, and the statue wasn\'t so burdened by moss and grime. It seemed happier than usual, but equally unwilling to give advice.')
			elif destination() == 'Before the Clocktower':
				io.say('The clocktower has run perfectly for as long as the mirror can recall, but no one seems to enter or leave.')
			elif destination() == '???':
				io.say('You search for any sign of maintenance or tourism of the massive tower, but it seems abandoned. Not even animals draw close.')
			elif destination() == 'Tower - L1':
				io.say('Dust swirls, but nothing else changes.')
			elif destination() == 'Tower - L2':
				io.say('Another lifeless floor. The fountain seems to require no maintenance, running for as long as the mirror can tell.')
			elif destination() == 'Tower - L3':
				io.say('This floor seems completely unvisited; you can\'t find any moment when the door opens. Whatever happened to this room, it happened a long time ago.')
			elif destination() == 'Tower - L4':
				if player.seen('Gremlin Trick'):
					io.say('You turn the mirror toward the kennels. They were constructed a few months ago, seemingly to contain the gremlins before they reached the upper floors of the tower. You see a mysterious figure enter the room, and begin drawing labels for each kennel. You see the gremlins use the same trick you observed before. Scrolling back just a bit more, you see...aha! The correct permutation!')
					io.say('But your victory is punctuated by a stomach-turning shriek. One of the gremlins noticed you using the mirror, and apparently interpreted it as cheating. Before you can react, it steals the mirror and shatters it.')
					io.say('Oh, well, at least you remember the solution...')
					loseItem('Mirror')
					io.option(player,'Place the gremlins in the correct kennels.')
					io.get(player,False)
					player.wait(52)
					io.say('It takes much longer to catch them this time; they don\'t seem to be dropping their grudge anytime soon. As soon as you get the ninth gremlin to the kennel, the door to the next floor opens, and you make a run for the stairs before it can close again.')
					io.option(player,'Climb the stairs.')
					io.get(player,False)
					player.setDestination('Tower - L5')
				else:
					io.say('But you soon decide not to use the mirror until you\'re sure you need it. This floor doesn\'t mix well with fragile glass.')
			elif destination() == 'Tower - L5':
				io.say('A-ha...looks like there\'s a part missing from the engine. A blue gremlin destroyed it a long time ago. You pause at the half-second before the missing machine is tossed from the elevator, and make out the words "JUYED AWK YACC."')
				io.say('You continue using the mirror, examining the spin of the engine. You notice that, when turned completely around, it reveals a note taped to the side. You reach behind the real engine and retrieve the page.')
				addItem('Engine Parts List')
				useOnce = True
			elif destination() == 'Tower - L6':
				io.say('A mysterious figure sometimes passes by to check the furnace, though you\'re not sure how it got here: The elevator stays motionless, and the furnace stays cold. Is the figure still here? Is it still on this floor? You gasp and look behind you.')
				io.say('Nobody here...')
			elif destination() == 'Tower - L7':
				io.say('You\'re not sure what you expected...this room hasn\'t been visible in months.')
			elif destination() == 'Tower - Catalogues':
				io.say('Strange characters wander the halls, but there is no sign of a human visitor.')
			elif destination() == 'The End':
				io.say('"You have the Mirror, too?" the magician asks you. "A great reward for your journey; it\'s fascinating to watch how the world changes. I guess I don\'t need it anymore...I watched the old-fashioned way.')
			else:
				io.say('But not much seems to change.')
	elif item == 'Compass':
		io.say('You hold the compass level and observe it.')
		player.wait(1)
		if hasUsed('Compass',destination()):
			io.say('But it doesn\'t reveal anything else.')
		else:
			if destination() == 'Crossroads':
				io.say('Sure enough, the needle points along the road to the garden.')
			elif destination() == 'Town - Outer Ring':
				io.say('You can infer where to find the town gate, but it reveals nothing else.')
			elif destination() == 'Town - General Store':
				io.say('Of course the needle points to the far--wait, that\'s not the north wall. There must be a set of magnets in that direction.')
			elif destination() == 'Before the Clocktower':
				io.say('The needle spins wildly. You suspect it\'s trying to intimidate you, but only as much as a tiny compass can muster.')
			elif destination() == '???':
				io.say('The needle points toward the vast quantities of nothing to the north. Away from it, there\'s just as much nothing to the south.')
			elif destination() == 'Tower - L3':
				io.say('The compass is about the same size as the keyhole.')
				io.option(player,'Unlock the door.')
				io.option(player,'Not yet...')
				c = io.get(player,False)
				if c == 1:
					io.say('You place the compass and give a quarter turn clockwise. It locks into place, and the door opens with a grumble.')
					io.say('Unfortunately, the compass is now locked in place...you won\'t be able to carry it any longer.')
					loseItem('Compass')
					player.remember('Tower - L4')
				elif c == 2:
					io.say('...okay?')
			elif destination() == 'Tower - L4':
				io.say('But the compass doesn\'t point north. You follow it to a little magnetized box, buried under a pile of sketchbooks, tableware, and empty picture frames. You find a few pencils and pens inside the box, as well as a torn piece of paper. You take the paper--maybe someone has tried to solve this puzzle before you?')
				addItem('Torn Page')
				useOnce = True
			elif destination() == 'Tower - L7':
				io.say('But you can\'t see how it reads.')
			elif destination() == 'The End':
				io.say('"I suppose you\'re wondering what\'s so special about that compass," the magician says. "Well, it doesn\'t have any special powers, but it\'s incredibly accurate--most compasses I\'ve seen are very unreliable.')
				io.say('"...I know, it sounded more exciting in my head."')
			else:
				io.say('The compass points north, but it isn\'t particularly useful.')
	elif item == 'Torch':
		if destination() in ['Copse','Town - Pheme\'s Shop','Town - The Inn','Garden - Entrance','Shrine - Vestibule','Tower - Catalogues']:
			io.say('That seems too dangerous to use here.')
		else:
			io.say('The torch shines with pale orange light.')
			if hasUsed('Torch',destination()):
				io.say('But it doesn\'t illuminate anything else.')
			else:
				if destination() == 'Crossroads' and player.is_night():
					io.say('You can read the signpost a bit easier now, but nothing more is revealed.')
				elif destination() == 'Town - Outer Gate' and player.is_night():
					io.say('As you move the torch along the wall, shadows spell out a couple lines of graffiti; they must have been carved into the stone a long time ago.')
					print('  " DON\'T COME BACK\n')
					print('    WE\'LL BE READY! "\n\n')
					io.say('It looks like there used to be paint here, but it was erased promptly.')
				elif destination() in ['Town - Outer Ring','Town - Inner Ring'] and player.is_night():
					io.say('It\'s a bit easier to see now, but the building signs are already revealed by hanging lanterns.')
				elif destination() == 'River - Northern Bank' and player.is_night():
					player.wait(2)
					io.say('While wandering the outside of the cabin, you notice a gleam between two planks. It\'s a tiny blue glow, which you could never have spotted in the daylight--apparently no one else did either.')
					io.say('You remove a little silver necklace, with a hexagonal greenish sapphire inside. Someone must have stashed the necklace here a long time ago--it seems to have been forgotten years ago. You take the necklace in hopes of returning it someday.')
					addItem('Necklace')
					useOnce = True
				elif destination() == 'The Off Road':
					io.say('You can see a bit farther into the woods, but you dare not move the torch any closer to the brush.')
				elif destination() == '???':
					io.say('You raise the torch for light, warmth, and if necessary, defense.')
				elif destination() == 'Tower - L1':
					io.say('You illuminate the walls to find lots of little drawings, but you can\'t identify any of the crude stick figures. It looks like a new drawing hasn\'t been added in a long time.')
				elif destination() == 'Tower - L6':
					if not player.seen('Tower - L7'):
						io.option(player,'Drop it into the furnace chute.')
						io.option(player,'Wait...')
						c = io.get(player,False)
						if c == 1:
							io.say('You drop the torch into the furnace chute. Sure enough, it lights the furnace and doesn\'t go out; a soft light envelops the room, and the elevator gears slowly build up speed. You can\'t reach the torch anymore, but you can advance to the next floor; you get the feeling your journey is almost over.')
							loseItem('Torch')
							player.remember('Tower - L7')
						elif c == 2:
							io.say('Okay...what else?')
					else:
						io.say('But with the furnace lit, you can\'t think of another use.')
				elif destination() == 'Tower - L7':
					io.say('You move along the wall and use the torch to reveal a rough tesselation of cobblestones. Eventually, the torch reveals the outline of a second door, with no label or lighting to mark it. You find a handle behind a loose cobblestone--the door can be opened.')
					player.remember('Catalogues')
					useOnce = True
				elif destination() == 'The End':
					io.say('"So that\'s how you got the furnace working--clever," the magician notes. "I hope you used the torch safely."')
				else:
					io.say('But nothing happens.')
	elif item == 'Idol':
		io.say('You call for the idol\'s help.')
		player.wait(1)
		if destination() == 'Crossroads':
			io.say('It lumbers over to the lake and returns with some greenish water. The data read:')
			readIdol(300.70,1.00,1.03)
		elif destination() == 'Town - The Stables':
			io.say('Unsure of what to do, it gathers data from a nearby trough.')
			readIdol(298.62,1.00,1.44)
			io.say('If the idol\'s left brow could move...')
		elif destination() == 'Canyon - L1':
			io.say('It wanders the site, staying far away from any ledge. Unsure of what else to do, it scoops up some sand and gravel and shakes it until level. The data read:')
			readIdol(306.22,1.00,1.92)
		elif destination() == 'River - Northern Bank':
			io.say('It heads down to the river bank and scoops up the water. The data read:')
			readIdol(293.88,1.00,1.02)
		elif destination() == 'The Off Road':
			io.say('But when you think it might be looking toward the old shrine, it seems to be concentrating in the direction of the tower. You feel like you\'ll need its help to get there, but for now it silently waits around.')
		elif destination() == 'Shrine - Vestibule':
			io.say('The gargoyle seems massive when compared to the little idol, which approaches it without fear. Although their stone eyes do not change, you imagine them in deep conversation.')
		elif destination() == 'Before the Clocktower':
			if haveAllTreasures():
				io.say('A genuine look crosses its unmoving face. It seems just as surprised that the tower is within your reach.')
			else:
				io.say('It approaches the tower and waits for you to do the same, but you still can\'t move forward. The idol thinks for a minute; it seems frustrated on your behalf. It looks like you\'ll need some more help to reach the tower.')
		elif destination() == '???':
			io.say('It expresses its support, but there\'s nothing it can do right now.')
		elif destination() == 'Tower - L1':
			io.say('It stays in place and stares forward--it seems lost in thought.')
		elif destination() == 'Tower - L2':
			io.say('It doesn\'t appear to be paying attention.')
		elif destination() == 'Tower - L3':
			io.say('It sits in demo mode. There\'s no puzzle to be solved on this floor--yet.')
		elif destination() == 'Tower - L4':
			io.say('But it doesn\'t move; its willpower is spent on grumpily tolerating the gremlins.')
		elif destination() == 'Tower - L5':
			io.say('The idol, in turn, points at the automaton. You suppose this isn\'t its area of expertise.')
		elif destination() == 'Tower - L6':
			io.say('It has no help or advice, but it seems to trust you, sitting calmly by the furnace. It knows your climb up the tower is almost done.')
		elif destination() == 'Tower - L7':
			io.say('But you don\'t know where the idol is right now. It\'s as silent as ever, and you can\'t tell if it\'s right in front of you or far, far away.')
		elif destination() == 'Tower - Catalogues':
			io.say('It innocently ignores you, as it\'s busy wandering the halls.')
		elif destination() == 'The End':
			io.say('"You\'re here too?" the magician asks the idol. Oh, good, you\'re not crazy--the idol really is alive.')
			io.say('"Ah, of course..." the magician says, "the door to the third level. But I thought the door only allowed one visitor?"')
		else:
			io.say('But it isn\'t sure what to do.')
	elif item == 'Sleeping Bag':
		if destination() == 'Copse':
			io.say('You set up the sleeping bag beside the familiar stump.')
			sleep()
		elif destination() == 'Crossroads':
			io.say('You find a dry patch of grass near the lake and decide to take a rest.')
			sleep()
		elif destination() == 'Town - The Inn':
			io.say('That would be ironic. Well, technically it\'s coincidental. Neither, actually. There is no excuse for this decision.')
			sleep()
		elif destination() == 'Canyon - L1':
			io.say('You find a pile of mats, blankets, and tarps, under a large roof of gray cloth over the south end of the canyon. Apparently some of the workers prefer to spend the night instead of making the trek back to town. You decide to do the same.')
			sleep()
		elif destination() == 'Garden - Entrance':
			io.say('You don\'t think you\'ll be allowed to sleep in a public garden.')
		elif destination() == 'River - Northern Bank':
			io.say('You bed down by the riverbank, just close enough to hear the water.')
			sleep()
		elif destination() == 'The Off Road':
			io.say('You find a little hill by the road, and set up the sleeping bag on the other side.')
			sleep()
		elif destination() == 'Shrine - Vestibule':
			io.say('There\'s an empty field near the far end of the shrine, where you decide to rest a while.')
			sleep()
		elif destination() == '???':
			io.say('Not now.')
		else:
			io.say('You have no use for a sleeping bag here.')
	elif item == 'Ribbon':
		if destination() == 'Tower - L2':
			io.say('You compare the perimeters of the ceramic bottles. The perimeter of the flower-shaped bottle is twice the perimeter of the circular bottle. The flower and the star have the same perimeter.')
		else:
			io.say('You\'re not sure how a ribbon will help here.')
	elif item == 'Weight':
		if player.has('Idol'):
			io.say('The idol identifies it as 1 kilogram exactly, but you\'re not sure how to use this.')
	elif item == 'Loaf of Bread':
		if destination() == 'Tower - L4':
			loseItem('Loaf of Bread')
			io.say('The instant you hold out the bread, an indigo gremlin apparates and steals it away.')
			io.say('After a while, the gremlin approaches you again, apparently trying to communicate. After failing to form words, it frustratedly moves you to the other side of the room, and points toward the centermost kennel. So that\'s what it was trying to tell you: one gift, one hint to the puzzle.')
		else:
			io.say('It looks a little...off. You\'re not sure what to do with it.')
	elif item == 'Crumpled Page':
		io.say('The page reads:')
		print(' Remember to check on')
		print('       Room 17\n')
	elif item == 'Torn Page':
		io.say('The notes are a little messy, but you read them as well as you can:')
		print(' Transmogrify spell:')
		print('    Blue  ---> Indigo')
		print('     A            |     !!!GREMLINS COPIED')
		print('     |            |         THE SPELL!!!')
		print('     |            V')
		print('   Purple <---  Pink')
		print(' - Seem to use spell on adjacent gremlins')
		print(' - Blue gremlins cast 1 transmogrification')
		print(' - Indigo gremlins cast 2')
		print(' - Pink 3')
		print(' - Purple 4')
		print('                  3 1 2    1 1 3')
		print('                  1 3 4 -> 1 1 4')
		print('                  2 4 3    3 4 3')
		print('')
		print(' 3 + 1 + 1 = 1     3 + 1 + 2 + 3 = 1')
		print('          1 + 2 + 4 = 3')
		io.say('Most of the other notes are crossed out or destroyed.')
	elif item == 'Engine Parts List':
		print(' The list is very poorly explained, but you decipher what you can:')
		print('         Machine | Returns')
		print(' ----------------+-------------')
		print('            TRUE | X')
		print('           FALSE | Y')
		print('           THARR | TRUE')
		print('       VELOX NEB | FALSE')
		print(' VENZAR BORGAVVE | X and Y')
		print('    HACKEM MUCHE | X or Y')
		print('       ELAM EBOW | X nand Y')
		print('      GARVEN DEH | X nor Y')
		print('  ANDOVA BEGARIN | not X')
		print('  VERR YED HORRE | not Y')
		print('  JUYED AWK YACC | X xor Y (*missing)')
		print('   DAIYEN FOOELS | X if Y')
		print(' LEP GEX VEN ZEA | Y if X')
		print('       ZELGO MER | not "X if Y"')
		print('           TEMOV | not "Y if X"')
		print('   FOOBIE BLETCH | X iff Y')
	else:
		io.say('You\'re not sure how to use that.')
	if not hasUsed(item,destination()) and useOnce:
		self.itemUses += [(item,destination())]