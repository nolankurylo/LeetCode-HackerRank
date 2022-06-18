def countPythagoreanTriplets(to_nodes, from_nodes, x, y, z) -> int:
    """ Finds the number of pythagorean triplets in a graph where distance from a node to nodes x,y,z
    satisfies: x^2 +y^2 = z^2
    :param to_nodes: edges
    :param from_nodes: edges
    :param x: node to find
    :param y: node to find
    :param z: node to find
    :return number of pythagorean triplets found
    """
    # Convert to adj list
    unique_nodes = list(set(to_nodes+from_nodes))
    graph = {node:[] for node in unique_nodes}

    for i in range(len(to_nodes)):
        to_node = to_nodes[i]
        from_node = from_nodes[i]

        graph[to_node].append(from_node)
        graph[from_node].append(to_node)


    # Perform BFS to determine shortest path to x,y,z for each node in the graph
    num_pythagorean_triplets = 0

    for node in graph:
        path_lens = BFS(node, graph, x, y, z)
        x_path_len = path_lens['x']
        y_path_len = path_lens['y']
        z_path_len = path_lens['z']

        print(f"Node: {node}, x_path_len: {x_path_len}, y_path_len: {y_path_len}, z_path_len: {z_path_len}")
        if x_path_len == -1 or y_path_len == -1 or z_path_len == -1:
            continue

        if x_path_len**2 + y_path_len**2 == z_path_len**2:
            num_pythagorean_triplets += 1

    return num_pythagorean_triplets

        

def BFS(start, graph, x, y, z) -> dict:
    """ Finds the shortests paths between current node start and each of x,y,z nodes
    :param start: current node to start search from
    :param graph: dict of unweighted bidirectional graph
    :param x: node to find
    :param y: node to find
    :param z: node to find
    :return dict containing shortest path lengths from node start to each of x,y,z
    """
    path_lens = {'x':-1, 'y':-1, 'z':-1}

    visited = []
    queue = [[start]]

    if start == x:
        path_lens['x'] = 0
    
    if start == y:
        path_lens['y'] = 0

    if start == z:
        path_lens['z'] = 0

    while queue:

        path = queue.pop(0)
        node = path[-1]

        if node not in visited:

            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                curr_path_len = len(new_path) - 1

                if neighbour == x and (curr_path_len < path_lens['x'] or path_lens['x'] == -1):
                    path_lens['x'] = curr_path_len

                if neighbour == y and (curr_path_len < path_lens['y'] or path_lens['y'] == -1):
                    path_lens['y'] = curr_path_len

                if neighbour == z and (curr_path_len < path_lens['z'] or path_lens['z'] == -1):
                    path_lens['z'] = curr_path_len
            visited.append(node)
    return path_lens






# Driver program to test above functions
if __name__=='__main__':
	
    to_nodes = [0,3,1,7,4,4,4,5,4,7]
    from_nodes = [1,0,2,3,3,7,6,6,5,6]
    x=3
    y=4
    z=6
    num_pythagorean_triplets = countPythagoreanTriplets(to_nodes, from_nodes, x, y, z)
    print(f"num_pythagorean_triplets: {num_pythagorean_triplets}")

	
