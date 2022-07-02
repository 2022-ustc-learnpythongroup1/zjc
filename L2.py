from sympy import *
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

f = symbols('f', cls=Function)
x = symbols('x')
eq = Eq(f(x).diff(x)-f(x), 0)
pprint(dsolve(eq, f(x)))

c=float(input("请确定常数C1:"))

x = np.arange(0, 5, 0.1)
y = np.exp(x)*c
plt.xlabel('x')
plt.ylabel('y')
plt.title("图像")
plt.plot(x, y)
plt.show()
