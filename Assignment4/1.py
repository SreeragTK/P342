import mylibrary
#defining function for LU decomposition
def LU_decomposition(m,b):
    n=len(m)
    a=[[0.0 for x in range(n)]for y in range(n)]
    #decomposing the given matrix into Upper and lower triangular matrix
    for j in range(n):
        mylibrary.partial_pivot(m,b,j)
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
#defining function for forward substitution
def forward_substitution(m,b):
    n=len(m)
    y=[0.0 for x in range(n)]
    for i in range(n):
        sum=0.0
        for j in range(i):
            sum+=((m[i][j])*(y[j]))
        y[i]=b[i]-sum
    return y
#defining function for forward substitution
def backward_substitution(m,y):
    n=len(m)
    x=[0.0 for k in range(n)] 
    for i in reversed(range(n)):
        sum=0.0
        for j in reversed(range((i+1),n)):
            sum+=((m[i][j])*(x[j]))
        x[i]=(y[i]-sum)/(m[i][i])
    return x
def main():
    #Opening matrix file
    f1=open("A.txt","r")
    #function for formation of matrix in float
    A=mylibrary.matrix_formation2D(f1)
    print("The given 'A' matrix is:",A)
    f2=open("B.txt","r")
    B=mylibrary.matrix_formation1D(f2)
    print("The given 'B' matrix is:",B)
    #computing the LU decomposed form
    LU,b=LU_decomposition(A,B)
    print("LU decomposition of the given matrix is:",LU)
    #computing X&Y values
    y=forward_substitution(LU,b)
    print("The 'Y' values are:",y)
    print("The 'X' values are:",backward_substitution(LU,y))
main()
#The outputs are
#The given 'A' matrix is: [[1.0,0.0,1.0,2.0],[0.0,1.0,-2.0,0.0],[1.0,2.0,-1.0,0.0],[2.0,1.0,3.0,-2.0]]
#The given 'B' matrix is:[6.0,-3.0,-2.0,0.0]
#The LU decomposition of the given matrix is:[[1.0,0.0,1.0,2.0],[0.0,1.0,-2.0,0.0],[1.0,2.0,2.0,-2.0],[2.0,1.0,1.5,-3.0]]
#The 'Y' values are:[6.0,-3.0,-2.0,-6.0]
#The 'X' values are:[1.0,-1.0,1.0,2.0]