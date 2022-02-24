from helpers import create_weighted_adjacency_list

n,T = create_weighted_adjacency_list() 
print(n)
print(T)





# I implemented this code for previous problem and copied it here.
'''
def limb_length_calculator(distance_matrix, n_leaves, j_index):
    leaves = []
    for i in range(n_leaves):
        if i != j_index:
            leaves.append(i)    # Find the corresponding leaves.
    limb_length_amount = []
    for i_index in range(len(leaves) - 1):  # Now calculate the limb length by performing a for loop in for loop
        for k_index in range(i_index, len(leaves)):
            i = leaves[i_index]
            k = leaves[k_index]
            limb_length_amount.append((distance_matrix[i][j_index] + distance_matrix[j_index][k] - distance_matrix[i][k]) / 2)
    limb_length_calculator = min(limb_length_amount) # Min of these limb length is our result.
    return limb_length_calculator
'''
# Since previous code used an extra argument, I modified it to this new code, much simpler!
def limb_length_calculator(distance_matrix, j_index, n_leaves):
    leaves = []
    for i in range(n_leaves):
        if i != j_index:
            leaves.append(i)    # Find the corresponding leaves.

    limb_length_amount = []
    for i_index in range(len(leaves) - 1):  # Now calculate the limb length by performing a for loop in for loop
        for k_index in range(i_index, len(leaves)):
            i = leaves[i_index]
            k = leaves[k_index]
            limb_length_amount.append((distance_matrix[i][j_index] + distance_matrix[j_index][k] - distance_matrix[i][k]) / 2)
    limb_length_calculator = min(limb_length_amount) # Min of these limb length is our result.
    return limb_length_calculator
    
# Now I implement additive phylogeny algorithm
def additive_phylogeny_algorithm(distance_matrix, number_of_leaves, graph, int_node):
    if number_of_leaves == 2: # The base case where there are only 2 nodes
        graph.add_edge(0, 1, weight = distance_matrix[0][1])   # Make  graph with corresponding 2 nodes and one single edge
        return graph

    new_n = number_of_leaves - 1    # If we don't have the abse case, we reduce the problem to new_n-1 and recursively do this.
    limb_length_here = limb_length_calculator(distance_matrix, new_n, number_of_leaves)

    for j in range(new_n):
        distance_matrix[j][new_n] -= limb_length_here
        distance_matrix[new_n][j] = distance_matrix[j][new_n]

    leaves = [] # Same as what I did in calculating the limb_length
    for i in range(number_of_leaves):
        if i != new_n:
            leaves.append(i)    # Find the corresponding leaves.
    # For the begining set i and j to -1 and find them.
    selected_i_node = -1
    selected_k_node = -1
    print("Debug, " + str(selected_i_node))
    print("Debug, " + str(selected_k_node))
    for index_1 in range(len(leaves) - 1):
        i = leaves[index_1]
        for index_2 in range(index_1 + 1, len(leaves)):
            k = leaves[index_2]
            if distance_matrix[i][new_n] + distance_matrix[new_n][k] == distance_matrix[i][k]:  # This means that i, k and j are a degenerete triple, i.e k lies in path from i to j
                selected_i_node = i
                selected_k_node = k
    x = distance_matrix[selected_i_node][new_n]

    print("# Debug, x = " + str(x))
    del distance_matrix[-1] # Delete the added node to the tree from matrix
    for i in range(len(distance_matrix)):   # And delete all of it's corresponding lengths.
        del distance_matrix[i][-1]
    print("# debug, new distance matrix:")
    for i in distance_matrix:
        print(i)
    print("# end of debug")  
    while int_node in list(graph.nodes):
        int_node += 1
    recursive_matrix = additive_phylogeny_algorithm(distance_matrix, number_of_leaves - 1, graph, int_node)

    number_of_vertices = -1
    source_path = nx.shortest_path(recursive_matrix, source=selected_i_node, target=selected_k_node)    # Find shortest path between source to target in new matrix
    distance = 0
    for j in range(1, len(source_path) - 1):    # Now find j
        distance += recursive_matrix[source_path[j - 1]][source_path[j]]['weight']
        if distance == x:
            number_of_vertices = source_path[j]

    # Now we either add a new node as an inner node or add this node to current graph.
    if number_of_vertices == -1:
        number_of_vertices = int_node
        while number_of_vertices in list(recursive_matrix.nodes):
            number_of_vertices += 1
            print("Debug, number_of_vertices =  " + str(number_of_vertices))
        distance = 0
        j = 0
        while distance < x:
            j += 1
            pdist = distance
            distance += recursive_matrix[source_path[j - 1]][source_path[j]]['weight']
        recursive_matrix.remove_edge(source_path[j - 1], source_path[j])
        recursive_matrix.add_edge(number_of_vertices, source_path[j], weight=distance - x)
        recursive_matrix.add_edge(number_of_vertices, source_path[j - 1], weight=x - pdist)

    recursive_matrix.add_edge(number_of_vertices, new_n, weight=limb_length_here)   # Now add a new edge to our graph

    return recursive_matrix

new_n = int(input())    # Read new_n and j_index from input.
import networkx as nx
distance_matrix = []
for i in range(new_n):
    row = list(map(int, input().split()))   # This does no magic, it just reads a line like 1 2 3 3, splits it to 1, 2, 3, 3 and then combines them into [1, 2, 3, 3], since we have a new_n*new_n matrix, we perform this new_n times to read the whole distance matrix!
    distance_matrix.append(row)

graph = nx.Graph()  # Create an empty graph
result = additive_phylogeny_algorithm(distance_matrix, new_n, graph, new_n)
adj_dict = nx.to_dict_of_lists(result)  # Convert the result to a dictionary
result = []
for key, value in adj_dict.items():
    for val in value:
        temp = str(key) + '->' 
        temp += str(val) 
        temp += ':' 
        weight = result[key][val]['weight']
        temp += str(int(weight))
        result.append(temp)
result.sort()
for l in result:
    print(l)


temp = str(key) + '->' + str(val) + ':' + str(int(result[key][val]['weight']))