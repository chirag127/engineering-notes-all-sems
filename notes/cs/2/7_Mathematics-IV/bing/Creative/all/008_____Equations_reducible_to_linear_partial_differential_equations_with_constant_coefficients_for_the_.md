# Equations reducible to linear partial differential equations with constant coefficients

- A linear partial differential equation (PDE) with constant coefficients is an equation of the form
$$
a_1 \frac{\partial u}{\partial x_1} + a_2 \frac{\partial u}{\partial x_2} + \cdots + a_n \frac{\partial u}{\partial x_n} + b u = f(x_1, x_2, \ldots, x_n)
$$
where $a_1, a_2, \ldots, a_n, b$ are constants and $u$ and $f$ are functions of $n$ variables $x_1, x_2, \ldots, x_n$ .

- A PDE is said to be reducible to a linear PDE with constant coefficients if it can be transformed into such an equation by a change of variables .

- Some examples of equations reducible to linear PDEs with constant coefficients are:

  - The heat equation
  $$
  \frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2}
  $$
  where $k$ is a constant. This equation can be reduced to a linear PDE with constant coefficients by the change of variables $v = e^{-kt} u$ and $y = x$.

  - The wave equation
  $$
  \frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
  $$
  where $c$ is a constant. This equation can be reduced to a linear PDE with constant coefficients by the change of variables $v = u$ and $y = x - ct$, $z = x + ct$.

  - The Laplace equation
  $$
  \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0
  $$
  This equation can be reduced to a linear PDE with constant coefficients by the change of variables $v = u$ and $w = x + iy$, $z = x - iy$.

- The general method for finding a change of variables that reduces a PDE to a linear PDE with constant coefficients is to use the characteristic equation of the PDE, which is obtained by replacing the partial derivatives by algebraic variables .

  - For example, the characteristic equation of the PDE
  $$
  x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} + u = 0
  $$
  is
  $$
  x p + y q + 1 = 0
  $$
  where $p = \frac{\partial u}{\partial x}$ and $q = \frac{\partial u}{\partial y}$.

  - The characteristic equation can be solved for $p$ and $q$ in terms of $x$ and $y$, and then integrated to find the new variables $v$ and $w$ such that
  $$
  p = \frac{\partial v}{\partial x} \frac{\partial u}{\partial v} + \frac{\partial w}{\partial x} \frac{\partial u}{\partial w}
  $$
  and
  $$
  q = \frac{\partial v}{\partial y} \frac{\partial u}{\partial v} + \frac{\partial w}{\partial y} \frac{\partial u}{\partial w}
  $$

  - In this example, the characteristic equation can be solved as
  $$
  p = -\frac{1}{x} \quad \text{and} \quad q = -\frac{1}{y}
  $$
  and then integrated to get
  $$
  v = \ln x \quad \text{and} \quad w = \ln y
  $$

  - The PDE can then be written as
  $$
  \frac{\partial u}{\partial v} + \frac{\partial u}{\partial w} + u = 0
  $$
  which is a linear PDE with constant coefficients.