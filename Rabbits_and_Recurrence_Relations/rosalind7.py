# Rabbits and Recurrence Relations
# http://rosalind.info/problems/fib/

def compute_num_pair_rabbits(num_month, num_born_rabbits):
    if num_month == 1:
        return 1
    if num_month == 2:
        return 1
    return compute_num_pair_rabbits(num_month-1, num_born_rabbits) + \
           num_born_rabbits * compute_num_pair_rabbits(num_month-2, num_born_rabbits)

def main():
    with open('rosalind_fib.txt') as f:
        n, k = [int(x) for x in next(f).split()]

    num_rabbits_pairs = compute_num_pair_rabbits(n, k)
    print(num_rabbits_pairs)
    with open('num_rabbits_pairs.txt', 'a') as the_file:
         the_file.write(f'{num_rabbits_pairs}')

if __name__ == '__main__':
    main()

