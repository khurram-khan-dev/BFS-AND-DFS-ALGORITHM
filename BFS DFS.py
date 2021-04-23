graph = {'A': ['B', 'D' ],
         'B': ['C', 'E'],
         'C': [],
         'D': ['E','G','H'],
         'E': ['C', 'F'],
         'F': [],
         'G': ['H'],
         'H': []}
def bfs_connected_component(graph, start):
    
    explored = []
    
    queue = [start]

def bfs_connected_component(graph, start):
    
    explored = []
    
    queue = [start]
 
    
    while queue:
        
        node = queue.pop(0)
        if node not in explored:
            
            explored.append(node)
            neighbours = graph[node]
 
           
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
 
bfs_connected_component(graph,'A') 


def bfs_shortest_path(graph, start, goal):
   
    explored = []
    
    queue = [[start]]
 
   
    if start == goal:
        return "That was easy! Start = goal"
 

    while queue:
    
        path = queue.pop(0)
     
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
           
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
              
                if neighbour == goal:
                    return new_path
 
        
            explored.append(node)
 

    return "doesn't exist "

print("BFS",bfs_shortest_path(graph, 'A', 'C'))
def dfs_path(graph,start,end):
    result = []
    dfs(graph,start,end,[],result)
    return result

def dfs(graph,start,end,path,result):
    path+=[start]
    if start == end:
        result.append(path)
    else:
        for node in graph[start]:
            if node not in path:
                dfs(graph,node,end,path[:],result)
print("DFS",dfs_path(graph,'A','C')) 
