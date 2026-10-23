#refer prob33.txt

import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

def g(x,derv=False):
    if derv:
        return 1/x
    return np.log(x) 

def h(x, derv=False):
    if derv:
        return 4*(x**3) + 60*(x**2)
    return (x**4) + (20*(x**3) + 100)

def f(x, derv=False):
    if derv:
        return g(h(x),True)*h(x,True) 
    return g(h(x))

def visualize(start,stop,spacing,trim=(-10,10)):
    xs = np.arange(start,stop,spacing) 
    y_dervs = f(xs, True) 
    y_origs = f(xs) 

    sign_changes = np.where(np.diff(np.sign(y_dervs)))[0] 
    print(xs[sign_changes]) 

    trim1,trim2 = trim 

    fg, (ax1, ax2) = plt.subplots(2,1,sharex=True) 
    sns.lineplot(x=xs, y=y_origs, ax=ax1) 
    ax1.set_title("a(t)") 
    ax1.set_ylim(trim1,trim2) 
    for cx in xs[sign_changes]:
        ax1.axvline(cx, color='red', linestyle='--', alpha=0.7) 
    ax1.axhline(0, color='green', linestyle='--', alpha=0.7) 

    sns.lineplot(x=xs, y=y_dervs, ax=ax2) 
    ax2.set_title("a'(t)")
    ax2.set_ylim(trim1,trim2) 
    
    for cx in xs[sign_changes]:
        ax2.axvline(cx, color='red', linestyle='--', alpha=0.7) 
    ax2.axhline(0,color='green',linestyle='--',alpha=0.7)
    
    plt.tight_layout() 
    plt.show()

visualize(-1,20,0.01)
