import os
import matplotlib.pyplot as plt
import networkx as nx

os.chdir('C:\\Users\\Swetha\\Desktop')

G = nx.DiGraph()

data = {}
total_durations = []

def single_source_path(graph,source):
    seen = {}
    level = 0
    nextlevel = {source:1}
    weight = []
    weight_int = []
    while nextlevel:
        thislevel = nextlevel
        nextlevel = {}
        for v in thislevel:
            if v not in seen:
                seen[v]=level
                nextlevel.update(graph[v])
                for node,value in nextlevel.items():
                    weight += [v for k,v in value.iteritems()]
    weight_int += list(map(int,weight))
    return sum(weight_int)

def get_duration_data(filename):
    global data
    global total_durations
    
    with open(filename) as f:
        temp = f.readlines()
    data = [line.strip().split(',') for line in temp]
    tasks = {x:(k,v) for x,k,v in data}
    
    for keys,values in tasks.iteritems():
        G.add_node(keys)
        G.add_edge(keys,values[1],weight=values[0])

    #nx.draw(G,with_labels = True)
    #plt.show()
   
    total_durations += (single_source_path(G,n) for n in G)
    print('The Total Duration to Complete the Task based on dependency is: '+str(max(total_durations)) +' days')
    
    
