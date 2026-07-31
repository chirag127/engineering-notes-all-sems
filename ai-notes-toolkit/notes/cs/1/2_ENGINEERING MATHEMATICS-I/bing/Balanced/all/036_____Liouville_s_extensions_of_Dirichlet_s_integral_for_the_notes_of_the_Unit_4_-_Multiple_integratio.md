# Liouville’s extensions of Dirichlet’s integral

- Dirichlet's integral is a special case of a multiple integral of the form
$$
\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} x^{l-1} y^{m-1} z^{n-1} F(x+y+z) \, dz \, dy \, dx
$$
where $l, m, n$ are positive constants and $F$ is a continuous function.

- Dirichlet's theorem states that this integral can be simplified as
$$
\frac{\Gamma(l) \Gamma(m) \Gamma(n)}{\Gamma(l+m+n)} \int_{0}^{1} F(h) h^{l+m+n-1} \, dh
$$
where $\Gamma$ is the gamma function, defined by
$$
\Gamma(t) = \int_{0}^{\infty} x^{t-1} e^{-x} \, dx
$$

- Liouville's extension of Dirichlet's theorem generalizes the result to any multiple integral of the form
$$
\int_{h_1}^{h_2} \int_{h_1}^{h_2} \cdots \int_{h_1}^{h_2} x_1^{l_1-1} x_2^{l_2-1} \cdots x_n^{l_n-1} F(x_1+x_2+\cdots+x_n) \, dx_1 \, dx_2 \cdots dx_n
$$
where $h_1, h_2$ are positive constants, $l_1, l_2, \ldots, l_n$ are positive constants, and $F$ is a continuous function.

- Liouville's extension states that this integral can be simplified as
$$
\frac{\Gamma(l_1) \Gamma(l_2) \cdots \Gamma(l_n)}{\Gamma(l_1+l_2+\cdots+l_n)} \int_{h_1}^{h_2} F(h) h^{l_1+l_2+\cdots+l_n-1} \, dh
$$

- The proof of Liouville's extension uses the change of variables $x_1+x_2+\cdots+x_n = h$ and the beta function, defined by
$$
B(p,q) = \int_{0}^{1} x^{p-1} (1-x)^{q-1} \, dx = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p+q)}
$$

- Liouville's extension can be used to evaluate various multiple integrals involving functions of the sum of the variables, such as
$$
\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} (x+y+z)^{p-1} \sin(x+y+z) \, dz \, dy \, dx
$$
or
$$
\int_{0}^{\pi/2} \int_{0}^{\pi/2} \int_{0}^{\pi/2} \cos(x+y+z) \, dx \, dy \, dz
$$

- Liouville's extension is not applicable to multiple integrals that involve functions of the product or the difference of the variables, such as
$$
\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} F(x y z) \, dz \, dy \, dx
$$
or
$$
\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} F(x-y-z) \, dz \, dy \, dx
$$