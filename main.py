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
