def mp1():
    v = 1
    n = 0
    b = 0
    ans = ''
    a = input("what number do you want to look for? ")
    a = float(a)
    i = 100
    while b != 1:
        v = v + 1
        n = 1.0
        while n != v:
            print(v)
            print(n)
            v_ = 3*v
            n_ = 5*n
            print(v_)
            print(n_)
            t = v_+n_
            t = float(t)
            print(t)
            t_ = v*a
            print(t_)
            print('')
            print(b)
            print('')
            if t_ == t:
                b = 1
                i = i-1
            else:
                n = n + 1
        b = 1

        i = i - 1
    n_2 = v-n
    while n > 0:
        ans = ans + ', 8'
        n=n-1
    while n_2 > 0:
        ans = ans + ', 3'
        n_2=n_2-1
    print('')
    print(ans)


