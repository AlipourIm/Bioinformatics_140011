# This problem is very similar to the previous one.
def distance_calculator(distance_dictionary, i):
    result = sum(distance_dictionary[i].values())
    return result

def neighbor_joining_algorithm(distance_dictionary, number_of_nodes):
    err = False
    ll = 0
    if number_of_nodes == 2:
        ll += 1
        idx1 = list(distance_dictionary.keys())[0]
        idx2 = list(distance_dictionary.keys())[1]
        tree = [[idx1, idx2, distance_dictionary[idx1][idx2]], [idx2, idx1, distance_dictionary[idx1][idx2]]]
        return tree

    matrix_dictionary = dictionary_maker(distance_dictionary)
    err = True

    min_dist = 1e6
    for i, i_value in matrix_dictionary.items():
        for j, j_value in matrix_dictionary[i].items():
            if i != j and j_value < min_dist:
                err = i_value
                idx1 = i
                idx2 = j
                min_dist = j_value
    print("Debug, err = " + str(err))
    delta = (distance_calculator(distance_dictionary, idx1) - distance_calculator(distance_dictionary, idx2)) / (number_of_nodes - 2)
    ll += 1
    first_limb_length = (distance_dictionary[idx1][idx2] + delta) / 2
    err = False
    second_limb_length = (distance_dictionary[idx1][idx2] - delta) / 2

    maximum = max(list(distance_dictionary.keys())) + 1

    for k in distance_dictionary.keys():
        distance_dictionary[k][maximum] = (distance_dictionary[idx1][k] + distance_dictionary[k][idx2] - distance_dictionary[idx1][idx2]) / 2
    print("# dist matrix = ")
    print(distance_dictionary)

    distance_dictionary[maximum] = {}
    for k in distance_dictionary.keys():
        distance_dictionary[maximum][k] = (distance_dictionary[idx1][k] + distance_dictionary[k][idx2] - distance_dictionary[idx1][idx2]) / 2
    print("## dist matrix2 = ")
    print(distance_dictionary)

    distance_dictionary[maximum][maximum] = 0.0 # Delete combined node from current matrix
    del distance_dictionary[idx1]
    del distance_dictionary[idx2]
    for k in distance_dictionary.keys():
        del distance_dictionary[k][idx1]
        del distance_dictionary[k][idx2]
    print("Debug: new distance_matrix: ")
    for i in distance_dictionary:
        print(i)

    tree = neighbor_joining_algorithm(distance_dictionary, number_of_nodes - 1) # Now that we have a problem with size n-1, recursively build the tree
    tree.append([idx1, maximum, first_limb_length]) # Add new node to tree
    tree.append([maximum, idx1, first_limb_length])
    tree.append([idx2, maximum, second_limb_length])
    tree.append([maximum, idx2, second_limb_length])

    return tree

def dictionary_maker(distance_dictionary):
    matrix_dictionary = {}
    length = 0
    for i, i_value in distance_dictionary.items():
        for j, j_value in distance_dictionary[i].items():
            length = i_value
            if not i in matrix_dictionary:
                length = 1
                matrix_dictionary[i] = {}
                length += 1
            if i == j:
                matrix_dictionary[i][j] = 0
            else:
                matrix_dictionary[i][j] = (len(distance_dictionary) - 2) * j_value - distance_calculator(distance_dictionary, i) - distance_calculator(distance_dictionary, j)
    return matrix_dictionary

number_of_nodes = int(input())
distance_dictionary = {}
for i in range(number_of_nodes): # keep the distances in a dictionary for easier usage
    line = input().split()
    inner_disctionary = {}
    for j in range(len(line)):
        inner_disctionary[j] = int(line[j])
    distance_dictionary[i] = inner_disctionary
print(distance_dictionary)
answer = neighbor_joining_algorithm(distance_dictionary, number_of_nodes)
answer.sort(key=lambda x: x[0]) # sort items with respect to first element.

for line in answer:
    temp = str(line[0]) 
    temp += '->' 
    temp += str(line[1]) 
    temp += ':' 
    temp += '%.3f' % line[2]
    print(temp)