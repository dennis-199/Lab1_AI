# LAB 1 GROUP ASSIGNMENT
# GROUP MEMBERS
# 123014 Dennis Ochieng Otieno

graph=[['J', 'K', 146],
       ['J', 'I', 172],
       ['J', 'E', 105],
       ['K', 'L', 152],
       ['K', 'E', 146],
       ['L', '0', 97],
       ['O', 'M', 100],
       ['M', 'N', 67],
       ['E', 'L', 110],
       ['E', 'A', 133],
       ['A', 'O', 151],
       ['A', 'D', 43],
       ['D', 'O', 136],
       ['D', 'M', 200],
       ['D', 'F', 111],
       ['F', 'G', 88],
       ['F', 'H', 130],
       ['G', 'H', 99],
       ['H', 'N', 80],
       ['I', 'A', 109],
       ['I', 'C', 102],
       ['C', 'D', 126],
       ['C', 'B', 171],
       ['B', 'G', 171],
       ['G', 'C', 140],
       ['G', 'D', 123]


]
temp = []
temp1 = []
for i in graph:
  temp.append(i[0])
  temp1.append(i[1])
nodes = set(temp).union(set(temp1))
def UCS(graph, costs, open, closed, cur_node):
  if cur_node in open:
    open.remove(cur_node)
  closed.add(cur_node)
  for i in graph:
    if(i[0] == cur_node and costs[i[0]]+i[2] < costs[i[1]]):
      open.add(i[1])
      costs[i[1]] = costs[i[0]]+i[2]
      path[i[1]] = path[i[0]] + ' -> ' + i[1]
  costs[cur_node] = 999999
  small = min(costs, key=costs.get)
  if small not in closed:
    UCS(graph, costs, open,closed, small)
costs = dict()
temp_cost = dict()
path = dict()
for i in nodes:
  costs[i] = 999999
  path[i] = ' '
open = set()
closed = set()
start_node = input("Enter the Start State: ")
open.add(start_node)
path[start_node] = start_node
costs[start_node] = 0
UCS(graph, costs, open, closed, start_node)
goal_node = input("Enter the Goal State: ")
print("UNIFORM COST SEARCH \nPath with least cost is: ",path[goal_node])

