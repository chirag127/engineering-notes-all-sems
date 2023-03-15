### Dirichlet's integral and its applications to area and volume

- Dirichlet's integral is a type of integral that appears in various contexts in mathematics and physics, such as Dirichlet's principle, Fourier series, and phase volume  .
- One form of Dirichlet's integral is given by

$$
D(f) = \int_{\Omega} |\nabla f|^2 dV
$$

where $\Omega$ is a bounded domain in $\mathbb{R}^n$, $f$ is a function defined on $\Omega$, and $\nabla f$ is the gradient of $f$.
- Another form of Dirichlet's integral is given by

$$
D_n(x) = \int_{-1}^1 \frac{\sin((n+1/2)x)}{\sin(x/2)} dx
$$

where $n$ is a positive integer, and the integrand is the Dirichlet kernel, which is used to obtain the partial sums of the Fourier series of a periodic function.
- A third form of Dirichlet's integral is given by

$$
D_n(a_1,\dots,a_n) = \int_0^{\infty} \frac{x^{a_1-1}}{(1+x)^{a_1+\dots+a_n}} dx
$$

where $a_1,\dots,a_n$ are positive real numbers, and the integrand is a special case of the beta function.
- Dirichlet's integral can be used to find the area and volume of certain surfaces and solids by applying the divergence theorem or the coarea formula .
- For example, let $S$ be a smooth surface in $\mathbb{R}^3$ that is the graph of a function $z=f(x,y)$ defined on a bounded domain $D$ in the $xy$-plane. Then the area of $S$ is given by

$$
A(S) = \int_D \sqrt{1+f_x^2+f_y^2} dA = D(f)
$$

where $f_x$ and $f_y$ are the partial derivatives of $f$ with respect to $x$ and $y$, and $dA$ is the area element in the $xy$-plane.
- Similarly, let $V$ be a solid in $\mathbb{R}^3$ that is bounded by two smooth surfaces $S_1$ and $S_2$ that are the graphs of functions $z=f_1(x,y)$ and $z=f_2(x,y)$ defined on a common bounded domain $D$ in the $xy$-plane, where $f_1 \leq f_2$ on $D$. Then the volume of $V$ is given by

$$
V(V) = \int_D (f_2-f_1) dA = D(f_2) - D(f_1)
$$

where $dA$ is the area element in the $xy$-plane.
- Another example is the Dirichlet problem with a volume constraint, which is to find a function $u$ defined on a bounded domain $\Omega$ in $\mathbb{R}^n$ that minimizes the Dirichlet integral $D(u)$ among all functions that have a given boundary value $g$ on $\partial \Omega$ and a given volume $V$ under the graph of $u$. This problem can be solved by using the Lagrange multiplier method and the Euler-Lagrange equation, and the solution is given by

$$
u(x) = g(x) + \frac{V - \int_{\Omega} g dV}{|\Omega|} + \frac{2H}{n} \text{dist}(x,\partial \Omega)
$$

where $H$ is a constant and $\text{dist}(x,\partial \Omega)$ is the distance from $x$ to the boundary of $\Omega$.