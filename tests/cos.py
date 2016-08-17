#encoding=UTF8
def cosVector(x,y):
    if(len(x)!=len(y)):
        print('error input,x and y is not in the same space')
        return;
    result1=0.0;
    result2=0.0;
    result3=0.0;
    for i in range(len(x)):
        result1+=x[i]*y[i]   #sum(X*Y)
        result2+=x[i]**2     #sum(X*X)
        result3+=y[i]**2     #sum(Y*Y)
    #print(result1)
    #print(result2)
    #print(result3)
    print("result is "+str(result1/((result2*result3)**0.5))) #结果显示
cosVector([2,1],[1,1])#0.9486832981010276计算器
