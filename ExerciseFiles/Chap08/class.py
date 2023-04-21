#!/usr/bin/env python3
# class.py by Bill Weinman [https://bw.org]
# as of 2023-03-29

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    donald.move()

if __name__ == '__main__':
    main()
