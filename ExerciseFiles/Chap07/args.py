#!/usr/bin/env python3
# args.py by Bill Weinman [https://bw.org]
# as of 2023-03-28

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')

def main():
    kitten('meow', 'grrr', 'purr')

if __name__ == '__main__':
    main()
