# Counting DNA Nucleotides
# http://rosalind.info/problems/dna/

def main():
    rosalind_dna = open("rosalind_dna.txt", "r")
    dna_string=rosalind_dna.read()

    print("Rosalind DNA is ")
    print(dna_string)
    print("\n")

    A_count = dna_string.count('A')
    C_count = dna_string.count('C')
    G_count = dna_string.count('G')
    T_count = dna_string.count('T')
    print("A count in DNA:", A_count)
    print("C count in DNA:", C_count)
    print("G count in DNA:", G_count)
    print("T count in DNA:", T_count)

    rosalind_dna.close()
    results = open("answer.txt", "w+")
    results.write(f'{A_count}\t{C_count}\t{G_count}\t{T_count}')
    results.close()

if __name__ == '__main__':
    main()


