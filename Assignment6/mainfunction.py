import math
import library6
def main():
    def f1(x):
        return x/(1+x)
    def f2(x):
        return math.exp(-(x*x))
    #Answering the 2nd question
    print("For the first question")
    print("For N=5:")
    print("Mid-point method:",library6.midpoint(1,3,5,f1))
    print("Trapezoidal method:",library6.trapezoidal(1,3,5,f1))
    print("Simpson's method:",library6.simpson(1,3,5,f1))
    print("For N=10:")
    print("Mid-point method:",library6.midpoint(1,3,10,f1))
    print("Trapezoidal method:",library6.trapezoidal(1,3,10,f1))
    print("Simpson's method:",library6.simpson(1,3,10,f1))
    print("For N=25:")
    print("Mid-point method:",library6.midpoint(1,3,25,f1))
    print("Trapezoidal method:",library6.trapezoidal(1,3,25,f1))
    print("Simpson's method:",library6.simpson(1,3,25,f1))
    #Answering the 3rd question
    print("For the second question")
    print("The N values corresponding to maximum error 0.001")
    print("For Mid-point method N=",library6.N_value(0,1,0.001,f2,library6.midpoint))
    print("For Trapezoidal method N=",library6.N_value(0,1,0.001,f2,library6.trapezoidal))
    print("For Simpson's method N=",library6.N_value(0,1,0.001,f2,library6.simpson))
    #Calculating the corresponding integral values in the range(0,1)
    print("For the third question")
    print("The corresponding integral values for these N values")
    print("For Mid-point method:",library6.midpoint(0,1,library6.N_value(0,1,0.001,f2,library6.midpoint),f2))
    print("For Trapezoidal method:",library6.trapezoidal(0,1,library6.N_value(0,1,0.001,f2,library6.trapezoidal),f2))
    print("For Simpson's method:",library6.simpson(0,1,library6.N_value(0,1,0.001,f2,library6.simpson),f2))
    #Answering the 4th question
    def f3(x):
        return (4/(1+(x*x)))
    #Monte-carlo integral solution for the given function for N=10000
    print("Monte-carlo solution for N=10000. The integral and the variance respectively")
    a,b=library6.monte_carlo(0,1,10000,f3)
    print("The integral=",a,"Standard Deviation=",b)
    #For plotting Fn(pi) vs N
    arr=[[0.0 for i in range(1000)]for j in range(2)]
    n=10
    for i in range(1000):
        a,b=library6.monte_carlo(0,1,n,f3)
        arr[0][i]=(i+1)
        arr[1][i]=a
        n+=10
    file1=open("integral_vs_N.txt",'w')
    library6.array_2D_to_txt(arr,file1)   
main()
#The outputs are
#For the first question
#For N=5:
#Mid-point method: 1.3080921142840647
#Trapezoidal method: 1.3043650793650796
#Simpson's method: 1.3068497693110694
#For N=10:
#Mid-point method: 1.3071646395900398
#Trapezoidal method: 1.3062285968245722
#Simpson's method: 1.3068526253348838
#For N=25:
#Mid-point method: 1.3069028019555278
#Trapezoidal method: 1.3067528394240822
#Simpson's method: 1.3068528144450458
#For the second question
#The N values corresponding to maximum error 0.001
#For Mid-point method N= 10
#For Trapezoidal method N= 13
#For Simpson's method N= 3
#The corresponding integral values for these N values
#For Mid-point method: 0.7471308777479975
#For Trapezoidal method: 0.7464612610366896
#For Simpson's method: 0.7468303914893448
#For the third question
#Monte-carlo solution for N=10000. The integral and the standard deviation respectively
#integral=3.140969505154503 Standard deviation=0.6461143619404108    
