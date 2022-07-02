from sympy import *  #导入sympy库，用于解函数
y=float(input("请输入一个数:"))  #给y赋值
x= symbols('x')    #定义x
print(solve(x**2-2*x+1-y,x))  #求解x，并打印