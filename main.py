     # AI LAB WORK
     #GROUP MEMBERS
#120627 Shelmith Nyagoha
#123014 Dennis Ochieng
#122566 Daphne Wambugu
#123946 Ngethe Cynthia
#119215 Stephen Mungai
#122278 Felix Orengo

from collections import defaultdict
from queue import PriorityQueue


# 1. Uniform Cost Search
class Graph:
    def __init__(self, directed):
        # Parametrized constructor of class Graph which takes True if Graph is directed otherwise False
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        # edges added between two nodes along with weight as Algorithm is of UCS
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        # It takes starting node and goal node as parameters then it returns a path using UCS Algorithm
        visited = []
        queue = PriorityQueue()
        queue.put((0, current_node))

        while not queue.empty():
            item = queue.get()
            current_node = item[1]

            if current_node == goal_node:
                print(current_node, end=" ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue

                print(current_node, end=" -> ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                    queue.put((neighbour[0], neighbour[1]))


g = Graph(False)
g.add_edge("J", "K", 146)
g.add_edge("J", "E", 105)
g.add_edge("J", "I", 172)
g.add_edge("K", "E", 146)
g.add_edge("K", "L", 152)
g.add_edge("E", "A", 133)
g.add_edge("E", "L", 110)
g.add_edge("L", "O", 97)
g.add_edge("A", "O", 151)
g.add_edge("A", "D", 43)
g.add_edge("O", "M", 100)
g.add_edge("D", "M", 200)
g.add_edge("D", "F", 111)
g.add_edge("D", "O", 136)
g.add_edge("M", "N", 67)
g.add_edge("F", "H", 130)
g.add_edge("F", "G", 88)
g.add_edge("G", "H", 99)
g.add_edge("G", "D", 123)
g.add_edge("G", "C", 140)
g.add_edge("B", "G", 171)
g.add_edge("C", "D", 126)
g.add_edge("C", "B", 171)
g.add_edge("I", "C", 102)
g.add_edge("I", "A", 109)

# g.graph
print("1. Uniform Cost Search:\t ", end=" ")
g.ucs('J', 'N')

# 2. IDDFS Search
adjacency_list = {
    'A': ['O', 'D'],
    'B': ['G'],
    'C': ['D', 'B'],
    'D': ['O', 'M', 'F'],
    'E': ['A', 'L'],
    'F': ['G', 'H'],
    'G': ['C', 'D', 'H'],
    'H': ['N'],
    'I': ['C', 'A'],
    'J': ['I', 'E', 'K'],
    'K': ['E', 'L'],
    'L': ['O'],
    'M': ['N'],
    'N': [],
    'O': ['M'],
}
path = list()


def DFS(currentNode, destination, graph, maxDepth, curList):
    curList.append(currentNode)
    if currentNode == destination:
        return True
    if maxDepth <= 0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node, destination, graph, maxDepth - 1, curList):
            return True
        else:
            curList.pop()
    return False


def iterativeDDFS(currentNode, destination, graph, maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode, destination, graph, i, curList):
            return True
    return False


if not iterativeDDFS('J', 'N', adjacency_list, 10):  # limit- 10
    print("Path is not available")
else:
    print()
    print("2. IDDFS:\t\t\t\t", path.pop())


# 3. A-Star Search
def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}

    g[start_node] = 0
    # start_node is root node
    # start_node is set to its own parent node
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        # node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # nodes m not in first and last set are added to first
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight


                # for each node m,compare its distance from start
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('This path does not exist!')
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('3. A* Algorithm:\t\t {}'.format(path))
            return path

        # adding n to closed_list and remove from open_list
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
    H_dist = {
        'A': 221,
        'B': 350,
        'C': 400,
        'D': 326,
        'E': 500,
        'F': 209,
        'G': 188,
        'H': 92,
        'I': 499,
        'J': 621,
        'K': 668,
        'L': 300,
        'M': 78,
        'N': 0,
        'O': 170,
    }

    return H_dist[n]


Graph_nodes = {
    'A': [('O', 151), ('D', 43)],
    'B': [('G', 171)],
    'C': [('D', 126), ('B', 171)],
    'D': [('O', 136), ('M', 200), ('F', 111)],
    'E': [('A', 133), ('L', 110)],
    'F': [('G', 88), ('H', 130)],
    'G': [('C', 140), ('D', 123), ('H', 99)],
    'H': [('N', 80)],
    'I': [('C', 102), ('A', 109)],
    'J': [('I', 172), ('E', 105), ('K', 146)],
    'K': [('E', 146), ('L', 152)],
    'L': [('O', 97)],
    'M': [('N', 67)],
    'N': None,
    'O': [('M', 100)],
}
aStarAlgo('J', 'N')

# 4. Depth First Search
adjacency_list = {
    'A': ['O', 'D'],
    'B': ['G'],
    'C': ['D', 'B'],
    'D': ['O', 'M', 'F'],
    'E': ['A', 'L'],
    'F': ['G', 'H'],
    'G': ['C', 'D', 'H'],
    'H': ['N'],
    'I': ['C', 'A'],
    'J': ['I', 'E', 'K'],
    'K': ['E', 'L'],
    'L': ['O'],
    'M': ['N'],
    'N': [],
    'O': ['M'],
}


def bfs(graph, start, finish):
    queue = [[start]]
    visited = set()

    while queue:
        track = queue.pop(0)
        state = track[-1]
        if state == finish:
            return track
        elif state not in visited:

            for branch in graph.get(state, []):
                if branch not in visited:
                    track_new = list(track)
                    track_new.append(branch)
                    queue.append(track_new)

            visited.add(state)


print("4. Depth First Search : ", bfs(adjacency_list, 'J','N'))

