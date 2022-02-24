import numpy as np


# Sources I used to get insight:
'''
https://en.wikipedia.org/wiki/Baum–Welch_algorithm
https://www.youtube.com/watch?v=SyFXnTqQRGs
https://www.coursera.org/lecture/dna-mutations/baum-welch-learning-2F980
https://www.youtube.com/watch?v=JRsdt05pMoI
video 17 from this link:
https://liulab-dfci.github.io/bioinfo-combio/hmm.html#baum-welch-algorithm-intuition
'''

with open('/Users/ImanAlipour/Downloads/rosalind_ba10k.txt', 'r') as input_file:    # We first read input the same way we did for previous problem
  expected_string = ''
  our_observations = {}
  graph_states = []
  transition_probabilities = [[]]
  emission_probabilities = [[]]
  length_of_string = int(input_file.readline().strip())
  input_file.readline() 
  expected_string = input_file.readline().strip()
  input_file.readline() 
  states = input_file.readline().strip().split()
  for i in range(len(states)):
      our_observations[states[i]] = i
  input_file.readline() 
  graph_states = input_file.readline().strip().split()
  input_file.readline() 
  input_file.readline() 
  transition_probabilities = np.zeros((len(graph_states), len(graph_states)))
  for i in range(len(graph_states)):
    transition_probabilities[i,:] = [float(i) for i in input_file.readline().strip().split()[1:]]
  input_file.readline() 
  input_file.readline() 
  emission_probabilities = np.zeros((len(graph_states), len(our_observations)))
  for i in range(len(graph_states)):
    emission_probabilities[i,:] = [float(i) for i in input_file.readline().strip().split()[1:]]
for m in range(length_of_string):
  forward_pass = np.zeros((len(graph_states), len(expected_string)))
  forward_pass[:, 0] = emission_probabilities[:, our_observations[expected_string[0]]]
  for j in range(1, len(expected_string)):
    for i in range(len(graph_states)):
      for k in range(len(graph_states)):
        forward_pass[i, j] += forward_pass[k, j-1] * transition_probabilities[k, i] * emission_probabilities[i, our_observations[expected_string[j]]]
  backward_pass = np.zeros((len(graph_states), len(expected_string)))
  backward_pass[:, len(expected_string) - 1] = 1 
  for j in range(len(expected_string)-2, -1, -1):
    for i in range(len(graph_states)):
      for k in range(len(graph_states)):
        backward_pass[i, j] += backward_pass[k, j+1] * transition_probabilities[i, k] * emission_probabilities[k, our_observations[expected_string[j+1]]]
  probability = forward_pass * backward_pass;
  probabilities_here = np.zeros([len(expected_string), len(graph_states), len(graph_states)])
  for i in range(len(expected_string) - 1):
    overall = np.sum(probability[:, i])
    for j in range(len(graph_states)):
      for k in range(len(graph_states)):
        probabilities_here[i, j, k] = forward_pass[j, i] * backward_pass[k, i+1] * transition_probabilities[j, k] * emission_probabilities[k, our_observations[expected_string[i+1]]] / overall
  for i in range(len(expected_string)):
    probability[:, i] = probability[:, i] / overall
  transition_probabilities = np.sum(probabilities_here, 0)
  for i in range(len(graph_states)):
    transition_probabilities[i] = transition_probabilities[i] / np.sum(transition_probabilities[i]) 
  emission_probabilities = np.zeros((len(graph_states), len(our_observations)))
  for i in our_observations:
    input_file = np.array(list(expected_string)) == i
    emission_probabilities[:, our_observations[i]] = np.sum(probability[:, input_file], 1)
  for i in range(len(graph_states)):
    emission_probabilities[i] /= np.sum(emission_probabilities[i])
    


# It's interesting that when I printed the putputs in colsole, I got wrong answers but when I wrote them in a file it got fixed
with open('/Users/ImanAlipour/Downloads/result.txt', 'w') as output_file:   # now print the outputs
  output_file.write("\t" + "\t".join(graph_states) + "\n")
  for i in range(len(graph_states)):
    s = np.array2string(
      transition_probabilities[i],
      formatter={'float_kind':lambda x: "%.4f" % x},
      separator='\t',
      prefix=""
    )

    output_file.write(graph_states[i] + "\t" + s[1:-1] + "\n")
  output_file.write("--------\n")
    
  output_file.write("\t" + "\t".join(our_observations.keys()) + "\n")
  for i in range(len(graph_states)):
    s = np.array2string(
      emission_probabilities[i],
      formatter={'float_kind':lambda x: "%.4f" % x},
      separator='\t',
      prefix=""
    )

    output_file.write(graph_states[i] + "\t" + s[1:-1] + "\n")