#!/usr/bin/env python3
# comprehension.py by Bill Weinman [https://bw.org]
# as of 2023-03-26

def print_seq(o):
    for x in o:
        print(x, end = ' ')
    print()

def main():
    seq = range(11)
    print_seq(seq)

if __name__ == '__main__':
    main()
