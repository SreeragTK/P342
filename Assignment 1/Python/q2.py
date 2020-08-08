n=int(input('Choose a number of your choice to compute factorial:\n'))
x=n
m=n
if n==0:
    print('The value of 0! is 1') 
else:
    if n>0:
        if n==1:
            print('The value of 1! is 1')
        else: 
            while n>1:
                x=x*(n-1)
                n=n-1
            print('The value of ', m,'! is',x)
    else: 
        print('The number you entered is negative!,please enter any positive number(zero included)')
       
        