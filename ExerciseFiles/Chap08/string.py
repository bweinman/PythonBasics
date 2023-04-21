#!/usr/bin/env python3
# hello.py by Bill Weinman [https://bw.org]
# as of 2023-03-29

class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__':
    main()
