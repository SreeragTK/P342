a=[1,3,6]
print("Matrix A is:",a)
f1=open("m.txt","r")
m=f1.read()
M=[item.split(',') for item in m.split('\n')[:3]]
print("Matrix M is:",M)
f2=open("n.txt","r")
n=f2.read()
N=[item.split(',') for item in n.split('\n')[:3]]
print("Matrix N is:",N)
i=0
j=0
k=[0,0,0]
l=[[0,0,0],[0,0,0],[0,0,0]]
while i<3:
    while j<3:
        k[i]=k[i]+(int(M[i][j])*a[j])
        j+=1
    j=0
    i+=1
print("M","x","A is:",k)
i=0
j=0
s=0
g=0
h=0

while h<3 and g<3:
    while i<3 and s<3:
        while j<3:
            l[g][s]=l[g][s]+(int(M[h][j])*int(N[j][i]))
            j+=1
        j=0    
        i+=1
        s+=1
    i=0
    s=0
    h+=1
    g+=1
print("M","x","N is:",l)
#The outputs are:
#The matrix M is:[[1,0,-1],[1,2,3],[1,-2,1]]
#The matrix N is:[[1,3,9],[-3,0,6],[2,4,5]]
#The matrix A is:[1,3,6]
#M x A is:[-5,25,1]
#The matrix M x N is:[[-1,-1,4],[1,15,36],[9,7,2]]



