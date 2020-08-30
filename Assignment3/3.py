#defining function for partial pivoting
def partial_pivot(n,b,r):
    i=r
    k=0
    l=0
    if n[r][r]==0:      
        for i in range(r,2):
            if n[r][r]==0 and abs(n[i+1][r])>abs(n[r][r]):
                for j in range(3):
                    k=n[i+1][j]
                    n[i+1][j]=n[r][j]
                    n[r][j]=k
                    l=n[i+1][j]
                    b[i+1][j]=b[r][j]
                    b[r][j]=l
            else:
                continue
    return n,b
#defining function for finding inverse with the help of function partial pivot
def inverse(n):
    b=[[1,0,0],[0,1,0],[0,0,1]]
    for r in range(3):
        partial_pivot(n, b, r)
        pivot=n[r][r]
        for c in range(3):
            n[r][c]=n[r][c]/pivot
            b[r][c]=b[r][c]/pivot
        for r2 in range(3):
            if r2==r or n[r2][r]==0:
                continue
            else:
                factor=n[r2][r]
                for c2 in range(3):
                    n[r2][c2]=n[r2][c2]-(n[r][c2]*factor)
                    b[r2][c2]=b[r2][c2]-(b[r][c2]*factor)
    return b
#defining function for matrix maltiplication
def matrix_maltiplication(a,b):
    l=[[0,0,0],[0,0,0],[0,0,0]]
    i=0
    j=0
    s=0
    g=0
    h=0
    while h<3 and g<3:
        while i<3 and s<3:
            while j<3:
                l[g][s]=l[g][s]+((a[h][j])*(b[j][i]))
                j+=1
            j=0    
            i+=1
            s+=1
        i=0
        s=0
        h+=1
        g+=1
    return l

def main():
    #reading the matrix A from a external file
    f1=open("A.txt","r")
    a=f1.read()
    a1=[item.split(' ') for item in a.split('\n')[:3]]
    A=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            A[i][j]=float(a1[i][j])  
    print("A matrix is:",A)
    #Computing inverse of A and printing it
    print("The inverse of A is:",inverse(A))
    #computing A X (A inverse)
    print("A X (A inverse) is:",matrix_maltiplication(A,inverse(A)))   
main()
#The outputs are
#A matrix is: [[1.0,-3.0,7.0],[-1.0,4.0,-7.0],[-1.0,3.0,-6.0]]
#The inverse of A is: [[-3.0,3.0,-7.0],[1.0,1.0,0.0],[1.0,0.0,1.0]]
#A X (A inverse) is: [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]