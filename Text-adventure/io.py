def wrap(s):
	words = s.split(' ')
	newStr = ' '
	n = 0
	for word in words:
		if n >= 65:
			n = 0
			newStr += '\n '
		elif n > 0:
			newStr += ' '
			n += 1
		newStr += word
		n += len(word)
	return newStr

def clear():
	print "\n"*40

def hline():
	print("\n" + 80*"-")

def say(s):
	print wrap(s + "\n")

def readIdol(temp,vol,weight):
	print(' ' + str(temp).rjust(8) + '  K')
	print(' ' + str(vol).rjust(8) + '  L')
	print(' ' + str(weight).rjust(8) + ' kg')
	print('\n')

def playEpilogue(i):
	#TODO
	if i == 'Town':
		pass
	elif i == 'Canyon':
		pass
	elif i == 'Garden':
		pass
	elif i == 'River':
		pass
	elif i == 'Shrine':
		pass
	elif i == 'Tock':
		pass
	option('Continue.')
	get(False)

def showResults(puzzle):
	rankReqs = [
	('  *  ', 1.0),
	(' * * ', 0.25),
	('* * *', 0.05)
	]
	used = gold_used[puzzle]
	needed = gold_needed[puzzle]
	rank = ' --- '
	hline()
	print(' RESULTS')
	hline()
	say('You needed: ' + str(needed) + ' G')
	say('You spent:  ' + str(used) + ' G\n (not including tools, daily costs, etc.)')
	for r in rankReqs:
		budget = int((1 + r[1])*needed)
		print(' ' + r[0] + ' : Spend ' + str(budget) + ' G or less.')
		if used <= budget:
			rank = r[0]
	ranks[puzzle] = rank
	say('\n YOUR RANK: ' + rank)
	option('Continue.')
	get(False)
def showFinalResults():
	rankReqs = [
	('    *    ', 5),
	('   * *   ', 8),
	('  * * *  ', 11),
	(' * * * * ', 13),
	('* * * * *', 15)
	]
	stars = 0
	hline()
	print(' FINAL RESULTS')
	hline()
	for puzzle in ranks.keys():
		rank = ranks[puzzle]
		print(' ' + puzzle + ': ' + rank)
		if rank == '* * *':
			stars += 3
		elif rank == ' * * ':
			stars += 2
		elif rank == '  *  ':
			stars += 1
	say('\n You obtained ' + str(stars) + ' stars.')
	rank = ' --- '
	for r in rankReqs:
		print(' ' + r[0] + ' : Obtain ' + str(r[1]) + ' stars.')
		if stars >= r[1]:
			rank = r[0]
	ending = rank
	say('\n FINAL RANK: ' + rank)
	option('Continue.')
	get(False)

def isInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def getInt(_max,value = 0):
	while True:
		if not isInt(value):
			say('Please enter a valid integer.')
		else:
			value = int(value)
			if value <= 0:
				say('Please enter a positive integer.')
			elif value > _max:
				say('Please enter a number less than or equal to ' + str(_max) + '.')
			else:
				clear()
				return value
		value = raw_input()

def count(x,word):
	if x == 0:
		return 'no ' + word + 's'
	if x == 1:
		return '1 ' + word
	return str(x) + ' ' + word + 's'

def ordinal(n):
	if n not in [11,12,13]:
		if n % 10 == 1:
			return str(n) + "st"
		if n % 10 == 2:
			return str(n) + "nd"
		if n % 10 == 3:
			return str(n) + "rd"
	return str(n) + "th"

def option(player,s):
	player.addChoice()
	print(" " + str(player.choices()) + ": " + s)

def get(player,commands = True):
	player.displayHUD(commands)

	value = raw_input()

	# The "response" is the number entered by the player.
	# If a special command is used, response should return 0.
	response = 0
	choices = player.choices()
	player.resetChoices()

	if (value == 'T' or value == 't'):
		player.command = 'Talk'
		
	elif (value == 'W' or value == 'w'):
		player.command = 'Wait'

	elif (value == 'I' or value == 'i'):
		player.command = 'Items'

	elif (value == 'A' or value == 'a'):
		player.command = 'Talk'

	elif (value == 'C' or value == 'c'):
		player.command = 'Calendar'

	elif (value == 'S' or value == 's'):
		player.command = 'Save/Load'

	else:
		response = getInt(choices,value)
	
	return response