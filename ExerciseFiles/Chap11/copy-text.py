#!/usr/bin/env python3
# copy-text.py by Bill Weinman [https://bw.org]
# as of 2023-04-03

from os import path

def main():
    file_path = path.dirname(__file__)
    infile = open(f'{file_path}/lines.txt', 'rt')
    outfile = open(f'{file_path}/lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    infile.close()
    outfile.close()
    print('\ndone.')

if __name__ == '__main__':
    main()
