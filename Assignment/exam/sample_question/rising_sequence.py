n = [1, 3, 5, 2, 1, 8, 4, 3, 2, 2, 3, 4, 5, 6, 7, 8, 9]


def rising_sequence(seq):
    seq_ = [[seq[0]]]
    s = 1
    while s < len(seq):
        if seq[s-1] < seq[s]:
            seq_[len(seq_)-1].append(seq[s])
        else:
            seq_.append([seq[s]])
        s = s+1
    return max(seq_, key=len)

print(rising_sequence(n)) 

def increasing(a_list, ):
