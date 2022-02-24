class Graph_node:   # A class for creating a graph, each object is an individual node
    def __init__(self,k_mer):
        self.k_mer = k_mer
        self.graph_edges = set()
    def __str__(self):
        result = "k_mer = "
        result += str(self.k_mer)
        result += "\n graph_edges = "
        result += str(self.graph_edges)
        return result

def kmers_list(m, string): # I make the k_mer list
	k_mers = []
	for i in range(len(string) - m + 1):
		k_mers.append(string[i: i + m])
	return k_mers

def reverse_complement_maker(DNA): # I create the reverse complement symply by changing C to G, A to T and vice-versa
	DNA_reverse_complement = ""

	DNA_string = list(DNA)
	DNA_string.reverse()

	DNA = ''.join(DNA_string)
	complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}

	for base in DNA:
		DNA_reverse_complement += complementDict[base]

	return DNA_reverse_complement

output_file=open("/Users/ImanAlipour/Documents/Programming/Python/bioinformatics/midterm_prep/result.txt", "a")


dna_list = []
with open("/Users/ImanAlipour/Documents/Programming/Python/bioinformatics/midterm_prep/rosalind_dbru.txt") as f:   # Read the input
    dna_list = f.read().splitlines()

dna_list+=[reverse_complement_maker(x) for x in dna_list]
length_of_k_mer = len(dna_list[0]) - 1  # All k_mers have the same length
nodes_of_graph = {}
for DNA_from_list in dna_list:
    last_node = None
    k_mer_list = kmers_list(length_of_k_mer, DNA_from_list)
    for k_mer in k_mer_list:
            if k_mer not in nodes_of_graph:
                nodes_of_graph[k_mer] = Graph_node(k_mer)
            if last_node:
                last_node.graph_edges.add(nodes_of_graph[k_mer])
            last_node = nodes_of_graph[k_mer]

# Now I write the output to output file
for k_mer, graph_node in sorted(nodes_of_graph.items()):
    for edge in graph_node.graph_edges:
        result = "("
        result += str(k_mer)
        result += ", "
        result += str(edge.k_mer)
        result += ")\n"
        output_file.write(result)
output_file.close()