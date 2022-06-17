import randomizer, params, io, data
import math, random

def go(player):
	if player.seen('Pheme'):
		io.say('"Welcome back to Pheme\'s," chimes the familiar voice behind the desk.')
	else:
		io.say('You walk into a violently overdecorated room. Every wall is colorful ceramic plates on top of colorful patches of wallpaper on top of colorful wooden planks. For a building with such terrible posture, you wouldn\'t expect such a wild interior.')
		io.say('At the end of the room is a white desk, made to look like a miniature palace, marble columns and all. Floral patterns are carved around the edges and painted in peach. Almost the entire desk is empty, but stacks of fragile paper are packed into the shelves behind it.')
		player.remember('Pheme')
		io.say('"Welcome to Pheme\'s!" You jump at the frighteningly happy voice. A young woman sits behind the desk. She intensely wields a fountain pen, as though her notebook might jump up and bite. Her round glasses magnify her blue eyes to scary proportions.')
	while True:
		if player.seen('Tock'):
			if not player.seen('Gold'):
				io.say('[hey--listen!] You hear the faint whisper. For some reason, Tock is trying to stay out of sight. [ask her about that bit of gold you found. i think it\'ll be really helpful.]')
			elif not player.seen('Surveys'):
				io.say('[remember to ask about the townsfolk too. there\'s decades\' worth of surveys here--they never get thrown out!]')
		io.option(player,'Leave.')
		io.option(player,'Ask about the Garden.')
		io.option(player,'Ask about the town.')
		if player.seen('Surveys'):
			io.option(player,'Read another survey.')
		else:
			io.option(player,'Ask about the townsfolk.')
		io.option(player,'Ask about the Canyon.')
		io.option(player,'Ask about the River.')
		io.option(player,'Ask about home.')
		if not player.seen('Gold'):
			io.option(player,'Ask about the gold trinket.')
		c = io.get(player)
		if c == 1:
			io.say('"Come back anytime," says Pheme.')
			break
		elif c == 2:
			io.say('"Oh, the Garden! It\'s a lovely place, if you\'re willing to make the trek. No one enjoys it more than the caretakers, though--they demanded it be the highest marker on the crossroads."')
		elif c == 3:
			io.say('"This town was founded 182 years ago, but it used to be much smaller. It was only \'finished\' about 32 years ago.')
			io.say('"The whole place is built in a big circle with twelve segments, like a--" Pheme glances around the room. "--like a plate. Every building is on either the outer ring, here, or the inner ring that way. The rest of the town is farmland, storehouses, and the central plaza."')
			if player.is_sundown():
				io.say('The inner ring has a nice little inn. You should go there soon--it\'s getting dark.')
		elif c == 4:
			if not player.seen('Surveys'):
				io.say('"Here are the town surveys from the past two months; read as many as you want!" Pheme lowers her voice for a moment. "Be careful with fact-checking, though. Our writers have to come up with a lot of buzz each week and, well...they do their best."')
				player.remember('Surveys')
			io.say('You take one of the papers and read a bit:')
			i = player.getChecks('surveys') % 7
			if i == 0:
				print(' ISSUE #9490: Fine Dining')
				print(' By L. Smith')
				io.say('In our latest questionnaire, 32 percent of participants identified themselves as vegetarian, citing the rural restaurants on the southwest side as their favorite place for a special occasion. Full disclosure: several of our readers have protested the statistic before this issue\'s release, citing the rumor that vegetarians are more likely to participate in surveys. Others have protested that the existence of this rumor has driven vegetarians away from our surveys. Do you still believe in \'32 percent?\' Please send us your opinions!')
			elif i == 1:
				print(' ISSUE #9489: Exercise')
				print(' By R. Connor')
				io.say('People here sure love to walk, don\'t they? A recent survey found people on the outer ring walk ' + str(round(params.TOWN_outer_walk_per_morning,2)) + ' hours each morning (that\'s 8 to noon,) while those on the inner ring walk ' + str(round(params.TOWN_inner_walk_per_morning,2)) + '. To note, we\'ve adhered to our readers\' suggestions, and conducted the survey house-by-house instead of interviewing morning strollers.')
			elif i == 2:
				print(' ISSUE #9488: Charity')
				print(' By anonymous')
				io.say('Good news! A study by anonymous, anonymous, and anonymous has shown that our beloved mayor has spent over 150,000,000 G on our damaged roofing and none of these funds were moved to his personal account at all! We\'d also like to thank the mayor for sponsoring this article in these financially difficult times...')
			elif i == 3:
				print(' ISSUE #9487: Housing')
				print(' By L. Smith')
				io.say('As extrapolated from the past 48 hours, the population of our town is on the up-and-up! At the moment, the average house has ' + str(round(params.TOWN_outer_adults_per_house,2)) + ' adults in the outer ring, and ' + str(round(params.TOWN_inner_adults_per_house,2)) + ' adults in the inner ring. Hopefully that will change soon; if you\'ll remember, a recent scientific study found that "crowded ... homes show ... increase in cognitive ... function ... and memory." (Jones 232-287)')
			elif i == 4:
				print(' ISSUE #9486: Hurry Along!')
				print(' By E. Turquoise')
				io.say('A new study shows that adults in this town have an average walking speed of ' + str(round(params.TOWN_walk_average_speed,2)) + ' kmph. To restore trust between our readers and writers, we\'ve confirmed this number through data provided by 230 citizens, a whole 228 above our previous fact threshold!"')
			elif i == 5:
				print(' ISSUE #9485: The Palace')
				print(' By L. Smith')
				io.say('I understand this is still a difficult subject, but I feel this is necessary information for you as readers. The palace at the center of town is easily exceeding its budget in maintenance. Just repainting the circular base is prohibitively expensive: there are %d murals, one every %.2f meters. These repairs also seem to accelerate the structural damage on the 8 upper floors.' % (params.TOWN_palace_mural_count, params.TOWN_palace_mural_width))
			elif i == 6:
				print(' ISSUE #9485B: Your Questions Answered MCCCLV')
				io.say('We\'d like to thank our readers yet again for the numerous letters we\'ve received. As usual, if you contacted us in the past week, please consult the table below for our response.')
				io.say('"Good sir, I assure you that I know what \'null hypothesis\' means, and I don\'t appreciate the insinuation. If you read my article closer, you\'ll find a hypothesis clearly written on paragraph two. Please look over your feedback before sending it in the future."')
				io.say('"Thanks for your interest! You see, our measurement of \'one foot\' is derived from the foot length of an anonymous employee of average height (approximately 10.2 feet.)"')
				io.say('"For your information, our studies are TRIPLE blind, because at Pheme\'s we always take that extra step for our readers. Thank you for your concern, and let us know how we can be of further help!"')
				io.say('A dozen more responses follow...you decide to stop here.')
			else:
				player.check('surveys')
		elif c == 5:
			io.say('"I hear the canyon was a popular tourist attraction. There was an avalance recently, so it\'s out of commission until we clear out the rubble."')
		elif c == 6:
			io.say('"I\'d stay far away from the river this time of year. I hear the whole system is falling apart--whatever channel isn\'t droughted is flooding instead. It\'s such a shame, too...that river\'s done more for the town than a hundred builders."')
		elif c == 7:
			io.say('"Never heard of it. You aren\'t trying to stump me, are you?" Pheme thinks for a moment. She looks a little worried. "Oh...well, I\'m sure you\'ll find it. Maybe you could ask around town. Most of us would be happy to help."')
	player.setDestination('Town - Outer Ring')