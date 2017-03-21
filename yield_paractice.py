#!/usr/bin/env python

import math

def simple_generator():
    for i in range(3):
        print "generator is invokded :: {}".format(i)
        yield i

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    i = 0
    while i < number:
        if is_prime(i):
            print 'i {}'.format(i)
            data = yield i
            print 'data {}'.format(data)
            print 'datatata'
        i += 1

if __name__ == '__main__':
    sg = simple_generator()
    print sg.next()
    print sg.next()
    print sg.next()
    print '#'*50
    prime_generator = get_primes(20)
    val = prime_generator.send(None)
    print 'val = {}'.format(val)
    val = prime_generator.send('send {}'.format(val))
    print 'val = {}'.format(val)
    val = prime_generator.send('send {}'.format(val))
    print 'val = {}'.format(val)
    print '#'*50
