import random
# for learning and understanding this topic, I used these links:
'''
https://towardsdatascience.com/gibbs-sampling-8e4844560ae5
https://www.sciencedirect.com/topics/mathematics/gibbs-sampler
https://www.youtube.com/watch?v=ER3DDBFzH2g
https://www.youtube.com/watch?v=9e4uqODjooo
https://www.youtube.com/watch?v=a_08GKWHFWo

and this link was more bioinformatics related:
https://www.youtube.com/watch?v=vupAgqunSGM
'''

def select_motifs_randomly(dna_string, k, t):
  motifs = []
  for seq in dna_string:
    index = random.randint(0, len(seq) - k)
    motifs.append(seq[index:index+k])

  return motifs

def find_score(motifs, k, t):
  profile = []
  for i in range(k):
    for j in range(len(motifs)):
      if j == 0:
        profile.append({ 'A': 1, 'T': 1, 'C': 1, 'G': 1 })
      profile[i][motifs[j][i]] += 1
  score = 0
  for i in range(len(profile)):
    score += (4 + t - profile[i][max(profile[i], key=profile[i].get)])
  return score

def gibs_sampler(dna_string, k, t, N):
  motifs = select_motifs_randomly(dna_string, k, t)
  answer = list(motifs)
  for _ in range(N):
    i = random.randint(0, t - 1)
    motifs.pop(i)
    profile = make_profile(motifs, k)
    temp = make_temp(profile, dna_string[i], k)
    index = random.choices(list(range(0, len(dna_string[i]) - k + 1)), temp)
    motifs.insert(i, dna_string[i][index[0]:index[0] + k])
    if find_score(motifs, k, t) < find_score(answer, k, t):
      answer = list(motifs)
  return answer

def make_profile(motifs, k):
  profile = []
  for i in range(k):
    for j in range(len(motifs)):
      if j == 0:
        profile.append({ 'A': 1, 'T': 1, 'C': 1, 'G': 1 })
      profile[i][motifs[j][i]] += 1
  return profile

def make_temp(profile, sequence, k):
  probabilities = []
  for i in range(len(sequence) - k + 1):
    overall_count = 1
    for j in range(k):
      overall_count *= (profile[j][sequence[i+j]])
    probabilities.append(overall_count)

  return probabilities

with open('/Users/ImanAlipour/Downloads/rosalind_ba2g.txt', 'r') as f:
  k, t, N = [int(x) for x in f.readline().strip().split(' ')]   # read the input from input file
  dna_string = [x.strip() for x in f.readlines()]  # read the input from input file
  answer = gibs_sampler(dna_string, k, t, N)
  for i in range(0, 20):
    motifs = gibs_sampler(dna_string, k, t, N)
    if find_score(motifs, k, t) < find_score(answer, k, t):
      answer = motifs
for motif in answer:
    print(motif)