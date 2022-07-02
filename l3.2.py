from sympy import *

a=int(input("请输入一个整数:"))
b=int(input("请输入一个整数:"))
c=int(input("请输入一个整数:"))

f = symbols('f', cls=Function)
x = symbols('x')
eq = Eq(a*f(x).diff(x, x) + b*f(x).diff(x) + c*f(x), 0)
pprint(dsolve(eq, f(x)))
