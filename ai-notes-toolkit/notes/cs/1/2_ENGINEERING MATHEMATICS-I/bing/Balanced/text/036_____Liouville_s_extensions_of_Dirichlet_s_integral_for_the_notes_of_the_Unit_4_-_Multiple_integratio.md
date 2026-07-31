### Liouville’s extensions of Dirichlet’s integral

- Dirichlet's integral is a special case of a multiple integral of the form

$$\int_{0}^{\infty} \int_{0}^{\infty} \frac{f(x+y)}{x^{\alpha} y^{\beta}} dx dy$$

where $\alpha, \beta > 0$ and $f$ is a continuous function.

- Dirichlet's theorem states that if $\alpha + \beta > 1$, then the integral is equal to

$$\frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha + \beta)} \int_{0}^{\infty} f(t) t^{\alpha + \beta - 1} dt$$

where $\Gamma$ is the gamma function.

- Liouville's extension of Dirichlet's theorem generalizes the result to higher dimensions and more general functions.

- Liouville's extension states that if $x, y, z$ are all positive such that $h_1 < (x + y + z) < h_2$, then

$$\int_{V} x^{l-1} y^{m-1} z^{n-1} F(x, y, z) dx dy dz = \frac{\Gamma(l) \Gamma(m) \Gamma(n)}{\Gamma(l + m + n)} \int_{h_1}^{h_2} F(h) h^{l + m + n - 1} dh$$

where $V$ is the region bounded by the planes $x = 0, y = 0, z = 0$ and $x + y + z = h_2$, and $F$ is a continuous function.

- Liouville's extension can be used to evaluate multiple integrals of the form

$$\int_{V} f(x + y + z) x^{l-1} y^{m-1} z^{n-1} dx dy dz$$

where $f$ is a continuous function and $l, m, n > 0$.

- Liouville's extension can also be applied to other variables and functions, as long as the integrand can be written as a product of a function of the sum of the variables and a function of the product of the variables. For example,

$$\int_{V} f(x + y + z) g(x y z) x^{l-1} y^{m-1} z^{n-1} dx dy dz = \frac{\Gamma(l) \Gamma(m) \Gamma(n)}{\Gamma(l + m + n)} \int_{h_1}^{h_2} f(h) g\left(\frac{h^{l + m + n}}{l! m! n!}\right) h^{l + m + n - 1} dh$$

where $V$ is the same region as before and $f, g$ are continuous functions.