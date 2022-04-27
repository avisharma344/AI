graph = {
  '5':['3','7'],
  '3':['2','4'],
  '4':['8'],
  '7':['8'],
  '8':[],
  '2':[]
}
v=[]

def dfs(v,graph,node):

  if node not in v:
    v.append(node)
    print("Visited: ",v,"\n")

  for n in graph[node]:
    dfs(v,graph,n)

print("DFS\n")
dfs(v,graph,'5')
