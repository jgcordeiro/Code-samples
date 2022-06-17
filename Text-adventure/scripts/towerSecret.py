import randomizer, params, io, data
import math, random

def go(player):
	io.say('You open the door to find the other side surprisingly well-lit. These last few floors have tested your suspension of disbelief, but to believe this would be insanity--you could walk ten times the width of the tower before reaching the opposite wall.')
	io.say('It\'s some sort of...hotel? Apartment building? Ballroom? The beautiful tiled floor weaves around blocks of numbered doors, some leading to rooms, others to storage closets and cabinets. Miniature chandeliers light every corner.')
	i = player.getChecks('Catalogues')
	if i < 5:
		io.say('Nobody seems to be around.')
	elif i < 10:
		io.say('Is it--no, the spider is still there.')
	elif i < 15:
		io.say('A small octopus floats in circles near the door.')
	elif i < 20:
		io.say('There\'s also an acid-blue spherical dragon, but at this point you\'re not even surprised.')
	elif i < 24:
		io.say('You jump a bit when you notice the behemoth sniffing around just beside the door.')
	else:
		io.say('Everyone\'s still here!')
	while True:
		io.say('What now?')
		io.option(player,'Try a door.')
		io.option(player,'Leave.')
		c = io.get(player)
		if c == 1:
			io.say('Which one? Enter an integer.')
			i = getInt(24)
			if i < 1:
				io.say('You can\'t find a label with that number.')
			elif i < 24:
				io.say('You find a label with that number:')
				io.hline()
				if i == 1:
					io.say('"Infinite Money"')
					io.say('A perfect way to make my introduction. I created 1,000,000 kilograms of money, so no one will go poor again.')
					io.say('RECALLED: All the money, even the money I didn\'t create, was considered worthless. The town was forced to make a difficult transition to another form of currency. The pile of coins collapsed under its own weight, and took weeks to clean up.')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('Inside the cabinet is a set of shelves, displaying various silver coins. Many of them are warped or crushed.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 2:
					io.say('"Wings"')
					io.say('Winged suits which allow flight to anyone!!')
					io.say('RECALLED: They don\'t melt in the sun or anything. Turns out they\'re just very, very, very dangerous...')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('Dozens of false folded wings are hung up in a row. Their span is too wide to open indoors.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 3:
					io.say('"Infinite Energy"')
					io.say('I created a torch which, when active, never goes out. It produces an unlimited quantity of light and heat.')
					io.say('I knew it would be useful, but I never realized it would be this...game changing. Apparently people are working on ever more efficient ways to harness its energy. But eventually it was hidden away in some locker; it\'s very dangerous in the wrong hands, and I\'ve created plenty of those.')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('This cabinet is empty, though one of the edges is charred.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 4:
					io.say('"Spell Checker"')
					io.say('A little idea I had for helping out around town. It notices and remarks on any error in spelling and grammar nearby. I felt like this was the best way to support the town paper.')
					io.say('RECALLED: It\'s a little too good at its job.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('The room looks like a giant birdcage. A giant parrot sits in the back corner, buried in fluffy feathers.')
						io.say('It looks menacing, but it doesn\'t seem dangerous. It\'s only a language expert, after all. You\'re not sure how it can be "too good at its job;" it\'s not like their can be a--')
						io.say('"*THERE!!!"')
						io.option(player,'Oww...')
						io.get(player,False)
				elif i == 5:
					io.say('"Infinite Food"')
					io.say('I placed a large but physically reasonable amount of food by every house in the country. No way that could go wrong, right?')
					io.say('It didn\'t go well...the scramble to claim these resources was only the start. A lot of people got sick from food that was left outside. Most of it went uneaten, and started to rot. I\'m going to avoid making "Infinite Whatevers" for a while.')
					io.option(player,'Open this pantry.')
					io.option(player,'Avoid this pantry.')
					c = io.get(player,False)
					if c == 1:
						io.say('You open the pantry to find--')
						io.say('--nope. Nope, nope, nope. You don\'t open the pantry. Goodbye.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 6:
					io.say('"Carousel"')
					io.say('So, how\'s this for clever? I noticed the large circular paths around town, and I turned them into--you guessed it--a carousel! Just step on and it will take you where you need to go in seconds!')
					io.say('RECALLED: Okay, I understand the carousel might have moved a little fast. What I don\'t understand is why people kept flying sideways off the road. Someone named Maria was warning people about something called "centripetal force;" maybe that has something to do with it?')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('Behind this door is a little storage room, holding many lifesize marble horses. Whoever invented the "carousel" motif wasn\'t kidding around.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 7:
					io.say('"Palace"')
					io.say('There\'s nothing in the center of town but a little field...yet! It seems like the perfect place for the most beautiful palace you\'ve ever seen. Look, I\'ll be first to admit my practical gifts haven\'t worked out so well, so why don\'t I take an artistic direction?')
					io.say('RECALLED: I didn\'t realize how terrible the upkeep costs would be. The palace is causing much more stress than joy.')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('All that\'s inside are a few chips of plaster and shards of plywood. Apparently the dismantling of the palace went wrong somehow.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 8:
					io.say('"Pet"')
					io.say('I\'ve noticed that a lot of people enjoy the company of animals, so I invented the optimal pet. Friendly, able, intelligent, impossible to harm; perfect in every quality.')
					io.say('RECALLED: Sure, it can be expensive to maintain, and sometimes it doesn\'t know its own strength, but I didn\'t expect the response to be so sharply negative. I forget how fragile civil infrastructure can be; people assumed my creation was some sort of advancing threat. I guess my past work precedes me, huh?')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						if player.getChecks('Catalogues') < 20:
							io.say('In a nice little playroom depicting an orchard and a serene pond, you happen upon a startling behemoth. It\'s about your height, but it has an imposing build: six legs, four eyes, wings, horns, a monster of a brain, and more, like a mash-up of every quality the artist could think up. The behemoth hops playfully forward, shaking the ground and splintering the ceiling.')
							io.option(player,'Run.')
							io.option(player,'Stay.')
							c = io.get(player,False)
							if c == 1:
								io.say('As the behemoth gains a frightening amount of momentum, you run for the door and slam it shut behind you. There\'s a collision on the other side which launches you to the opposite wall, but nothing else--you can barely hear its footsteps as it walks away.')
							else:
								io.say('Aww, look, it just wants to be friends...with anyone who can dodge, apparently. Fortunately, it calms down before causing too much danger.')
						else:
							io.say('Well, there isn\'t much of a door left to open, as it\'s mostly been reduced to a pile of splinters. Behind the door is a bunch of artificial scenery, a food bowl, and a weird smell, but nothing else of note.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 9:
					io.say('"Improved Currency"')
					io.say('Under disguise, I swallowed my pride and requested public input. I asked people what they consider a perfect form of currency. Hopefully the solution will fix that "infinite money" debacle.')
					io.say('Distribution was tricky, but the new system actually works really well! I wish I could collaborate more, but people have started seeing through my disguise. I\'ll have to wait until the climate dies down.')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('You find a pile of polls, sketches, and notes. You recognize the later drawings: they resemble the town\'s odd units of money.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 10:
					io.say('"Crane"')
					io.say('I have an idea for getting rid of that palace. This crane is miles high; it will pluck the palace right off the ground, and safely carry it away. Who knows how else it can be of use?')
					io.say('RECALLED: Before it even attached to the palace, the crane toppled over. The instant it toched the ground, it collapsed under its own weight. Thank goodness I constructed it outside the town.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('The crane lies disassembled in a large storage room. You count 11,000 girders, 1 right-angle piece, and 1 giant cable. Each is too heavy to lift.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 11:
					io.say('"Aquarium"')
					io.say('I tried something a little simpler this time. They swim through air as if it were water, so people can see the ocean anytime, anywhere!')
					io.say('RECALLED: Not the best idea for a busy town. Most of them disappeared into the sky. Those which didn\'t bumped into windows, disrupted walkers, and left a mess everywhere.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('This door falls open at the slightest touch. The room inside has rocky walls, a delicate skylight, and a floor of metal grating.')
						if player.getChecks('Catalogues') < 10:
							io.say('Hundreds upon hundreds of fish swirl around the room, alongside dozens of crustaceans and a few hammerhead sharks. You look at your hands--you\'re definitely not underwater...')
						else:
							io.say('A small school of fish floats around here, at eye level with you. Strange...')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 12:
					io.say('"Automata"')
					io.say('Due to my past mistakes, many valuables have been lost. These mechanical rabbits have an exceptional talent for finding things. Hopefully they can clean up some of the damage.')
					io.say('RECALLED: They don\'t understand the difference between recovery and pickpocketing. Don\'t worry about the one that\'s missing--a man in town kindly decided to look after it.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('Opening the door reveals a droning, rattling murmur. Little cages are stacked floor to ceiling. Hundreds of machines, just like your automaton, are kept here. One cage is empty, aligned with a mousehole at the base of the door.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 13:
					io.say('"Gremlin"')
					io.say('Before I consider granting my powers to another human, I created a sort of test subject: a creature the size of a thumbtack which shares my abilities. It was created never to harm others, but I\'m not sure how it will act beyond that.')
					io.say('RECALLED: Never again. Within forty-six minutes, the gremlin discovered or invented a plethora of catastrophic powers: replication, invulnerability, flight, extreme longevity, evolution (I don\'t know if I\'m using the term "evolution" right, considering I didn\'t the past hundred times,) etc. Although it could destroy the planet in a thousand different ways, it\'s busy fighting with its new clones...I need to find a way to control them before they do something too insane.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('It looks like this used to be a nice bedroom. One problem: the floor has been completely destroyed, and the crater leads farther down than you can see. It\'s sealed by steel bars, but they aren\'t fixed very carefully; whoever installed them already knew they wouldn\'t work.')
						io.option(player,'"Hello?"')
						io.option(player,'Keep your voice down.')
						c = io.get(player,False)
						if c == 1:
							io.say('Apparently no one has been here in a while, because excitable chaos and cacaphony erupts from three floors down. With a sudden crash, a pink gremlin appears on the other side of the bars, bestows a high five, and disappears. Apparently you\'re friends now.')
						elif c == 2:
							io.say('You keep quiet. It seems to be working.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 14:
					io.say('"Jabberwock"')
					io.say('There was a young man who felt unappreciated, like nobody cared about his accomplishments. I created the jabberwock in such a way that only he could defeat it, so he would be revered as a hero.')
					io.say('RECALLED: He ran away the moment he saw the jabberwock. It charged through sixteen houses and a lamppost before the townsfolk put a stop to it.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('There\'s a bed as wide as a swimming pool, a tree made of lumber and cloth, and a squeaky toy as tall as yourself. The room looks like it was made for a monumental cat.')
						io.say('No one is here.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 15:
					io.say('"Magic Marker"')
					io.say('Unoriginal, I know, but the "anything you draw comes to life" gimmick is tried and true--and I don\'t have to keep thinking of ideas myself.')
					io.say('I was pretty excited at the feedback; someone said they found a "weapon" to defeat some kind of "monster." It sure was a laugh when I discovered whom they meant.')
					io.say('RECALLED: I would still have been happy if it actually worked. Turns out a crude two-dimensional image isn\'t enough information for a machine in three dimensions.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('The doorknob is disconnected, but you can simply push the door open.')
						if player.getChecks('Catalogues') < 15:
							io.say('You\'re greeted by a neon-green kangaroo who seems to believe that its legs are arms and its ears are legs. Elsewhere, hundreds of equally strange characters loaf about. Composed of unnatural shapes and bright hues, you\'re not even sure if they\'re real or not. At least they seem harmless enough.')
							io.option(player,'Talk to them.')
							io.option(player,'Leave.')
							c = io.get(player,False)
							if c == 1:
								io.say('Besides footsteps and occasional loss of balance, they are completely silent.')
						else:
							io.say('The room is mostly empty, except for a few...well...you\'re not sure if they match any single noun. The "magic marker" lies discarded on the floor; it seems to be broken.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 16:
					io.say('"Architects"')
					io.say('The townsfolk need more materials to repair their buildings, so I created a team of 40 architects to help them along. Seven feet tall and exceptionally strong, each one is incredible at making structures which are built to last.')
					io.say('RECALLED: Why do people have such a problem with arachnids?')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('The door is slightly open already, but it\'s very difficult to move. The room on the other side is weighed down by a canopy of webs.')
						if player.getChecks('Catalogues') < 5:
							io.say('It\'s a very lively place. You count at least three hundred legs.')
							io.option(player,'Run away.')
							io.option(player,'Please run away.')
							io.option(player,'Definitely run away.')
							io.option(player,'"Hi!"')
							c = io.get(player,False)
							if c < 4:
								io.say('You slam the door. It stays shut.')
							else:
								io.say('One of the spiders awkwardly waves hello. You have as decent a conversation as you\'d expect, considering your new friend\'s lack of voicebox.')
						else:
							io.say('Oh. So this is where the giant spider came from. You honestly thought there could only be one...')
							io.option(player,'Run away.')
							io.option(player,'Please run away.')
							io.option(player,'Definitely run away.')
							io.option(player,'"Hi!"')
							c = io.get(player,False)
							if c < 4:
								io.say('The others don\'t seem interested in following.')
							else:
								io.say('The spiders wave and chatter. You imagine them saying "Hello there! Did you meet Fred in the hallway? You\'re alright by us!" At least it\'s better than "Hello there! We\'re all extremely venomous!"')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 17:
					io.say('"Tock"')
					io.say('This creation mirrors my own will to help others, allowing me to act more efficiently. Tock doesn\'t have the same abilities as I do, but should still have the strength and compassion to impact the world in a good way.')
					io.say('RECALLED: For the same reason as myself. I had to deactivate Tock to avoid any more trouble...and also for Tock\'s sake, who seems to be taking a lot of stress. I can only hope nobody figures out the reactivation phrase; at least, not until I can fix all this.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('In the clumsily-decorated room, there\'s nothing but a large wooden chest.')
						if player.seen('Tock'):
							io.say('The chest lies open. There\'s a little bed inside, but nothing else.')
							io.option(player,'Leave.')
							io.get(player,False)
						else:
							io.say('The chest is closed.')
							io.option(player,'Open it.')
							io.option(player,'Leave.')
							c = io.get(player,False)
							if c == 1:
								io.say('You find a strange doll inside. It certainly isn\'t designed after any human, but you\'re not sure it\'s inanimate--it seems to be sleeping peacefully.')
								while True:
									io.option(player,'"Wake up!"')
									io.option(player,'"Hello?"')
									io.option(player,'"Tock, activate!"')
									io.option(player,'"Duam Xnaht!"')
									io.option(player,'"Enable Verbose Mode!"')
									io.option(player,'"Someone needs help!"')
									io.option(player,'"Reactivation Phrase!"')
									io.option(player,'Leave.')
									c = io.get(player,False)
									if c == 5:
										io.say('Tock leaps into the air so suddenly that you nearly fall over. After knocking the already-broken clock from the wall, Tock settles down and hovers in front of you.')
										io.say('[hi there...don\'t scare me like that! who are you? is the tower fixed yet?')
										io.option(player,'"Yes."')
										io.option(player,'"No."')
										c = io.get(player,False)
										if c == 1:
											io.say('Face alight with joy, Tock motions for you to wait and flies away, crashing into several walls on the way out. But Tock soon returns, head hung low.')
											io.say('[i\'m sorry, you must have been mistaken.]')
										elif c == 2:
											io.say('[oh. but...you\'re human. aren\'t you? nevermind.]')
										while True:
											io.option(player,'"Who are you?"')
											io.option(player,'"What are you?')
											io.option(player,'"How are you?')
											io.option(player,'"Uh...why are you?"')
											io.option(player,'"I should go."')
											c = io.get(player,False)
											if c == 1:
												io.say('[i\'m still working on that one. let\'s see: i\'m was created by the magician, i like to solve puzzles but i\'m not good at it...that\'s all i\'ve got. i\'d like to become more than that, someday.]')
											elif c == 2:
												io.say('[uh...a "sentient being?" there isn\'t a word for what i am specifically. "gremlin," maybe.]')
											elif c == 3:
												io.say('[i\'m doing fine, thanks for asking. could be better. that\'s why i\'m waiting here.]')
											elif c == 4:
												io.say('[because someone might need me someday.]')
											elif c == 5:
												break
										io.say('[okay. i\'ll probably go back to sleep, then...i won\'t be of much help to you. good luck!]')
										io.option(player,'"Wait..."')
										io.option(player,'"Bye."')
										c = io.get(player,False)
										if c == 1:
											io.say('[...me?]')
											io.option(player,'"What\'s on the top floor of this tower?"')
											io.option(player,'"Maybe you should visit the town first?"')
											c = io.get(player,False)
											if c == 1:
												io.say('[the magician is probably there now. you should probably head there--i won\'t keep you.]')
												io.say('Tock yawns and returns to sleep.')
											elif c == 2:
												io.say('[the town?? but...]')
												io.say('Tock thinks for an oddly long time.')
												io.say('[...okay, i will. i don\'t know whom this is supposed to help, though.]')
												io.say('Tock reluctantly opens the window and flies away...')
												unlockEpilogue('Tock')
												player.remember('Tock')
										elif c == 2:
											io.say('Tock waves goodbye, returns to the box, and becomes inanimate once more.')
										io.option(player,'Leave.')
										io.get(player,False)
										break
									elif c == 8:
										break
									else:
										io.say('No response.')
				elif i == 18:
					io.say('"Measuring Urns"')
					io.say('Maybe I\'m just not thinking quantitatively. These containers provide vital information about the items within. Not very exciting, but hopefully useful!')
					io.say('Everyone\'s probably busy right now, though.')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('There\'s a small stack of stone pots, like the one the idol carried around. Three are missing.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 19:
					io.say('"Gargoyle"')
					io.say('The gargoyle might be able to help me figure all this out. It certainly has a calmer disposition.')
					io.say('RECALLED: People were afraid of it. Then they forgot about it. I hope it\'s okay; it didn\'t want to return here.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('This room is completely empty, like it\'s never been used before.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 20:
					io.say('"Rex"')
					io.say('One more try. I noticed people carrying water near the river in stone pots, and decided to make a helper for them. Rex is an ambulatory idol which obtains vital information.')
					io.say('I don\'t know where Rex ended up; hopefully somewhere purposeful. Well, if not, you\'re always welcome to return.')
					io.option(player,'Open this door.')
					io.option(player,'Avoid this door.')
					c = io.get(player,False)
					if c == 1:
						io.say('Nothing here but a fairly standard zen garden. And, uh...a stack of board games.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 21:
					io.say('"Sorry"')
					io.say('I know my past 20 works haven\'t gone over so well, so I thought I\'d let everyone know I\'m making a fresh start. This indestructible message can be passed throughout town.')
					io.say('If only I knew how to start it.')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('The cabinet is empty except for a single envelope, with a meticulous wax seal and an impressive level of care.')
						io.say('The envelope is empty.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 22:
					io.say('"Reflection Mirror" (working title)')
					io.say('This mirror will let me look back in time and study my previous actions. Maybe then I can figure all this out, as long as I remember to study every day.')
					io.say('Actually, I ended up donating it. There are some people who found it really useful for their work. Funny, isn\'t it? And all by accident...')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('The cabinet is empty, save a cloud of dust.')
						io.option(player,'Leave.')
						io.get(player,False)
				elif i == 23:
					io.say('"Compass"')
					io.say('Normally this one wouldn\'t be worth mentioning, but I created a door below which can only be opened with this compass. From the outside, anyway. As a safety precaution.')
					io.say('I gave it away too.')
					io.option(player,'Open this cabinet.')
					io.option(player,'Avoid this cabinet.')
					c = io.get(player,False)
					if c == 1:
						io.say('The cabinet is empty.')
						io.option(player,'Leave.')
						io.get(player,False)
			elif i == 24:
				io.say('The label is otherwise blank.')
				io.option(player,'Open this door.')
				io.option(player,'Avoid this door.')
				c = io.get(player,False)
				if c == 1:
					io.say('The door leads to a short, plain balcony outside the tower. There actually is a label for this room, but it\'s on the other side of the door.')
					io.hline()
					io.say('"Clocktower"')
					io.say('The tower is tall enough that anyone with binoculars can see it. Just a small convenience for...busy birdwatchers? Whatever.')
					io.say('It\'s far away from everyone. Totally inaccessible. Built to last for years and years. It\'s better this way.')
					io.option(player,'Leave.')
					io.get(player,False)
			player.check('Catalogues')
			i = player.getChecks('Catalogues')
			if i == 5:
				io.say('As you return to the hall, you hear a strange noise drawing near. Around the corner, a leviathan of a spider shows up.')
				io.option(player,'Run away.')
				io.option(player,'Seriously, run away.')
				io.option(player,'"Hi!"')
				c = io.get(player,False)
				if c < 3:
					io.say('At lightning speed, you find the exit and return to the penultimate floor.')
					player.setDestination('Tower - L7')
					break
				elif c == 3:
					io.say('The spider stops in its tracks, looking down at you. It pensively lifts one of its forelegs, and waves "hello."')
					io.say('Soon it leaves to wander aimlessly near door #13.')
					io.option(player,'That went relatively well.')
					io.get(player,False)
			elif i == 10:
				io.say('As you turn back toward the hall, you immediately have to duck, as one of the tower\'s hammerhead sharks floats above your head.')
				io.say('Likewise, a school of tuna swim down the hall and disperse at the next intersection.')
				io.say('You wonder if you\'ve been here a little too long.')
			elif i == 15:
				io.say('As you return to the hall, you hear something approaching...again. What now?')
				io.say('Oh, of course it\'s a golden pterodactyl with totally unviable feet and a wing which is six times the size of the other.')
				io.say('You catch it before it falls again, confirming that it is, in fact, a thing that exists. Many equally strange things appear after it, just as awkwardly sketched and blindingly painted.')
				io.say('This floor is becoming very unrealistic. Almost like...')
			elif i == 20:
				io.say('You continue walking, only to hear a room-shaking crash from another room. From down the hall draws that indescribable behemoth from room 8. Its yawn is like a shrieking howl--you thought you had heard it before, but assumed it was your imagination.')
				io.option(player,'Approach.')
				io.option(player,'Run.')
				c = io.get(player,False)
				if c == 1:
					io.say('A behemoth may be dangerous, but not nearly as dangerous as a behemoth with as much inertia as an oncoming truck. You approach peacefully before allowing that to happen.')
					io.say('The behemoth is clearly friendly (you can just imagine it having an ironic name, like Precious or Fluffy or something,) but it seems genuinely surprised by your fearlessness.')
				else:
					io.say('You make a quick escape, and the behemoth quickly forgets about you, deciding instead to charge around aimlessly.')
			elif i == 24:
				io.say('You return to the hall to discover...everyone.')
				io.say('Just like the gremlins before, they were apparently overjoyed to meet someone new. So they all got together, and somehow found a supply of 2,000 party hats.')
				io.say('They look like a group of extraterrestrials trying way too hard to impress the first astronaut they met.')
				io.say('Thanks, everyone...what a sendoff.')
				io.option(player,'Enjoy the block party.')
				io.get(player,False)
		elif c == 2:
			io.say('You leave, returning to the penultimate floor.')
			player.setDestination('Tower - L7')
			break