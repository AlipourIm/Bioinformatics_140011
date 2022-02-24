def hamming_distance(s, t):     # I implemented this code in first HW(previous homework) and copied it here.
    # Computes hamming distance of two given strings(same length) by performing a loop over one of the strings and counting the matches.
    counter = 0
    count = 0
    while(counter < len(s)):
        if(s[counter] != t[counter]):
            count += 1
        counter += 1
    return count

# I implemented this code in the first problem of this homework :) I reused it!
def reverse_complement_maker(DNA): # I create the reverse complement symply by changing C to G, A to T and vice-versa
	DNA_reverse_complement = ""

	DNA_string = list(DNA)
	DNA_string.reverse()

	DNA = ''.join(DNA_string)
	complement_dicttionary = {"C": "G", "G": "C", "T": "A", "A": "T"}

	for base in DNA:
		DNA_reverse_complement += complement_dicttionary[base]

	return DNA_reverse_complement


def error_corrector(input_DNAs):
    correct_forms = []
    correct_reads, incorrect_reads = [], []

    for DNA_sequence_1 in input_DNAs:
        reverse_r = reverse_complement_maker(DNA_sequence_1)
        if input_DNAs.count(DNA_sequence_1) + input_DNAs.count(reverse_r) >= 2:
            correct_reads.append(DNA_sequence_1)
        else:
            incorrect_reads.append(DNA_sequence_1)

    for DNA_sequence_2 in incorrect_reads:
        for correct_read in correct_reads:
            reverse_cr = reverse_complement_maker(correct_read)
            if hamming_distance(DNA_sequence_2, correct_read) == 1:
                correct_forms.append((DNA_sequence_2, correct_read))
                break
            if hamming_distance(DNA_sequence_2, reverse_cr) == 1:
                correct_forms.append((DNA_sequence_2, reverse_cr))
                break

    return correct_forms

# I also used this code in previous homework but didn't submit it because I didn't have to make a list and the number of sequences we read in that assignment were limited, but here we have to read multiple lines froom input file :)
def read_dna_sequence(data_location):
    with open(data_location) as input_file:
        DNA_list=[]
        for input_file_line in input_file:
            if input_file_line[0] == '>':  # If the input_file_line starts with '>' we have a new DNA to add to our array, so append the one we fetched before and fetch a new one from file.   
                try:    # Since first time we haven't fetched a DNA yet, we don't do anything, and from second pass we add DNAs to our list
                    DNA_list.append(fetched_DNA)
                except:
                    pass
                fetched_DNA = [input_file_line.lstrip('>').rstrip('\n'),''] # We just remove the first line and keep the second as DNA value
            else:
                fetched_DNA[1] += input_file_line.rstrip('\n')
        DNA_list.append(fetched_DNA)  # This is the last DNA in the file, we have fetched it but not yet added it to our array, we do it in the end
    return DNA_list
input_DNA_list = []
for i in read_dna_sequence('/Users/ImanAlipour/Downloads/rosalind_corr.txt'):
    input_DNA_list.append(i[1])
correct_forms = error_corrector(input_DNA_list)
for DNA_sequence_2, correct_read in correct_forms:
    result = "" + DNA_sequence_2 + "->" + correct_read
    if len(result) != 0:
        print(result)