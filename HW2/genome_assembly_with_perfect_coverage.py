with open('/Users/ImanAlipour/Downloads/rosalind_pcov.txt') as input_file:
	input_k_mers = [line.strip() for line in input_file.readlines()]
input_file.close()

# Instead of using the code I had before for creating the graph, I will make a better and simpler implementation here:
de_brujin_k_mers = []  # I first make the de brujin graph
for k_mer in input_k_mers:
	de_brujin_k_mers.append(k_mer)

length_of_DNAs = len(input_k_mers[0])
graph_edges = []
for i in range(len(de_brujin_k_mers)):
    graph_edges.append([de_brujin_k_mers[i][0:length_of_DNAs-1], de_brujin_k_mers[i][1:length_of_DNAs]])

temporary_edges = graph_edges.pop(0)    # Everytime we pop an edge and add to the result a character and continue till graph_edges becomes empty
result = temporary_edges[0][len(temporary_edges)-2]
while len(graph_edges) != 0:
    result += temporary_edges[1][len(temporary_edges)-2]
    tmp_graph_edges = graph_edges
    index = 0
    for i in range(len(tmp_graph_edges)):
        if graph_edges[i][0] == temporary_edges[1]:
            index = i
    temporary_edges = graph_edges.pop(index)

print(result)