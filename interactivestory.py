from math import ceil
import random
markovTable = {}
sentenceStarters = []
averageSentenceLength = 0

def getInput(inp):
	global averageSentenceLength
	inp = inp.lower().split(" ")
	averageSentenceLength = (averageSentenceLength + len(inp)) / 2
	for x in inp:
		x = x.lower()
		if not x in markovTable:
			markovTable[x] = []
			markovTable[x].append("")
		try:
			markovTable[x].append(inp[inp.index(x) + 1])
			markovTable[x].remove("")
		except IndexError:
			continue
		except ValueError:
			markovTable[x].append(inp[inp.index(x) + 1])
	return inp[len(inp) - 1]
			
def produceOutput(lastWord):
	length = averageSentenceLength
	out = ""
	x = 0
	while x < length:
		out += " " 
		lastWord = random.choice(markovTable[lastWord])
		if lastWord == "":
			lastWord = random.choice(list(markovTable.keys()))
		out += lastWord
		x += 1
	print("\n" + out + "\n")
	getInput(out)
	
while True:
	txt = getInput(input())
	produceOutput(txt)
