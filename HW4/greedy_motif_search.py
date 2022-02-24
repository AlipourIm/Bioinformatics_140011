# I first answered problem 3 then this one, a lot of the code was originall yimplemented for problem 3 and copied here! like make profile and calculate score and profile  maekr
# The sources I used for this one are the same as the ones I used in problem 3(I solved problem 3 first then problem 2)
'''
https://www.bioinformaticsalgorithms.org/bioinformatics-chapter-2
https://www.youtube.com/watch?v=R5DVi25kqAY
https://www.coursera.org/lecture/dna-analysis/how-rolling-dice-helps-us-find-regulatory-motifs-part-1-12-43-DxbJn
https://www.coursera.org/lecture/bioinformatics/optional-how-rolling-dice-helps-us-find-regulatory-motifs-part-2-05-37-DwJGf
https://www.coursera.org/lecture/bioinformatics/optional-how-rolling-dice-helps-us-find-regulatory-motifs-part-1-12-43-AYObU
'''

# This problem was very much the same as problem 3, I just wrote greedy_motif_search_algorithm() and the rest was implemented before
def greedy_motif_search_algorithm(dna,k,t):
    best_motif = [s[:k] for s in dna]
    for i in range(len(dna[0])-k+1):
        best_found_untill_here = [dna[0][i:i+k]]
        for m in range(1,t):
            matrix = make_profile(best_found_untill_here)
            best_found_untill_here.append(profile_maker(dna[m], k, matrix))
        if calculate_score(best_found_untill_here) < calculate_score(best_motif):
            best_motif = best_found_untill_here
    return best_motif

def calculate_score(motifs):
    motifs_zipped = zip(*motifs)
    found_score = 0
    for string in motifs_zipped:
        calculate_score = len(string) - max([string.count('A'), string.count('C'), string.count('G'), string.count('T')])
        found_score += calculate_score
    return found_score

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

def profile_maker(text, k , matrix):
    maximum_points = None
    k_mer_to_be_reported = None
    for i in range(len(text)-k+1):
        k_mer = text[i:i+k]
        sum_points = 1
        for j in range(k):
            points_here = matrix[k_mer[j]][j]
            sum_points *=points_here
        if maximum_points == None or sum_points > maximum_points:
            maximum_points = sum_points
            k_mer_to_be_reported = k_mer
    return k_mer_to_be_reported

with open('/Users/ImanAlipour/Downloads/rosalind_ba2e.txt') as f:
    k,t = map(int,f.readline().rstrip().split(' '))
    dna_strings = [st.rstrip() for st in f.readlines()]
motifs = greedy_motif_search_algorithm(dna_strings, k, t)
for motif in motifs:
    print(motif)