import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

def s(x, derv=False):
    if derv:
        return 3 * np.cos(3 * x) - 2
    return np.sin(3 * x) - 2*x + 4 

def run(start,end,spacing):
    xs = np.arange(start,end,spacing)
    ys_derv = s(xs, True)
    ys_orig = s(xs, False)

    sign_changes = np.where(np.diff((np.sign(ys_derv))))[0]
    print(xs[sign_changes])

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    sns.lineplot(x=xs, y=ys_orig, ax=ax1)
    ax1.set_title("s(x) = sin(3x) - 2x + 4")
    for cx in xs[sign_changes]:
        ax1.axvline(cx, color='red', linestyle='--', alpha=0.7)

    sns.lineplot(x=xs, y=ys_derv, ax=ax2)
    ax2.set_title("s'(x) = 3cos(3x) - 2")
    ax2.axhline(0, color='gray', linestyle='--', alpha=0.5)
    for cx in xs[sign_changes]:
        ax2.axvline(cx, color='red', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

run(-3,3.01,0.01)