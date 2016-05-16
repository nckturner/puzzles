from queue import Queue

instr = '''10 2
28 2
2 10
2 4
2 29
2 15
23 24
23 29
15 29
15 14
15 34
7 4
7 24
14 2
14 7
14 29
14 11
14 9
14 15
34 15
34 14
34 29
34 24
34 11
34 33
34 20
29 23
29 7
29 2
29 18
29 27
29 4
29 13
29 24
29 11
29 20
29 9
29 34
29 14
29 15
18 27
18 13
18 11
18 29
27 18
27 4
27 24
4 2
4 27
4 13
4 35
4 24
4 20
4 29
13 18
13 16
13 30
13 20
13 29
13 4
13 2
24 4
24 30
24 5
24 19
24 21
24 20
24 11
24 29
24 7
11 18
11 24
11 30
11 33
11 20
11 34
11 14
20 29
20 11
20 4
20 24
20 13
20 33
20 21
20 26
20 22
20 34
22 34
22 11
22 20
9 29
9 20
21 9
21 20
21 19
21 6
33 24
33 35
33 20
33 34
33 14
33 11
35 33
35 4
35 30
35 16
35 19
35 12
35 26
30 13
30 19
30 35
30 11
30 24
16 36
16 19
16 35
16 13
36 16
31 16
31 19
5 19
19 30
19 16
19 5
19 35
19 33
19 24
12 33
12 35
12 3
12 26
26 21
26 35
6 21
6 19
1 6
8 3
8 6
3 8
3 6
3 12
3 35
33 29
29 33
14 33
29 21'''

def find_shortest_path(src, dest, conns):
    q = Queue()
    q.put(src)
    visited = {}
    # visited contains each visited node with a parent and a distance from src
    visited[src] = {"parent": None, "dist": 0}
    distance = -1
    while not q.empty():
        i = q.get()
        if i == dest: 
            distance = visited[i]["dist"]
            break
        for c in conns[i]:
            if c not in [x for x in visited.keys()]:
                q.put(c)
                visited[c] = {"parent": i, "dist": visited[i]["dist"]+1}
    return distance

def eccentricity(v, n, conns): 
    '''Eccentricity of vertex v is the greatest distance in the graph G from v to any other node.  
    N is total number of vertexes in the graph.'''
    maximum = 0
    for i in range(1,n+1):
        d = find_shortest_path(v, i, conns)
        if d > maximum:
            maximum = d
    return maximum

def radius(n, conns):
    '''Radius is the smallest eccentricity of any vertex in a graph.'''
    minimum = None
    for i in range(1,n+1):
        e = eccentricity(i, n, conns)
        if not minimum:
            minimum = e
        elif e < minimum:
            minimum = e
    return minimum
        
def diameter(n, conns): 
    '''Diameter is the largest eccentricity of any vertex in a graph.'''
    maximum = 0
    for i in range(1,n+1):
        e = eccentricity(i, n, conns)
        if e > maximum:
            maximum = e
    return maximum

def find_max_vertex(edges):
    max = 0
    for e in edges: 
        if e[0] > max:
            max = e[0]
        if e[1] > max: 
            max = e[1]
    return max

def create_connections_list(edges, n):
    conns = [[] for i in range(n+1)]
    for e in edges:
        # e[0] is source, e[1] is destination in edge
        conns[e[0]].append(e[1])
    return conns

if __name__ == "__main__":
    l1 = instr.split('\n')
    l2 = [s.split(' ') for s in l1] 
    edges = [[int(x[0]),int(x[1])] for x in l2]
    print("Edges: ",edges)

    n = find_max_vertex(edges)

    conns = create_connections_list(edges, n)
    print("Connections: ",conns)

    radius = radius(n, conns)
    diameter = diameter(n, conns)

    print("Radius: {0}\nDiameter: {1}".format(radius, diameter))

