# Method to find Analytic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- A function of a complex variable is said to be **analytic** in a region of the complex plane if it has a derivative at each point of the region and if it is single valued.
- A function is analytic if and only if it is **holomorphic** or **complex analytic**, which means that it is locally given by a convergent power series in the complex variable  .
- To find if a function is analytic, one can use the following methods:
  - **Cauchy-Riemann equations**: These are two partial differential equations that relate the real and imaginary parts of a complex function. If a function satisfies these equations in a region, then it is analytic in that region . The equations are:

    $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

    $$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

    where $u$ and $v$ are the real and imaginary parts of the function, respectively.

  - **Harmonic functions**: These are real-valued functions that satisfy Laplace's equation, which is a second-order partial differential equation. If the real and imaginary parts of a complex function are both harmonic, then the function is analytic . Laplace's equation is:

    $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = 0$$

    where $f$ is a harmonic function.

  - **Conformal mapping**: This is a transformation that preserves angles and shapes locally. If a function is analytic and has a non-zero derivative everywhere in a region, then it is a conformal mapping in that region . Conformal mappings are useful for solving boundary value problems and mapping complex domains to simpler ones.