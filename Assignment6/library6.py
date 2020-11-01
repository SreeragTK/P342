import math
import random
#defining function for midpoint method
def midpoint(a,b,n,f):
    #a=lower limit b=upper limit n=no. of divisions
    h=(b-a)/n
    s=0
    for i in range(1,n+1):
        x=(a+(a+h))/2
        a+=h
        s+=(h*f(x))
    return s
#defining function for midpoint method
def trapezoidal(a,b,n,f):
    #a=lower limit b=upper limit n=no. of divisions
    h=(b-a)/n
    s=0
    x=a
    for i in range(1,n):
        x+=h
        s+=(2*f(x))
    r=(h/2)*(f(a)+s+f(b))
    return r
#defining function for midpoint method
def simpson(a,b,n,f):
    #a=lower limit b=upper limit n=no. of divisions
    h1=(b-a)/n
    #as we are approximaring the curve as quadratic
    #instead of two points we need three points for integral calculation in each step
    #so after including mid points h1 becomes h2 ,which is half of h1
    h2=h1/2
    #before including mid-points number of points were n+1
    #after including mid points number of points becomes n+1+n=2n+1
    #because for n+1 points there are n mid points
    s=0
    x=a
    for i in range((2*n)+1):
        if i==0 or i==(2*n):
            s+=((h2/3)*f(x))
        else:
            if (i%2)==0:
                s+=((h2/3)*(2*f(x)))
            else:
                s+=((h2/3)*(4*f(x)))
        x+=h2
    return s
#defining function for computing N
def N_value(a,b,e,f,method):
    #a=lower limit b=upper limit e=maximum error
    if method==midpoint:
        n=math.ceil(math.sqrt(((math.pow((b-a),3))*(2.0))/(e*24.0)))
    if method==trapezoidal:
         n=math.ceil(math.sqrt(((math.pow((b-a),3))*(2.0))/(e*12.0)))
    if method==simpson:
        n=math.ceil(math.pow((((math.pow((b-a),5))*12.0)/(e*180)),(1/4)))
    return n
#defining function for Monte-Carlo method
def monte_carlo(a,b,n,f):
    #a=lower limit b=upper limit n=no. of points
    import random
    h=0.0
    k=0.0
    l=0.0
    for i in range(n):
        s=random.uniform(a,b)
        h+=f(s)
        k+=(f(s)*f(s))
    m=((float(b-a)*h)/n)
    p=h/n
    v=math.sqrt((k/n)-(math.pow(p,2)))
    return m,v
#defining function for converting 2D array to .txt file
def array_2D_to_txt(x,f1):
    M=[[0.0 for i in range(len(x[0]))]for j in range(2)]
    for i in range(len(x[0])):
        M[0][i]=str(x[0][i])
        M[1][i]=str(x[1][i])
    n=len(x[0])
    for i in range(n):
        print(M[0][i],M[1][i],file=f1)
    return None


    
    

                
        
    