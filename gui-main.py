from builtins import range
import networkx as nx
import matplotlib.pyplot as plt
import graphviz
from tkinter import Tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import dash
from colour import Color
import wx
import wx.grid
from prettytable import PrettyTable
win=Tk()
win.title('گراف')
win.minsize(505,300)
win.maxsize(505,300)
#jadval
cols=['X','Y','Z','f']
data = [ ["0", "0", "0",""],
         ["0", "0", "1",""],
         ["0", "1", "0",""],
         ["0", "1", "1",""],
         ["1", "0", "0",""],
         ["1", "0", "1",""],
         ["1", "1", "0",""],
         ["1", "1", "1",""]
         ]
for y in range(len(data)+1):
    for x in range(len(cols)):
        if y==0:
            e=ttk.Entry(font=('Consolas 8 bold'),justify='center')
            e.grid(column=x, row=y)
            e.insert(0,cols[x])
        else:
            e=ttk.Entry()
            e.grid(column=x, row=y)
            e.insert(0,data[y-1][x])


def showgraph():
    G = nx.DiGraph()
    G.add_edges_from(
    [('Y ','X'),('Y','1 '),('Y','X'),('Y ','Z'),('Y ','Z '),('Z',' 1'),('Z ','1')
     ])

    val_map = {'X': 0.2,
               'Y': 0.1,
               'Z': 0.3}

    values = [val_map.get(node,0.25) for node in G.nodes()]
    # Specify the edges you want here
    line_edges = [('X', 'Y'),('Y','1 '),('Y ','Z'),('Z',' 1')]
    edge_colours = ['black' if not edge in line_edges else 'blue'
                for edge in G.edges()]
    dashed_edges = [('Y ','X'),('Y ','Z '),('Z ','1')]

    plt.figure(figsize=(3, 6))



    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, style='dashed')
    nx.draw_networkx_labels(G, pos,orient='vertical')
    nx.draw_networkx_edges(G, pos, edgelist=line_edges, edge_color='black', arrows=False)
    nx.draw_networkx_edges(G, pos, edgelist=dashed_edges,style='dashed', arrows=False)

    plt.show()
l=Label(win,text='مقادیر  را وارد کنید f:')
l.config(font="Mitra")
l.place(x=10,y=230)
e1=ttk.Entry(win)
e1.place(x=120,y=230)

def int_to_bin_list():
    x = int(e1.get())
    assert x >= 0
    if x == 0:
        return [[0]]
    binary = []
    while x != 0:
        temp = [0, 0, 0]
        for k in range(3):
            temp[k] = ((x % 10) //(2**(2-k))) % 2
        binary.append(temp.copy())
        x = x // 10
    binary.reverse()
    #mylist=binary
    for i in range(0, len(binary) - 1):
        for k in range(i + 1, len(binary)):
            print("comparing sublist {0} and {1} : ".format(i, k))
            tmp = []
            for j in range(0, len(binary[i])):
                if (binary[k][j] == binary[i][j]):
                    tmp.append(binary[k][j])
                else:
                    tmp.append(-1)
            print(tmp)
    print(binary)
    print(binary)

b1 = Button(win, text='نمایش دودویی', command=int_to_bin_list)
b1.config(font="Mitra")
b1.place(x=120,y=260)

b=ttk.Button(win,text='نمایش نمودار',command=showgraph)
#b.config(font="Mitra")
b.place(x=290,y=229)
win.mainloop()
