# How to Tell if a Function is Increasing or Decreasing

This is one of the most useful things the derivative can tell you.

---

## What does the derivative actually mean?

Think of the derivative as the **slope** at any point. It answers one simple question:

> "Is the function going up or going down right now?"

- If the slope is **positive** (above zero), the function is going **up** — we call that **increasing**.
- If the slope is **negative** (below zero), the function is going **down** — we call that **decreasing**.

That's it. That's the whole idea.

## Finding where the function changes direction

The function switches from going up to going down (or vice versa) at special points called **critical points**. These are where the derivative equals zero — the slope is flat for just a moment before it tips the other way.

### The steps

1. **Find the derivative** — this is your slope function.
2. **Set the derivative equal to zero and solve** — these are your critical points.
3. **Check the sign of the derivative between those points** — positive means increasing, negative means decreasing.

## A real example: s(x) = sin(3x) - 2x + 4

Let's walk through it on the range (0, 3).

### Step 1: Find the derivative

s'(x) = 3cos(3x) - 2

### Step 2: Find where s'(x) = 0

Set 3cos(3x) - 2 = 0, which gives us cos(3x) = 2/3.

Solving: x = arccos(2/3) / 3

On the range (0, 3), there are three critical points:

| x     |
|-------|
| 0.28  |
| 1.81  |
| 2.37  |

### Step 3: Check the sign between critical points

Pick any x-value in each interval. Plug it into s'(x). Is the answer positive or negative?

| interval       | s'(x) is...  | so s(x) is... |
|----------------|---------------|----------------|
| (0, 0.28)      | positive      | increasing     |
| (0.28, 1.81)   | negative      | decreasing     |
| (1.81, 2.37)   | positive      | increasing     |
| (2.37, 3)      | negative      | decreasing     |

And that's your answer.

## How to see it visually

If you plot both the function and its derivative on two graphs (stacked on top of each other), something cool happens:

- Every time the **derivative crosses zero** (bottom graph), the **original function hits a peak or valley** (top graph).
- When the derivative line is **above the x-axis**, the original function is climbing.
- When the derivative line is **below the x-axis**, the original function is falling.

The red vertical lines at the critical points make this really easy to see — they line up perfectly between both graphs.

## Quick summary

| derivative | function is... |
|-----------|----------------|
| positive  | increasing (going up) |
| zero      | flat — peak or valley |
| negative  | decreasing (going down) |

That's all there is to it. The derivative is just a slope-checker.
