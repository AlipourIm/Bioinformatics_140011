import numpy as np

def skip_input_line(file):
    file.readline()

with open("/Users/ImanAlipour/Downloads/rosalind_ba10c.txt") as input_file:
    # In bellow lines, I read the input
	given_string_or_dna = input_file.readline().strip()    # result we want to find max probability path to, like FFBBFBFB where F stands for fair and B stands for biased dice!
	skip_input_line(input_file) # this is the input_line in input containing ------ between string and alphabet_letters letters :)
	alphabet_letters = dict((char, index) for index, char in enumerate(input_file.readline().strip().split()))  #
	skip_input_line(input_file)   # this is the second input_line in input containing ------ between alphabet_letters and ststes
	graph_states = dict((state, index) for index, state in enumerate(input_file.readline().strip().split()))
	skip_input_line(input_file)   # this is the third input_line in input containing ------ between tranitioin matrix and graph_states
	skip_input_line(input_file)   
	transition_probability = np.zeros( (len(graph_states), len(graph_states)))
	for row in range(len(graph_states)):
		input_line = input_file.readline()
		for coloumn, probability in enumerate(input_line.split()[1:]):
			transition_probability[row][coloumn] = probability
	skip_input_line(input_file) # this is the fourth input_line in input containing ------ between tranitioin matrix and emition matrix
	skip_input_line(input_file) 
	dp_matrix = np.zeros( (len(graph_states), len(alphabet_letters)))
	for row, input_line in enumerate(input_file.readlines()):
		for coloumn, probability in enumerate(input_line.split()[1:]):
			dp_matrix[row][coloumn] = probability
	normalizer = np.zeros(len(given_string_or_dna)) # to scale factors
	from operator import itemgetter as it
	dictionary = [{state_of_grph : {"probability" : (1.0 / len(graph_states)) * dp_matrix[graph_states[state_of_grph]][alphabet_letters[given_string_or_dna[0]]], "previous" : None} for state_of_grph in graph_states}]
	normalizer[0] = 1.0 / sum(dictionary[0][state_of_grph]["probability"] for state_of_grph in graph_states)
	for state_of_grph in graph_states: # perform the forward pass
		dictionary[0][state_of_grph]["probability"] *= normalizer[0] 

	for n in range(1, len(given_string_or_dna)):
		dictionary.append({})
		for state in graph_states:
			probability, prev_st = max(((dictionary[n-1][prev_state]["probability"] * transition_probability[graph_states[prev_state]][graph_states[state]], prev_state) for prev_state in graph_states), key = it(0))
			dictionary[n][state] = {"probability" : probability * dp_matrix[graph_states[state]][alphabet_letters[given_string_or_dna[n]]], "previous" : prev_st}
		normalizer[n] = 1.0 / sum(dictionary[n][state_of_grph]["probability"] for state_of_grph in graph_states)
		for state_of_grph in graph_states:
			dictionary[n][state_of_grph]["probability"] *= normalizer[n]
	previous, state = max(((dictionary[-1][state_of_grph]["previous"], state_of_grph) for state_of_grph in dictionary[-1]), key=lambda s: dictionary[-1][s[1]]["probability"])
	path = state
	for i in range(len(dictionary) - 2, -1, -1):    # traverse the path with max probabiolity and get the path :) the way we did in normal dp for finding alignments.
		path = previous + path
		previous = dictionary[i][previous]["previous"]
	print(path)
