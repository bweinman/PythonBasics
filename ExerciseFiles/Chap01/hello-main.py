#!/usr/bin/env python3
# hello-main.py by Bill Weinman [https://bw.org]
# as of 2023-03-20

import platform

def main():
    version = platform.python_version()
    print(f'This is python version {version}')

if __name__ == '__main__': 
    main()
