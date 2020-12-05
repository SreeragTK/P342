import math
#defining function for Explicit Euler
def explicit_Euler_forward(f,y_0,x_0,h,n):
    #arrays for storing outputs
    #these arrays will be returned as the output
    Y=[]
    X=[]
    #functions for calculations in explicit euler
    def yn(y,x):
        y1=y+((f(y,x))*h)
        return y1
    y=y_0
    Y.append(y_0)
    X.append(x_0)
    for i in range(n):
        x_n=(x_0)+(i*h)
        k=yn(y,x_n)
        Y.append(k)
        X.append(x_n+h)
        y=k
    return Y,X
#defining function for RK4
def Runge_Kutta_4(g,f,z_0,y_0,x_0,y_range,x_range,h,n):
    #arrays for storing outputs
    #these arrays will be returned as the output
    Y=[]
    X=[]
    Z=[]
    K=[0.0,0.0,0.0,0.0]
    L=[0.0,0.0,0.0,0.0]
    #functions for calculations in RK4
    #for kand 1 calculation
    def k_and_l(zn,yn,xn):
        k=h*(f(zn,yn,xn))
        l=h*(g(zn,yn,xn))
        K[0]=k
        L[0]=l
        for i in range(2):
            K[i+1]=h*f((zn+(l/2)),(yn+(k/2)),(xn+(h/2)))
            L[i+1]=h*g((zn+(l/2)),(yn+(k/2)),(xn+(h/2)))
            k=K[i+1]
            l=L[i+1]
        K[3]=h*f((zn+l),(yn+k),(xn+h))
        L[3]=h*g((zn+l),(yn+k),(xn+h))
        return L,K
    #for y and z of next step 
    def y_and_z(zn,yn,L,K):
        y1=yn+((1/6)*(K[0]+(2*K[1])+(2*K[2])+K[3]))
        z1=zn+((1/6)*(L[0]+(2*L[1])+(2*L[2])+L[3]))
        return z1,y1
    z_n=z_0
    y_n=y_0
    x_n=x_0
    L,K=k_and_l(z_0,y_0,x_0)
    Z.append(z_0)
    Y.append(y_0)
    X.append(x_0)
    #calculation with various conditions of x and y inputs
    #storing each ouput in the arrays defined
    for i in range(n):
        if x_range==None and y_range!=None:
            if abs(y_n)<abs(y_range):
                x_n=(x_0)+(i*h)
                L,K=k_and_l(z_n,y_n,x_n)
                z,y=y_and_z(z_n,y_n,L,K)
                Z.append(z)
                Y.append(y)
                X.append(x_n+h)
                z_n=z
                y_n=y
            else:
                continue
        if y_range==None and x_range!=None:
            if abs(x_n)<abs(x_range):
                x_n=(x_0)+(i*h)
                L,K=k_and_l(z_n,y_n,x_n)
                z,y=y_and_z(z_n,y_n,L,K)
                Z.append(z)
                Y.append(y)
                X.append(x_n+h)
                z_n=z
                y_n=y
            else:
                continue
        if y_range==None and x_range==None:
            x_n=(x_0)+(i*h)
            L,K=k_and_l(z_n,y_n,x_n)
            z,y=y_and_z(z_n,y_n,L,K)
            Z.append(z)
            Y.append(y)
            X.append(x_n+h)
            z_n=z
            y_n=y
        if y_range!=None and x_range!=None:
            if abs(y_n)<abs(y_range) and abs(x_n)<abs(x_range):
                x_n=(x_0)+(i*h)
                L,K=k_and_l(z_n,y_n,x_n)
                z,y=y_and_z(z_n,y_n,L,K)
                Z.append(z)
                Y.append(y)
                X.append(x_n+h)
                z_n=z
                y_n=y
            else:
                continue     
    return Y,X
#Defining function for shooting method
def shooting_method(f,g,beta):
    #functions for calculation using RK4
    def RK4(c1,c2):
        Y1,X1=Runge_Kutta_4(g,f,c1,1.0,0.0,None,None,.01,100)
        Y2,X2=Runge_Kutta_4(g,f,c2,1.0,0.0,None,None,.01,100)
        return Y1,X1,Y2,X2
    #function which asks user input and returns suitable guess(c_h and c_t) which makes yn enclosed between yn values returned from RK4
    def guess():
        for i in range(30):
            guess_1=input("Enter your first guess:")
            c_h=float(guess_1)
            guess_2=input("Enter your second guess:")
            c_t=float(guess_2)
            Y1,X1,Y2,X2=RK4(c_h,c_t)
            if (Y2[100]>beta and Y1[100]>beta) or (Y2[100]<beta and Y1[100]<beta):
                print("Try with another value of c_h or c_t" )
                continue
            else:
                return c_h,c_t 
    c_h,c_t=guess()  
    #calculations using the above defined functions
    for i in range(30): 
        Y1,X1,Y2,X2=RK4(c_h,c_t)
        #accuracy stting upto 0.003(clossness of beta value with the calculated value from RK4 using guessed z value)
        if abs(Y1[100]-beta)<0.003:
            print("The obtained solution for z is :",c_h)
            return Y1,X1
        if abs(Y2[100]-beta)<0.003:
            print("The obtained solution for z is :",c_t)
            return Y2,X2
        if Y1[100]>beta and Y2[100]<beta:
            c=c_t+(((c_h-c_t)/((Y1[100])-Y2[100]))*((beta)-Y2[100]))
            Y3,X3=Runge_Kutta_4(g,f,c,1.0,0.0,None,None,.01,100)
            if abs(Y3[100]-beta)<0.003:
                print("The obtained solution for z is :",c)
                return Y3,X3
            else:
                if c<beta:
                    c_t=c
                else:
                    c_h=c
        if Y2[100]>beta and Y1[100]<beta:
            c=c_h+(((c_t-c_h)/((Y2[100])-Y1[100]))*((beta)-Y1[100]))
            Y3,X3=Runge_Kutta_4(g,f,c,1.0,0.0,None,None,.01,100)
            if abs(Y3[100]-beta)<0.003:
                print("The obtained solution for z is :",c)
                return Y3,X3
            else:
                if c<beta:
                    c_h=c
                else:
                    c_t=c
#defining function for converting 1D array to 2D array           
def array_1D_to_2D(X,Y):
        arr=[[0.0 for i in range(len(Y))]for j in range(2)]
        for i in range(len(Y)):
            arr[0][i]=X[i]
            arr[1][i]=Y[i]
        return arr
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
    
    
        
        
        