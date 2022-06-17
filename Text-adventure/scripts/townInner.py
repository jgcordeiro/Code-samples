import randomizer, params, io, data
import math, random

def go(player):
	io.say('You stand before a ring of buildings, much smaller than the one around the edge of town. These little houses and shacks have stitched roofs and wooden stairs beneath each door. The only particularly large building is the inn to your right.')
	if player.verbose():
		print(' Tock floats lazily by.')
		if not player.seen('Lucas'):
			if player.is_morning():
				io.say('[there\'s the inn! lucas should be there now.]')
			else:
				io.say('[there\'s the inn! just ask to stay until 8:00 am--lucas usually shows up then.]')
		elif not player.seen('Maria'):
			io.say('[see that building with all the gears in front? that store has lots of stuff for solving problems. i\'m sure maria would be glad to help you.]')
		elif not player.has('Automaton'):
			io.say('[remember to talk to lucas if you need to hear the instructions again.]')
		else:
			io.say('[looks like we\'re finished up here. where to next?]')
	while True:
		io.option(player,'Look around.')
		io.option(player,'Leave.')
		io.option(player,'Examine the center of town.')
		io.option(player,'Examine the building with a wreath of cogs and gears.')
		io.option(player,'Examine the inn.')
		c = io.get(player)
		if c == 1:
			io.say('Moving clockwise around the town, you don\'t see nearly as many signs as you did on the outer ring. The little houses and shops look rather similar, and the labels and numbers are nearly faded. You reach the next crossroads, but you\'ve lost count of the identical buildings.')
			player.travel(params.TOWN_inner_circumference / 12)
		elif c == 2:
			io.say('You walk along the road at your usual pace, between wide fields of various vegetables, and a hundred lampposts on either side--well, ' + str(params.TOWN_lampposts_along_road) + ' actually. You feel very disappointed.')
			player.travel(params.TOWN_distance_between_rings)
			player.setDestination('Town - Outer Ring')
			break
		elif c == 3:
			io.say('A building, almost like a palace, looks over the plaza in the center of town. Giant trees are sculpted into the walls, and cracked stone leads nearly all the way to the top. It\'s difficult to tell at a distance, but it seems like the magnificent structure is falling apart.')
			io.say('You notice a withered sign at the edge of the road. On its last legs, it reads: "Palace, ' + str(params.TOWN_palace_margin / 1000.0) + ' km."')
		elif c == 4:
			io.say('This convenient little shop sits between the indistinguishable houses. Half of the shop is outdoors, and the other half is lit all around by circular windows. A sign on the doorknob says "General Store - OPEN."')
			io.option(player,'Go inside.')
			io.option(player,'Maybe later.')
			c = io.get(player)
			if c == 1:
				player.setDestination('Town - General Store')
				break
			elif c == 2:
				io.say('Well...maybe not. You return to the circle of houses.')
		elif c == 5:
			io.say('A pleasant-looking inn sits by the crossroads, three times the width of the nearby houses. Through the window you can see a cozy fireplace and a lounge with a stack of books in the center.')
			io.option(player,'Go inside.')
			io.option(player,'Maybe later.')
			c = io.get(player)
			if c == 1:
				if player.verbose():
					if player.is_morning():
						io.say('[okay, lucas is here--he\'s the one in the brown cap. let me know how it goes.]')
					else:
						io.say('[lucas will be here in the morning. why not stay until then?]')
				io.say('The building glows with warm color from the cherry walls and the vibrant linen rugs. The inn is brought to life by paintings, candles, and rows upon rows of mantelpiece sculptures. But something is missing--a few things, actually. There\'s a game board on each table, but no pieces. Pale circles on the walls indicate decorations which were just recently removed.')
				player.setDestination('Town - The Inn')
				break
			elif c == 2:
				io.say('Well...maybe not. You return to the circle of houses.')