import params, io

class Player:
	def __init__(self):
		self.inventory = {
			#'Idol':1,'Compass':1,'Automaton':1,'Torch':1,'Mirror':1
		}

		self.seed = 0

		self.verbose_mode = False

		self.epilogues = {
			'Town' : False,
			'Canyon' : True,
			'Garden' : True,
			'River' : True,
			'Shrine' : True,
			'Tock' : False
		}

		# Counters for achievements.
		self.achievements = {
			'Efficient (Town)' : (0,'Before Day 3, solve the town model with at least 2 stars.'),
			'Timeless' : (0,'Solve the town model without the Clock, and with at least 2 stars.'),
			'Spaceless' : (0,'Solve the town model without the Meterstick, and with at least 2 stars.'),
			#'Town Prodigy' : (0,'Solve the town model without opening the Items menu, with at least 2 stars.'),
			#'Friendly' : (0,'Help everyone in the town.'),
			#'Not Quite Alone' : (0,'Return home with the idol.'),
			#'Crafty' : (0,'Return home with at least three treasures.'),
			#'Adventurer' : (0,'Find the secret room in the tower.'),
			'Teachable Moments' : (0,'Unlock the best ending.'),
			'They\'ll Be Just Fine' : (0,'Unlock all six epilogue scenes.')
		}

		# Controllers for results.
		self.ranks = {
			'Town' : 'Incomplete',
			'Canyon' : '* * *',
			'Garden' : '* * *',
			'River' : '* * *',
			'Shrine' : '* * *'
		}
		self.ending = 'Incomplete'

		self.steed = 'none'

		self.vars = {}

		self.timeMemory = 0

		# day     =  481 - 1200
		# sundown = 1201 - 1260
		# night   = 1261 - 420
		# sunrise =  421 - 480
		self.time = 1200
		self.timeStr = '8:00 PM'
		self.day = 1

		self.destination = 'Tutorial'
		self.command = ''

		self.furnaceSwitches = {}

		self.memories = []

		self.itemUses = []

		self.setSteed('none')

		self.numChoices = 0

		self.schedule = []

		self.finishedTutorial = False

	def inSchedule(self,s):
		for item in self.schedule:
			if item[2] == s:
				return True
		return False

	def checkSchedule(self,t,start,end):
		if start < end:
			return t >= start and t <= end
		else:
			return t >= start or t <= end

	def scheduleOverlap(self,start,end):
		for (start2,end2,name) in self.schedule:
			if self.checkSchedule(start2,start,end) \
			or self.checkSchedule(end2,start,end) \
			or self.checkSchedule(start,start2,end2) \
			or self.checkSchedule(end,start2,end2):
				return name
		return ''

	def seen(self, s):
		return s in self.memories

	def remember(self, s):
		self.memories += [s]
	
	def hasUsed(self, item, location):
		return (item,location) in self.itemUses

	def setDestination(self, s):
		self.destination = s
		
	def getTime(self):
		return self.time % 1440
	def setTime(self, i):
		self.time = i
	def timeStr(self):
		return self.timeStr
	def setTimeStr(self, s):
		self.timeStr = s
	def day(self):
		return self.time / 1440
		
	def timeMemory(self):
		return self.timeMemory
	def setTimeMemory(self, t):
		self.timeMemory = t

	def changeVar(self, s, i):
		if s in self.vars:
			self.vars[s] += i
		else:
			self.vars[s] = i
	def setVar(self, s, i):
		self.vars[s] = i
	def getVar(self, s):
		if s in self.vars:
			return self.vars[s]
		return 0

	def unlockAchievement(self, a):
		pass
		#self.achievements[a][0] = 1
		#io.hline()
		#io.say('ACHIEVEMENT UNLOCKED!')
		#io.say(a + ': ' + self.achievements[a][1])
		#io.hline()

	def unlockEpilogue(self, i):
		self.epilogues[i] = True

	def playEpilogues(self):
		allEpilogues = True
		for i in self.epilogues.keys():
			if self.epilogues[i]:
				playEpilogue(i)
			else:
				allEpilogues = False
		if allEpilogues:
			unlockAchievement('They\'ll Be Just Fine')

	def has(self, item, need=1):
		return item in self.inventory and self.inventory[item] >= need

	def amount(self, item):
		if item in self.inventory:
			return self.inventory[item]
		return 0

	def getItem(self, item, count=1):
		if self.has(item):
			self.inventory[item] += count
		else:
			self.inventory[item] = count

	def loseItem(self, item, count=-1):
		if item in self.inventory:
			if count == -1 or count >= self.inventory[item]:
				self.inventory.remove(item)
			else:
				self.inventory[item] -= count

	def inventory(self):
		return self.inventory

	def verbose(self):
		return self.verbose_mode

	def setVerbose(self, b):
		self.verbose_mode = b

	def save_game(self, fn):
		pass
		# TODO

	def load_game(self, fn):
		pass
		# TODO

	def haveAllTreasures(self):
		return all(self.has(finalKey) for finalKey in ['Mirror', 'Automaton', 'Torch', 'Compass', 'Idol'])

	def is_day(self):
		return self.is_morning() or self.is_afternoon()

	def is_sundown(self):
		t = self.getTime()
		return t >= 1200 and t < 1260

	def is_night(self):
		t = self.getTime()
		return t >= 1260 or t < 420

	def is_sunrise(self):
		t = self.getTime()
		return t >= 420 and t < 480

	def is_morning(self):
		t = self.getTime()
		return t >= 480 and t < 720

	def is_afternoon(self):
		t = self.getTime()
		return t >= 720 and t < 1200

	def sun(self):
		if self.is_night():
			return 'Nighttime'
		if self.is_sunrise():
			return 'Sunrise'
		if self.is_morning():
			return 'Morning'
		if self.is_afternoon():
			return 'Afternoon'
		return 'Sundown'

	def setSteed(self, s):
		self.steed = s
		self.kmph = params.kmph_dict[s]
		self.daycost = params.daycost_dict[s]
		self.loseItem('Gold',-params.cost_dict[s])

	def displayHUD(self, commands = True):
		print("\n" + 80*"-")

		seeClock = (self.destination in ['Before the Clocktower','Town - Pheme\'s Shop','Town - The Stables','Town - General Store','???']) or self.has('Clock')

		if commands:
			status = " T: talk      A: Achievements"
		else:
			status = "        "
		status += " "*20
		status += self.destination
		print status

		s = "   "
		if commands:
			if len(self.schedule) > 0:
				if seeClock:
					t = min([int(self.timeUntil(item[0])) for item in self.schedule])
					s = "(event in " + io.count(t,"min") + ")"
				else:
					s = "(" + io.count(len(self.schedule),"event") + ")"
			status = " W: wait      C: Calendar " + s
		else:
			status = "        "
		status += " "*(23 - len(s))
		status += "Day "
		status += str(self.day)
		status += ", "
		if seeClock:
			status += self.timeStr.rjust(8)
		else:
			status += self.sun()
		print status

		if commands:
			status = " I: items     S: Save/Load   "
		else:
			status = "        "
		status += " "*20
		if self.has('Gold'):
			status += str(self.amount('Gold'))
			status += " G"
		print status

		print("\n" + 80*"-")

	def wait(self,i,asleep = False):
		newTime = self.time
		newTime += i

		# TODO: Check schedule

		self.setTimeStr(self.timeToString(newTime))
		self.setTime(newTime)

		#if not paid_daily and not is_day():
		#	changeGold(-daycost())
		#	io.say('(The day is over. It cost ' + str(daycost()) + ' G to feed the ' + steed() + '.)')

	def waitUntil(self,i):
		self.wait(self.timeUntil(i))

	def timeUntil(self,i):
		difference = i - self.time
		if difference <= 0:
			difference += 1440
		return difference

	def timeToString(self,t):
		m = t
		if m > 720:
			m -= 720
			s = 'PM'
		else:
			s = 'AM'
		h,m = divmod(m,60)
		if h == 0:
			h = 12
		return '%d:%02d ' % (h,m) + s

	def travel(self,d):
		self.wait(60.0 * d / self.kmph / 1000)

	def haveCarriage(self):
		return self.steed != 'none'

	def choices(self):
		return self.numChoices

	def addChoice(self):
		self.numChoices += 1

	def resetChoices(self):
		self.numChoices = 0

	def leavePlace(self,origin):
		if self.has('Compass'):
			io.say('You check your notes from the crossroads. With your compass, you can travel directly to any of these destinations:')
			places = [p for p in self.polars.keys() if p != origin]
			for place in places:
				self.option(place)
			c = self.get(False)
			dest = places[c-1]
		else:
			dest = 'Crossroads'
		self.travel(params.distanceBetween(origin,dest))
		if dest == 'Town':
			destStr = 'Town - Outer Gate'
		elif dest == 'Canyon':
			destStr = 'Canyon - L1'
		elif dest == 'River':
			destStr = 'River - Northern Bank'
		elif dest == 'Garden':
			destStr = 'Garden - Entrance'
		else:
			destStr = 'Crossroads'
		self.setDestination(destStr)