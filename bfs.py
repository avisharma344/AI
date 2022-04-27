graph = {
  '5':['3','7'],
  '3':['2','4'],
  '4':['8'],
  '7':['8'],
  '8':[],
  '2':[]
}

visited = []
queue = []
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)

    print("visited: ",visited)
    print("queue: ",queue,"\n")

    for n in graph[m]:
      if n not in visited:
        visited.append(n)
        queue.append(n)

print("Following is the Breadth-First Search")
bfs(visited, graph, '5')
