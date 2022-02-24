# Since I didn;t really know what to do, I read this forumn: https://www.biostars.org/p/61843/ and this lead to some articles that I got the idea from.
collection_of_DNAs=[]

with open('/Users/ImanAlipour/Downloads/rosalind_asmq.txt') as output_file:     # Read the inputs from input file.
    for line in output_file:
        collection_of_DNAs.append(line.strip())  

def assessing_assembly_quality_calculator(collection_of_DNAs,N):    # Main function to calculate what we need
    collection_of_DNAs.sort()
    amount=sum(sequence for sequence in collection_of_DNAs)
    target=N*amount/100
    l_amount=0
    n=len(collection_of_DNAs)-1
    while l_amount<target:
        l_amount+=collection_of_DNAs[n]
        n-=1
    return collection_of_DNAs[n+1]
    
length_of_DNAs_in_collection_of_DNAs = []
for i in range(len(collection_of_DNAs)):
    length_of_DNAs_in_collection_of_DNAs.append(len(collection_of_DNAs[i]))
n_50 = assessing_assembly_quality_calculator(length_of_DNAs_in_collection_of_DNAs, 50)    # Calculate the result for N = 50
n_75 = assessing_assembly_quality_calculator(length_of_DNAs_in_collection_of_DNAs, 75)    # Calculate the result for N = 75
output = ""
output += str(n_50) + " " + str(n_75)   # Now prepare the final answer and print it. :)
print (output) 