### Expansion of functions by Taylor’s and Maclaurin’s theorems for functions of one and two variables

#### Unit 3 - Differential Calculus-II, ENGINEERING MATHEMATICS-I

1. **Taylor's Theorem**: Taylor's theorem states that any function that is infinitely differentiable in a neighborhood of a point can be represented as an infinite sum of terms, known as the Taylor series. The Taylor series is calculated using the derivatives of the function at that point.

2. **Maclaurin's Theorem**: Maclaurin's theorem is a special case of Taylor's theorem, where the expansion is taken around the point x = 0. The resulting series is known as the Maclaurin series.

3. **Functions of One Variable**: For a function of one variable, the Taylor series expansion around the point x = a is given by:
```
f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2/2! + ... + f^n(a)(x-a)^n/n! + ...
```
where f^n(a) denotes the nth derivative of the function f at the point x = a.

4. **Functions of Two Variables**: For a function of two variables, the Taylor series expansion around the point (x,y) = (a,b) is given by:
```
f(x,y) = f(a,b) + fx(a,b)(x-a) + fy(a,b)(y-b) + fxx(a,b)(x-a)^2/2! + fyy(a,b)(y-b)^2/2! + fxy(a,b)(x-a)(y-b) + ... 
```
where fx, fy, fxx, fyy, and fxy denote the partial derivatives of the function f with respect to x, y, xx, yy, and xy, respectively, evaluated at the point (x,y) = (a,b).

These theorems allow us to approximate functions using polynomials, which can be useful in many applications, including numerical analysis and mathematical modeling. It is important to note that the accuracy of the approximation depends on the number of terms included in the series and the smoothness of the function being approximated.