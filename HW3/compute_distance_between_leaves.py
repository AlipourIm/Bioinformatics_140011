# I use a reccurcive function to evaluate this.
def distance_between_two_nodes(i_node,j_node,path_between_i_to_j=[]):
        if i_node==j_node:  
            return 0
        distance = float('inf')    # Set initial distance to infinite and reduce it...
        for node,weight in T[i_node]:
            if node==j_node:
                return weight
            if node in path_between_i_to_j:
                continue
            check_condition = weight + distance_between_two_nodes(node,j_node,path_between_i_to_j+[node])
            if check_condition < distance: # If new distance is smaller, update it!
                distance=check_condition
        return distance

def reccursive_distance_finder(n,T):
    distances = []
    for i_node in range(n):  # Create the initial n*n matrix filled up with zeroes "the hard way", there are multiple much neater and simpler codes for this! one way is with numpy, which is for some odd reason not allowed!
        distances.append([])
        for j_node in range(n):
            distances[i_node].append(0)

    for i_node in range(n):  # Now compute distances of each two elemetns with a for loop in for loop
        for j_node in range(n):
            distances[i_node][j_node] = distance_between_two_nodes(i_node,j_node)
    return distances

# I first read and process the input file, since I use os and some other libraries, I made a seperate code for that and put in the result here.
# The reason is one of the TAs in our forst assignment told us even usage of numpy is not possible, from then I seperated 
# reading inputs and processing them from logic of my code.
# The logic behind the reader code is simple, I read the first line for n, then I convert each line from 0->4:11 to form 0: [(4, 11)] in a python dictionary.
n = 32
T =  {0: [(35, 13)], 1: [(42, 15)], 2: [(53, 12)], 3: [(59, 13)], 4: [(48, 8)], 5: [(50, 13)], 6: [(32, 13)], 7: [(49, 9)], 8: [(51, 13)], 9: [(39, 14)], 10: [(47, 11)], 11: [(37, 14)], 12: [(34, 14)], 13: [(45, 12)], 14: [(57, 15)], 15: [(56, 12)], 16: [(60, 15)], 17: [(46, 5)], 18: [(33, 14)], 19: [(40, 8)], 20: [(55, 14)], 21: [(43, 11)], 22: [(32, 9)], 23: [(58, 5)], 24: [(38, 15)], 25: [(52, 12)], 26: [(36, 8)], 27: [(44, 5)], 28: [(61, 5)], 29: [(41, 9)], 30: [(54, 5)], 31: [(43, 6)], 32: [(22, 9), (33, 8), (6, 13)], 33: [(34, 13), (32, 8), (18, 14)], 34: [(35, 6), (12, 14), (33, 13)], 35: [(36, 9), (0, 13), (34, 6)], 36: [(35, 9), (37, 12), (26, 8)], 37: [(36, 12), (38, 14), (11, 14)], 38: [(39, 11), (24, 15), (37, 14)], 39: [(9, 14), (38, 11), (40, 5)], 40: [(41, 8), (19, 8), (39, 5)], 41: [(42, 14), (29, 9), (40, 8)], 42: [(1, 15), (41, 14), (44, 14)], 43: [(21, 11), (31, 6), (45, 10)], 44: [(42, 14), (48, 14), (27, 5)], 45: [(13, 12), (46, 9), (43, 10)], 46: [(17, 5), (47, 13), (45, 9)], 47: [(54, 15), (10, 11), (46, 13)], 48: [(44, 14), (4, 8), (49, 9)], 49: [(50, 5), (48, 9), (7, 9)], 50: [(5, 13), (51, 14), (49, 5)], 51: [(8, 13), (52, 9), (50, 14)], 52: [(53, 6), (25, 12), (51, 9)], 53: [(2, 12), (55, 14), (52, 6)], 54: [(30, 5), (47, 15), (56, 8)], 55: [(20, 14), (58, 9), (53, 14)], 56: [(57, 6), (15, 12), (54, 8)], 57: [(60, 9), (14, 15), (56, 6)], 58: [(23, 5), (55, 9), (59, 6)], 59: [(58, 6), (61, 5), (3, 13)], 60: [(57, 9), (16, 15), (61, 5)], 61: [(60, 5), (28, 5), (59, 5)]}
distances = reccursive_distance_finder(n,T)
for row in distances:
    for item in row:
        print(str(item) + ' ', end = '')
    print() # For the final \n of end of each line