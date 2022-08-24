import re
mode = raw_input("Mode (b-d or d-b)? ")
while mode not in ['b-d','d-b']:
    mode = raw_input("Mode (b-d or d-b)? ")
valid = False
while not valid:
    base = raw_input("Base? ")
    if base.isdigit():
        if int(base) > 1 and int(base) < 37:
            valid = True
base = int(base)
bases = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:base]
if mode == 'b-d':
    valid = False
    while not valid:
        num = raw_input("Base number: ")
        valid = True
        for i in list(num):
            if i not in bases:
                valid = False
    num = list(num)
    num.reverse()
    out = 0
    for i in range(len(num)):
        out += int(bases.index(num[i]))*(base**i)
    print(out)
else:
    num = raw_input("Decimal number: ")
    while not num.isdigit():
        num = raw_input("Decimal number: ")
    i = 0
    num = int(num)
    while base**i <= num:
        i += 1
    out = []
    while i >= 0:
        out.append(bases[num/(base**i)])
        num -= (num/base**i)*base**i
        i -= 1
    print("".join(out[1:]))