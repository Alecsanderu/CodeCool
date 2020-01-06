def dnaComplement(s):
    reverse = s[::-1]
    print(reverse)
    complemented = ''
    for letter in reverse:
        if letter == 'T':
            complemented += 'A'
        elif letter == 'A':
            complemented += 'T'
        elif letter == 'C':
            complemented += 'G'
        elif letter == 'G':
            complemented += 'C'
    return complemented


print(dnaComplement('ATGC'))
