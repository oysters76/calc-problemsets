# NumPy and Seaborn Basics

A beginner-friendly guide to the tools we used for plotting and analyzing math functions in Python.

---

## Trig functions in NumPy

NumPy has `np.sin()` and `np.cos()` built in. One thing to remember: they expect **radians**, not degrees.

If you have degrees, convert them first:

```python
import numpy as np

np.sin(np.deg2rad(90))  # gives 1.0
```

## Vectorization — no loops needed

This is one of the coolest things about NumPy. If you give it a whole list of numbers, it does the math on **every single one** automatically. No for-loops required.

```python
angles = np.array([0, 30, 45, 60, 90])
results = np.sin(np.deg2rad(angles))
# gives you 5 results, one for each angle
```

This also works with your own functions, as long as you use NumPy operations inside:

```python
def f(x):
    return np.sin(x) + np.cos(x)

xs = np.array([0, 1, 2, 3])
ys = f(xs)  # computes f for all 4 values at once
```

## linspace vs arange — two ways to make a range of numbers

These do similar things but you tell them different things.

**`np.linspace(start, stop, how_many_points)`** — you say how many points you want. The stop value IS included.

```python
np.linspace(0, 1, 5)
# [0.0, 0.25, 0.5, 0.75, 1.0]  — 5 evenly spaced points
```

**`np.arange(start, stop, step_size)`** — you say what step size to use. The stop value is NOT included.

```python
np.arange(0, 1, 0.25)
# [0.0, 0.25, 0.5, 0.75]  — 4 points, stops before 1.0
```

Use `linspace` when you know how many points you want. Use `arange` when you know the gap between each point.

## Finding where a function crosses zero

This is a really handy trick. Say you have a list of y-values and you want to know where the function crosses zero (goes from positive to negative, or the other way around). Here's how it works, step by step:

### Step 1: `np.sign()` — simplify everything to -1, 0, or 1

It just tells you if a number is negative, zero, or positive:

```python
ys       = [ 1.0,  0.5, -0.3, -0.8,  0.2]
np.sign  = [  1,    1,   -1,   -1,    1  ]
```

### Step 2: `np.diff()` — check if neighbors changed sign

This subtracts each value from the one after it. If two neighbors have the same sign, you get 0. If they flipped, you get -2 or 2:

```python
signs    = [  1,    1,   -1,   -1,    1  ]
np.diff  = [    0,   -2,    0,    2      ]
#            same  flip!  same  flip!
```

### Step 3: `np.where()` — find where the flips are

This gives you the positions where the value isn't zero (meaning a flip happened):

```python
diff     = [ 0,  -2,   0,   2 ]
np.where = [      1,        3  ]   # positions where flips happened
```

### Putting it all together

```python
sign_changes = np.where(np.diff(np.sign(ys)))[0]
critical_xs = xs[sign_changes]
```

The `[0]` at the end is just because `np.where` wraps the answer in a tuple — `[0]` unwraps it.

## Seaborn — prettier plots, less code

Seaborn makes good-looking plots with very little effort:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(x=xs, y=ys)
plt.show()
```

But here's the thing: **seaborn sits on top of matplotlib**. It handles the actual drawing, but you still need matplotlib for things like:

- `plt.show()` — display the plot
- `plt.savefig('plot.png')` — save it as an image
- `plt.axvline(x, ...)` — draw a vertical line
- `plt.axhline(y, ...)` — draw a horizontal line
- `plt.title(...)` — add a title

There's no way around it — you'll always `import matplotlib.pyplot as plt` alongside seaborn.

## Making two plots stacked on top of each other

Sometimes you want to compare two things side by side (or top and bottom). Use `plt.subplots()`:

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#                                ^  ^  ^^^^^^^^^
#                          2 rows  1 col  same x-axis

sns.lineplot(x=xs, y=ys_original, ax=ax1)   # top plot
ax1.set_title("The function")

sns.lineplot(x=xs, y=ys_derivative, ax=ax2)  # bottom plot
ax2.set_title("The derivative")

plt.tight_layout()  # prevents overlap
plt.show()
```

The key is passing `ax=ax1` or `ax=ax2` to tell seaborn which subplot to draw on.

## Adding vertical marker lines

To highlight specific x-values (like critical points) on your plot:

```python
for cx in critical_points:
    plt.axvline(cx, color='red', linestyle='--', alpha=0.7)
```

This draws red dashed vertical lines. `alpha=0.7` makes them slightly transparent so they don't overpower the graph.
