# Enter your code here. Read input from STDIN. Print output to STDOUT

def calcDist(u, v, graph):
    explored = []
    queue = [[u]]
     
    if u == v:
        return 0
     
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == v: 
                    return len(new_path) - 1
            explored.append(node)
 
    return -1
    

def kittyCalc(n, sets, edges):
   
    graph = { node: set() for node in range(1, n+1)}
    for edge in edges:
        
        graph[edge[1]].add(edge[0])
        graph[edge[0]].add(edge[1])
    # print(graph)
    dp = {}
    no_path = {}
    for query_set in sets:
        setCalc = 0

        for i in range(len(query_set)):
            for j in range(i+1, len(query_set)):
                start_node = query_set[i]
                end_node = query_set[j]
                
                if (start_node, end_node) in no_path or (end_node, start_node) in no_path:
                    continue
    
                
                if (start_node, end_node) in dp:
                    dist = dp[(start_node, end_node)]
                elif (end_node, start_node) in dp:
                    dist = dp[(end_node, start_node)]
                else:
                    dist = calcDist(start_node, end_node, graph)
                dp[(start_node,end_node)] = dist
                # print(f"dist between {start_node} and {end_node} = {dist}")
                if dist != -1:
                    setCalc += (start_node * end_node * dist)
                else:
                    no_path[(start_node, end_node)] = True
                    
        print(setCalc % (10**9 + 7))
        
        


if __name__ == "__main__":
    first_line = list(map(int, input().split()) )
    n_len, q_len = first_line[0], first_line[1]
    
    edges = [list(map(int, input().split())) for _ in range(n_len-1)]
    
    # print(edges)
    sets = []
    
    for i in range(q_len):
        set_len = list(map(int, input().split()))[0]
        sets.append(list(map(int, input().split())))
    
    calcs = kittyCalc(n_len, sets, edges)
