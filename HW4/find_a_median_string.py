def median_string_finder(k, dna):   # Simply calculate total distance of all possible motifs to dna segments and report the best one
    all_possible_motifs = make_all_4_to_k_possible_all_possible_motifss(k)
    minimum_dna_sequence = len(dna) 
    minimum_dna_sequence *= len(all_possible_motifs)
    distance_of_each_motif = {} # put total distance of eachpossible motif in a dictionary and report the min value in the end

    for i in all_possible_motifs:
        total_distance = 0
        for j in range(len(dna)):
            total_distance += hamming_distance_modified(i, dna[j])

        distance_of_each_motif[i] = total_distance

        if total_distance < minimum_dna_sequence:
            minimum_dna_sequence = total_distance

    for i in distance_of_each_motif.keys():
        if distance_of_each_motif[i] == minimum_dna_sequence:
            print(i)
            return

# I implemented the simple hamming distance finder in assignent 1, I modified it here, it calculates hamming distance  for every starting point and keeps the max values
def hamming_distance_modified(all_possible_motifs, dna_string):
    all_possible_starting_points = len(dna_string) - len(all_possible_motifs) + 1
    best_result = len(all_possible_motifs)
    for starting_index in range(all_possible_starting_points):
        distance = 0
        for j_th_element in range(len(all_possible_motifs)):
            if all_possible_motifs[j_th_element] != dna_string[starting_index:starting_index+len(all_possible_motifs)][j_th_element]:
                distance += 1
        if distance < best_result:
            best_result = distance
    return best_result

def make_all_4_to_k_possible_all_possible_motifss(k): # This function generates all possible k mers
    all_possible_all_possible_motifss = ['G', 'T', 'C', 'A']
    for _ in range(k-1):        # Starts from A, C, T, G and adds one of them to previous one to generate all posible 4^k combinations
        tmp_array = all_possible_all_possible_motifss
        all_possible_all_possible_motifss = []
        for i in tmp_array:
            for j in ['A', 'C', 'G', 'T']:
                all_possible_all_possible_motifss.append(i+j)
    return all_possible_all_possible_motifss

with open("/Users/ImanAlipour/Downloads/rosalind_ba2b.txt", "r") as file:
        k = int(file.readline().strip())
        dna_segments = [line.strip() for line in file]  # read input from input file

median_string_finder(k, dna_segments)