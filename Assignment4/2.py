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
    a1=f1.read()
    a2=[item.split(" ") for item in a1.split("\n")[:4]]
    #function for formation of matrix in float
    A2=mylibrary.matrix_formation2D(a2)
    print("The given matrix is:",A2)
    b=mylibrary.Identity_matrix()
    #we are computing inverse of the matrix using the formula A(A_inverse)=I
    #computing LU decomposed form of the given system
    M1,B=LU_decomposition(A2, b)
    #Checking whether the diterminent of the given matrix is non zero or not
    p=1
    for i in range(4):
        p=p*(M1[i][i])
    print("The diterminant of the system is:",p,"which is nonzeo ,so inverse of the matrix exist")
    print("The LU decomposed form of the given system is:",M1)
    #solving equation Ly=b & Ux=y considering y,b,x column vise
    b=[[0.0 for i in range(4)]for j in range(4)]
    for i in range(4):
        for j in range(4):
            b[i][j]=B[j][i]
    y=[]
    k=[]
    #computing 'y' matrix
    for i in range(4):
        y.append(mylibrary.forward_substitution(M1,b[i]))
    y1=[[0.0 for i in range(4)]for j in range(4)]
    for i in range(4):
        for j in range(4):
            y1[i][j]=y[j][i]
    print("y matrix is:",y1)
    #computing 'x' whixh is the inverse of the given system
    for i in range(4):
        k.append(mylibrary.backward_substitution(M1,y[i]))
    x=[[0.0 for i in range(4)]for j in range(4)]
    for i in range(4):
        for j in range(4):
            x[i][j]=k[j][i]
    print("The inverse of the given matrix is:",x)
main()
#The outputs are
#The given matrix is:[[0.0,2.0,8.0,6.0],[0.0,0.0,1.0,2.0],[0.0,1.0,0.0,1.0],[3.0,7.0,1.0,0.0]]
#The diterminant of the system is: -36.0 which is nonzero ,so inverse of the matrix exist
#The LU decomposed form of the given system is:[[3.0,7.0,1.0,0.0],[0.0,1.0,0.0,1.0],[0.0,0.0,1.0,2.0],[0.0,2.0,8.0,-12.0]]
#y matrix is:[[0.0,0.0,0.0,1.0,],[0.0,0.0,1.0,0.0],[0.0,1.0,0.0,0.0],[1.0,-8.0,-2.0,0.0]]
#The inverse of the given matrix is:[[-0.249999,1.6666,-1.8333,0.33333],[0.0833333,-0.6666,0.83333,0.0],[0.16666,-0.33333,-0.333333,0.0],[-0.083333,0.66666,0.166666,0.0]]




    
    

        
        