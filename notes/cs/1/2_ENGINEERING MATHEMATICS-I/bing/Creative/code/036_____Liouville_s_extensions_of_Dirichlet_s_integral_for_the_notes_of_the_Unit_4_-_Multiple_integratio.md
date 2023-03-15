### Liouville’s extensions of Dirichlet’s integral

- Dirichlet's integral is a special case of a multiple integral of the form

$$\int_{0}^{\infty} \int_{0}^{\infty} \frac{x^{\alpha-1} y^{\beta-1}}{(x+y)^{\alpha+\beta+\gamma}} F(x+y) \, dx \, dy$$

where $\alpha, \beta, \gamma$ are positive constants and $F$ is a continuous function.

- Dirichlet's theorem states that this integral can be simplified as

$$\frac{\Gamma(\alpha) \Gamma(\beta) \Gamma(\gamma)}{\Gamma(\alpha+\beta+\gamma)} \int_{0}^{\infty} F(t) t^{\alpha+\beta+\gamma-1} \, dt$$

where $\Gamma$ is the gamma function, defined by

$$\Gamma(z) = \int_{0}^{\infty} t^{z-1} e^{-t} \, dt$$

- Liouville's extension of Dirichlet's theorem generalizes the result to integrals of the form

$$\int_{V} x^{\alpha-1} y^{\beta-1} z^{\gamma-1} F(x+y+z) \, dx \, dy \, dz$$

where $V$ is the region bounded by $x \geq 0, y \geq 0, z \geq 0$ and $h_1 \leq x+y+z \leq h_2$, where $h_1$ and $h_2$ are positive constants.

- Liouville's theorem states that this integral can be simplified as

$$\frac{\Gamma(\alpha) \Gamma(\beta) \Gamma(\gamma)}{\Gamma(\alpha+\beta+\gamma)} \int_{h_1}^{h_2} F(t) t^{\alpha+\beta+\gamma-1} \, dt$$

- The proof of Liouville's theorem uses the change of variables $u = x+y+z, v = x/y, w = x/z$ and the properties of the beta function, defined by

$$B(p,q) = \int_{0}^{1} t^{p-1} (1-t)^{q-1} \, dt = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p+q)}$$

- Liouville's extension of Dirichlet's theorem can be used to evaluate various integrals involving symmetric functions of three variables, such as

$$\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} \frac{1}{(1+xyz)^2} \, dz \, dy \, dx$$

- The applications of Liouville's extension of Dirichlet's theorem include the study of the Dirichlet series, the Riemann zeta function, and the polygamma functions.