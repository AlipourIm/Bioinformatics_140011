import sys
def ReadFASTA(data_location):
        '''Determines the data type of the FASTA format data and passes the appropriate information to be parsed.'''
        
        # If given a list, return fasta information from all items in the list.
        if type(data_location) == list:
                fasta_list =[]
                for location in data_location:
                        fasta_list+=ReadFASTA(location)
                return fasta_list


        # Check for a text file, return fasta info from the text file.
        if data_location[-4:] == '.txt':
                with open(data_location) as f:
                        return ParseFASTA(f)

def ParseFASTA(f):
        '''Extracts the Sequence Name and Nucleotide/Peptide Sequence from the a FASTA format file or website.'''
        fasta_list=[]
        for line in f:

                # If the line starts with '>' we've hit a new DNA strand, so append the old one and create the new one.
                if line[0] == '>':
                        
                        # Using try/except because intially there will be no current DNA strand to append.
                        try:
                                fasta_list.append(current_dna)
                        except UnboundLocalError:
                                pass

                        current_dna = [line.lstrip('>').rstrip('\n'),'']

                # Otherwise, append the current DNA line to the current DNA
                else:
                        current_dna[1] += line.rstrip('\n')
        
        # Append the final DNA strand after reading all the lines.
        fasta_list.append(current_dna)

        return fasta_list

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read and parse the input data.
    #input_lines = sys.stdin.read().splitlines()
    #string1 = input_lines[0]
    #string2 = input_lines[1]
    #print(string1)
    #print()
    #print()
    #print(string2)
    col = [fasta[1] for fasta in ReadFASTA('/Users/ImanAlipour/Downloads/rosalind_corr.txt')]
    print(col)

    # Get the fitting alignment.
    #alignment = fitting_alignment(word1, word2)
    #print(word1)
    #print("\n###\n")
    #print(word2)
    # Print and save the answer.
    #print '\n'.join(alignment)
    #with open('output/100_SIMS.txt', 'w') as output_data:
        #output_data.write('\n'.join(alignment)

main()