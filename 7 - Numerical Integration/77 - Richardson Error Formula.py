import numpy as np

#current(higher) h step value
h1 = 8
#previous(lower) h step value
h2 = 4

#order of truncation error
q = 3

def i(x):
    #integral
    return x

def e():
    #error formula
    return abs((i(h2) - i(h1))/((h1/h2)**q - 1))


def en():
    #error formula
    return abs((4.89476 - 4.89269)/((h1/h2)**q - 1))
