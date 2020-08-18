arr=[1,2,3,4,5,6]
i=0
j=0
k=0
while i<6:
    while j<6:
        k=k+abs(arr[j]-arr[i])
        j+=1
    j=0
    i+=1
average=k/36
print("The average distance is:",average)

