### Functions of complex variable

- A function of a complex variable is a rule that assigns a complex number to another complex number. For example, if z is a complex variable, then f(z) = z^2 + 2z - 1 is a function of a complex variable.
- A function of a complex variable can also be seen as a function of two real variables, x and y, where z = x + iy and f(z) = u(x, y) + iv(x, y), where u and v are real functions of x and y. For example, if f(z) = z^2 + 2z - 1, then u(x, y) = x^2 - y^2 + 2x - 1 and v(x, y) = 2xy + 2y.
- A function of a complex variable can be represented graphically by using a complex plane, where the horizontal axis is the real part of z and the vertical axis is the imaginary part of z. The graph of f(z) is then a surface in a four-dimensional space, where the height and color of each point represent the real and imaginary parts of f(z), respectively. For example, the graph of f(z) = z^2 + 2z - 1 is shown below:

![Graph of f(z) = z^2 + 2z - 1](https://i.imgur.com/2QY7Z0n.png)

- A function of a complex variable is said to be analytic or holomorphic at a point z if it is differentiable at z and at every point in some neighborhood of z. The derivative of f(z) at z is defined by the limit

f'(z) = lim_(h->0) (f(z + h) - f(z))/h

where h is any complex number. For example, f(z) = z^2 + 2z - 1 is analytic at every point in the complex plane, and its derivative is f'(z) = 2z + 2.
- A function of a complex variable is said to be entire if it is analytic at every point in the complex plane. For example, f(z) = e^z, f(z) = sin(z), and f(z) = z^2 + 2z - 1 are entire functions.
- A function of a complex variable is said to be harmonic if its real and imaginary parts are harmonic functions, that is, they satisfy the Laplace equation

del^2 u = 0 and del^2 v = 0

where del^2 is the Laplacian operator. For example, f(z) = e^z, f(z) = sin(z), and f(z) = z are harmonic functions.
- A function of a complex variable is said to satisfy the Cauchy-Riemann equations if

du/dx = dv/dy and du/dy = -dv/dx

where u and v are the real and imaginary parts of f(z). These equations are necessary and sufficient conditions for a function to be analytic. For example, f(z) = z^2 + 2z - 1 satisfies the Cauchy-Riemann equations, since

du/dx = 2x + 2 = dv/dy and du/dy = -2y = -dv/dx

- A function of a complex variable has many applications in physics, engineering, and mathematics, such as solving differential equations, evaluating integrals, finding asymptotic solutions, modeling waves, quantum mechanics, fluid dynamics, and conformal mapping.

Some possible mnemonics and learning tricks for the topic are:

- To remember the Cauchy-Riemann equations, use the acronym CRUD: Cauchy-Riemann U and D, where U stands for u(x, y) and D stands for dv/dx.
- To remember the Laplace equation, use the phrase "Laplace is zero": del^2 u = 0 and del^2 v = 0.
- To remember the definition of the derivative of a complex function, use the formula "f prime is f plus h minus f over h": f'(z) = (f(z + h) - f(z))/h.
- To remember some common entire functions, use the word "SEZ": Sine, Exponential, and Z.