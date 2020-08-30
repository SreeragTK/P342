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
                    l=b[i+1]
                    b[i+1]=b[r]
                    b[r]=l
            else:
                continue
    return n,b
#defining function for gauss jordan
def gauss_jordan(n,b):
    for r in range(3):
        partial_pivot(n, b, r)
        pivot=n[r][r]
        for c in range(3):
            n[r][c]=n[r][c]/pivot
        b[r]=b[r]/pivot
        for r2 in range(3):
            if r2==r or n[r2][r]==0:
                continue
            else:
                factor=n[r2][r]
                for c2 in range(3):
                    n[r2][c2]=n[r2][c2]-(n[r][c2]*factor)
                b[r2]=b[r2]-(factor*b[r])
    return n,b
#Answering the first Question
#reading files of matrices
f1=open("m1.txt","r")
m1=f1.read()
n1=[item.split(' ') for item in m1.split('\n')[:3]]
M1=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        M1[i][j]=float(n1[i][j])
print("The first set of equations are:")
print("M1 is:",M1)
f2=open("b1.txt","r")
b1=f2.read()
v1=(b1.split(' '))
B1=[0,0,0]
for i in range(3):
    B1[i]=float(v1[i])
print("b1 is:",B1)
#computing the solution for first set of equations using defined functions
print("The solution for first set of equations is(The resulting Identity matrix and the solution set respectively):",gauss_jordan(M1,B1))
#Answering the second Question
#reading files of matrices
f3=open("m2.txt","r")
m2=f3.read()
n2=[item.split(' ') for item in m2.split('\n')[:3]]
M2=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        M2[i][j]=float(n2[i][j]) 
print("The second set of equations are:")
print("M2 is:",M2)
f4=open("b2.txt","r")
b2=f4.read()
v2=(b2.split(' '))
B2=[0,0,0]
for i in range(3):
    B2[i]=float(v2[i])
print("b2 is:",B2)
#computing the solution for second set of equations using defined functions
print("The solution for second set of equations is(The resulting Identity matrix and the solution set respectively):",gauss_jordan(M2,B2))
#The outputs are:
#The first set of equations are:
#M1 is: [[1.0,3.0,2.0],[2.0,7.0,7.0],[2.0,5.0,2.0]]
#b1 is: [2.0,-1.0,7.0]
#The solution set of first set of equations is(The resulting Identity matrix and the solution set respectively):
#([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]],[3.0,1.0,-2.0])
#Here [3.0,1.0,-2.0] is the solution set for first set of equations
#The second set of equations are:
#M2 is: [[2.0,0.0,5.0],[3.0,-1.0,2.0],[1.0,-1.0,3.0]]
#b2 is: [1.0,-2.0,3.0]
#The solution set of second set of equations is(The resulting Identity matrix and the solution set respectively):
#([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]],[-2.0,-2.0,1.0])
#Here [-2,-2.0,1.0] is the solution set for second set of equations

        
        
    
                    
                    
                
    