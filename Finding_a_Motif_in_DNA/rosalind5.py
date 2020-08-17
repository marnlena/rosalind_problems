# Finding a Motif in DNA
# http://rosalind.info/problems/subs/

def get_location(fragment, dna_string):
    ind_fragment = []
    ind_start_search = 0
    ind_fragment_new = 0
    while ind_fragment_new != -1:
        ind_fragment_new = dna_string.find(fragment, ind_start_search, -1)
        if ind_fragment_new != -1:
            ind_start_search = ind_fragment_new + 1
            ind_fragment.append(ind_fragment_new+1)

    return(ind_fragment)

def main():
    with open('rosalind_subs.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("DNA string s is")
    print(content[0])
    print("DNA fragment t is")
    print(content[1])

    answer = get_location(content[1], content[0])
    with open('answer_rosalind5.txt', 'a') as the_file:
        for i in answer:
            the_file.write(f'{i}\t')

if __name__ == '__main__':
    main()