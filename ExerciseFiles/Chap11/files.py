#!/usr/bin/env python3
# files.py by Bill Weinman [https://bw.org]
# as of 2023-04-03

def main():
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__':
    main()
