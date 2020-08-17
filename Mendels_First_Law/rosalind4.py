# Mendel's First Law
# http://rosalind.info/problems/iprb/

def calc_probability(k, m, n):
    N = k + m + n
    XX_prob = k/N
    Xy_prob = m/N
    yy_prob = n/N

    probability = XX_prob*(k-1)/(N-1) + XX_prob*m/(N-1) + XX_prob*n/(N-1) + \
                  Xy_prob*k/(N-1) + Xy_prob*(m-1)/(N-1)*3/4 +Xy_prob*n/(N-1)*1/2 + \
                  yy_prob*k/(N-1) + yy_prob*m/(N-1)*1/2
    return probability

def main():
    with open('rosalind_iprb.txt') as f:
        k, m, n = [int(x) for x in next(f).split()]
    probability = calc_probability(k, m, n)
    print(probability)

    results = open("answer_rosalind4.txt", "w+")
    results.write(f'{probability}')
    results.close()

if __name__ == '__main__':
    main()


