#!/usr/bin/env python3
# tuple.py by Bill Weinman [https://bw.org]
# as of 2023-03-26

def print_tuple(o):
    for i in o: print(i, end=' ')
    print()

def main():
    game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    print_tuple(game)

if __name__ == '__main__':
    main()
