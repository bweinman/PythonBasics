#!/usr/bin/env python3
# sets.py by Bill Weinman [https://bw.org]
# as of 2023-03-26

def print_set(o):
    print('{', end = '')
    for x in o:
        print(x, end = '')
    print('}')

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)

if __name__ == '__main__':
    main()
