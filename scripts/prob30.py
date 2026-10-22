#refer problems/prob30.txt 

def h(x, derv=False): 
    if derv:
        return 4 * (x ** 3) 
    return (x ** 4)

def g(x, derv=False):
    if derv:
        return 6 * ((2*x - 8) ** 2)  
    return (2*x - 8) ** 3

def f(x, derv=False):
    if derv:
        return h(x,True)*g(x) + h(x)*g(x,True) 
    return h(x) * g(x) 


derv = True
print(f(-2, derv), f(0, derv), f(16/7,derv), f(3,derv), f(5,derv))