n = int(input())    # Read n and j_index from input.
j_index = int(input())
distance_matrix = []
for i in range(n):
    row = list(map(int, input().split()))   # This is no magic!, it just reads a line like 1 2 3 3, splits it to 1, 2, 3, 3 and then combines them into [1, 2, 3, 3], since we have a n*n matrix, we perform this n times to read the whole distance matrix!
    distance_matrix.append(row)

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
    limb_length = min(limb_length_amount) # Min of these limb length is our answer.
    return limb_length

print(int(limb_length_calculator(distance_matrix, n, j_index))) # I use int() to perform the 0-based indexing.