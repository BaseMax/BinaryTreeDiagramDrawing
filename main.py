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