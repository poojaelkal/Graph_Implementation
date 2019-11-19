import time
filename = 'input1.txt'

#read the given input file
def read_input(filename):

    file = open(filename)
    line = file.readlines()
    content = [l.strip('\n').split() for l in line]
    edges = []
    weights = []
    unsorted_edges = []
    vertices = set()
    n = len(content) - 1
    if len(content[n]) != 1:
        for i in range(len(content)):
            if i == 0:
                V = content[i][0]  # No of vertices
                e = content[i][1]  # No of edges
                direct = content[i][2]

            else:
                unsorted_edges.append([content[i][0],content[i][1],int(content[i][2])])

    else:
        for i in range(len(content) - 1):
            if i == 0:
                V = content[i][0]  # No of vertices
                e = content[i][1]  # No of edges
                direct = content[i][2]

            else:
                unsorted_edges.append([content[i][0], content[i][1], int(content[i][2])])
                # unsorted_edges.append(content[i])
    # for i in unsorted_edges:

    unsorted_edges = sorted(unsorted_edges, key=lambda e: e[2]) #sort the edges based on its weights

    for edge in unsorted_edges:

        edges.append([edge[0], edge[1]])
        weights.append(int(edge[2]))
        vertices.add(edge[0])
        vertices.add(edge[1])

    vert = list(vertices)
    print("Edges = ",edges)
    print("Weights = ",weights)
    return vert, edges, weights


class weightedGraphRank:
    edges = []
    vertices = []
    weights = []
    vertex_set = {}
    rank = {}

    def __init__(self, vertices, edges, weights):
        self.edges = edges
        self.vertices = vertices
        self.weights = weights

    def print(self):
        print("Graph Edges: ", self.edges)
        print("Graph vertices: ", self.vertices)
        print("Graph weights: ", self.weights)
        print("Graph vertex_set: {}".format(self.vertex_set))

#make set of the vertices
    def makeSet(self):
        for i in range(len(self.vertices)):
            tmp = [self.vertices[i]]
            self.vertex_set[i] = tmp
            self.rank[i] = 0

#find the set of the vertices
    def findSet(self, vertex):
        for k in self.vertex_set.keys():
            for v in self.vertex_set[k]:
                if v == vertex:
                    return k
        return -1

#union the two vertices if its in two different sets
    def UnionSet(self, u, v):

        # key_add = self.findSet(u)
        # key_remove = self.findSet(v)
        key_u = self.findSet(u)
        key_v = self.findSet(v)
        rank_u = self.rank[key_u]
        rank_v = self.rank[key_v]

        # tmp_list = []
        if rank_u > rank_v:
            tmp_list = self.vertex_set[key_v]
            self.vertex_set[key_v] = []
            self.vertex_set[key_u].extend(tmp_list)

        else:
            tmp_list = self.vertex_set[key_u]
            self.vertex_set[key_u] = []
            self.vertex_set[key_v].extend(tmp_list)

            if rank_u == rank_v:
                rank_v = rank_v + 1
                self.rank[key_v] = rank_v

#kruskal algorithm implementation
    def MST_Kruskal(self):
        result = []
        result_weights = []
        cost = 0
        self.makeSet()

        index = 0
        print("Minimum Spanning Tree:")
        for edge in self.edges:
            if self.findSet(edge[0]) != self.findSet(edge[1]):
                print("edge: ", edge, "- and its weight: ", self.weights[index])
                result.append(edge)
                result_weights.append(self.weights[index])

                cost = cost + int(self.weights[index])
                self.UnionSet(edge[0], edge[1])
            index = index + 1
        print("Total cost of the tree = ", cost)

    #         return result, result_weights, cost





v, e, w = read_input(filename)
start_time = time.process_time()
G = weightedGraphRank(v, e, w)
G.MST_Kruskal()
end_time = time.process_time()
total_run_time = 1000*(end_time - start_time)
print("run time = ", total_run_time)

