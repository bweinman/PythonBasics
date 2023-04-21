#!/usr/bin/env python3
# copy-bin.py by Bill Weinman [https://bw.org]
# as of 2023-04-03

from os import path

def main():
    file_path = path.dirname(__file__)
    infile = open(f'{file_path}/berlin.jpg', 'rb')
    outfile = open(f'{file_path}/berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10 * 1024)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    infile.close()
    outfile.close()
    print('\ndone.')

if __name__ == '__main__':
    main()
