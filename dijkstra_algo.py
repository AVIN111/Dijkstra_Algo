class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def routetable(self, dist, prev):
        print("for node ")

        print("Vertex \tDistance\tprevious")
        for node in range(self.V):
            print(node, "\t", dist[node], "\t\t", prev[node])

    def node(self, dist, sptSet):

        min = float('inf')

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def path(self, src):

        dist = [float('inf')] * self.V
        prev = [0] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.node(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    prev[v] = u

        self.routetable(dist, prev)


g = Graph(6)
g.graph = [[0, 4, 2, 0, 0, 0],
           [4, 0, 1, 5, 0, 0],
           [2, 1, 0, 8, 10, 0],
           [0, 5, 8, 0, 2, 6],
           [0, 0, 10, 2, 0, 3],
           [0, 0, 0, 6, 3, 0]
           ]
for node in range(6):
    g.path(node)
