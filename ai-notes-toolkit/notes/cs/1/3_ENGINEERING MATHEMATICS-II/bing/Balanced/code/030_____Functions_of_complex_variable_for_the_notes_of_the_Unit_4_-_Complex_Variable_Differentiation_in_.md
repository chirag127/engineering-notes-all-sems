### Functions of complex variable

- A complex function is a function that maps complex numbers to complex numbers, i.e., $w(z) = u(x,y) + iv(x,y)$, where $z = x + iy$ and $w, u, v$ are complex-valued functions of two real variables $x$ and $y$  .
- A complex function can be seen as a pair of real functions, the real part $u(x,y)$ and the imaginary part $v(x,y)$, that satisfy the Cauchy-Riemann equations  :
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$
$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$
- A complex function is said to be holomorphic or analytic if it is differentiable at every point in its domain, i.e., if the limit
$$\lim_{\Delta z \to 0} \frac{w(z + \Delta z) - w(z)}{\Delta z}$$
exists and is independent of the direction of $\Delta z$  .
- A holomorphic function has many remarkable properties, such as:
  - It is infinitely differentiable and can be expressed as a power series in a neighborhood of any point in its domain  .
  - It satisfies the maximum modulus principle, which states that the modulus of a holomorphic function cannot have a local maximum in the interior of its domain  .
  - It satisfies the Cauchy integral formula, which relates the value of a holomorphic function at a point to its values on a closed contour around that point  .
  - It satisfies the residue theorem, which relates the integral of a holomorphic function over a closed contour to the sum of its residues at the isolated singularities inside the contour  .
- A complex function can be extended to a function of several complex variables, i.e., $w(z_1, z_2, \dots, z_n) = u(x_1, y_1, \dots, x_n, y_n) + iv(x_1, y_1, \dots, x_n, y_n)$, where $z_i = x_i + iy_i$ and $w, u, v$ are complex-valued functions of $2n$ real variables .
- A function of several complex variables is said to be holomorphic or analytic if it is holomorphic in each variable separately, i.e., if the partial derivatives
$$\frac{\partial w}{\partial z_i} = \frac{1}{2} \left( \frac{\partial w}{\partial x_i} - i \frac{\partial w}{\partial y_i} \right)$$
exist and are continuous for all $i = 1, 2, \dots, n$ .
- A function of several complex variables has similar properties to a function of one complex variable, such as power series expansion, maximum modulus principle, Cauchy integral formula, and residue theorem, but they are more complicated and require more assumptions .

: https://people.umass.edu/bvs/605.pdf
: https://vdocument.in/functions-of-a-complex-variables.html
: https://en.wikipedia.org/wiki/Complex_analysis
: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/
: https://en.wikipedia.org/wiki/Function_of_several_complex_variables