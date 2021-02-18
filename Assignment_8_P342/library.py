import math
import random
def random_walk_2D(n):
    import math
    import random
    #n=number of steps
    x=0.0;xf=0.0
    y=0.0;yf=0.0
    k=0.0;l=0,0
    m=0.0
    #defining matrices for storing resultant dispacement after each step
    X=[]
    Y=[]
    for i in range(n):
        #Defining steps
        h=random.uniform(0.0,(2*(math.pi)))
        x+=math.cos(h)
        y+=math.sin(h)
        k=pow(x,2)
        l=pow(y,2)
        m=m+k+l
        X.append(x)
        Y.append(y)
    R=math.sqrt((pow(x,2)+pow(y,2)))
    R_rms=math.sqrt(m/n)
    return R,R_rms,x,y,X,Y
def monte_carlo_for_3D(x,y,z,n,f):
    def x_and_y_and_z():
        x2=random.uniform(-x,x)
        y2=random.uniform(-y,y)
        z2=random.uniform(-z,z)
        return x2,y2,z2
    V=8.0*x*y*z #It is the total volume of the xyx space
    count=0
    M=[];Q=[]
    for i in range(n):
        x3,y3,z3=x_and_y_and_z()
        if f(x3,y3,z3)<1.0:  
            count+=1
            Q=[count,x3,y3,z3]
            M.append(Q)
    #now we can compute the volume of the 3D object obtained from the given function
    Volume=(count/n)*V
    return Volume,M,count
def array_1D_to_2D(X,Y):
        arr=[[0.0 for i in range(len(Y))]for j in range(2)]
        for i in range(len(Y)):
            arr[0][i]=X[i]
            arr[1][i]=Y[i]
        return arr
#defining function for converting 2D array to .txt file
def array_2D_to_txt(x,count,f1):
    M=[[0.0 for j in range(4)]for i in range(count)]
    for i in range(count):
        M[i][0]=str(x[i][0])
        M[i][1]=str(x[i][1])
        M[i][2]=str(x[i][2])
        M[i][3]=str(x[i][3])
    for i in range(count):
        print(M[i][0],M[i][1],M[i][2],M[i][3],file=f1)
    return None
def array_2D_to_txt_transpose(x,f1):
    M=[[0.0 for j in range(5)]for i in range(len(x[0]))]
    for i in range(len(x[0])):
        M[i][0]=str(x[0][i])
        M[i][1]=str(x[1][i])
        M[i][2]=str(x[2][i])
        M[i][3]=str(x[3][i])
        M[i][4]=str(x[4][i])
    n=len(x[0])
    for i in range(n):
        print(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4],file=f1)
    return None
def transpose(a):
    m=len(a)
    n=len(a[0])
    l=[[0.0 for j in range(m)] for i in range(n)]
    for i in range(m):
        for j in range(n):
            l[i][j]=a[j][i]
    return l
def array_to_txt(x,f1):
    M=[[0.0 for i in range(len(x[0]))]for j in range(2)]
    for i in range(len(x[0])):
        M[0][i]=str(x[0][i])
        M[1][i]=str(x[1][i])
    n=len(x[0])
    for i in range(n):
        print(M[0][i],M[1][i],file=f1)
    return None
    
            
    
    
    
        