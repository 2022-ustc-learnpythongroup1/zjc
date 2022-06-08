from scipy import integrate
def f(x, y):
    return (x**2+y**2)**0.5

def bounds_x(y):
    return [0, 1]

def bounds_y():
    return [-x,x]

print(integrate.nquad(f, [bounds_x, bounds_y]))
