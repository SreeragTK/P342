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
def partial_pivot2DX2D(n,b,r):
    i=r
    k=0
    l=0
    h=len(n)
    if n[r][r]==0:      
        for i in range(r,(h-1)):
            if n[r][r]==0 and abs(n[i+1][r])>abs(n[r][r]):
                for j in range(h):
                    k=n[i+1][j]
                    n[i+1][j]=n[r][j]
                    n[r][j]=k
                    l=b[i+1][j]
                    b[i+1][j]=b[r][j]
                    b[r][j]=l
            else:
                continue
    return n,b
def gauss_jordan(n,b):
    h=len(n)
    for r in range(h):
        partial_pivot(n, b, r)
        pivot=n[r][r]
        for c in range(h):
            n[r][c]=n[r][c]/pivot
        b[r]=b[r]/pivot
        for r2 in range(h):
            if r2==r or n[r2][r]==0:
                continue
            else:
                factor=n[r2][r]
                for c2 in range(h):
                    n[r2][c2]=n[r2][c2]-(n[r][c2]*factor)
                b[r2]=b[r2]-(factor*b[r])
    return n,b
def inverse(n):
    h=len(n)
    b=[]
    for i in range(h):
        row=[]
        for j in range(h):
            if i==j:
                row.append(1)
            else:
                row.append(0)
        b.append(row)
    for r in range(h):
        partial_pivot(n, b, r)
        pivot=n[r][r]
        for c in range(h):
            n[r][c]=n[r][c]/pivot
            b[r][c]=b[r][c]/pivot
        for r2 in range(h):
            if r2==r or n[r2][r]==0:
                continue
            else:
                factor=n[r2][r]
                for c2 in range(h):
                    n[r2][c2]=n[r2][c2]-(n[r][c2]*factor)
                    b[r2][c2]=b[r2][c2]-(b[r][c2]*factor)
    return b
def matrix_multiplication_1DX1D(a,b):
    f=len(a)
    l=[0]
    for i in range(f):
        l[0]+=(a[i]*b[i])
    return l
def matrix_multiplication_1DX2D(a,b):
    f=len(a)
    d=len(b[0])
    l=[]
    for i in range(d):
        l.append(0)
    for i in range(d):
        for j in range(f):
            l[i]=l[i]+((a[j])*(b[j][i]))
    return l
def matrix_multiplication_2DX1D(a,b):
    f=len(a)
    k=len(a[0])
    l=[]
    row=[0]
    for i in range(f):
        l.append(row)
    for i in range(f):
        for j in range(k):
            l[i][0]+=(a[i][j]*b[j])
    return l
def matrix_multiplication_2DX2D(a,b):
    f=len(a)
    d=len(b[0])
    k=len(a[0])    
    l=[]
    for i in range(f):
        row=[]
        for j in range(d):
            row.append(0.0)
        l.append(row)
    i=0
    j=0
    s=0
    g=0
    h=0
    while h<f and g<f:
        while i<d and s<d:
            while j<k:
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
def matrix_formation2D(a):
    m=len(a)
    n=len(a[0])
    l=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(0.0)
        l.append(row)
    for i in range(m):
        for j in range(n):
            l[i][j]=float(a[i][j])
    return l
def Identity_matrix():
    b=[]
    for i in range(4):
        row=[]
        for j in range(4):
            if i==j:
                row.append(1)
            else:
                row.append(0)
        b.append(row)
    return b
def LU_decomposition(m,b):
    n=len(m)
    a=[[0.0 for x in range(n)]for y in range(n)]
    #decomposing the given matrix into Upper and lower triangular matrix
    for j in range(n):
        partial_pivot(m,b,j)
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
def forward_substitution(m,b):
    n=len(m)
    y=[0.0 for x in range(n)]
    for i in range(n): 
        sum=0.0
        for j in range(i):
            sum+=((m[i][j])*(y[j]))
        y[i]=b[i]-sum
    return y
def backward_substitution(m,y):
    n=len(m)
    x=[0.0 for k in range(n)] 
    for i in reversed(range(n)):
        partial_pivot(m, y, i)
        sum=0.0
        for j in reversed(range((i+1),n)):
            sum+=((m[i][j])*(x[j]))
        x[i]=(y[i]-sum)/(m[i][i])
    return x

    
