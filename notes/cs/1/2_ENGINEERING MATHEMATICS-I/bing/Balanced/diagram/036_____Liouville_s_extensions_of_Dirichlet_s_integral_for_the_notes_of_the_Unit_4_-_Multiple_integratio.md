### Liouville’s extensions of Dirichlet’s integral

- Dirichlet's integral is a special case of a multiple integral of the form

$$\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} x^{l-1} y^{m-1} z^{n-1} F(x+y+z) \, dz \, dy \, dx$$

where $l, m, n$ are positive constants and $F$ is a continuous function.

- Liouville's extension of Dirichlet's theorem states that if $x, y, z$ are all positive such that $h_1 < (x+y+z) < h_2$, then

$$\int_{0}^{\infty} \int_{0}^{\infty} \int_{0}^{\infty} x^{l-1} y^{m-1} z^{n-1} F(x+y+z) \, dz \, dy \, dx$$

$$= \frac{\Gamma(l) \Gamma(m) \Gamma(n)}{\Gamma(l+m+n)} \int_{h_1}^{h_2} F(h) h^{l+m+n-1} \, dh$$

where $\Gamma$ is the gamma function.

- The proof of Liouville's extension is based on the change of variables $u = x+y+z, v = x+y, w = x$, and the properties of the gamma and beta functions.

- Liouville's extension can be used to evaluate multiple integrals of the form

$$\int_{V} x^{l-1} y^{m-1} z^{n-1} F(x+y+z) \, dV$$

where $V$ is a region bounded by planes of the form $x+y+z = c$ and the coordinate axes.

- Liouville's extension can also be generalized to higher dimensions and other functions of the variables.