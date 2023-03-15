## Unit 4 - Complex Variable–Differentiation

- Complex differentiation is the process of finding the rate of change of a complex-valued function with respect to a complex variable.
- The definition of complex derivative is similar to the derivative of a real function: if f(z) is a complex function, then its derivative at a point z0 is given by

  $$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$

  if the limit exists and is independent of the direction of approach of $\Delta z$ to zero.
- A complex function that is differentiable at every point in a domain is called holomorphic or analytic in that domain.
- A remarkable feature of complex differentiation is that the existence of one complex derivative automatically implies the existence of infinitely many derivatives, and that the function is equal to its own Taylor series expansion in a neighborhood of any point in the domain.
- A necessary condition for a complex function to be differentiable is that it satisfies the Cauchy-Riemann equations, which are partial differential equations that link the real and imaginary parts of the function . These equations are given by

  $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

  where $f(z) = u(x,y) + iv(x,y)$ and $z = x + iy$.
- A sufficient condition for a complex function to be differentiable is that it is continuous and satisfies the Cauchy-Riemann equations in a domain.
- Complex differentiation can be used to study various properties of complex functions, such as harmonic functions, conformal mappings, analytic continuation, residues, and contour integration.
- Complex differentiation can also be applied to real-valued functions of a real variable, using a technique called complex step differentiation, which avoids the loss of precision inherent in traditional finite differences. This technique involves evaluating the function at a small imaginary step and taking the imaginary part of the result as an approximation of the derivative. For example, if f(x) is a real function, then

  $$f'(x) \approx \frac{\mathrm{Im}(f(x + ih))}{h}$$

  where h is a small positive number and $\mathrm{Im}$ denotes the imaginary part.