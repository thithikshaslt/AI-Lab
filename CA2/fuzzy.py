def triangular(x,a,b,c):
    v1 = (x-a)/(b-a)
    v2 = (c-x)/(c-b)

    return max(min(v1,v2),0)

def trapezoidal(x,a,b,c,d):
    v1 = (x-a)/(b-a)
    v2 = (d-x)/(d-c)

    return max(min(v1,1,v2),0)

