# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 02:51:18 2019

@author: Elvin
"""

from random import randint
from math import log, floor

def to_reversed_binary(n):
    r = []
    while n > 0:
        r.append(n & 1)
        n //= 2
    return r


def test(a, n):
    """
        test(a, n) -> bool. Tests whether n is complex.
        Returns:
            - True, if n is complex.
            - False, if n is probably prime.
    """
    b = to_reversed_binary(n - 1)
    k = 1
    for i in range(len(b) - 1, -1, -1):
        x = k
        k = (k * k) % n
        if k == 1 and x != 1 and x != n - 1:
            return True     #Complex
        if b[i] == 1:
            k = (k * a) % n
    if k != 1:
        return True     #Complex
    return False        #Probably prime


def milrab(n):
    """
        milrab(n) -> bool Checks whether n is prime or not
        Returns:
        - True, if n is probably prime.
        - False, if n is complex.
    """
    if n == 1:
        return False
    s = int(floor(log(n, 2)))
    for j in range(1, s + 1):
        a = randint(1, n - 1)
        if test(a, n):
            return False                #n is complex
    return True                         #n is probably prime

print (milrab(510241663229783503211079698102859446339))
