#!/usr/bin/env python3
# inheritance.py by Bill Weinman [https://bw.org]
# as of 2023-03-29

class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t = None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n = None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s = None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None
        
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

def main():
    a0 = Kitten(name = 'fluffy', sound = 'rwar')
    a1 = Duck(name = 'donald', sound = 'quack')
    print(a0)
    print(a1)

if __name__ == '__main__':
    main()
