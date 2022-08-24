from __future__ import division
import random

def Tabletest():
    #NUMBERS
    tn = input('what number? ')
    print('')
    i = input('How many sums do you want? ')
    print('')
    a = i
    sc = 0
    while i > 0:
        rn = random.randint(0,12)

        #TEST NUMBERS
        #i = 13
        #while i > 0:
        #    rn = random.randint(0,12)
        #    ta=tn*rn
        #    print(rn)
        #    print(ta)
        #    i = i - 1
        #    print('')

        #IMORTANT NUMBERS
        ca = tn*rn
        aa = input(str("What is ")+str(tn)+str('x')+str(rn)+str('? '))

        #ANSWERS
        if ca == aa:
            print('You got it right. :-)')
            sc = sc + 1
        else:
            print(str('YOU WERE WRONG. The answer is ')+str(ca))
        i = i-1
        print('')

    #PRINT
    print(str('You got ')+str(sc)+str(' out of ')+str(a))
    scp = (sc/a)*100
    print('')
    print(str('In percentage, it is, ')+str(scp)+str('%.'))

