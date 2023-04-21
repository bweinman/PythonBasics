#!/usr/bin/env python3
# kwargs.py by Bill Weinman [https://bw.org]
# as of 2023-03-28

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

if __name__ == '__main__':
    main()
