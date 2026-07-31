
### Euler’s Theorem for homogeneous functions

Euler's Theorem for homogeneous functions states that if a function is homogeneous of degree n, then the sum of its partial derivatives of order 1 is equal to n times the function itself. This theorem is named after the Swiss mathematician Leonhard Euler.

**Definition**: A function f(x,y) is said to be homogeneous of degree n if it satisfies the equation:

f(tx,ty) = t<sup>n</sup>f(x,y)

where t is a non-zero real number.

**Euler's Theorem**: If f(x,y) is homogeneous of degree n, then

nf(x,y) = xf<sub>x</sub> + yf<sub>y</sub>

where f<sub>x</sub> and f<sub>y</sub> denote the partial derivatives of f with respect to x and y, respectively.

**Proof**:

Let g(t) = f(tx,ty). Then

g'(t) = xf<sub>x</sub>(tx,ty) + yf<sub>y</sub>(tx,ty)

Using the chain rule,

g'(t) = xf<sub>x</sub>(tx,ty) + yf<sub>y</sub>(tx,ty) = txf<sub>x</sub>(x,y) + tyf<sub>y</sub>(x,y)

By the definition of homogeneous functions,

g(t) = t<sup>n</sup>f(x,y)

Differentiating both sides of the equation with respect to t,

ng(t) = t<sup>n-1</sup>f(x,y) + t<sup>n</sup>f<sub>x</sub>(x,y)

Comparing the coefficients of t<sup>n-1</sup> on both sides,

nf(x,y) = xf<sub>x</sub>(x,y) + yf<sub>y</sub>(x,y)

This completes the proof.