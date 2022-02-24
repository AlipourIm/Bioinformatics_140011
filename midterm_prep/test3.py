# The same dictionary I used in questions 2 and 3...
blosum62 = {('A', 'A'): 3, ('A', 'T'): -1, ('A', 'C'): -2, ('A', 'G'): -2, ('T', 'T'): 1, ('T', 'C'): -1, ('T', 'G'): -1, ('C', 'C'): 2, ('C', 'G'): -2, ('G', 'G'): 1}

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

s = 'ACGCTGA'
t = 'ACTGATGC'

path = alignment_using_linear_space(s, t)

s_aligned, t_aligned = backtrack_path(path, s, t)
score = alignment_score_calculator(s_aligned, t_aligned, 1)
print(score)
print(s_aligned)
print(t_aligned)

