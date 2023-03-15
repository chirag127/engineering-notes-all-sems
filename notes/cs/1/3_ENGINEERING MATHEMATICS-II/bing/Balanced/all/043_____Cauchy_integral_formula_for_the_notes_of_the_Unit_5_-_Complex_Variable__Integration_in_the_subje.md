# Cauchy Integral Formula

- The Cauchy integral formula is a fundamental result in complex analysis that relates the value of a holomorphic function at a point to its values on a circle around that point.
- The formula can be stated as follows: if f(z) is a holomorphic function on a domain U and γ is a positively oriented simple closed contour in U that encloses a point z_0, then

  f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z-z_0} dz

- The formula can be proved using the Cauchy-Goursat theorem, which says that the integral of a holomorphic function over a simple closed contour is zero, and the residue theorem, which says that the integral of a function with a simple pole at z_0 over a circle around z_0 is equal to 2\pi i times the residue of the function at z_0.
- The Cauchy integral formula has several important consequences and applications, such as:

  - It implies that holomorphic functions are infinitely differentiable and analytic, meaning that they can be expressed as power series around any point in their domain.
  - It provides a formula for the derivatives of a holomorphic function, namely

    f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}} dz

    for any positive integer n.
  - It allows us to evaluate integrals of holomorphic functions over simple closed contours using the values of the function at the interior points, without knowing the function explicitly.
  - It enables us to define the concept of a harmonic function, which is a real-valued function that satisfies Laplace's equation, as the real or imaginary part of a holomorphic function.