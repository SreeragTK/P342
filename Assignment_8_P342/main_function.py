import library
import math
import random
def main():
    #Defining matrices for storing datas
    steps=[int(250),int(500),int(1000),int(2500),int(5000)]
    D1=[];D2=[];D3=[];D4=[];D5=[]
    D=[D1,D2,D3,D4,D5]
    X1=[];X2=[];X3=[];X4=[];X5=[]
    X=[X1,X2,X3,X4,X5]
    Y1=[];Y2=[];Y3=[];Y4=[];Y5=[]
    Y=[Y1,Y2,Y3,Y4,Y5]
    x1=[];x2=[];x3=[];x4=[];x5=[]
    x_final_displacement=[x1,x2,x3,x4,x5]
    y1=[];y2=[];y3=[];y4=[];y5=[]
    y_final_displacement=[y1,y2,y3,y4,y5]
    rms1=[];rms2=[];rms3=[];rms4=[];rms5=[]
    rms=[rms1,rms2,rms3,rms4,rms5]
    R_values_of_a_set=[]
    R=[];X_avg=[];Y_avg=[]
    #Computing required datas
    R_rms=0.0;x_sum=0.0;x_avg=0.0;y_sum=0.0;y_avg=0.0
    #performinh 100 random walks for 100 different step sizes
    for i in range(5):
        n=steps[i]
        r=0.0
        for j in range(100):
            R_value,r_rms,xk,yk,Xk,Yk=library.random_walk_2D(int(n))
            D[i].append(R)
            X[i].append(Xk)
            Y[i].append(Yk)
            r+=pow(r_rms,2)
            R_values_of_a_set.append(R_value)
            x_final_displacement[i].append(xk)
            y_final_displacement[i].append(yk)
            x_sum+=xk
            y_sum+=yk
        x_avg=x_sum/100
        X_avg.append(x_avg)
        y_avg=y_sum/100
        Y_avg.append(y_avg)
        R_rms=math.sqrt(r/100)
        R.append(R_rms)
    #Computing
    #Adding X datas to .txt file for plotting
    file1=open("x_datas_for__x_vs_y_plot_for_step_number_250.txt",'w')
    file2=open("x_datas_for__x_vs_y_plot_for_step_number_500.txt",'w')
    file3=open("x_datas_for__x_vs_y_plot_for_step_number_1000.txt",'w')
    file4=open("x_datas_for__x_vs_y_plot_for_step_number_2500.txt",'w')
    file5=open("x_datas_for__x_vs_y_plot_for_step_number_5000.txt",'w')
    
    library.array_2D_to_txt_transpose(X1,file1)
    library.array_2D_to_txt_transpose(X2,file2)
    library.array_2D_to_txt_transpose(X3,file3)
    library.array_2D_to_txt_transpose(X4,file4)
    library.array_2D_to_txt_transpose(X5,file5)
    
    #Adding Y_avg datas to .txt file for plotting
    file1=open("y_datas_for__x_vs_y_plot_for_step_number_250.txt",'w')
    file2=open("y_datas_for__x_vs_y_plot_for_step_number_500.txt",'w')
    file3=open("y_datas_for__x_vs_y_plot_for_step_number_1000.txt",'w')
    file4=open("y_datas_for__x_vs_y_plot_for_step_number_2500.txt",'w')
    file5=open("y_datas_for__x_vs_y_plot_for_step_number_5000.txt",'w')
    library.array_2D_to_txt_transpose(Y1,file1)
    library.array_2D_to_txt_transpose(Y2,file2)
    library.array_2D_to_txt_transpose(Y3,file3)
    library.array_2D_to_txt_transpose(Y4,file4)
    library.array_2D_to_txt_transpose(Y5,file5)
    
    #Printig the average x values for each step number
    print("The average x values are :")
    print("For number of steps = 250  , X_avg = ",X_avg[0])
    print("For number of steps = 500  , X_avg = ",X_avg[1])
    print("For number of steps = 1000  , X_avg = ",X_avg[2])
    print("For number of steps = 2500  , X_avg = ",X_avg[3])
    print("For number of steps = 5000  , X_avg = ",X_avg[4])
    
    #Printing the average y values for each step number
    print("The average y values are :")
    print("For number of steps = 250  , Y_avg = ",Y_avg[0])
    print("For number of steps = 500  , Y_avg = ",Y_avg[1])
    print("For number of steps = 1000  , Y_avg = ",Y_avg[2])
    print("For number of steps = 2500  , Y_avg = ",Y_avg[3])
    print("For number of steps = 5000  , Y_avg = ",Y_avg[4])
    
    #Printing R_rms values or each step sizes 
    print("The R_rms values of each step sizes are :")
    print("For number of steps = 250  , R_rms = ",R[0])
    print("For number of steps = 500  , R_rms = ",R[1])
    print("For number of steps = 1000  , R_rms = ",R[2])
    print("For number of steps = 2500  , R_rms = ",R[3])
    print("For number of steps = 5000  , R_rms = ",R[4])
 
    #For plotting the R_rms vs square root of number of steps adding datas to .txt file
    arr=library.array_1D_to_2D(steps,R)
    filek=open("n_vs_R_rms_data.txt",'w')
    library.array_to_txt(arr,filek)
    #Answering the second question
    def f(x,y,z):
        return (pow(x,2)/pow(1,2))+(pow(y,2)/pow(1.5,2))+(pow(z,2)/pow(2,2))
    N=[100,500,1000,3000,5000,10000,15000,20000,30000,40000]
    V=[]
    for i in range(10):
        n=int(N[i])
        v,matrix,count1=library.monte_carlo_for_3D(1,1.5,2,n,f)
        V.append(v)
    #printing the computed volume for each step number
    print("Answering the second question")
    print("Computing the volume of the given ellipsoid")
    print("Volume computed by taking step number = 100 is :",V[0],"unit cube")
    print("Volume computed by taking step number = 500 is :",V[1],"unit cube")
    print("Volume computed by taking step number = 1000 is :",V[2],"unit cube")
    print("Volume computed by taking step number = 3000 is :",V[3],"unit cube")
    print("Volume computed by taking step number = 5000 is :",V[4],"unit cube")
    print("Volume computed by taking step number = 10000 is :",V[5],"unit cube")
    print("Volume computed by taking step number = 15000 is :",V[6],"unit cube")
    print("Volume computed by taking step number = 20000 is :",V[7],"unit cube")
    print("Volume computed by taking step number = 30000 is :",V[8],"unit cube")
    print("Volume computed by taking step number = 40000 is :",V[9],"unit cube")
    V_analytical=(4/3)*math.pi*(1*1.5*2)
    print("Analytical solution of Volume is : ", V_analytical,"unit cube")
    #for 3D plotting of the ellipsoid 
    Volume,W,count2=library.monte_carlo_for_3D(1,1.5,2,30000,f)
    file3D=open("data_set_for_3D_plot_for_step_number_30000.txt",'w')
    library.array_2D_to_txt(W,count2,file3D)
    #For plotting the R_rms vs square root of number of steps adding datas to .txt file
    arr2=library.array_1D_to_2D(N,V)
    filel=open("datas_for_V_calculated_Vs_analytical_solution_plot.txt",'w')
    library.array_to_txt(arr2,filel)
main()
#The outputs are
#The average x values are :
#For number of steps = 250  , X_avg =  0.46538483911420897
#For number of steps = 500  , X_avg =  2.241519555590416
#For number of steps = 1000  , X_avg =  3.8065616884019158
#For number of steps = 2500  , X_avg =  6.800356469862694
#For number of steps = 5000  , X_avg =  4.387882349511091
#The average y values are :
#For number of steps = 250  , Y_avg =  0.7944056960176806
#For number of steps = 500  , Y_avg =  -0.17471414262252816
#For number of steps = 1000  , Y_avg =  -0.057100711561291394
#For number of steps = 2500  , Y_avg =  3.6608964118520806
#For number of steps = 5000  , Y_avg =  -2.967117137889844
#The R_rms values of each step sizes are :
#For number of steps = 250  , R_rms =  11.32544044382417
#For number of steps = 500  , R_rms =  16.61776874589801
#For number of steps = 1000  , R_rms =  24.067168114091526
#For number of steps = 2500  , R_rms =  35.585192104042335
#For number of steps = 5000  , R_rms =  51.475235350355256
#Answering the second question
#Computing the volume of the given ellipsoid
#Volume computed by taking step number = 100 is : 12.72 unit cube
#Volume computed by taking step number = 500 is : 12.336 unit cube
#Volume computed by taking step number = 1000 is : 13.488000000000001 unit cube
#Volume computed by taking step number = 3000 is : 12.8 unit cube
#Volume computed by taking step number = 5000 is : 12.5136 unit cube
#Volume computed by taking step number = 10000 is : 12.6144 unit cube
#Volume computed by taking step number = 15000 is : 12.5872 unit cube
#Volume computed by taking step number = 20000 is : 12.427200000000001 unit cube
#Volume computed by taking step number = 30000 is : 12.567999999999998 unit cube
#Volume computed by taking step number = 40000 is : 12.669 unit cube
#Analytical solution of Volume is :  12.566370614359172 unit square       
        
    