#引入库
import scipy.integrate
import math
from numpy import exp
from math import sqrt

#写出表达式
f=lambda x,y:(x**2+y**2)**0.5

p,err=scipy.integrate.dblquad(f,-x,x,lambda g:0,lambda h:1)
print(p) 