def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("lengths of strand_a and strand_b not equal.")
    number = 0
    for i, c in enumerate(strand_a):
        if c != strand_b[i]:
            number += 1
    return number


print(distance("GGACGGATTCTG", "AGGACGGATTCT"))


