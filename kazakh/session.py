with open('kazakh/edok2013.txt') as inf, open('kazakh/edok2013.csv', 'w') as outf:
    for line in inf:
        line = line.strip().replace('\t', ' ')
        if line[:2].isupper():
            line = line.replace(' ', '\t', 1)
            try:
                word, rest = line.split('\t')
            except ValueError:
                word = line
            print(word.upper() + '\t' + rest, file=outf)

