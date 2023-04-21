#!/usr/bin/env python3
# decorator.py by Bill Weinman [https://bw.org]
# as of 2023-03-28

import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000:.3f} ms')
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 987654)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

if __name__ == '__main__':
    main()
