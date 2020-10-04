import library
def main():
    #Answering the first question
    #Defining the input functions for question 1
    def f1(x):
        import math
        r=float(float(math.log(x,math.exp(1)))-float(math.sin(x)))
        return r
    def f2(x):
        import math
        r=float(float(-x)-float(math.cos(x)))
        return r
    print("For the first function for first qustion using the interval [1.5,2.5]")
    #Calling functions from the library and finding the roots of given equations
    a,x,y=library.bisection(1.5,2.5,f1)
    file1=open("bisection_1a.txt",'w')
    library.array_2D_to_txt(x,y,file1)
    print("Root obtained by bisection method is:",a)
    a,x,y=library.regula_falsi(1.5,2.5,f1)
    file2=open("regula_falsy_1a.txt",'w')
    library.array_2D_to_txt(x,y,file2)
    print("Root obtained by regula_falsi method is:",a)
    a,x,y=library.newton_raphson(1.5,f1)
    file3=open("newton_raphson_1a.txt",'w')
    library.array_2D_to_txt(x,y,file3)
    print("Root obtained by newton raphson method is:",a)
    print("For the second function for first qustion using the interval [-3,-1]")
    a,x,y=library.bisection(-3,-1,f2)
    file11=open("bisection_1b.txt",'w')
    library.array_2D_to_txt(x,y,file11)
    print("Root obtained by bisection method is:",a)
    a,x,y=library.regula_falsi(-3,-1,f2)
    file22=open("regula_falsy_1b.txt",'w')
    library.array_2D_to_txt(x,y,file22)
    print("Root obtained by regula_falsi method is:",a)
    a,x,y=library.newton_raphson(-1,f2)
    file33=open("newton_raphson_1b.txt",'w')
    library.array_2D_to_txt(x,y,file33)
    print("Root obtained by newton raphson method is:",a)

    #Answering the second question
    #The input array containing the coefficients of the given polynomial
    z=[1.0,-3.0,-7.0,27.0,-18.0]
    print("For the second question")
    print("The array containing the coefficients of the given polynomial is:",z)
    #Computing roots of the polynomial using Laguerre's method
    a=library.root_polynomial_laguerre(4,z)
    print("The array containing the roots of the given polynomial is:",a)
main()
#Outputs
#For the first question
#For the first function for first qustion using the interval [1.5,2.5]
#Root obtained by bisection method is:2.2191076278686523
#Root obtained by regula_falsi method is:2.2191071418525734
#Root obtained by newton raphson method is:2.2191071489137406
#For the second function for first qustion using the interval [-3,-1]   
#Root obtained by bisection method is:-0.7390844821929932
#Root obtained by regula_falsi method is:-0.7390851291322078
#Root obtained by newton raphson method is:-0.7390851332151608
#For the second question
#The array containing the coefficients of the given polynomial is:[1.0,-3.0,-7.0,27.0,-18.0]
#The array containing the roots of the given polynomial is:[3.0,2.0,1.0,-3.0]
    
    
            
            
            
    
                
                    
                    
                
            
        