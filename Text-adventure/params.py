# Parameters for the town puzzle.
#
# Distances are in meters, rates are in kmph (since they're usually written as such)
# They should be slightly randomized in the final version.

import randomizer, math

kmph_dict = {
	'none' : 4,
	'horses' : 7,
	'oxen' : 6,
	'jabberwock' : 24
}
cost_dict = {
	'none' : 0,
	'horses' : 6000,
	'oxen' : 8000,
	'jabberwock' : 14000
}
daycost_dict = {
	'none' : 0,
	'horses' : 2000,
	'oxen' : 1200,
	'jabberwock' : 3300
}

TOWN_lampposts_along_road = randomizer.randomInt(94,99)
TOWN_distance_between_lampposts = randomizer.randomRange(16.00,48.00)
TOWN_distance_between_rings = (TOWN_lampposts_along_road - 1) * TOWN_distance_between_lampposts
TOWN_width_of_road = randomizer.randomRange(4.00,9.00)
TOWN_walk_average_speed = randomizer.randomRange(4.5,5.5)
TOWN_distance_from_crossroads = 200

TOWN_inner_building_width = randomizer.randomRange(9.0,20.0)
TOWN_inner_distance_between_buildings = randomizer.randomRange(2.0,5.0)
TOWN_inner_adults_per_house = randomizer.randomRange(1.4,3.2)
TOWN_inner_walk_per_morning = randomizer.randomRange(0.2,1.6)
TOWN_inner_radius = randomizer.randomRange(1501,3001)
TOWN_inner_circumference = 2 * math.pi * TOWN_inner_radius
TOWN_inner_houses_per_segment = int(((TOWN_inner_circumference / 12) - TOWN_width_of_road) / (TOWN_inner_building_width + TOWN_inner_distance_between_buildings))
TOWN_inner_houses = 12 * TOWN_inner_houses_per_segment - 2 # The inn is 3 buildings long
TOWN_inner_people = int(TOWN_inner_houses * TOWN_inner_adults_per_house)
TOWN_inner_morning_walkers_per_minute = TOWN_inner_people * ((1000 * TOWN_walk_average_speed / 60.0) / TOWN_inner_circumference) * (TOWN_inner_walk_per_morning / 4)

TOWN_outer_building_width = randomizer.randomRange(9.0,20.0)
TOWN_outer_distance_between_buildings = randomizer.randomRange(2.0,5.0)
TOWN_outer_adults_per_house = randomizer.randomRange(1.4,3.2)
TOWN_outer_walk_per_morning = randomizer.randomRange(0.2,1.6)
TOWN_outer_radius = TOWN_inner_radius + TOWN_distance_between_rings
TOWN_outer_circumference = 2 * math.pi * TOWN_outer_radius
TOWN_outer_houses_per_segment = int(((TOWN_outer_circumference / 12) - TOWN_width_of_road) / (TOWN_outer_building_width + TOWN_outer_distance_between_buildings))
TOWN_outer_houses = 12 * TOWN_outer_houses_per_segment
TOWN_outer_people = int(TOWN_outer_houses * TOWN_outer_adults_per_house)
TOWN_outer_morning_walkers_per_minute = TOWN_outer_people * ((1000 * TOWN_walk_average_speed / 60.0) / TOWN_outer_circumference) * (TOWN_outer_walk_per_morning / 4)

TOWN_palace_margin = 1260
TOWN_palace_mural_count = randomizer.randomRange(150,300)
TOWN_palace_mural_width = (2.0 * math.pi * (TOWN_inner_radius - TOWN_palace_margin)) / TOWN_palace_mural_count

# This demo assumes that the roads are thin and long enough for such an estimation to make sense. It can be changed later.
TOWN_gold_needed = 10 * (2 * TOWN_inner_houses + 2 * TOWN_outer_houses)

# Parameters for the shrine puzzle.
#
#
#

SHRINE_distance_from_crossroads = 2400

SHRINE_gold_needed = 0

# Parameters for the canyon puzzle.
#
#
#

CANYON_distance_from_crossroads = 21600

CANYON_gold_needed = 0

# Parameters for the river puzzle.
#
#
#

RIVER_distance_from_crossroads = 32400

RIVER_gold_needed = 0

# Parameters for the garden puzzle.
#
#
#

GARDEN_distance_from_crossroads = 43200

GARDEN_gold_needed = 0

polars = {
	'Crossroads' : (0,0),
	'Town' : (TOWN_distance_from_crossroads,135),
	'Canyon' : (CANYON_distance_from_crossroads,315),
	'River' : (RIVER_distance_from_crossroads,270),
	'Garden' : (GARDEN_distance_from_crossroads,90)
}
coords = {}
for place in polars:
	(r, theta) = polars[place]
	coords[place] = (r * math.cos(theta),r * math.sin(theta))
def distanceBetween(des1,des2):
	(x1,y1) = coords[des1]
	(x2,y2) = coords[des2]
	return math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
