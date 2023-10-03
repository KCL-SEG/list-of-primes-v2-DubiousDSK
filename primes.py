"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    
    if number_of_primes < 1:
        raise ValueError
    
    i = 0
    x = 2
    while i < number_of_primes:
        y = 1
        counter = 0
        while y <= x:
            if (x % y) != 0:
                counter += 1
            y += 1
        if counter == (x - 2):
            list.append(x)
            i += 1
        x += 1
    return list
