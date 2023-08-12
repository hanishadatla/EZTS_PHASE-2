def krushkals(graph):
    edge_list=[]
    for source in graph:
        for edge in graph[source]:
            weight,dest=edge
            edge_list.append((weight,source,dest))
    edge_list.sort()
    print(*edge_list,sep='\n')
    parents={}
    for vertex in graph:
        parents[vertex]=vertex
    print(parents)
    mst=[]
    def find_parent(vertex):
        if parents[vertex] != vertex:
            parents[vertex]=find_parent(parents[vertex])
        return parents[vertex]
    for edge in edge_list:
        weight,source,dest=edge
        if find_parent(source)!=find_parent(dest):
            mst.append(edge)
            parents[find_parent(source)]=find_parent(dest)
    return mst
graph={'a':[(10,'f'),(28,'b')],
       'b':[(14,'g'),(16,'c'),(28,'b')],
       'c':[(12,'d'),(16,'b')],
       'd':[(12,'c'),(18,'g'),(22,'e')],
       'f':[(25,'e'),(10,'a')],
       'e':[(22,'e'),(24,'g'),(25,'f')],
       'g':[(14,'b'),(18,'d'),(24,'e')]}
mst=krushkals(graph)
print(mst)