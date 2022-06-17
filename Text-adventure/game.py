#TODO:
# Implement achievements
# Add seed to HUD
# Test town puzzle
# Implement mirror with the Wait command
# Add uses of Meterstick and Wait
# Handle invalid inputs better
# Penalty for going without sleep
# Second line of commands:
#	Achievements
#	Calendar
#	Save/Load
# Title Screen

import randomizer, params, io, data
import math, random, sys
from scripts import *

def sleep():
	io.say('How many minutes do you want to sleep?')
	time = getInt()
	sleepFor(time)

def run():
	player = data.Player()
	while True:
		place = player.destination
		command = player.command
		if command == 'Talk':
			player.command = ''
			talk.go(player)
		elif command == 'Wait':
			player.command = ''
			wait.go(player)
		elif command == 'Items':
			player.command = ''
			items.go(player)
		elif command == 'Achievements':
			player.command = ''
			achievements.go(player)
		elif command == 'Calendar':
			player.command = ''
			calendar.go(player)
		elif command == 'Save/Load':
			player.command = ''
			saveload.go(player)
		elif place == 'Tutorial':
			tutorial.go(player)
		elif place == 'Copse':
			copse.go(player)
		elif place == 'Crossroads':
			crossroads.go(player)
		elif place == 'Town - Outer Gate':
			townGate.go(player)
		elif place == 'Town - Outer Ring':
			townOuter.go(player)
		elif place == 'Town - Pheme\'s Shop':
			townPheme.go(player)
		elif place == 'Town - The Stables':
			townStables.go(player)
		elif place == 'Town - Inner Ring':
			townInner.go(player)
		elif place == 'Town - General Store':
			townStore.go(player)
		elif place == 'Town - The Inn':
			townInn.go(player)
		elif place == 'Canyon - L1':
			canyonTop.go(player)
		elif place == 'The Off Road':
			shrineOffRoad.go(player)
		elif place == 'Shrine - Vestibule':
			shrineVestibule.go(player)
		elif place == 'Garden - Entrance':
			gardenEntrance.go(player)
		elif place == 'River - Northern Bank':
			riverNorthBank.go(player)
		elif place == 'Before the Clocktower':
			towerDistant.go(player)
		elif place == '???':
			towerApproach.go(player)
		elif place == 'Tower - L1':
			towerBase.go(player)
		elif place == 'Tower - L2':
			towerFountain.go(player)
		elif place == 'Tower - L3':
			towerGameRoom.go(player)
		elif place == 'Tower - L4':
			towerGremlins.go(player)
		elif place == 'Tower - L5':
			towerMachines.go(player)
		elif place == 'Tower - L6':
			towerFurnace.go(player)
		elif place == 'Tower - L7':
			towerDarkRoom.go(player)
		elif place == 'Tower - Catalogues':
			towerSecret.go(player)
		elif place == 'The End':
			towerTop.go(player)
		else:
			io.say('ERROR: No location "' + place + '."')
	self.run()

def main():
	run()
if __name__ == '__main__':
	sys.exit(main())
