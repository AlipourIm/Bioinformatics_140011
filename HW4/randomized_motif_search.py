import random
# I read our book about this specific problem, I also used these links:
'''


https://www.bioinformaticsalgorithms.org/bioinformatics-chapter-2
https://www.youtube.com/watch?v=R5DVi25kqAY
https://www.coursera.org/lecture/dna-analysis/how-rolling-dice-helps-us-find-regulatory-motifs-part-1-12-43-DxbJn
https://www.coursera.org/lecture/bioinformatics/optional-how-rolling-dice-helps-us-find-regulatory-motifs-part-2-05-37-DwJGf
https://www.coursera.org/lecture/bioinformatics/optional-how-rolling-dice-helps-us-find-regulatory-motifs-part-1-12-43-AYObU
'''

import random

def randomized_motif_search_algorithm(dna,k,t):
    motifs = select_a_random_k_mer(dna,k)
    best_motif = motifs
    while True:
        matrix = make_profile(motifs)
        motifs = []
        for i in range(t):
            motifs.append(profile_maker(dna[i],k,matrix))
        if calculate_score(motifs) < calculate_score(best_motif):
            best_motif = motifs
        else:
            return best_motif

def make_profile(motifs):
    dictionary = {}
    n = float(len(motifs))
    motifs_zipped = list(zip(*motifs))
    for i in range(len(motifs_zipped)):
        dictionary.setdefault('A', []).append((motifs_zipped[i].count('A')+1)/n/2)
        dictionary.setdefault('C', []).append((motifs_zipped[i].count('C')+1)/n/2)
        dictionary.setdefault('G', []).append((motifs_zipped[i].count('G')+1)/n/2)
        dictionary.setdefault('T', []).append((motifs_zipped[i].count('T')+1)/n/2)
    return dictionary

def profile_maker(string, k , matrix):
    maximum_point = None
    k_mer_to_be_reported = None
    for i in range(len(string)-k+1):
        k_mer = string[i:i+k]
        points_here = 1
        for j in range(k):
            point_here = matrix[k_mer[j]][j]
            points_here *=point_here
        if maximum_point == None or points_here > maximum_point:
            maximum_point = points_here
            k_mer_to_be_reported = k_mer
    return k_mer_to_be_reported

def calculate_score(motifs):
    motifs_zipped = zip(*motifs)
    found_score = 0
    for motif_loop in motifs_zipped:
        calculate_score = len(motif_loop) - max([motif_loop.count('A'), motif_loop.count('C'), motif_loop.count('G'), motif_loop.count('T')])
        found_score += calculate_score
    return found_score

def select_a_random_k_mer(dna,k):
    motifs = []
    for dna_seq in dna:
        position = random.randrange(0,len(dna[0])-k+1)
        motifs.append(dna_seq[position:position+k])
    return motifs

def run_algorithm(dna,k,t,times):
    best_motifs = []
    max_score = None
    for i in range(int(times)):
        tmp_motifs = randomized_motif_search_algorithm(dna, k, t)
        tempscore = calculate_score(tmp_motifs)
        if max_score == None or max_score > tempscore:
            max_score = tempscore
            best_motifs = tmp_motifs
    return best_motifs

with open('/Users/ImanAlipour/Downloads/rosalind_ba2f.txt') as input_file:
    k,t = map(int,input_file.readline().rstrip().split(' '))
    dna_strings = [st.rstrip() for st in input_file.readlines()] # read input from input file
motifs = run_algorithm(dna_strings, k, t, 1000)
for motif in motifs:
    print(motif)
