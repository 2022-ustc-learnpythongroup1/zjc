from sympy import *  #导入sympy库，用于解函数

#导入绘图所需模块
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

f = symbols('f', cls=Function)                #定义函数f
x = symbols('x')                              #定义x
eq = Eq(f(x).diff(x)-f(x), 0)                 #求解函数f
pprint(dsolve(eq, f(x)))                      #打印函数f

c=float(input("请确定常数C1:"))                #确定函数f中常数C1    

#绘图
x = np.arange(0, 5, 0.1)                      #生成等差数组
y = np.exp(x)*c
plt.xlabel('x')
plt.ylabel('y')
plt.title("图像")
plt.plot(x, y)
plt.show()
