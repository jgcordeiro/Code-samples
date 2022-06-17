import random

def randomize(value,stdev):
	n = random.normalvariate(value,stdev)
	if n < 0:
		n = 0
	return n

def randomInt(start,stop):
	return random.randint(start,stop)

def randomRange(start,stop):
	return random.uniform(start,stop)

def countovertime(per_minute,stdev,time):
	n = 0
	for i in range(time):
		n += randomize(per_minute,stdev)
	return int(n)