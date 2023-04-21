#!/usr/bin/env python3
# dict.py by Bill Weinman [https://bw.org]
# as of 2023-03-26

def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')

def main():
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}

    print_dict(animals)

if __name__ == '__main__':
    main()
