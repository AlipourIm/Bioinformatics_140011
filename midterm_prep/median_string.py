from itertools import product


def median_string(k, dna_list):
    # Initialize the best pattern score as one greater than the maximum possible score.
    best_score = k*len(dna_list) + 1
    best_pattern = ''
    # Check the scores of all k-mers.
    for pattern in product('ACGT', repeat=k):
        print("##" + best_pattern + ' ' + str(best_score))
        current_score = sum([motif_score(''.join(pattern), dna) for dna in dna_list])
        if current_score < best_score:
            best_score = current_score
            best_pattern = ''.join(pattern)
            

    return best_pattern


def motif_score(pattern, motif):
    '''Returns the score of d(pattern, motif).'''
    return min([hamming_distance(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])

def hamming_distance(s, t):     # I implemented this code in first HW(previous homework) and copied it here.
    # Computes hamming distance of two given strings(same length) by performing a loop over one of the strings and counting the matches.
    counter = 0
    count = 0
    while(counter < len(s)):
        if(s[counter] != t[counter]):
            count += 1
        counter += 1
    return count

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('/Users/ImanAlipour/Documents/Programming/Python/bioinformatics/midterm_prep/median.txt') as input_data:
        k = int(input_data.readline())
        dna_list = [line.strip() for line in input_data.readlines()]

    # Get the best pattern.
    best_pattern = median_string(k, dna_list)

    # Print and save the answer.
    print (best_pattern)

if __name__ == '__main__':
    main()