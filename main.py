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
