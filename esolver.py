from __future__ import division
from math import sqrt
alphabet = list('abcdefghijklmnopqrstuvwxyz')
def errorfinder(nerror):
    errors = {1:"Cannot square root a negative number"}
    print(errors[nerror])

def lformula(ab):
    [a,b] = ab
    ans = (-1*b)/a
    return(ans)
def qformula(abc):
    [[a,b,c]] = abc
    ans = b**2
    ans = -b+(-4*a*c)
    if ans < 0:
        return(["ERROR 1"])
    ans = sqrt(ans)
    ans = [(-1*b)+ans,(-1*b-ans)]
    for i in range(0,2):
        ans[i] = str(ans[i]/(2*a))
    return(ans)
def mformula(aetc):
    def erunner(x,aetc):
        ans_ = 0
        for i in range(0,len(aetc)):
            ans_ += (x**i + aetc[i])
        return(ans_)
    divisor = 1
    ans = 0
    for i in range(0,50):
        if erunner(ans,aetc) != 0:
            if erunner(ans+divisor,aetc) == 0:
                ans += divisor
            elif erunner(ans-divisor,aetc) == 0:
                ans -= divisor
            elif erunner(ans+divisor,aetc) > erunner(ans,aetc) and erunner(ans+divisor,aetc) < 0:
                ans += divisor
            elif erunner(ans-divisor,aetc) > erunner(ans,aetc) and erunner(ans-divisor,aetc) < 0:
                ans -= divisor
            elif erunner(ans+divisor,aetc) < erunner(ans,aetc) and erunner(ans+divisor,aetc) < 0:
                ans -= divisor
            elif erunner(ans-divisor,aetc) < erunner(ans,aetc) and erunner(ans-divisor,aetc) < 0:
                ans += divisor

            elif erunner(ans+divisor,aetc) > erunner(ans,aetc) and erunner(ans+divisor,aetc) > 0:
                ans -= divisor
                divisor/=2
            elif erunner(ans-divisor,aetc) > erunner(ans,aetc) and erunner(ans-divisor,aetc) > 0:
                ans += divisor
                divisor/=2
            elif erunner(ans+divisor,aetc) < erunner(ans,aetc) and erunner(ans+divisor,aetc) > 0:
                ans += divisor
                divisor/=2
            elif erunner(ans-divisor,aetc) < erunner(ans,aetc) and erunner(ans-divisor,aetc) > 0:
                ans -= divisor
                divisor/=2
    return(ans)

etype = ''
while etype != 'quit':
    etype = raw_input("How many parts to your equasion? (type help for help or quit to quit) ")
    if etype == 'help':
        hinput = input("You have reached the help screen\ntype 1 for errors\n")
        if hinput == 1:
            errorfinder(input('What error are you having? '))
    elif etype != 'quit':
        etype = int(etype)
        inputs = []
        for i in range(0,etype):
            inputs.append(input(alphabet[i] + '*x^' + str(etype-i-1) + ': '))
        if etype == 1:
            print('x = ' + str(inputs[0]))
        elif etype == 2:
            print('x = ' + str(lformula(inputs)))
        elif etype == 3:
            print('x = ' + ' or '.join(qformula([inputs])))
        else:
            print('A possible value of x = ' + str(mformula(inputs)))
