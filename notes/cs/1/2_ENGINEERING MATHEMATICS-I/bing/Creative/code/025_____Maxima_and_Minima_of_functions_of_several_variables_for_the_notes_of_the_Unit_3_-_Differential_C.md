Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Maxima and Minima of functions of several variables for the notes of the Unit 3 - Differential Calculus-II in the subject of ENGINEERING MATHEMATICS-I.

```markdown
### Maxima and Minima of functions of several variables

- A function of several variables, f(x,y), has a local maximum at a point (a,b) if f(x,y) ≤ f(a,b) for all points (x,y) near (a,b).
- Similarly, f(x,y) has a local minimum at (a,b) if f(x,y) ≥ f(a,b) for all points (x,y) near (a,b).
- A point (a,b) where f(x,y) has a local maximum or minimum is called a local extremum of f(x,y).
- To find the local extrema of f(x,y), we use the following steps:
  - Find the first-order partial derivatives of f(x,y) and set them equal to zero: f<sub>x</sub>(x,y) = 0 and f<sub>y</sub>(x,y) = 0.
  - Solve the system of equations to find the critical points of f(x,y), i.e., the points where both partial derivatives are zero or undefined.
  - Use the second derivative test to classify the critical points as local maxima, local minima, or saddle points. The second derivative test is based on the value and sign of the Hessian matrix of f(x,y) at the critical point, which is given by:

    H = | f<sub>xx</sub> f<sub>xy</sub> |
        | f<sub>yx</sub> f<sub>yy</sub> |

  - The second derivative test states that:
    - If H > 0 and f<sub>xx</sub> > 0, then f(x,y) has a local minimum at the critical point.
    - If H > 0 and f<sub>xx</sub> < 0, then f(x,y) has a local maximum at the critical point.
    - If H < 0, then f(x,y) has a saddle point at the critical point.
    - If H = 0, then the test is inconclusive and further analysis is needed.
- A function of several variables, f(x,y), has a global maximum at a point (a,b) if f(x,y) ≤ f(a,b) for all points (x,y) in the domain of f(x,y).
- Similarly, f(x,y) has a global minimum at (a,b) if f(x,y) ≥ f(a,b) for all points (x,y) in the domain of f(x,y).
- A point (a,b) where f(x,y) has a global maximum or minimum is called a global extremum of f(x,y).
- To find the global extrema of f(x,y), we use the following steps:
  - Find the local extrema of f(x,y) using the method described above.
  - Find the boundary points of the domain of f(x,y) and evaluate f(x,y) at these points.
  - Compare the values of f(x,y) at the local extrema and the boundary points and determine the global maximum and minimum values of f(x,y).
```