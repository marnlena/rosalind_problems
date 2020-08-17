# Transcribing DNA into RNA
# http://rosalind.info/problems/rna/

def main():
    rosalind_rna = open("rosalind_rna.txt", "r")
    dna_string = rosalind_rna.read()
    rosalind_rna.close()

    print("Rosalind DNA is ")
    print(dna_string)
    print("\n")

    rna_string = dna_string.replace('T','U')
    print("Rosalind RNA is ")
    print(rna_string)
    print("\n")

    results = open("answer_rosalind2.txt", "w+")
    results.write(f'{rna_string}')
    results.close()

if __name__ == '__main__':
    main()


