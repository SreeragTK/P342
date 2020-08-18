a=[1,3,6]
print("The vector A is:",a)
b=[2,7,9]
print("The vector B is:",b)
Sum=[0,0,0]
dot_product=0
i=0
while i<3:
    Sum[i]=a[i]+b[i]
    i+=1
print("The sum of these vectors is:",Sum)
i=0
while i<3:
    dot_product=dot_product+(a[i]*b[i])
    i+=1
print("The dot product of these to vectors is:",dot_product)