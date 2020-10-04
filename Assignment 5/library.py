#defining function for bracketing
def bracketing(a,b,f):
    import math
    if f(a)==float(0):
        print("Your root is:",a)
        return a,b
    if f(b)==float(0):
        print("your root is:",b)
        return a,b
    if (f(a)*f(b))<float(0):
        print("Your function is already bracketed with your initial guess")
        return a,b
    #for f(a) and f(b) are in same side of the root
    if (f(a)*f(b))>0.0:
        if abs(f(a))>abs(f(b)): 
            for i in range(15):
                if (f(a)*f(b))<float(0):
                    return a,b
                if (f(a)*f(b))==float(0):
                    print("Your root is:",b)
                    return a,b
                else:
                    b=b+(0.5*(b-a))
                    print(b,i)
        if abs(f(a))<abs(f(b)):
            for i in range(15):
                if (f(a)*f(b))<float(0):
                    return a,b
                if (f(a)*f(b))==float(0):
                    print("Your root is:",a)
                    return a,b
                else:
                    a=a-(0.5*(b-a))
                    print(a,i)
#defining function for bisection
def bisection(c,d,f):
    import math
    X=[]
    Y=[]
    a,b=bracketing(c,d,f)
    for i in range(25):
        X.append(i)
        c=((a+b)/2)
        if f(a)==0:
            print("Your root is:",a)
            return a,X,Y
        if f(b)==0:
            print("your root is:",b)
            return b,X,Y
        if (f(a)*f(c))<0:
            b=c
            if (abs(a-b))<(.000001):
                print("Your root is:",b)
                return b,X,Y
        if (f(a)*f(c))>0:
            a=c
            if (abs(a-b))<(.000001):
                print("Your root is:",a)
                return a,X,Y
        m=abs(a-b)
        Y.append(m)
        print(m,i)
#defining function for regula_falsi
def regula_falsi(c,d,f):
    import math
    X=[]
    Y=[]
    a,b=bracketing(c,d,f)
    m=0.0
    n=0.0
    for i in range(25):
        X.append(i)
        c=b-(((b-a)*f(b))/(f(b)-f(a)))
        m=c-n
        Y.append(abs(m))
        n=c
        if f(a)==0:
            print("Your root is:",a)
            return a,X,Y
        if f(b)==0:
            print("your root is:",b)
            return b,X,Y
        if (f(a)*f(c))<0:
            b=c
            if (abs(m))<(.000001):
                print("Your root is:",b)
                return b,X,Y
        if (f(a)*f(c))>0:
            a=c
            if (abs(m))<(.000001):
                print("Your root is:",a)
                return a,X,Y
        print(abs(m),i)
        print(a)
#defining funtion for finding first derivative
def first_derivative(f,x,h):
    import math
    a=((f(x+h)-f(x-h))/(2*h))
    return a
#defining funtion for newton_rapson method
def newton_raphson(a,f):
    import math
    X=[]
    Y=[]
    for i in range(25):
        X.append(i)
        m=a
        a=a-(f(a)/first_derivative(f,a,.01))
        n=a-m
        Y.append(abs(n))
        print(n,i)
        if abs(n)<(0.000001):
            print("Your root is:",a)
            return a,X,Y
    return a,X,Y
#definig function for creating a polynomial from an array containing it's coefficients
def f(x,a):
    import math
    r=0.0
    for i in range(len(a)):
        r=r+(float(a[i])*math.pow(x,(len(a)-(i+1))))
    return r
#defining function for finding first derivative of a polynomial at a point
def first_derivative_polynomial(x,a,h):
    import math
    b=float((f(x+h,a)-f(x-h,a))/(2*h))
    return b
#defining function for finding second derivative of a polynomial at apoint
def second_derivative_polynomial(x,a,h):
    import math
    b=float((f(x+h,a)+f(x-h,a)-(2*f(x,a)))/(h*h))
    return b
#defining function for synthetic division
def synthetic_division(a,l):
    n=len(l)-1
    m=[0.0 for i in range(n)]
    for i in range(n):
        if i==0:
            m[i]=float(l[i])
        else:
            m[i]=(a*(m[i-1]))+float(l[i])
    return m
#defining function for finding root of a polynmial using lagurre's method
def root_polynomial_laguerre(b,l):
    import math
    #defining function for computing the algorithms in laguerre's mathod
    def function(x,c):
        n=float(len(c))
        G=first_derivative_polynomial(x,c,.01)/f(x,c)
        H=G*G-(second_derivative_polynomial(x,c,.01)/f(x,c))    
        a1=n/(G+(math.sqrt((n-1)*(n*H)-(G*G))))
        a2=n/(G-(math.sqrt((n-1)*(n*H)-(G*G))))
        if a1>a2:
            return float(a1)
        else:
            return float(a2)
    def function2(x,c):
        M=[]
        for i in range(50):
            a=x
            if f(x,c)==0:
                return x,M
            else:
                a1=function(x,c)
                x=x-a1
                if abs(a-x)<0.000001:
                    return x
        return x,M
    #Using function and function2 executing Laguerre's method
    a=[]
    n=int(len(l)-1)
    for i in range(n-1):
        if f(b,l)==0:
            a.append(b)
            m=synthetic_division(b,l)
            l=m
        else:
            z=function2(b,l)
            a.append(round(z,6))
            l=synthetic_division(float(z),l)
    a.append(float(round((-l[1])/l[0])))
    return a
#Defining function for exporting a 2D array into .txt file
def array_2D_to_txt(x,y,f1):
    M=[[0.0 for i in range(len(x))]for j in range(2)]
    print(M)
    for i in range(len(y)):
        M[0][i]=str(x[i])
        M[1][i]=str(y[i])
    n=len(x)
    for i in range(n):
        print(M[0][i],M[1][i],file=f1)
    return None


    
    
            
            
            
    
                
                    
                    
                
            
        