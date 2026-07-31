# Change of variables for the notes of the Unit 2 - Differential Calculus- I in the subject of ENGINEERING MATHEMATICS-I

- Change of variables is a method of transforming a differential equation into a simpler or more convenient form by introducing a new dependent or independent variable.
- Change of variables can be useful for solving separable, homogeneous, or Bernoulli differential equations, as well as for evaluating integrals by substitution.
- Some examples of change of variables are:

  - Substituting $u = y'$ to reduce a homogeneous differential equation of the form $y' = Q(x) - P(x)y$ to a separable equation of the form $u = Q(x) - P(x)u$.
  - Substituting $y = xV(x)$ to reduce a homogeneous differential equation of the form $y' = f(x,y)$ to a separable equation of the form $\frac{1}{F(V) - V} \frac{dV}{dx} = \frac{1}{x}$.
  - Substituting $y = vx^n$ to reduce a Bernoulli differential equation of the form $y' + p(x)y = q(x)y^n$ to a linear equation of the form $v' + (1-n)p(x)v = (1-n)q(x)$.
  - Substituting $u = g(x)$ to evaluate an integral of the form $\int f(g(x))g'(x) dx$ by using the formula $\int f(g(x))g'(x) dx = \int f(u) du$.

- Change of variables can also be applied to multivariable functions, such as in the change of variables theorem for multiple integrals, which states that if $T$ is a one-to-one and continuously differentiable transformation from a region $D$ in the $uv$-plane to a region $R$ in the $xy$-plane, then $\iint_R f(x,y) dA = \iint_D f(T(u,v)) |J| du dv$, where $J$ is the Jacobian determinant of the transformation.