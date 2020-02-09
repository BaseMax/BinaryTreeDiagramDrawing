# Max Base
# https://github.com/BaseMax/PhdMathProject
import string
data=[
	[0,0,1],
	[0,1,1],
	[0,1,0],
	[0,1,0],
]
print(data);
data2=[]
for x in range(len(data)-1):
	for y in range(x+1, len(data)):
		r=[]
		for z in range(len(data[0])):
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
		#print(x,y)
	if len(g) > 1:
		formula.append(g)
print(formula)

line_edges=[]
dashed_edges=[]
for x in range(len(formula)):
	formula[x].append(1)
	for y in range(len(formula)):
		if formula[x][y][ len(formula[x][y]) -1] == "'":
			formula[x][ len(formula[x]) -1]=0
			break
	if formula[x][ len(formula[x]) -1] == 0:
		dashed_edges.append(formula[x][:-1])
	else:
		line_edges.append(formula[x][:-1])

print(formula)
print("")
print(line_edges)
print(dashed_edges)

if len(line_edges) != 0:
	line_edges.append([line_edges[len(line_edges)-1][ len(line_edges[len(line_edges)-1]) -1], "1"])
if len(dashed_edges) != 0:
	dashed_edges.append([dashed_edges[len(dashed_edges)-1][ len(dashed_edges[len(dashed_edges)-1]) -1], "1"])
# dashed_edges.append()

print(line_edges)
print(dashed_edges)
