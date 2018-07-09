#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mathematical functions which are not adequately covered by standard libraries.

Standard libraries are:

* [`math`](https://docs.python.org/3/library/math.html)
* [`scipy`](https://docs.scipy.org/doc/scipy/reference/)
* [`sympy`](http://docs.sympy.org/latest/index.html)

"""

from __future__ import absolute_import

# core functions
import math as math_stl


def generate_primes():
    """
    Generate an infinite sequence of prime numbers.

    The algorithm was originally written by David Eppstein, UC Irvine. See:
    http://code.activestate.com/recipes/117119/

    Examples
    --------
    >>> g = generate_primes()
    >>> next(g)
    2
    >>> next(g)
    3
    >>> next(g)
    5
    """
    divisors = {}  # map number to at least one divisor

    candidate = 2  # next potential prime

    while True:
        if candidate in divisors:
            # candidate is composite. divisors[candidate] is the list of primes
            # that divide it. Since we've reached candidate, we no longer need
            # it in the map, but we'll mark the next multiples of its witnesses
            # to prepare for larger numbers
            for p in divisors[candidate]:
                divisors.setdefault(p + candidate, []).append(p)
            del divisors[candidate]
        else:
            # candidate is a new prime
            yield candidate

            # mark its first multiple that isn't
            # already marked in previous iterations
            divisors[candidate * candidate] = [candidate]

        candidate += 1


def factorize(number):
    """
    Get the prime factors of an integer except for 1.

    Parameters
    ----------
    number : int

    Returns
    -------
    primes : iterable

    Examples
    --------
    >>> factorize(-17)
    [-1, 17]
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(3**25)
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    >>> factorize(1)
    [1]
    """
    if not isinstance(number, int):
        raise ValueError('integer expected, but type(number)={}'
                         .format(type(number)))
    if number < 0:
        return [-1] + factorize(number * (-1))
    elif number == 0:
        raise ValueError('All primes are prime factors of 0.')
    else:
        for i in range(2, int(math_stl.ceil(number**0.5)) + 1):
            if number % i == 0:
                if i == number:
                    return [i]
                else:
                    return [i] + factorize(int(number / i))
        return [number]


def is_prime(number):
    """
    Check if a number is prime.

    Parameters
    ----------
    number : int

    Returns
    -------
    is_prime_number : bool

    Examples
    --------
    >>> is_prime(-17)
    False
    >>> is_prime(17)
    True
    >>> is_prime(47055833459)
    True
    """
    return len(factorize(number)) == 1
