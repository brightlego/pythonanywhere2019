#This code will add calculate the length of the hypotenuse of a triangle using Pythagoras' theorem

import numpy as np

def calcsquare_of_a(a):
    a_sq = a**2
    return(a_sq)

'''def calcsquare_of_b(b):
    b_sq = b**2
    return(b_sq)'''

def calchypotenuse_ab(a,b):
    a_sq = calcsquare_of_a(a)
    print a_sq
    b_sq = calcsquare_of_a(b)
    print b_sq

    hypotenuse = np.sqrt(a_sq+b_sq)
    return(hypotenuse)

a = 3
b = 4

hypotenuse = calchypotenuse_ab(a,b)

hypotenuse = np.sqrt(a**2+b**2)
print(hypotenuse)
