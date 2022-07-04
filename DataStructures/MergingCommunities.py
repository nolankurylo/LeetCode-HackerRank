# Enter your code here. Read input from STDIN. Print output to STDOUT

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.rank = 0
        self.size = 1


class DisJointSet():
    def __init__(self) -> None:
        pass

    def create_node(self, i):
        return Node(i)


    def find(self, node):
        if node != node.parent:

            node.parent = self.find(node.parent)
        return node.parent

    def mergeCommunities(self, node_a, node_b):
        # print(node_a.data, node_b.data)
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        if root_a != root_b:
            if root_a.rank > root_b.rank:
                root_b.parent = root_a
                root_a.size += root_b.size
            else:
                root_a.parent = root_b
                root_b.size += root_a.size
                if root_a.rank == root_b.rank:
                    root_b.rank += 1


if __name__ == "__main__":
    first_line = list(map(int, input().split()) )
    n_len, q_len = first_line[0], first_line[1]
    
    DJS = DisJointSet()
    communities = [DJS.create_node(i) for i in range(1, n_len+1)]
    
    
    for i in range(q_len):
        line = list(map(str, input().split()))
        command = line[0]
        inputs = list(map(int, line[1:]))
        # print(inputs, inputs[0]-1)
        
        if command == "M":
            DJS.mergeCommunities(communities[inputs[0]-1], communities[inputs[1]-1])
        elif command == "Q":
            print(DJS.find(communities[inputs[0]-1]).size)
            
    
