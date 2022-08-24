flag = True

def cs():
    for i in range(40):
        print('\n')

def reduce_sf(f,sf):
    f = str(f)
    f = f[:(sf+1)]
    f = float(f)
    return f

def fraction(f):
    if f.is_integer():
        return str(int(f))
    dom = 1.0
    while not dom*f.is_integer():
        print(dom*f,f,dom)
        dom += 1
    num = f//1
    while num/dom != f:
        num += f/abs(f)
    return( str(int(num)) + '/' + str(int(dom)))

def is_positive(f):
    if f < 0:
        return 0
    else:
        return 1

while flag:
    try:
        cs()
        print('Use the format ax^2 + bx + c')
        a = float(raw_input('a: '))
        b = float(raw_input('b: '))
        c = float(raw_input('c: '))
        flag = False
    except KeyboardInterrupt:
        break
    except:
       flag = True


try:
    if a  == 0:
        print('---------------------------------------------------------------------------')
        print(str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c))
        print('This equasion is not a quadratic. Please enter a quadratic equasion')

    if a == 1:
        b_ = b/2
        brc = '(x' + ('+'*is_positive(b_) + fraction(b_))*bool(b_) + ')^2'
        const = -1*(b_**2) + c
        const = ('+'*is_positive(const) + fraction(const))*bool(const)
        if const:
            const = const[0] + ' ' + const[1:]
        print(brc+ ' ' + const)
    else:
        b_ = b/(2*a)
        brc = fraction(a) + '(x' + ('+'*is_positive(b_) + fraction(b_))*bool(b_) + ')^2'
        const = -1*a*(b_**2) + c
        const = ('+'*is_positive(const) + fraction(const))*bool(const)
        const = const[0] + ' ' + const[1:]
        print(brc+ ' ' + const)
except:
    a = 0