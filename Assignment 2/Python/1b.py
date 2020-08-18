arr=[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
i=0
j=0
k=0
l=0
m=0
while i<6:
    while m<6:
        while j<6:
            while l<6:
                k=k+abs(arr[i][m]-arr[j][l])+abs(i-j)
                l+=1
            l=0    
            j+=1
        j=0    
        m+=1
    m=0
    i+=1
average=(k)/(36*36)
print("The average distance is:",average)
#The output is:
#The avarage distance is:3.88889
