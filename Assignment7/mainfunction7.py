import math
import library7
def main():
    #Answering the first question
    #For the first function
    def f1(y,x):
        return ((y*math.log(y))/x)
    #Taking 0.5,0.1,0.05,0.01 as different h values
    for i in range(4):
        h=[0.5,0.1,0.05,0.01]
        Y,X=library7.explicit_Euler_forward(f1,2.71828,2,h[i],int(1000*(0.01/h[i])))
        #For plotting Y vs X 
        #creating a .txt file for uploading the output X and Y values
        arr=library7.array_1D_to_2D(X,Y)
        if i==0:
            file=open("Y1a1_vs_X1a1.txt",'w')
        if i==1:
            file=open("Y1a2_vs_X1a2.txt",'w')
        if i==2:
            file=open("Y1a3_vs_X1a3.txt",'w')
        if i==3:
            file=open("Y1a4_vs_X1b4.txt",'w')
        library7.array_2D_to_txt(arr,file)
        
    #For the second function
    def f2(y,x):
        return (6-((2*y)/x))
    for i in range(4):
        h=[0.5,0.1,0.05,0.01]
        Y,X=library7.explicit_Euler_forward(f2,1,3,h[i],int(1000*(0.01/h[i])))
        #For plotting Y vs X
        #creating a .txt file for uploading the output X and Y values
        arr=library7.array_1D_to_2D(X,Y)
        if i==0:
            file=open("Y1b1_vs_X1b1.txt",'w')
        if i==1:
            file=open("Y1b2_vs_X1b2.txt",'w')
        if i==2:
            file=open("Y1b3_vs_X1b3.txt",'w')
        if i==3:
            file=open("Y1b4_vs_X1b4.txt",'w')
        library7.array_2D_to_txt(arr,file)
        
        
    #Answering the second question
    #defining f and g values which is the reduced first order form of the given second order differential equation
    def f(z,y,x):
        return z
    def g(z,y,x):
        return (1.0-x-z)
    #y and x solutions in the x range of [-5 to 5] in two steps
    #first calculating for [0,5] and then for [-5,0]
    Y,X=library7.Runge_Kutta_4(g,f,1,0,0,None,5,0.01,1000)
    #For plotting Y vs X ,uploading values to a txt file
    arr=library7.array_1D_to_2D(X,Y)
    file=open("Y2a1_vs_X2a1.txt",'w')
    library7.array_2D_to_txt(arr,file)
    #for [-5,0] by changing h t0 -0.01
    Y,X=library7.Runge_Kutta_4(g,f,1,0,0,None,5,-0.01,1000)
    #For plotting Y vs X ,uploading values to a txt file
    arr=library7.array_1D_to_2D(X,Y)
    file=open("Y2a2_vs_X2a2.txt",'w')
    library7.array_2D_to_txt(arr,file)
    
    #y and x solutions in the y range of [-5 to 5] in two steps
    #first calculating for [0,5] and then for [-5,0]
    Y,X=library7.Runge_Kutta_4(g,f,1,0,0,5,None,0.01,1000)
    #For plotting Y vs X ,uploading values to a txt file
    arr=library7.array_1D_to_2D(X,Y)
    file=open("Y2b1_vs_X2b1.txt",'w')
    library7.array_2D_to_txt(arr,file)
    #for [-5,0] by changing h t0 -0.01
    Y,X=library7.Runge_Kutta_4(g,f,1,0,0,5,None,-0.01,1000)
    #For plotting Y vs X ,uploading values to a txt file
    arr=library7.array_1D_to_2D(X,Y)
    file=open("Y2b2_vs_X2b2.txt",'w')
    library7.array_2D_to_txt(arr,file)
    
    #Answering the third question
    #defining f and g values which is the reduced first order form of the given second order differential equation
    def f(z,y,x):
        return z
    def g(z,y,x):
        return (z+1.0)
    #Now solving the equation using shooting method
    Y,X=library7.shooting_method(f,g,3.43656)
    #For plotting Y vs X ,uploading values to a txt file
    arr=library7.array_1D_to_2D(X,Y)
    file=open("Y3_vs_X3.txt",'w')
    library7.array_2D_to_txt(arr,file)
main()
#The outputs are:
#For all these three questions the ouptput is their respective plots
#Which are there in the submitted files
#the .txt files containing all the ouputs are also there in submitted files
#For the third question outputs otherthan the plot are:
#(taking .9 and 1.1 as first and second guess respectively)
#Enter your first guess:.9
#Enter your second guess:1.1
#The obtained solution for z is : 0.9999978720203266
