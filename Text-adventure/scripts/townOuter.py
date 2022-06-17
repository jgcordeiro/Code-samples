import randomizer, params, io, data
import math, random

def changeStreet(newStreet):
	currentStreet = player.getVar('Town Street')
	if currentStreet == newStreet:
		return
	ccw, cw = (currentStreet - newStreet) % 12, (newStreet - currentStreet) % 12
	if ccw < cw:
		io.say('You begin traveling counter-clockwise.')
		numStreets = ccw
	else:
		io.say('You begin traveling clockwise.')
		numStreets = cw
	player.travel(params.TOWN_outer_circumference * numStreets)
	io.say('Soon you arrive on ' + io.ordinal(newStreet) + ' street.')
	player.setVar('Town Street',newStreet)

def go(player):
	io.option(player,'Travel along the circular road.')
	io.option(player,'Travel further into town.')
	io.option(player,'Examine the nearby bulletin.')
	currentStreet = player.getVar('Town Street')
	if currentStreet == 2:
		if player.seen('Restaurant'):
			io.option(player,'Go to Rosa\'s Restaurant.')
		else:
			io.option(player,'Go to the restaurant with the "Now Hiring" sign.')
	elif currentStreet == 3:
		if player.seen('Storehouse'):
			io.option(player,'Go to the nearby storehouse.')
		else:
			io.option(player,'Go to the nearby storehouse with the "Now Hiring" sign.')
	elif currentStreet == 5:
		if player.seen('Pheme'):
			io.option(player,'Go to Pheme\'s.')
		else:
			io.option(player,'Examine the building with a winged figure on the door.')
		if player.seen('Stables'):
			io.option(player,'Go to the stables.')
		else:
			io.option(player,'Examine the building with a window shaped like a wagon wheel.')
		io.option(player,'Leave town.')
		if player.seen('Clocktower'):
			io.option(player,'Examine the gate.')
		c = io.get(player)
	elif currentStreet == 8:
		io.option(player,'Go to the nearby observatory.')
	elif currentStreet == 10:
		io.option(player,'Go to the nearby radio station.')
	if c == 1:
		io.say('You scan the buildings on either side of you. Only a few of the shops are open, and even they seem pressed for customers.')
		io.say('A nearby sign calls this "' + io.ordinal(player.getVar('Town Street')) + ' street." Where do you want to go?')
		io.option(player,'1st Street')
		io.option(player,'2nd Street')
		io.option(player,'3rd Street')
		io.option(player,'4th Street')
		io.option(player,'5th Street (Town Entrance)')
		io.option(player,'6th Street')
		io.option(player,'7th Street')
		io.option(player,'8th Street')
		io.option(player,'9th Street')
		io.option(player,'10th Street')
		io.option(player,'11th Street')
		io.option(player,'12th Street')
		c = io.get(player)
		changeStreet(c)
	elif c == 2:
		io.say('You find your way to a road leading directly through the town. Just above it, a huge building with gilded shingles and marble buttresses stands in the center of town.')
		if player.haveCarriage():
			s = 'ride'
		else:
			s = 'walk'
		io.say('You ' + s + ' along the road at your usual pace, between wide fields of various vegetables. From street corner to street corner, there are a hundred lampposts at each side--well, ' + str(params.TOWN_lampposts_along_road) + ' actually. You feel slightly disappointed.')
		player.travel(params.TOWN_distance_between_rings)
		player.setDestination('Town - Inner Ring')

	elif c == 3:
		io.say('There\'s a bulletin board at the nearest intersection, but it\'s gone mostly unused. You do notice some advertisements for jobs.')
		io.option(player,'Read.')
		io.option(player,'Nevermind.')
		c = io.get(player)
		if c == 1:
			while True:
				i = player.getVar('Town Bulletin')
				if i == 0:
					print " Print our new newspapers!"
					print " ---"
					io.say('Lucas here, addressing all our readers who so kindly subscribed to the newspaper. Now that I\'m back on my feet, I\'m looking for contributors: if you remember our paper fondly, help us bring it back!')
					io.say('I\'m looking for a printing press operator. Materials can be expensive, but I\'ll reimburse 10 G for every delivered newspaper. Come see me if you\'re interested!')
					print " Hours: N/A"
					io.say('Requirements: Knowledge of the printing press and enough money for materials (600 G to schedule, 8 G per newspaper.)\n')
					io.say('Something draws you to this listing in particular.')
					io.option(player,'Look for Lucas.')
					io.option(player,'Stop reading.')
					io.option(player,'Read the next job listing.')
					io.option(player,'Stop reading.')
					c = io.get(player,False)
					if c == 1:
						player.wait(5)
						io.say('A passerby tells you that Lucas usually works at the inn. "He\'s only there in the morning, I think," he says.')
						break
					elif c == 2:
						break
					elif c == 3:
						player.changeVar('Town Bulletin',1)
					elif c == 4:
						break
				elif i == 1:
					print " Now hiring at Rosa\'s Restaurant!"
					print " ---"
					io.say('***We welcome new employees!*** We offer **easy to learn** work and a *great* first step in the **business** *****world*****!')
					io.say('Pay is *50 G/hour* immediately, and *100 G/hour* after your first week (until you miss a day.) *~*~Sign up now!~*~*')
					print " Hours: 2-hour shifts. 8AM-10AM, 12AM-2PM, 2PM-4PM, 6PM-8PM available."
					io.say('Requirements: None.\n')
					io.option(player,'Go to Rosa\'s Restaurant (2nd street.)')
					io.option(player,'Read the previous job listing.')
					io.option(player,'Read the next job listing.')
					io.option(player,'Stop reading.')
					c = io.get(player,False)
					if c == 1:
						changeStreet(2)
						player.remember('Restaurant')
						break
					elif c == 2:
						player.changeVar('Town Bulletin',-1)
					elif c == 3:
						player.changeVar('Town Bulletin',1)
					elif c == 4:
						break
				elif i == 2:
					print " Afternoon chores at the stables."
					print " ---"
					io.say('Any help is appreciated. 300 G/day.')
					print " Hours: 1PM-6PM."
					io.say('Requirements: None.\n')
					io.option(player,'Go to the stables (5th street.)')
					io.option(player,'Read the previous job listing.')
					io.option(player,'Read the next job listing.')
					io.option(player,'Stop reading.')
					c = io.get(player,False)
					if c == 1:
						changeStreet(5)
						setDestination('Town - Stables')
						break
					elif c == 2:
						player.changeVar('Town Bulletin',-1)
					elif c == 3:
						player.changeVar('Town Bulletin',1)
					elif c == 4:
						break
				elif i == 3:
					print " Need radio operators"
					print " ---"
					io.say('The public radio system is finally here! To make sure we have the best coverage possible, we\'re looking for operators to keep the broadcast running overnight. We\'re offering 500G per shift, so apply quickly!')
					print " Hours: 4-hour shifts. 6PM-10PM ######## 2AM-6AM ########."
					io.say('Requirements: Experience in radio technology.\n')
					io.option(player,'Go to the radio station (10th street.)')
					io.option(player,'Read the previous job listing.')
					io.option(player,'Read the next job listing.')
					io.option(player,'Stop reading.')
					c = io.get(player,False)
					if c == 1:
						changeStreet(10)
						player.remember('Radio Station')
						break
					elif c == 2:
						player.changeVar('Town Bulletin',-1)
					elif c == 3:
						player.changeVar('Town Bulletin',1)
					elif c == 4:
						break
				elif i == 4:
					print " HIRING: Storehouse on 3rd street"
					print " ---"
					io.say('We\'re always looking for more help. There are thousands of crates to be moved, so if you\'re looking for a place to apply your strength, why not apply here?')
					io.say('You don\'t need to record any hours; just move supplies for 5G per box. Also apply to our competition; can you beat the champion\'s score of 16 boxes per hour?')
					print " Hours: Show up anytime between 1PM and 6PM."
					io.say('Requirements: Technically none, but it isn\'t easy work.\n')
					io.option(player,'Go to the storehouse (3rd street.)')
					io.option(player,'Read the previous job listing.')
					io.option(player,'Read the next job listing.')
					io.option(player,'Stop reading.')
					c = io.get(player,False)
					if c == 1:
						changeStreet(3)
						player.remember('Storehouse')
						break
					elif c == 2:
						player.changeVar('Town Bulletin',-1)
					elif c == 3:
						player.changeVar('Town Bulletin',1)
					elif c == 4:
						break
				elif i == 5:
					print " Looking for a tour guide at the observatory!"
					print " ---"
					io.say('Do you know what\'s so amazing about the observatory? If so, there needs to be more of you! Apply to give daily tours, both for visitors and investors. The pay is 750G for each tour!')
					print " Hours: 2PM to 5PM."
					io.say('Requirements: Experience in communications and astronomy.\n')
					io.option(player,'Go to the observatory (8th street.)')
					io.option(player,'Read the previous job listing.')
					io.option(player,'Stop reading.')
					io.option(player,'Stop reading.')
					c = io.get(player,False)
					if c == 1:
						changeStreet(8)
						player.remember('Observatory')
						break
					elif c == 2:
						player.changeVar('Town Bulletin',-1)
					elif c == 3:
						break
					elif c == 4:
						break
			player.setVar('Town Bulletin',0)
		elif c == 2:
			pass

	elif c == 4:
		if currentStreet == 2:
			pass #TODO
		elif currentStreet == 3:
			pass #TODO
		elif currentStreet == 5:
			io.say('One building in particular catches your eye. It\'s a crooked structure, like an old tree. Lanterns in half a dozen colors sway on every limb. You approach it by a trail of flattened grass, with circular cobblestones dotted throughout.')
			io.say('The door is engraved with a strange character. At first you see a woman with wings, but as you draw closer, you see that dozens of eyes and ears are faintly drawn around her. Beneath her feet are what look like blades of grass...they\'re buildings.')
			if not player.seen('Pheme'):
				io.say('It looks like a shop of some kind, but you have no idea what it\'s for.')
			io.option(player,'Go inside.')
			io.option(player,'Maybe later.')
			c = io.get(player)
			if c == 1:
				player.setDestination('Town - Pheme\'s Shop')
			elif c == 2:
				io.say('Well...maybe not. You head back down the trail and step onto the main road.')
		elif currentStreet == 8:
			pass #TODO
		elif currentStreet == 10:
			pass #TODO

	elif c == 5:
		if currentStreet == 1:
			pass
		elif currentStreet == 5:
			io.say('Sitting lowly by a row of near-identical shoppes, this place looks more like a barn than a furnished building. It seems to be the entrace to a field, lightly cloaked in hay and mosquitoes, but you can\'t quite see past the other storefronts. You glance through the front window--the space inside is brightly lit, and workers stroll back and forth on muddy boots which kick up the earth.')
			if not player.seen('Ronald'):
				io.say('It looks like some kind of stable. The country is far too big to travel by foot--the stable seems like a good place to go.')
			io.option(player,'Go inside.')
			io.option(player,'Maybe later.')
			c = io.get(player)
			if c == 1:
				if player.verbose():
					io.say('[i\'ll wait outside for now. uh...i had a nasty run-in with a big dog once, and i\'d feel much safer out here.]')
				io.say('The ground crunches and the walls creak. You look around, but a thicket of fences obscures both wings of the rustic castle. A counter is placed as far from the noise and stench as possible. Behind it, a thin man pores over a clipboard, his long brown hair draped over him like a yolk.')
				if player.seen('Ronald'):
					io.say('"Welcome back," says Ronald, immobile.')
				else:
					io.say('The hay beneath your feet alerts him. "Welcome," he says tiredly, "to the town stable. My name is Ronald--are you looking to rent a carriage?"')
					player.remember('Ronald')
				player.setDestination('Town - The Stables')
			elif c == 2:
				io.say('Well...maybe not. You head back down the trail and step onto the main road.')

	elif c == 6:
		io.say('You return to the town gate.')
		player.setDestination('Town - Outer Gate')

	elif c == 7:
		if currentStreet == 1:
			pass
		elif currentStreet == 5:
			io.say('Oh--you hadn\'t noticed this before. On the gate is a mural of curled metal bars, the outline of a skyline. You recognize the building in the center: it\'s the clocktower. You recognize the spire, the white brick turrets, and the diamond-shaped hands. These ones seem to be welded in the 9:00 position.')
			io.say('The skyline looks so much...fuller. It isn\'t any horizon you know--the ground has teeth, steeples nearly half as tall as the clocktower. Even as a mural, they look full of life.')
			io.say('Below, a gaggle of crudely sculpted people is scattered beneath the buildings, portrayed in solid bronze instead of wiry steel. It\'s hard to tell, but they look content.')
