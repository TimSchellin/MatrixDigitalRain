import random
import time

infinite = True         # run the the script forever?
maxTick = 100000        # how many lines are printed (more lines means longer d$
speed = 1               # vertical scroll speed, very sensitive
width = 148              # works perfectly with xterm fontsize 26
minHeight = 1           # min line height
maxHeight = 9           # max line height
minModulo = 1           # effects how frequently lines are created
maxModulo = 4           #       so it changes the 'density'
maxColumns = 100         # max number of columns that can contain symbols at any$
densityModifier = 3

waterfall_list = []


def main():
	tick = 0
	while infinite:
		tick += 1;
		mainLoop(tick)
	if not infinite:
		for x in range(maxTick):
			mainLoop(x)

def mainLoop(tick):
	#debugMsg()
	delay()
	updateWaterfalls()
	startNewWaterfall(tick)
	printCurrentLine()

def delay():
	delayModifier = 3
	time.sleep(delayModifier/100*speed)

def updateWaterfalls():
	if len(waterfall_list) > 0:
		for x in waterfall_list:
			if x[1] <= 0:
				waterfall_list.remove(x)
			else:
				x[1] -= 1

def startNewWaterfall(tick):
	#global nextActiveTick
	for x in range(densityModifier):
		if(len(waterfall_list) < maxColumns):
			addNewWaterfall()
		#nextActiveTick = getNextTick(tick)

def printCurrentLine():
	line = ''.join(createMatrixLine())
	print(line)

def addNewWaterfall():
	spaceTaken = True
	while(spaceTaken):
		column = random.randint(0, width-1)
		spaceTaken = isSpaceTaken(column)
	height = random.randint(minHeight, maxHeight)
	waterfall = [column, height]
	waterfall_list.append(waterfall)

def createMatrixLine():
	matrix_str = list(' '*width)
	for pos in waterfall_list:
		matrix_str[pos[0]] = '{}'.format(getSym())
	return matrix_str

def isSpaceTaken(index):
	for x in waterfall_list:
		if x[0] == index:
			return True
	return False

def getSym():
	return chr(random.randrange(33, 126))

def testWaterfalls():			
	if len(waterfall_list) > 0:
		for waterfall in waterfall_list:
			print('[ {} ] [ {} ]'.format(waterfall[0], waterfall[1]))

def debugMsg():
	time.sleep(0.5)
	print('new tick')

'''
def getNextTick(tick):
	global lineFrequency
	if(lineFrequency > 100):
		lineFrequency = 100
	maxRange = -1 * int(lineFrequency/2) + 50
	return tick + (random.randrange(0, maxRange))
'''

main()