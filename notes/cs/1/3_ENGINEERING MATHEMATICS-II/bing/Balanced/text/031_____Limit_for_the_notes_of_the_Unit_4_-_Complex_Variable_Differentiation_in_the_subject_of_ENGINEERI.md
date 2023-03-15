### Limit for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Complex variable–differentiation is the study of functions of a complex variable and their derivatives.
- A complex variable is a variable that can take values in the complex numbers, which are numbers of the form $z = x + iy$, where $x$ and $y$ are real numbers and $i$ is the imaginary unit such that $i^2 = -1$.
- The complex numbers can be represented geometrically as points in the complex plane, where the horizontal axis is the real axis and the vertical axis is the imaginary axis.
- A function of a complex variable is a rule that assigns a complex number to each complex number in its domain, which is a subset of the complex plane. For example, $f(z) = z^2$ is a function of a complex variable that maps each complex number $z$ to its square $z^2$.
- The derivative of a function of a complex variable is a measure of how fast the function changes with respect to a small change in the input variable. The derivative of $f(z)$ at a point $z_0$ in its domain is denoted by $f'(z_0)$ and defined by the limit
$$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$
where $\Delta z$ is a complex number that approaches zero.
- The derivative of a function of a complex variable has the following properties:
  - Linearity: If $f(z)$ and $g(z)$ are differentiable functions and $c$ is a constant, then $(cf + g)'(z) = cf'(z) + g'(z)$.
  - Product rule: If $f(z)$ and $g(z)$ are differentiable functions, then $(fg)'(z) = f'(z)g(z) + f(z)g'(z)$.
  - Quotient rule: If $f(z)$ and $g(z)$ are differentiable functions and $g(z) \neq 0$, then $(f/g)'(z) = \frac{f'(z)g(z) - f(z)g'(z)}{g(z)^2}$.
  - Chain rule: If $f(z)$ and $g(z)$ are differentiable functions, then $(f \circ g)'(z) = f'(g(z))g'(z)$, where $f \circ g$ denotes the composition of $f$ and $g$.
  - Power rule: If $f(z) = z^n$, where $n$ is a constant, then $f'(z) = nz^{n-1}$.
  - Exponential rule: If $f(z) = e^z$, then $f'(z) = e^z$.
  - Logarithmic rule: If $f(z) = \log z$, where $\log z$ is the principal branch of the complex logarithm, then $f'(z) = \frac{1}{z}$.
  - Trigonometric rules: If $f(z) = \sin z$, then $f'(z) = \cos z$. If $f(z) = \cos z$, then $f'(z) = -\sin z$. If $f(z) = \tan z$, then $f'(z) = \frac{1}{\cos^2 z}$.
  - Hyperbolic rules: If $f(z) = \sinh z$, then $f'(z) = \cosh z$. If $f(z) = \cosh z$, then $f'(z) = \sinh z$. If $f(z) = \tanh z$, then $f'(z) = \frac{1}{\cosh^2 z}$.
- A function of a complex variable is said to be analytic or holomorphic at a point $z_0$ in its domain if it has a derivative at $z_0$ and at every point in some neighborhood of $z_0$. A function is said to be analytic or holomorphic in a domain if it is analytic at every point in that domain.
- A remarkable feature of complex differentiation is that the existence of one complex derivative automatically implies the existence of infinitely many. This is in contrast to the case of the function of real variable $g(x