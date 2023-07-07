class Graph:
    def __init__(self,n,directed=True):#n=no of nodes
        self.nn = n#5
        self.m=range(self.nn)
        #define the type of a graph
        self.ndirected = directed
        #output is dictionary nodes as keys
        #adjacent vertices with weight
        #key is set bcoz no duplicates
        #bcoz it is directed graph
        self.adjlist={node:set() for node in self.m}
    def addedge(self,node1,node2,weight=1):
        self.adjlist[node1].add((node2,weight))
        if not self.ndirected:
            self.adjlist[node2].add((node1,weight))
    def printadilist(self):
        for key in self.adjlist.keys():
            print("node",key,":",self.adjlist[key])
g=Graph(5)
g.addedge(0,0,25)
g.addedge(0,1,5)
g.addedge(0,2,3)
g.addedge(1,3,1)
g.addedge(1,4,15)
g.addedge(4,3,11)
g.addedge(4,2,7)
g.printadilist()