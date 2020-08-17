# Consensus and Profile
# http://rosalind.info/problems/cons/

import numpy as np

def main():
    with open('rosalind_cons.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    dna_strings = []
    one_string=''
    for x in content[1:len(content)]:
        line = x.strip()
        if x[0] != '>':
            one_string += (x[0:(len(x)-1)])
        else:
            dna_strings.append(one_string)
            one_string = ''

    dna_strings_array = np.chararray((len(dna_strings), len(dna_strings[0])), unicode=True)
    for i in range(len(dna_strings)):
        for j in range(len(dna_strings[0])):
            dna_strings_array[i, j] = dna_strings[i][j]
        print(dna_strings[i])

    transpose_dna_strings = []
    aa_names=['A', 'C', 'G', 'T']
    profile_matrix = np.zeros((4, len(dna_strings[0])))
    # for i in aa_names:
    #     for j in len(dna_strings[0]):
    #         profile_matrix[i, j] = sum()

if __name__ == '__main__':
    main()