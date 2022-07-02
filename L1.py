from sympy import *
y=float(input("请输入一个数:"))
x= symbols('x')
print(solve(x**2-2*x+1-y,x))

