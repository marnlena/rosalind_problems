# Counting Point Mutations
# http://rosalind.info/problems/hamm/

def count_hamming_distance(a, b):
    num_diff_symbols = 0
    for x, y in zip(a, b):
        if x != y:
            num_diff_symbols = num_diff_symbols + 1
    return num_diff_symbols

def main():
    with open('rosalind_hamm.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    hamming_distance = count_hamming_distance(content[0], content[1])
    print(f'Hamming distance is {hamming_distance}')

    with open('hamming_distance.txt', 'a') as the_file:
         the_file.write(f'{hamming_distance}')


if __name__ == '__main__':
    main()

