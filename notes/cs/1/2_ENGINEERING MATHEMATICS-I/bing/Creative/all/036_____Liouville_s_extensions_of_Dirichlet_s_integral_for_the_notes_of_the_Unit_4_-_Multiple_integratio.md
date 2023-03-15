# Liouville’s extensions of Dirichlet’s integral

- Dirichlet's integral is a special case of a multiple integral of the form

$$
\int_{0}^{\infty} \int_{0}^{\infty} \frac{x^{a-1} y^{b-1}}{(x+y)^{a+b}} d x d y=\frac{\Gamma(a) \Gamma(b)}{\Gamma(a+b)}
$$

where $\Gamma$ is the gamma function and $a, b > 0$.

- Liouville's extension of Dirichlet's integral is a generalization that allows the integration region to be any bounded domain $V$ in $\mathbb{R}^n$ and the integrand to be any function $F(x_1, x_2, \ldots, x_n)$ that depends only on the sum of the variables $x_1 + x_2 + \cdots + x_n = h$.

- Liouville's extension states that if $x_1, x_2, \ldots, x_n$ are all positive such that $h_1 < h < h_2$, then

$$
\int_{V} x_{1}^{a_{1}-1} x_{2}^{a_{2}-1} \cdots x_{n}^{a_{n}-1} F\left(x_{1}+x_{2}+\cdots+x_{n}\right) d x_{1} d x_{2} \cdots d x_{n}=\frac{\Gamma\left(a_{1}\right) \Gamma\left(a_{2}\right) \cdots \Gamma\left(a_{n}\right)}{\Gamma\left(a_{1}+a_{2}+\cdots+a_{n}\right)} \int_{h_{1}}^{h_{2}} F(h) h^{a_{1}+a_{2}+\cdots+a_{n}-1} d h
$$

where $a_1, a_2, \ldots, a_n > 0$.

- The proof of Liouville's extension is based on the change of variables $x_1 + x_2 + \cdots + x_n = h$ and $x_1 / h = u_1, x_2 / h = u_2, \ldots, x_n / h = u_n$, which transforms the multiple integral into a product of a single integral and a beta function.

- Liouville's extension can be used to evaluate multiple integrals that involve functions of the sum of the variables, such as

$$
\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} \frac{1}{(1+x+y+z)^{4}} d z d y d x=\frac{\pi^{2}}{36}
$$

by applying the extension with $n = 4$, $a_1 = a_2 = a_3 = a_4 = 1$, $F(h) = 1 / (1 + h)^4$, $h_1 = 0$, and $h_2 = 1$.