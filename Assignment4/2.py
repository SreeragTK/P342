import mylibrary
#defing function for LU decomposition
def LU_decomposition(m,b):
    n=len(m)
    a=[[0.0 for x in range(n)]for y in range(n)]
    #decomposing the given matrix into Upper and lower triangular matrix
    for j in range(n):
        mylibrary.partial_pivot2DX2D(m,b,j)
        for i in range(n):
            if i<=j:
                sum=0
                for k in range(i):
                    sum+=((a[i][k])*(a[k][j]))
                a[i][j]=m[i][j]-sum
            else:
                sum=0
                for k in range(j):
                    sum+=((a[i][k])*(a[k][j]))
                a[i][j]=(m[i][j]-sum)/a[j][j]
    return a,b
def main():
    #Opening matrix file
    f1=open("A2.txt","r")
    A=mylibrary.matrix_formation2D(f1)
    f2=open("A2.txt","r")
    A2=mylibrary.matrix_formation2D(f2)
    print("The given matrix(A) is:",A2)
    #we are computing inverse of the matrix using the formula A(A_inverse)=I
    #computing LU decomposed form of the given 
    b=mylibrary.Identity_matrix()
    M1,B=LU_decomposition(A2, b)
    #Checking whether the diterminent of the given matrix is non zero or not
    p=1
    for i in range(4):
        p=p*(M1[i][i])
    print("The diterminant of the system is:",p,"which is nonzeo ,so inverse of the matrix exist")
    print("The LU decomposed form of the given system is:",M1)
    #solving equation Ly=b & Ux=y considering y,b,x column vise
    b=mylibrary.transpose(B)
    y=[]
    k=[]
    #computing 'y' matrix
    for i in range(4):
        y.append(mylibrary.forward_substitution(M1,b[i]))
    y1=mylibrary.transpose(y)
    print("y matrix is:",y1)
    #computing 'x' whixh is the inverse of the given system
    for i in range(4):
        k.append(mylibrary.backward_substitution(M1,y[i]))
    x=mylibrary.transpose(k)
    print("The inverse of the given matrix is:",x)
    s=[[0.0 for i in range(4)]for j in range(4)]
    for i in range(4):
        for j in range(4):
            s[i][j]=round(x[i][j],2) 
    c=mylibrary.matrix_multiplication_2DX2D(A,s)
    for i in range(4):
        for j in range(4):
            s[i][j]=round(c[i][j],1) 
    print(" A*(A_inverse) is:",s)
main()
#The outputs are
#The given matrix is:[[0.0,2.0,8.0,6.0],[0.0,0.0,1.0,2.0],[0.0,1.0,0.0,1.0],[3.0,7.0,1.0,0.0]]
#The diterminant of the system is: -36.0 which is nonzero ,so inverse of the matrix exist
#The LU decomposed form of the given system is:[[3.0,7.0,1.0,0.0],[0.0,1.0,0.0,1.0],[0.0,0.0,1.0,2.0],[0.0,2.0,8.0,-12.0]]
#y matrix is:[[0.0,0.0,0.0,1.0,],[0.0,0.0,1.0,0.0],[0.0,1.0,0.0,0.0],[1.0,-8.0,-2.0,0.0]]
#The inverse of the given matrix is:[[-0.249999,1.6666,-1.8333,0.33333],[0.0833333,-0.6666,0.83333,0.0],[0.16666,-0.33333,-0.333333,0.0],[-0.083333,0.66666,0.166666,0.0]]
#A*(A_inverse) is:[[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0]]



    
    

        
        