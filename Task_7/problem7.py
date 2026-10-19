# Alphabet Rangoli

# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        s = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4*size-3, '-'))

    print('\n'.join(lines[::-1] + lines[1:]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)