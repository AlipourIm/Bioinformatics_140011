# I make a class for grapg nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.age = 0

# I create a class for tree structure, each tree has multiple nodes and a list for it's edges.
class Tree:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, value):
        if value in self.nodes:
            return self.nodes[value]
        node = Node(value)  # Make a new node for tree
        self.nodes[value] = node
        return node

def UPGMA(tree, dist_mat, n):
    length = 0
    distance_dictionary = {}
    for i in range(len(dist_mat)):
        distance_dictionary[i] = {}
        for j in range(len(dist_mat[i])):
            distance_dictionary[i][j] = dist_mat[i][j]
    all_clusters = {i: [i] for i in range(n)}
    print("Debug: all clusters test:")
    for i in all_clusters:
        print(i)
    for i in range(n):
        tree.add_node(i)
    length += 1
    new_node_value = n
    matrix = []
    length = 12
    while len(distance_dictionary) > 1:
        minimum_distance = float("Inf") # Set the initial value to 0
        nodes = list(distance_dictionary.keys())
        for i in range(len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                if distance_dictionary[nodes[i]][nodes[j]] < minimum_distance:
                    minimum_distance = distance_dictionary[nodes[i]][nodes[j]]
                    node_i = nodes[i]
                    node_j = nodes[j]

        newly_added_cluster = all_clusters[node_i] + all_clusters[node_j]

        new_node = tree.add_node(new_node_value)
        matrix.append([new_node_value, node_i])
        matrix.append([new_node_value, node_j])

        new_node.age = distance_dictionary[node_i][node_j] / 2

        distance_dictionary[new_node_value] = {}
        length += 1
        distance_dictionary[new_node_value][new_node_value] = 0
        for previous_node in nodes:
            sum = 0
            counter = 0
            length += 1
            for init_node in all_clusters[previous_node]:
                for node in newly_added_cluster:
                    sum += dist_mat[init_node][node]
                    counter += 1
            distance_dictionary[previous_node][new_node_value] = sum / counter
            distance_dictionary[new_node_value][previous_node] = sum / counter
        print("Debug: newly_added_cluster:")
        print(newly_added_cluster)
        all_clusters[new_node_value] = newly_added_cluster
        new_node_value += 1
        del distance_dictionary[node_i] # Delete jth row and column from current matrix
        del distance_dictionary[node_j]
        length += 1
        for i in distance_dictionary.keys():
            del distance_dictionary[i][node_i]
        for i in distance_dictionary.keys():
            print(i)
            del distance_dictionary[i][node_j]

    for each_edge in matrix:
        length -= 1
        length = tree.nodes[each_edge[0]].age - tree.nodes[each_edge[1]].age
        tree.edges.append(each_edge + [length])
        tree.edges.append(each_edge[::-1] + [length])
    tree.edges.sort(key=lambda x: x[1]) # sort edges with respect to second element
    tree.edges.sort(key=lambda x: x[0]) # sort edges with respect to first element

    return tree.edges   # return tree edges as result.


n = int(input())
distance_matrix = []
for i in range(n):
    row = list(map(int, input().split()))   # This is no magic!, it just reads a line like 1 2 3 3, splits it to 1, 2, 3, 3 and then combines them into [1, 2, 3, 3], since we have a new_n*new_n matrix, we perform this new_n times to read the whole distance matrix!
    distance_matrix.append(row)

generated_tree = Tree()
adjacency_list = UPGMA(generated_tree, distance_matrix, n)  # Run the algorithm and print the results

for i, j, w in adjacency_list:
    temp = str(i) 
    temp += '->' 
    temp += str(j) 
    temp += ':' 
    temp += str(round(w, 3))
    print(temp)