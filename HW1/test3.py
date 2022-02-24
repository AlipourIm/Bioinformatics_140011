# The same dictionary I used in questions 2 and 3...
blosum62 = {('A', 'A'): 4, ('A', 'C'): 0, ('A', 'D'): -2, ('A', 'E'): -1, ('A', 'F'): -2, ('A', 'G'): 0, ('A', 'H'): -2, ('A', 'I'): -1, ('A', 'K'): -1, ('A', 'L'): -1, ('A', 'M'): -1, ('A', 'N'): -2, ('A', 'P'): -1, ('A', 'Q'): -1, ('A', 'R'): -1, ('A', 'S'): 1, ('A', 'T'): 0, ('A', 'V'): 0, ('A', 'W'): -3, ('A', 'Y'): -2, ('C', 'A'): 0, ('C', 'C'): 9, ('C', 'D'): -3, ('C', 'E'): -4, ('C', 'F'): -2, ('C', 'G'): -3, ('C', 'H'): -3, ('C', 'I'): -1, ('C', 'K'): -3, ('C', 'L'): -1, ('C', 'M'): -1, ('C', 'N'): -3, ('C', 'P'): -3, ('C', 'Q'): -3, ('C', 'R'): -3, ('C', 'S'): -1, ('C', 'T'): -1, ('C', 'V'): -1, ('C', 'W'): -2, ('C', 'Y'): -2, ('D', 'A'): -2, ('D', 'C'): -3, ('D', 'D'): 6, ('D', 'E'): 2, ('D', 'F'): -3, ('D', 'G'): -1, ('D', 'H'): -1, ('D', 'I'): -3, ('D', 'K'): -1, ('D', 'L'): -4, ('D', 'M'): -3, ('D', 'N'): 1, ('D', 'P'): -1, ('D', 'Q'): 0, ('D', 'R'): -2, ('D', 'S'): 0, ('D', 'T'): -1, ('D', 'V'): -3, ('D', 'W'): -4, ('D', 'Y'): -3, ('E', 'A'): -1, ('E', 'C'): -4, ('E', 'D'): 2, ('E', 'E'): 5, ('E', 'F'): -3, ('E', 'G'): -2, ('E', 'H'): 0, ('E', 'I'): -3, ('E', 'K'): 1, ('E', 'L'): -3, ('E', 'M'): -2, ('E', 'N'): 0, ('E', 'P'): -1, ('E', 'Q'): 2, ('E', 'R'): 0, ('E', 'S'): 0, ('E', 'T'): -1, ('E', 'V'): -2, ('E', 'W'): -3, ('E', 'Y'): -2, ('F', 'A'): -2, ('F', 'C'): -2, ('F', 'D'): -3, ('F', 'E'): -3, ('F', 'F'): 6, ('F', 'G'): -3, ('F', 'H'): -1, ('F', 'I'): 0, ('F', 'K'): -3, ('F', 'L'): 0, ('F', 'M'): 0, ('F', 'N'): -3, ('F', 'P'): -4, ('F', 'Q'): -3, ('F', 'R'): -3, ('F', 'S'): -2, ('F', 'T'): -2, ('F', 'V'): -1, ('F', 'W'): 1, ('F', 'Y'): 3, ('G', 'A'): 0, ('G', 'C'): -3, ('G', 'D'): -1, ('G', 'E'): -2, ('G', 'F'): -3, ('G', 'G'): 6, ('G', 'H'): -2, ('G', 'I'): -4, ('G', 'K'): -2, ('G', 'L'): -4, ('G', 'M'): -3, ('G', 'N'): 0, ('G', 'P'): -2, ('G', 'Q'): -2, ('G', 'R'): -2, ('G', 'S'): 0, ('G', 'T'): -2, ('G', 'V'): -3, ('G', 'W'): -2, ('G', 'Y'): -3, ('H', 'A'): -2, ('H', 'C'): -3, ('H', 'D'): -1, ('H', 'E'): 0, ('H', 'F'): -1, ('H', 'G'): -2, ('H', 'H'): 8, ('H', 'I'): -3, ('H', 'K'): -1, ('H', 'L'): -3, ('H', 'M'): -2, ('H', 'N'): 1, ('H', 'P'): -2, ('H', 'Q'): 0, ('H', 'R'): 0, ('H', 'S'): -1, ('H', 'T'): -2, ('H', 'V'): -3, ('H', 'W'): -2, ('H', 'Y'): 2, ('I', 'A'): -1, ('I', 'C'): -1, ('I', 'D'): -3, ('I', 'E'): -3, ('I', 'F'): 0, ('I', 'G'): -4, ('I', 'H'): -3, ('I', 'I'): 4, ('I', 'K'): -3, ('I', 'L'): 2, ('I', 'M'): 1, ('I', 'N'): -3, ('I', 'P'): -3, ('I', 'Q'): -3, ('I', 'R'): -3, ('I', 'S'): -2, ('I', 'T'): -1, ('I', 'V'): 3, ('I', 'W'): -3, ('I', 'Y'): -1, ('K', 'A'): -1, ('K', 'C'): -3, ('K', 'D'): -1, ('K', 'E'): 1, ('K', 'F'): -3, ('K', 'G'): -2, ('K', 'H'): -1, ('K', 'I'): -3, ('K', 'K'): 5, ('K', 'L'): -2, ('K', 'M'): -1, ('K', 'N'): 0, ('K', 'P'): -1, ('K', 'Q'): 1, ('K', 'R'): 2, ('K', 'S'): 0, ('K', 'T'): -1, ('K', 'V'): -2, ('K', 'W'): -3, ('K', 'Y'): -2, ('L', 'A'): -1, ('L', 'C'): -1, ('L', 'D'): -4, ('L', 'E'): -3, ('L', 'F'): 0, ('L', 'G'): -4, ('L', 'H'): -3, ('L', 'I'): 2, ('L', 'K'): -2, ('L', 'L'): 4, ('L', 'M'): 2, ('L', 'N'): -3, ('L', 'P'): -3, ('L', 'Q'): -2, ('L', 'R'): -2, ('L', 'S'): -2, ('L', 'T'): -1, ('L', 'V'): 1, ('L', 'W'): -2, ('L', 'Y'): -1, ('M', 'A'): -1, ('M', 'C'): -1, ('M', 'D'): -3, ('M', 'E'): -2, ('M', 'F'): 0, ('M', 'G'): -3, ('M', 'H'): -2, ('M', 'I'): 1, ('M', 'K'): -1, ('M', 'L'): 2, ('M', 'M'): 5, ('M', 'N'): -2, ('M', 'P'): -2, ('M', 'Q'): 0, ('M', 'R'): -1, ('M', 'S'): -1, ('M', 'T'): -1, ('M', 'V'): 1, ('M', 'W'): -1, ('M', 'Y'): -1, ('N', 'A'): -2, ('N', 'C'): -3, ('N', 'D'): 1, ('N', 'E'): 0, ('N', 'F'): -3, ('N', 'G'): 0, ('N', 'H'): 1, ('N', 'I'): -3, ('N', 'K'): 0, ('N', 'L'): -3, ('N', 'M'): -2, ('N', 'N'): 6, ('N', 'P'): -2, ('N', 'Q'): 0, ('N', 'R'): 0, ('N', 'S'): 1, ('N', 'T'): 0, ('N', 'V'): -3, ('N', 'W'): -4, ('N', 'Y'): -2, ('P', 'A'): -1, ('P', 'C'): -3, ('P', 'D'): -1, ('P', 'E'): -1, ('P', 'F'): -4, ('P', 'G'): -2, ('P', 'H'): -2, ('P', 'I'): -3, ('P', 'K'): -1, ('P', 'L'): -3, ('P', 'M'): -2, ('P', 'N'): -2, ('P', 'P'): 7, ('P', 'Q'): -1, ('P', 'R'): -2, ('P', 'S'): -1, ('P', 'T'): -1, ('P', 'V'): -2, ('P', 'W'): -4, ('P', 'Y'): -3, ('Q', 'A'): -1, ('Q', 'C'): -3, ('Q', 'D'): 0, ('Q', 'E'): 2, ('Q', 'F'): -3, ('Q', 'G'): -2, ('Q', 'H'): 0, ('Q', 'I'): -3, ('Q', 'K'): 1, ('Q', 'L'): -2, ('Q', 'M'): 0, ('Q', 'N'): 0, ('Q', 'P'): -1, ('Q', 'Q'): 5, ('Q', 'R'): 1, ('Q', 'S'): 0, ('Q', 'T'): -1, ('Q', 'V'): -2, ('Q', 'W'): -2, ('Q', 'Y'): -1, ('R', 'A'): -1, ('R', 'C'): -3, ('R', 'D'): -2, ('R', 'E'): 0, ('R', 'F'): -3, ('R', 'G'): -2, ('R', 'H'): 0, ('R', 'I'): -3, ('R', 'K'): 2, ('R', 'L'): -2, ('R', 'M'): -1, ('R', 'N'): 0, ('R', 'P'): -2, ('R', 'Q'): 1, ('R', 'R'): 5, ('R', 'S'): -1, ('R', 'T'): -1, ('R', 'V'): -3, ('R', 'W'): -3, ('R', 'Y'): -2, ('S', 'A'): 1, ('S', 'C'): -1, ('S', 'D'): 0, ('S', 'E'): 0, ('S', 'F'): -2, ('S', 'G'): 0, ('S', 'H'): -1, ('S', 'I'): -2, ('S', 'K'): 0, ('S', 'L'): -2, ('S', 'M'): -1, ('S', 'N'): 1, ('S', 'P'): -1, ('S', 'Q'): 0, ('S', 'R'): -1, ('S', 'S'): 4, ('S', 'T'): 1, ('S', 'V'): -2, ('S', 'W'): -3, ('S', 'Y'): -2, ('T', 'A'): 0, ('T', 'C'): -1, ('T', 'D'): -1, ('T', 'E'): -1, ('T', 'F'): -2, ('T', 'G'): -2, ('T', 'H'): -2, ('T', 'I'): -1, ('T', 'K'): -1, ('T', 'L'): -1, ('T', 'M'): -1, ('T', 'N'): 0, ('T', 'P'): -1, ('T', 'Q'): -1, ('T', 'R'): -1, ('T', 'S'): 1, ('T', 'T'): 5, ('T', 'V'): 0, ('T', 'W'): -2, ('T', 'Y'): -2, ('V', 'A'): 0, ('V', 'C'): -1, ('V', 'D'): -3, ('V', 'E'): -2, ('V', 'F'): -1, ('V', 'G'): -3, ('V', 'H'): -3, ('V', 'I'): 3, ('V', 'K'): -2, ('V', 'L'): 1, ('V', 'M'): 1, ('V', 'N'): -3, ('V', 'P'): -2, ('V', 'Q'): -2, ('V', 'R'): -3, ('V', 'S'): -2, ('V', 'T'): 0, ('V', 'V'): 4, ('V', 'W'): -3, ('V', 'Y'): -1, ('W', 'A'): -3, ('W', 'C'): -2, ('W', 'D'): -4, ('W', 'E'): -3, ('W', 'F'): 1, ('W', 'G'): -2, ('W', 'H'): -2, ('W', 'I'): -3, ('W', 'K'): -3, ('W', 'L'): -2, ('W', 'M'): -1, ('W', 'N'): -4, ('W', 'P'): -4, ('W', 'Q'): -2, ('W', 'R'): -3, ('W', 'S'): -3, ('W', 'T'): -2, ('W', 'V'): -3, ('W', 'W'): 11, ('W', 'Y'): 2, ('Y', 'A'): -2, ('Y', 'C'): -2, ('Y', 'D'): -3, ('Y', 'E'): -2, ('Y', 'F'): 3, ('Y', 'G'): -3, ('Y', 'H'): 2, ('Y', 'I'): -1, ('Y', 'K'): -2, ('Y', 'L'): -1, ('Y', 'M'): -1, ('Y', 'N'): -2, ('Y', 'P'): -3, ('Y', 'Q'): -1, ('Y', 'R'): -2, ('Y', 'S'): -2, ('Y', 'T'): -2, ('Y', 'V'): -1, ('Y', 'W'): 2, ('Y', 'Y'): 7}


def alignment_using_linear_space(s_string, t_string, up=0, down=None, bottom=0, right=None):
    if down is None:
        down = len(s_string)
    if right is None:
        right = len(t_string)

    if bottom == right:
        return "v" * (down - up)
    if up == down:
        return "h" * (right - bottom)

    mid_edge, mid_edge_from_source, mid_edge_to_dest = handle_top(s_string, t_string, up, down, bottom, right)
    midNode, middle = mid_edge_from_source
    path_left = alignment_using_linear_space(s_string, t_string, up, midNode, bottom, middle)
    midNode, middle = mid_edge_to_dest
    path_right = alignment_using_linear_space(s_string, t_string, midNode, down, middle, right)
    return path_left + mid_edge + path_right


def backtrack_path(path, s_string, t_string):
    s_aligned = ''
    i = 0
    t_aligned = ''
    j = 0
    for arrow in path:
        if arrow == "d":
            s_aligned += s_string[i]
            t_aligned += t_string[j]
            i += 1
            j += 1
        elif arrow == "v":
            s_aligned += s_string[i]
            t_aligned += '-'
            i += 1
        else:
            s_aligned += '-'
            t_aligned += t_string[j]
            j += 1
    return s_aligned, t_aligned

def using_linear_memory(s_string, t_string, indel_penalty=5):
    s_string = "-" + s_string
    t_string = "-" + t_string
    current_strong = [0] * len(s_string)
    for i in range(1, len(s_string)):
        current_strong[i] = current_strong[i - 1] - indel_penalty

    for j in range(1, len(t_string)):
        S_next = [-indel_penalty * j] * len(s_string)
        for i in range(1, len(s_string)):
            if (s_string[i], t_string[j]) in blosum62:
                key = (s_string[i], t_string[j])
            else:
                key = (t_string[j], s_string[i])
            S_next[i] = max(current_strong[i - 1] + blosum62[key], S_next[i - 1] - indel_penalty, current_strong[i] - indel_penalty)
        current_strong = S_next

    return current_strong


def handle_top(s_string, t_string, up=0, down=None, bottom=0, right=None):
    if down is None:
        down = len(s_string)
    if right is None:
        right = len(t_string)
    middle_coloumn = (right + bottom) // 2
    start_from_source = using_linear_memory(s_string[up:down], t_string[bottom:middle_coloumn])
    end_to_sink = using_linear_memory(s_string[up:down][::-1], t_string[middle_coloumn:right][::-1])[::-1]
    maximum_length = -1e6
    for i in range(len(start_from_source)):
        current_length = start_from_source[i] + end_to_sink[i]
        if current_length > maximum_length:
            maximum_length = current_length
            index_1 = i
    start_from_source_re = using_linear_memory(s_string[up:down], t_string[bottom:middle_coloumn + 1])
    end_to_sink_re = using_linear_memory(s_string[up:down][::-1], t_string[middle_coloumn + 1:right][::-1])[::-1]
    maximum_length = -1e6
    for i in range(len(start_from_source_re)):
        current_length = start_from_source_re[i] + end_to_sink_re[i]
        if current_length > maximum_length:
            maximum_length = current_length
            index_2 = i

    if index_2 == index_1 + 1:
        return "d", (index_1 + up, middle_coloumn), (index_1 + up + 1, middle_coloumn + 1)
    if index_2 == index_1:
        return "h", (index_1 + up, middle_coloumn), (index_1 + up, middle_coloumn + 1)
    return "v", (index_1 + up, middle_coloumn), (index_1 + up + 1, middle_coloumn)

def alignment_score_calculator(s_string, t_string, indel_penalty=5):
    score = 0
    for i in range(len(s_string)):
        if s_string[i] == '-' or t_string[i] == '-':
            score -= indel_penalty
        else:
            if (s_string[i], t_string[i]) in blosum62:
                key = (s_string[i], t_string[i])
            else:
                key = (t_string[i], s_string[i])
            score += blosum62[key]
    return score

s = 'PLEASANTLY'
t = 'MEANLY'

path = alignment_using_linear_space(s, t)

s_aligned, t_aligned = backtrack_path(path, s, t)
score = alignment_score_calculator(s_aligned, t_aligned)
print(score)
print(s_aligned)
print(t_aligned)
