from array import *

num_nodes = 16
edges_str = '''
1 2
1 3
2 3
1 4
3 4
1 5
2 5
1 6
2 6
3 6
3 7
5 7
6 7
3 8
4 8
6 8
7 8
2 9
5 9
6 9
2 10
9 10
6 11
7 11
8 11
9 11
10 11
1 12
6 12
7 12
8 12
11 12
6 13
7 13
9 13
10 13
11 13
5 14
8 14
12 14
13 14
1 15
2 15
5 15
9 15
10 15
11 15
12 15
13 15
1 16
2 16
5 16
6 16
11 16
12 16
13 16
14 16
15 16
'''

# For Bonus: 
class Matrix:
   
    width = 0
    height = 0
    data = array('i')
    
    def __init__(self, width, height, data=None):
        self.width = width
        self.height = height
        gen = True
        if data:
            if len(data) != self.width * self.height:
                print("Data length is not width x height! Creating empty matrix instead.")
            elif not isinstance(data, array):
                print("Data is not an array! Creating empty matrix instead.")
            elif data.typecode != 'i':
                print("Data is not an integer array! Creating empty matrix instead.")
            else:
                self.data = data
                gen = False
        if gen:
            self.data = array('i', (0 for x in range(self.width*self.height)))

    """Starting with row 0 and column 0"""
    def set_data(self, i, r, c): 
        self.data[self.width*r + c] = i


    def __repr__(self):
        s = ""
        for h in range(self.height): 
            s = s + " ".join(str(i) for i in self.data[self.width*h:self.width*(h+1)]) + "\n"
        return s

# For Bonus:
def create_adj_matrix(edges, num_nodes):
    m = Matrix(num_nodes, num_nodes)
    for e in edges:
        m.set_data(1, e[0]-1, e[1]-1)
        m.set_data(1, e[1]-1, e[0]-1)

    return m


if __name__ == "__main__":
    print("Challenge 266")
    l1 = edges_str.split('\n')
    edges = []
    for l in l1:
        if l:
            p = l.split()
            edges.append([int(x) for x in p])
    print("\nEdges: \n{0} \n".format(edges))
    nodes = [0 for x in range(num_nodes+1)]
    for i in edges:
        nodes[i[0]] = nodes[i[0]]+1
        nodes[i[1]] = nodes[i[1]]+1
    nodes = nodes[1:]
    print("Degree: ")
    for i,n in enumerate(nodes): 
        print("Node {0} has a degree of {1}".format(i,n))

    # Bonus: 
    am = create_adj_matrix(edges, num_nodes)
    print("\nAdjacency Matrix: \n{0}\n".format(am))





