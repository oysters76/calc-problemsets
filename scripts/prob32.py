# check refer in problems/prob32.txt
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

def h(t, derv=False):
    if derv:
        return 2 * t 
    return t ** 2 

def g(t, derv=False):
    if derv:
        return -1 * (np.e ** (5 - t))
    return np.e ** (5-t)

def a(t, derv=False):
    if derv:
        return h(t,True) * g(t) + h(t) * g(t,True) 
    return h(t) * g(t) 

def run(start, stop, spacing):
    xs = np.arange(start,stop,spacing) 
    ys_derv = a(xs, True) 
    ys_orig = a(xs) 

    sign_changes = np.where(np.diff((np.sign(ys_derv))))[0] 
    print(xs[sign_changes]) 

    fg, (ax1, ax2) = plt.subplots(2,1,sharex=True) 

    sns.lineplot(x=xs, y=ys_orig, ax=ax1)
    ax1.set_title("a(t)")
    ax1.set_ylim(-10, 60) 
    for cx in xs[sign_changes]:
        ax1.axvline(cx, color='red', linestyle='--', alpha=0.7)
    ax1.axhline(1, color='green', linestyle='--', alpha=0.7)    

    sns.lineplot(x=xs, y=ys_derv, ax=ax2)
    ax2.set_title("a'(t)")
    ax2.set_ylim(-50, 50) 
    for cx in xs[sign_changes]:
        ax2.axvline(cx, color='red', linestyle='--', alpha=0.7)
    ax2.axhline(1, color='green', linestyle='--', alpha=0.7)    

    plt.tight_layout() 
    plt.show() 

run(-4,4,0.01)  