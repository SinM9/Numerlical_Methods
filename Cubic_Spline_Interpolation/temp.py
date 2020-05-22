import matplotlib.pyplot as plt
import random
#from scipy.interpolate import CybicSpline 
 
class SplineParameters:
    def __init__(self, a, b, c, d, x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x
 
def BuildSpline(x, y, n):
    spline = [SplineParameters(0, 0, 0, 0, 0) for _ in range(0, n)]
    for i in range(0, n):
        spline[i].x = x[i]
        spline[i].a = y[i]
    
    spline[0].c = spline[n - 1].c = 0.0
    
    alpha = [0.0 for _ in range(0, n - 1)]
    beta  = [0.0 for _ in range(0, n - 1)]
 
    for i in range(1, n - 1):
        hi  = x[i] - x[i - 1]
        hi1 = x[i + 1] - x[i]
        A = hi
        C = 2.0 * (hi + hi1)
        B = hi1
        F = 6.0 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
        z = (A * alpha[i - 1] + C)
        alpha[i] = -B / z
        beta[i] = (F - A * beta[i - 1]) / z
      
    for i in range(n - 2, 0, -1):
        spline[i].c = alpha[i] * spline[i + 1].c + beta[i]
    
    for i in range(n - 1, 0, -1):
        hi = x[i] - x[i - 1]
        spline[i].d = (spline[i].c - spline[i - 1].c) / hi
        spline[i].b = hi * (2.0 * spline[i].c + spline[i - 1].c) / 6.0 + (y[i] - y[i - 1]) / hi
    return spline
 

def Interpolate(spline, x):
    if not spline:
        return None 
    n = len(spline)
    s = SplineParameters(0, 0, 0, 0, 0)
    
    if x <= spline[0].x: 
        s = spline[0] 
    elif x >= spline[n - 1].x: 
        s = spline[n - 1]
    else: 
        i = 0
        j = n - 1
        while i + 1 < j:
            k = i + (j - i) // 2
            if x <= spline[k].x:
                j = k
            else:
                i = k
        s = spline[j]
    
    dx = x - s.x
    return s.a + (s.b + (s.c / 2.0 + s.d * dx / 6.0) * dx) * dx;
    
####################################################################################


flag1=1
while(flag1==1):
    print("\n Введите 1 - Запустить пробный тест c константными значениями\n 2 - Ввести значения самостоятельно\n 3 - Сгенерировались значения  случайно\n 4 - Записать значения коэффициентов в файл\n 5 - Завершить работу")

    key=int(input())
    x=[]
    y=[]
    if key == 1: #test
        x = [2, 6, 11, 15, 19, 25, 30, 36]
        y = [8, 7, 1, 6, 3, 10, 0, 3]
        
    if key == 2: #input
        flag=1
        print("Введите число начальных точек")
        n=int(input())
        for i in range (0,n,1):
            if i==0:
               print("Введите ", i + 1,"значение по оси Х")
               xi=int(input())
               x.append(xi) 
               print("Введите значение значение функции в данной точке")
               yi=int(input())
               y.append(yi)
               continue
            while (flag==1):
                print("Введите ", i + 1 ,"значение по оси Х")
                xi=int(input())
                if xi>x[i-1]:
                    x.append(xi)
                    print("Введите значение значение функции в данной точке")
                    yi=int(input())
                    y.append(yi)
                    flag=0
                else:
                    ("Введите правильное значение по оси Х")
            flag=1      
    
    if key == 3: #random
        for i in range (8):
            flag2=1
            while flag2==1 :
                tmp=random.randint(1, 250)
                if tmp not in x:
                    x.append(tmp)
                    y.append(random.randint(0, 200))
                    flag2=0
        x.sort() 

    if key == 5:
        flag1=0
        break
    
    mini = min(x)
    maxi = max(x)
    
    spline = BuildSpline(x, y, len(x))
    
    points=[i for i in range(mini, (maxi+1)) ]
    koeff=[Interpolate(spline, i) for i in range(mini, (maxi+1))]
    
    if key == 4:
        with open("mytxt.txt", "w") as my_file:  
            for k in koeff:
                my_file.write('%s\n' % k)    
        my_file.close()    
    #C:\Users\Маруся1\.spyder-py3
        
    
    #plt.scatter(points, koeff)
    plt.scatter(x, y, label = 'Начальные точки', color='black')
    plt.plot(points, koeff, label = 'Кубический сплайн',color='y')
    
    #plt.plot(x, y)
    
    plt.xlabel('Ось Х')
    plt.ylabel('Ось У')
    plt.legend()
    plt.show()    
    
    