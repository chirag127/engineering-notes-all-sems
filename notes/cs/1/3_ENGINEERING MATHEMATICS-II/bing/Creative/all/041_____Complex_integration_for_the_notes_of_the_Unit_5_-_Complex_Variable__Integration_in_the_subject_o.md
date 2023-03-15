# Complex integration

Complex integration is a generalization of real integration to the complex domain. It is useful for studying the properties and applications of analytic functions, which are complex functions that are differentiable in some domain.

## Complex functions of a real variable

A complex function of a real variable is a function of the form

$$f(t) = u(t) + iv(t)$$

where $t$ is a real variable and $u(t)$ and $v(t)$ are real functions. Such a function can be interpreted as a curve in the complex plane, parametrized by $t$.

The derivative of a complex function of a real variable is defined as

$$f'(t) = \lim_{h \to 0} \frac{f(t+h) - f(t)}{h}$$

if the limit exists. The derivative can be computed by differentiating the real and imaginary parts separately, using the rules of real calculus. That is,

$$f'(t) = u'(t) + iv'(t)$$

The integral of a complex function of a real variable is defined as

$$\int_a^b f(t) dt = \int_a^b u(t) dt + i \int_a^b v(t) dt$$

where the integrals on the right-hand side are real integrals. The integral can be interpreted as the net change of the function along the curve from $t=a$ to $t=b$.

## Complex functions of a complex variable

A complex function of a complex variable is a function of the form

$$f(z) = u(x,y) + iv(x,y)$$

where $z = x + iy$ is a complex variable and $u(x,y)$ and $v(x,y)$ are real functions of two real variables. Such a function can be interpreted as a mapping from the complex plane to the complex plane.

The derivative of a complex function of a complex variable is defined as

$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z+\Delta z) - f(z)}{\Delta z}$$

if the limit exists and is independent of the direction of $\Delta z$. The derivative can be interpreted as the rate of change of the function at a point in the complex plane.

A complex function of a complex variable is said to be analytic (or holomorphic) in a domain if it is differentiable at every point in that domain. A function that is analytic in the whole complex plane is called entire.

A necessary (but not sufficient) condition for a complex function of a complex variable to be analytic is that it satisfies the Cauchy-Riemann equations, which are

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

## Complex integration of a complex variable

A complex integration of a complex variable is an integral of the form

$$\int_C f(z) dz$$

where $C$ is a curve (or contour) in the complex plane and $f(z)$ is a complex function of a complex variable. Such an integral can be interpreted as the net change of the function along the curve.

To evaluate a complex integration of a complex variable, one can parametrize the curve $C$ by a complex function of a real variable, say $z(t) = x(t) + iy(t)$, where $t$ ranges from $a$ to $b$. Then, by the chain rule, one can write

$$\int_C f(z) dz = \int_a^b f(z(t)) z'(t) dt$$

which is a complex integration of a real variable.

Alternatively, one can split the complex function $f(z)$ into its real and imaginary parts, say $f(z) = u(x,y) + iv(x,y)$, where $z = x + iy$. Then, by the definition of complex integration, one can write

$$\int_C f(z) dz = \int_C (u dx - v dy) + i \int_C (v dx + u dy)$$

which are two real line integrals along the curve $C$.

## Properties and applications of complex integration

Complex integration has many properties and applications in complex analysis. Some of them are:

- The Fundamental Theorem of Calculus: If $f(z)$ is an analytic function in a domain $D$ and $F(z)$ is an antiderivative of