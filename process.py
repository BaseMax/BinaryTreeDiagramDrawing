# Max Base
# https://github.com/BaseMax/PhdMathProject
import string
import sys
# x = int(e1.get())
# assert x >= 0
# if x == 0:
# 	return [[0]]
# binary = []
# while x != 0:
# 	temp = [0, 0, 0]
# 	for k in range(3):
# 		temp[k] = ((x % 10) // (2 ** (2 - k))) % 2
# 	binary.append(temp.copy())
# 	x = x // 10
# binary.reverse()
# data = (binary)
data=[
	[0,1,1],
	[1,0,0],
	[1,0,1],
]
# 145
data=[
	[0,0,1],
	[1,0,0],
	[1,0,1],
]
# 137
data=[
	[0,0,1],##1
	[0,1,1],##3
	[1,1,1],##7
]
# 123
data=[
	[0,0,1],##1
	[0,1,0],##2
	[0,1,1],##3
]
newData=[]
bits=3
count=len(data)
countChild=0
if count > 0:
	countChild=len(data[0])

print("Data size is: ", count)
print("Data subitem size is: ", countChild)

print("Data is: ", data)

alphas=string.ascii_lowercase
alphas=alphas[-3:] + alphas[0:-3]
alphas=alphas[0:countChild]
# alphas="xyz"
print("Alpha is :", alphas)
print("AlphaCount is :", len(alphas))
# print("AlphaIndex Search X is :", alphas.index("x"))
# print("AlphaIndex Search Y is :", alphas.index("y"))
# print("AlphaIndex Search Z is :", alphas.index("z"))

for x in range(1, count+1):
	print()
	for y in range(x+1, count+1):
		r=[]
		print(x, y)
		print(data[x-1], data[y-1])
		for z in range(countChild):
			r.append(-1)
			if data[x-1][z] == data[y-1][z]:
				r[z]=data[x-1][z]
			# print(z, data[x-1][z-1], data[y-1][z-1], r[z])
			# print(data[x-1][z-1], data[y-1][z-1], r[z])
		print("result: ", r)
		newData.append(r)

if newData == [] and count == 1:
	newData=data

print("Checked Data is: ", newData)

formula=[]
formulas=[]
clearformulas=[]

for x in range(len(newData)):
	g=[]
	for y in range(len(newData[0])):
		if newData[x][y] == 0:
			g.append(alphas[y] + "'")
		elif newData[x][y] == 1:
			g.append(alphas[y])
	formulas.append(g)
	if len(g) > 1:
		formula.append(g)
	if len(g) >= 1:
		clearformulas.append(g)

print("formula: ", formula)
print("all formula: ", formulas)
print("clear formula: ", clearformulas)

line_edges=[]
dashed_edges=[]

for x in range(len(clearformulas)):
	if len(clearformulas[x]) == 1:
		clearformulas[x].append(clearformulas[x][0])
	clearformulas[x]= ( clearformulas[x][0] , clearformulas[x][1])
	isDash=False
	selectedValue=clearformulas[x]
	for clearItem in clearformulas[x]:
		if clearItem.endswith("'"):
			isDash=True
			break
	if isDash:
		dashed_edges.append(selectedValue)
	else:
		line_edges.append(selectedValue)

print("Add bordertype to clearformulas: ", clearformulas)

# if len(line_edges) != 0:
# 	line_edges.append([line_edges[len(line_edges)-1][ len(line_edges[len(line_edges)-1]) -1], "1"])
# if len(dashed_edges) != 0:
# 	dashed_edges.append([dashed_edges[len(dashed_edges)-1][ len(dashed_edges[len(dashed_edges)-1]) -1], "1"])

print("line edges: ", line_edges)
print("dashed edges: ", dashed_edges)

def toChild(value):
	return value
	return alphas.index(value[0])
	# return int(ord(value))

grapsLine=[]
for i in range(len(line_edges)):
	if len(line_edges[i]) == 1:
		if len(line_edges) != 1:
			grapsLine.append((toChild(line_edges[i][0]), toChild(line_edges[i+1][0])))
		else:
			print("Error: cannot find a edges to connect to this single edge to create a vertex!")
	if len(line_edges[i]) == 2:
		grapsLine.append((toChild(line_edges[i][0][0]), toChild(line_edges[i][1][0])))

# grapsLine=[(1,2), (1,2)]
# grapsLine=[(1,2), (1,3), (1,4)]

print("grapsLine: ", grapsLine)

grapsDashed=[]
for i in range(len(dashed_edges)):
	if len(dashed_edges[i]) == 1:
		if len(dashed_edges) != 1:
			grapsDashed.append((toChild(dashed_edges[i][0][0]), toChild(dashed_edges[i+1][0][0])))
		else:
			print("Error: cannot find a edges to connect to this single edge to create a vertex!")
	if len(dashed_edges[i]) == 2:
		grapsDashed.append((toChild(dashed_edges[i][0][0]), toChild(dashed_edges[i][1][0])))

# dashed_edges=[(1,2), (1,2)]
# dashed_edges=[(1,2), (1,3), (1,4)]

print("grapsDashed: ", dashed_edges)

# use grapsLine
# use grapsDashed
