# Plot Scaling and Reference Lines

When your plot looks squashed and you can't see the interesting part — these two tricks fix it.

---

## The problem: extreme values squash everything else

When we plotted A(t) = t² · e^(5-t) on the range (-4, 4), the left side of the graph had enormous values (around t = -4, the function hits ~8000). That made the interesting part — where the function increases between 0 and 2 — look completely flat.

The graph was technically correct, but useless for seeing what we cared about.

## Fix 1: Clip the y-axis with `set_ylim`

Instead of letting matplotlib auto-scale to fit everything, you can tell it to only show a specific y-range:

```python
ax1.set_ylim(-10, 60)
```

This clips the view. Anything above 60 or below -10 just gets cut off — like zooming in on the part that matters.

### How to pick good bounds

- Look at the y-values in the region you care about. For us, A(t) between 0 and 2 peaks around 30, so (-10, 60) gives breathing room.
- You can also just try a few values and adjust. There's no formula — eyeball it.
- You can set limits on just one side too:

```python
ax1.set_ylim(bottom=-10)  # only clip the bottom
ax1.set_ylim(top=60)      # only clip the top
```

### The other option: narrow the x-range

Sometimes it's simpler to just change the range of x-values you're plotting. We also tried `run(-1, 4, 0.01)` instead of `run(-4, 4, 0.01)` — cutting out the extreme left side entirely. Both work. Use whichever makes the graph more readable.

## Fix 2: Horizontal reference lines with `axhline`

To draw a horizontal line at a specific y-value:

```python
ax.axhline(1, color='green', linestyle='--', alpha=0.7)
```

This draws a dashed green line at y = 1 across the entire plot.

### When it's useful

- **y = 0 on a derivative plot** — makes it easy to see where the derivative is positive vs negative (above vs below the line). This tells you where the original function is increasing or decreasing.
- **y = some threshold** — if you're checking whether a function exceeds a certain value.
- **Comparing against a constant** — "does the function ever hit 1?" becomes obvious with a horizontal line at y = 1.

### It works the same as `axvline`

You've already used `axvline` for vertical lines at critical points. Same idea, just the other direction:

| function   | draws           | you give it |
|-----------|-----------------|-------------|
| `axvline` | vertical line   | an x-value  |
| `axhline` | horizontal line | a y-value   |

Both take the same styling options: `color`, `linestyle`, `alpha`.
