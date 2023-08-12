#here graph is a dictionary with keys and multiple values
import heapq
graph = {
    'a':[(1,'b'),(3,'e')],
    'b':[(1,'a'),(2,'e'),(1,'d'),(4,'c')],
    'c':[(4,'b'),(1,'d')],
    'd':[(1,'b'),(2,'e'),(1,'c')],
    'e':[(3,'a'),(2,'b'),(2,'d')],
    }
def prims(graph,start):
    parents={}
    weights={}
    queue=[]
    visited=set()
    for vertex in graph:
        weights[vertex]=999
    weights[start]=0
    heapq.heappush(queue,(0,start))
    while len(queue)!=0:
        cur_weight ,cur_node=heapq.heappop(queue)
        if cur_node in visited:
            continue
        for weight ,node in graph[cur_node]:
            if node not in visited and weight < weights[node]:
                weights[node]=weight
                parents[node] =cur_node
                heapq.heappush(queue,(weight,node))
            visited.add(cur_node)
    print(weights)
prims(graph,'a')