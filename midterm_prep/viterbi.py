import numpy as np
import operator
import pdb

with open("/Users/ImanAlipour/Documents/Programming/Python/bioinformatics/midterm_prep/viterbi_in.txt") as infile, open("/Users/ImanAlipour/Documents/Programming/Python/bioinformatics/midterm_prep/viterbi_out.txt", "w") as outfile:
	observations = infile.readline().strip()
	infile.readline() # separating line
	alphabet = dict((char, index) for index, char in enumerate(infile.readline().strip().split()))
	infile.readline() # separating line
	states = dict((state, index) for index, state in enumerate(infile.readline().strip().split()))

	infile.readline() # separating lines
	infile.readline() # separating lines

	t = np.zeros( (len(states), len(states)))
	for row in range(len(states)):
		line = infile.readline()
		for col, prob in enumerate(line.split()[1:]):
			t[row][col] = prob

	infile.readline() # separating lines
	infile.readline() # separating lines

	e = np.zeros( (len(states), len(alphabet)));
	for row, line in enumerate(infile.readlines()):
		for col, prob in enumerate(line.split()[1:]):
			e[row][col] = prob

	c = np.zeros( len(observations) ) # to scale factors

	# build trellis
	V = [{st : {"prob" : (1.0 / len(states)) * e[states[st]][alphabet[observations[0]]], "prev" : None} for st in states}]
	c[0] = 1.0 / sum(V[0][st]["prob"] for st in states)
	for st in states:
		V[0][st]["prob"] *= c[0] # normalize

	for n in range(1, len(observations)):
		V.append({})
		for state in states:
			prob, prev_st = max(((V[n-1][prev_state]["prob"] * t[states[prev_state]][states[state]], prev_state) for prev_state in states), key = operator.itemgetter(0))
			V[n][state] = {"prob" : prob * e[states[state]][alphabet[observations[n]]], "prev" : prev_st}
		c[n] = 1.0 / sum(V[n][st]["prob"] for st in states)
		for st in states:
			V[n][st]["prob"] *= c[n] # normalize		

	# pdb.set_trace()
	for item in V:
		print(item)
	prev, state = max(((V[-1][st]["prev"], st) for st in V[-1]), key=lambda s: V[-1][s[1]]["prob"])
	path = state
	for i in range(len(V) - 2, -1, -1):
		path = prev + path
		prev = V[i][prev]["prev"]

	print(observations)
	print(states)
	print(t)
	print(e)
	print(path)

	outfile.write(path)