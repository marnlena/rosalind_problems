# Complementing a Strand of DNA
# http://rosalind.info/problems/revc/

def get_complement(symbol):
    if symbol == 'A':
        return 'T'
    elif symbol == 'T':
        return 'A'
    elif symbol == 'C':
        return 'G'
    elif symbol == 'G':
        return 'C'


def get_complement_string(revc_string):
    num_symbols = len(revc_string)
    complement_string = ""
    for i in range(num_symbols-1):
        complement_string += str(get_complement(revc_string[i]))
    return complement_string

def main():
    rosalind_revc = open("rosalind_revc.txt", "r")
    revc_string = rosalind_revc.read()
    rosalind_revc.close()

    print("Rosalind string is ")
    print(revc_string)
    print("\n")

    complement_string = get_complement_string(revc_string)

    print("Complement string is ")
    print(complement_string)
    print("\n")

    print("Reversed complement string is ")
    print(complement_string[::-1])
    print("\n")

    results = open("answer_rosalind3.txt", "w+")
    results.write(f'{complement_string[::-1]}')
    results.close()

if __name__ == '__main__':
    main()


