def Gcd(a,b):
    if(b == 0):
        return a
    else:
        r = a% b
        return Gcd(b,r)
