from sympy import *             #导入sympy库，用于解函数

a=int(input("请输入一个整数a:"))  #确定方程中C1
b=int(input("请输入一个整数b:"))  #确定方程中C2
c=int(input("请输入一个整数c:"))  #确定方程中C3

f = symbols('f', cls=Function)  #定义函数f
x = symbols('x')                #定义x
eq = Eq(a*f(x).diff(x, x) + b*f(x).diff(x) + c*f(x), 0)  #求解函数f
pprint(dsolve(eq, f(x)))        #打印函数f