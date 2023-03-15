# Maxima and Minima of Functions of Several Variables

- A function f(x, y) of two independent variables has a **maximum** at a point (x0, y0) if f(x0, y0) ≥ f(x, y) for all points (x, y) in the neighborhood of (x0, y0). Such a function has a **minimum** at a point (x0, y0) if f(x0, y0) ≤ f(x, y) for all points (x, y) in the neighborhood of (x0, y0).
- The maximum and minimum values of a function are also called the **extrema** of the function. The highest and lowest values of a function within a particular set of ranges are known as **local maxima and minima**. The highest and lowest values of the function under the whole range are known as the **absolute maxima and minima**.
- To find the extrema of a function of several variables, we need to use the **partial derivatives** of the function. A point (x0, y0) is called a **critical point** of f(x, y) if either f<sub>x</sub>(x0, y0) = 0 and f<sub>y</sub>(x0, y0) = 0, or one or both of these partial derivatives do not exist.
- To determine whether a critical point is a maximum, a minimum, or a **saddle point** (a point where the function has neither a maximum nor a minimum), we need to use the **second partial derivatives** of the function. The **second derivative test** is based on the following formula:

  D = f<sub>xx</sub>(x0, y0)f<sub>yy</sub>(x0, y0) - [f<sub>xy</sub>(x0, y0)]<sup>2</sup>

  - If D > 0 and f<sub>xx</sub>(x0, y0) > 0, then f(x, y) has a local minimum at (x0, y0).
  - If D > 0 and f<sub>xx</sub>(x0, y0) < 0, then f(x, y) has a local maximum at (x0, y0).
  - If D < 0, then f(x, y) has a saddle point at (x0, y0).
  - If D = 0, then the test is inconclusive.

- To find the absolute extrema of a function of several variables on a closed, bounded set, we need to check the critical points of the function inside the set, as well as the **boundary points** of the set. The boundary points can be found by using **Lagrange multipliers** or by parameterizing the boundary curve.
- The extrema of functions of several variables have many applications in optimization problems, such as finding the maximum or minimum area, volume, profit, cost, etc. of a given situation.