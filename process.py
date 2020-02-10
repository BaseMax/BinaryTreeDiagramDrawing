# Max Base
# https://github.com/BaseMax/PhdMathProject
import string
data=[
	# [0,0,1],
	# [0,1,0],
	[0,1,1],
	[1,0,0],
	# [1,0,1],
	# [1,1,0],
	# [1,1,1],
]
data2=[]
bits=3
count=len(data)
countChild=len(data[0])
isSingle=False

if len(data) == 1:
	isSingle=True
if isSingle:
	count=1

for x in range(1, count+1):
	begin=x+1
	if isSingle:
		begin=begin-1
	print(x, begin)
	for y in range(begin, count):
		r=[]
		print(countChild)
		for z in range(countChild):
			print(x,y,z,z)
			r.append(-1)
			print(data[x][z], data[y][z])
			if data[x][z] == data[y][z]:
				r[z]=data[x][z]
		data2.append(r)

print(data2)

alphas=string.ascii_lowercase
alphas="xyz"
formula=[]

for x in range(len(data2)):
	g=[]
	for y in range(len(data2[0])):
		if data2[x][y] == 0:
			g.append(alphas[y] + "'")
		elif data2[x][y] == 1:
			g.append(alphas[y])
	if len(g) > 1:
		formula.append(g)

print(formula)

result=[]
line_edges=[]
dashed_edges=[]

for x in range(len(formula)):
	formula[x].append(1)
	for y in range(bits):
		try:
			if formula[x][y][ len(formula[x][y]) -1] == "'":
				formula[x][ len(formula[x]) -1]=0
				break
		except IndexError:
			continue
	if formula[x][ len(formula[x]) -1] == 0:
		dashed_edges.append(formula[x][:-1])
	else:
		line_edges.append(formula[x][:-1])

print(formula)

if len(line_edges) != 0:
	line_edges.append([line_edges[len(line_edges)-1][ len(line_edges[len(line_edges)-1]) -1], "1"])
if len(dashed_edges) != 0:
	dashed_edges.append([dashed_edges[len(dashed_edges)-1][ len(dashed_edges[len(dashed_edges)-1]) -1], "1"])

print(line_edges)
print(dashed_edges)
