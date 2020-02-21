import sys
import string
from builtins import range
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
	if subscriptions == None or len(subscriptions) == 0:
		return ""
	result=""

	for subscription in subscriptionsAll:
		# subscription=removeNoneArray(subscription)
		# if subscription != None and len(subscription) != 0:
		# 	result+='*'.join(subscription)+'+'
		result+='*'.join(subscription)+'+'

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
