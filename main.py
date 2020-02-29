import sys
import string
from builtins import range
from collections import OrderedDict
# from tkinter import *
# from tkinter import ttk
# import matplotlib.pyplot as plt
# import networkx as nx

def isOcta(number):
	isValid=True
	base=8
	if number == "":
		isValid=False
	for char in number:
		if char.isdigit() and int(char)<base:
			continue
		else:
			isValid=False
	return isValid

def charsRepeated(number):
	digits=[]
	repeated=False
	for char in number:
		if digits.count(char) == 0:
			digits.append(char)
		else:
			repeated=True
			break
	return repeated

def charsToBin(number):
	results=[]
	for char in number:
		results.append(charToBin(char))
	return results

def charToBin(char):
	if char == "0":
		return [0,0,0]
	elif char == "1":
		return [0,0,1]
	elif char == "2":
		return [0,1,0]
	elif char == "3":
		return [0,1,1]
	elif char == "4":
		return [1,0,0]
	elif char == "5":
		return [1,0,1]
	elif char == "6":
		return [1,1,0]
	elif char == "7":
		return [1,1,1]
	return None

def binsToFormula(bin):
	results=[]
	for bi in bin:
		results.append(binToFormula(bi))
	return results

def binToFormula(bin):
	if bin != None and len(bin) == countChild:
		results=[]
		i=0
		for bi in bin:
			if bi == 0:
				results.append(alphas[i] + "'")
			else:
				results.append(alphas[i])
			i=i+1
		return results
	else:
		return None

def binToFormulaOld(bin):
	if bin == [0,0,0]:
		return ["x'","y'","z'"]
	elif bin == [0,0,1]:
		return ["x'","y'","z"]
	elif bin == [0,1,0]:
		return ["x'","y","z'"]
	elif bin == [0,1,1]:
		return ["x'","y","z"]
	elif bin == [1,0,0]:
		return ["x","y'","z'"]
	elif bin == [1,0,1]:
		return ["x","y'","z"]
	elif bin == [1,1,0]:
		return ["x","y","z'"]
	elif bin == [1,1,1]:
		return ["x","y","z"]

def subscriptionOfFormulas(formula1, formula2):
	finalFormula=[]
	i=0
	for formula in formula1:
		if formula1[i] == formula2[i]:
			finalFormula.append(formula1[i])
		# else:
		# 	finalFormula.append(None)
		i=i+1
	return finalFormula

def valuesAreSame(array):
	if array == None or len(array) == 0:
		return False
	isSame=True
	firstValue=array[0]

	# loop 1 until countChild-1
	# for i in range(1, countChild):
	# 	if array[i] != firstValue:
	# 		isSame=False

	for value in array:
		if value != firstValue:
			isSame=False
	return isSame

def subscriptionsOfFormulas(subscriptions):
	results=[]
	if subscriptions == None or len(subscriptions) == 0:
		return results
	# loop 0 until countChild-1
	for i in range(0, countChild):
		values=[]
		for v in subscriptions:
			if v[i] != None:
				values.append(v[i])
		isSame=valuesAreSame(values)
		print("Check", i+1,"th values of arrays:", values, "is", isSame)
		if isSame:
			results.append(subscriptions[0])
	return results

def subscriptionsFilter(subscriptions):
	results=[]
	if subscriptions == None or len(subscriptions) == 0:
		return results
	for subscription in subscriptions:
		if len(subscription) >= countChild-1:
			results.append(subscription)
	return results

def removeNoneArray(array):
	result=[]
	for item in array:
		if item != None:
			result.append(item)
	return result

def removeNoneArrays(array):
	result=[]
	for item in array:
		if item != None:
			data=[]
			for value in item:
				if value != None:
					data.append(value)
			result.append(data)
	return result

def toFormula(subscriptionsAll):
	if subscriptionsAll == None or len(subscriptionsAll) == 0:
		return ""
	result=""

	for subscription in subscriptionsAll:
		if isinstance(subscription, list):
			result+='*'.join(subscription)+'+'
		else:
			result+=subscription+'+'

	return result.rstrip('+')

def evalAlgorithm(newFormula, formula, binary):
	# We not need to use eval(), We can do this with an algorithm, It's not hard!
	return eval(newFormula)

def evalFormula(formula, binaries):
	print("formula:", formula)
	# print(binaries)
	print("Solving g for binaries:")
	results=[]
	for binary in binaries:
		newFormula=formula
		i=0
		# newFormula=newFormula.replace("x", str(binary[0]))
		# newFormula=newFormula.replace("y", str(binary[1]))
		# newFormula=newFormula.replace("z", str(binary[2]))
		for alpha in alphas:
			newFormula=newFormula.replace(alpha+"'", str(binary[i]))
			newFormula=newFormula.replace(alpha, str(binary[i]))
			i=i+1

		calcFormula=evalAlgorithm(newFormula, formula, binary)
		calcFormula=1 if calcFormula >=1 else 0
		print("\t", binary, formula, newFormula, calcFormula)
		if calcFormula == 1:
			results.append(binary)
	return results


def nonSubscribers(subscriptions1, subscriptions2):
	results=[]
	if subscriptions1 == None or len(subscriptions1) == 0:
		return results
	if subscriptions2 == None or len(subscriptions2) == 0:
		return results
	for subscription in subscriptions1:
		if subscriptions2.count(subscription) == 0:
			results.append(subscription)
	return results

def normalize(g):
	results=[]
	for items in g:
		result=[]
		i=0
		added=0
		for item in items:
			if alphas.index(item[0]) != i+added:
				result.append(None)
				added=added+1
			result.append(item)
			i=i+1
		# Add none at end of list when your list size is 0 or 1 or 2
		# This will not run when your list size is 3
		for i in range(len(result), countChild):
			result.append(None)
		results.append(result)
	return results

def removeDublicateValue(array):
	result=[]
	for item in array:
		if result.count(item) == 0:
			result.append(item)
	return result

def commonValues(array):
	# if array != None and len(array) != 0:
	# print(array)
	for x in array[0]:
		# print("x", x)
		tc=0
		for y in array[1:]:
			# print("y", y)
			c=0
			for z in y:
				# print("z", z)
				if z == x:
					c=c+1

			if c > 0:
				# print("yes", c)
				tc=tc+1
			# else:
			# 	print("no")

			# print()

		if tc > 0:
			return x
			# print("yes", c)
		# else:
			# print("no")
		# print("----------")

	return None

def removeValue(array, values):
	result=[]
	for item in array:
		for x in item:
			if isinstance(values, list):
				for i in values:
					if x != i:
						result.append(x)
			else:
				if x != values:
					result.append(x)
	return result

def filterGArray(g):
	# print(g)
	if len(g) >=2 and isinstance(g[1], list):
		# print("i",g[1][0])
		# n=0
		for x in g[1][0]:
			# m=0
			for y in g[1][0]:
				# print(x, y)
				if (x == "x" and y == "x'") or (x == "x'" and y == "x"):
					# print("del", g[1][0])
					g[1][0].remove(x)
					g[1][0].remove(y)
				elif (x == "y" and y == "y'") or (x == "y'" and y == "y"):
					g[1][0].remove(x)
					g[1][0].remove(y)
				elif (x == "z" and y == "z'") or (x == "z'" and y == "z"):
					g[1][0].remove(x)
					g[1][0].remove(y)
				# m=m+1
			# n=n+1
		g[1]=g[1][0]
		if len(g[1]) == 0:
			g.remove(g[1])
	return g

# number="156"
# number="0367"
# number="45"
# number="145"
# number="457"

# number="1357"
number="0246"
number="0167"
number="1247"
number="25"
countChild=3
numberLength=len(number)
alphas=string.ascii_lowercase
alphas=alphas[-3:] + alphas[0:-3]
alphas=alphas[0:countChild]
alphasLength=len(alphas)
binaries=None
formulas=None

print("Number: ", number)
print("NumberLength: ", numberLength)

if not isOcta(number):
	print("Error: Number not valid!")
	sys.exit(-1)

if charsRepeated(number):
	print("Error: Number not valid, You cannot use dublicate digit in your number!")
	sys.exit(-1)

print("Alpha is :", alphas)
print("AlphaCount is :", alphasLength)

binaries=charsToBin(number)
if binaries == None:
	print("Error: binaries is None!")
	sys.exit(-1)
binariesLength=len(binaries)
print("Binaries: ", binaries)
print("BinariesLength: ", binariesLength)

formulas=binsToFormula(binaries)
if formulas == None:
	print("Error: formulas is None!")
	sys.exit(-1)

print("Formulas: ", formulas)

subscriptions=[]

# loop 0 until numberLength-1
for x in range(0, numberLength):
	# loop x+1 until numberLength-1
	for y in range(x+1, numberLength):
		print("[ ",x+1,"th <-> ",y+1,"th ] : {", formulas[x] , ", ", formulas[y], "}")
		subscription=subscriptionOfFormulas(formulas[x], formulas[y])
		print("                    Subscription: ", subscription)
		subscriptions.append(subscription)

print("Subscriptions: ", subscriptions)
g=subscriptionsFilter(subscriptions)
print("g, SubscriptionsAll: ", g)

if g != None and len(g) != 0:
	commonSubscriptions=commonValues(g)
	print("commonSubscriptions: ", commonSubscriptions)
	if commonSubscriptions != None:
		newG=[commonSubscriptions, [removeValue(g, commonSubscriptions)]]
	else:
		newG=g
	print("newG: ", newG)
	newG=filterGArray(newG)
	print("newG: ", newG)
	if newG != None and len(newG) != 0:
		gFormula=toFormula(newG)
		print("gFormula: ", gFormula) #It's $g formula

		gValues=evalFormula(gFormula, binaries)
		gValuesCount=len(gValues)

		print("gValues: ", gValues)
		print("gValuesCount: ", gValuesCount)
		print("Compare gValuesCount with binariesLength: ", gValuesCount, "??", binariesLength)

		if gValuesCount == binariesLength:
			print("\tThey are equal!")
			g=newG
		elif gValuesCount < binariesLength:
			print("\tbinariesLength is bigger then gValuesCount.")
			g=newG
			print("Diff two array:")
			print("\tsubscriptions1: ", binaries)
			print("\tsubscriptions2: ", gValues)
			nonSubscribersAll=nonSubscribers(binaries, gValues)
			print("NonSubscribers: ", nonSubscribersAll)
			nonSubscribersAllFormula=binsToFormula(nonSubscribersAll)
			print("nonSubscribersAllFormula: ", nonSubscribersAllFormula)
			g=g + nonSubscribersAllFormula
		else:
			print("Error: binariesLength is more then gValuesCount and we not except it!")
			sys.exit(-1)


	else:
		print("newG formula is empty!")
else:
	subscriptions
	print("g formula is empty!")
# if subscriptionsAll != None and len(subscriptionsAll) != 0:
# 	subscriptionsAllFormula=toFormula(subscriptionsAll)
# 	print("SubscriptionsAllFormula: ", subscriptionsAllFormula) #It's $g formula

# 	gValues=evalFormula(subscriptionsAllFormula, binaries)
# 	gValuesCount=len(gValues)

# 	print("gValues: ", gValues)
# 	print("gValuesCount: ", gValuesCount)
# 	print("Compare gValuesCount with binariesLength: ", gValuesCount, "??", binariesLength)
# 	g=[]
# 	if gValuesCount == binariesLength:
# 		print("\tThey are equal!")
# 		g=subscriptionsAll
# 	elif gValuesCount < binariesLength:
# 		print("\tbinariesLength is bigger then gValuesCount.")
# 		g=subscriptionsAll
# 		print("Diff two array:")
# 		print("\tsubscriptions1: ", binaries)
# 		print("\tsubscriptions2: ", gValues)
# 		nonSubscribersAll=nonSubscribers(binaries, gValues)
# 		print("NonSubscribers: ", nonSubscribersAll)
# 		nonSubscribersAllFormula=binsToFormula(nonSubscribersAll)
# 		print("nonSubscribersAllFormula: ", nonSubscribersAllFormula)
# 		g=g + nonSubscribersAllFormula
# 	else:
# 		print("Error: binariesLength is more then gValuesCount and we not except it!")
# 		sys.exit(-1)

# 	print("g: ", g)
# 	gFormula=toFormula(g)
# 	print("gFormula: ", gFormula)
# 	gNormalize=normalize(g)
# 	print("gNormalize: ", gNormalize)
# 	gNormalizeSubscriptions=subscriptionsOfFormulas(gNormalize)
# 	print("gNormalizeSubscriptions: ", gNormalizeSubscriptions)
# 	gNormalizeSubscriptionsCount=len(gNormalizeSubscriptions)
# 	print("gNormalizeSubscriptionsCount: ", gNormalizeSubscriptionsCount)
# 	gNormalizeSubscriptionsFilter=removeNoneArrays(gNormalizeSubscriptions)
# 	print("gNormalizeSubscriptionsFilter: ", gNormalizeSubscriptionsFilter)

# 	gNormalizeSubscriptionsFilterDublicate=removeDublicateValue(gNormalizeSubscriptionsFilter)
# 	print("gNormalizeSubscriptionsFilterDublicate: ", gNormalizeSubscriptionsFilterDublicate)

# 	if gNormalizeSubscriptionsCount == 0:
# 		print("Error: Cannot draw this graph!")
# 		sys.exit(-1)

# 	g=gNormalizeSubscriptionsFilterDublicate

# else:
# 	print("Not need to calc g formula!")
# 	g=subscriptionsAll

# graph=g
# print("Graph: ", graph)
