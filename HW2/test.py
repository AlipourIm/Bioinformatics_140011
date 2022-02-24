with open('/Users/ImanAlipour/Downloads/rosalind_pcov.txt') as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]

# Begin by constructing the De Bruijn Graph
DBG_edge_elmts = set()
for kmer in k_mers:
	DBG_edge_elmts.add(kmer)

# Create the edges of the Graph.
k = len(k_mers[0])
edge = lambda elmt: [elmt[0:k-1],elmt[1:k]]
DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

# Construct the cyclic superstring from the edges. 
temp = DBG_edges.pop(0)
cyclic = temp[0][-1]
while DBG_edges != []:
	cyclic += temp[1][-1]
	[index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp[1]]
	temp = DBG_edges.pop(index)

# Print and save the output.
print (cyclic)
print(cyclic, end="")
print(cyclic)


""""""
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
	complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}

	for base in DNA:
		DNA_reverse_complement += complementDict[base]

	return DNA_reverse_complement

def error_correct(input_DNAs):
    corrected_form = []
    correct_form = []
    wrong_form = []

    for DNA_sequence_1 in input_DNAs:
        reverse_r = reverse_complement_maker(DNA_sequence_1)[::-1]
        if input_DNAs.count(DNA_sequence_1) + input_DNAs.count(reverse_r) >= 2:
            correct_form.append(DNA_sequence_1)
        else:
            wrong_form.append(DNA_sequence_1)

    for DNA_sequence_2 in wrong_form:
        for cr in correct_form:
            reverse_cr = reverse_complement_maker(cr)[::-1]
            if hamming_distance(DNA_sequence_2, cr) == 1:
                corrected_form.append((DNA_sequence_2, cr))
                break
            if hamming_distance(DNA_sequence_2, reverse_cr) == 1:
                corrected_form.append((DNA_sequence_2, reverse_cr))
                break

    return corrected_form

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
corrected_form = error_correct(input_DNA_list)
for DNA_sequence_2, cr in corrected_form:
    result = "" + DNA_sequence_2 + "->" + cr
    print(result)
""""""