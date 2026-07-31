### Liouville’s extensions of Dirichlet’s integral

- Dirichlet's integral is a special case of a multiple integral of the form

$$
\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} f(x+y+z) \, dz \, dy \, dx
$$

- Dirichlet's theorem states that if $f$ is a continuous function on $[0,1]$, then

$$
\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} f(x+y+z) \, dz \, dy \, dx = \frac{1}{6} \int_{0}^{1} f(t) \, dt
$$

- Liouville's extension of Dirichlet's theorem generalizes the result to any positive exponents $l,m,n$ such that $l+m+n>1$, and any positive limits $h_1<h_2$. It states that if $f$ is a continuous function on $[h_1,h_2]$, then

$$
\int_{0}^{h_2} \int_{0}^{h_2-x} \int_{0}^{h_2-x-y} x^{l-1} y^{m-1} z^{n-1} f(x+y+z) \, dz \, dy \, dx = \frac{\Gamma(l) \Gamma(m) \Gamma(n)}{\Gamma(l+m+n)} \int_{h_1}^{h_2} f(t) t^{l+m+n-1} \, dt
$$

- The proof of Liouville's extension uses the change of variables $x=ht$, $y=hs$, $z=hr$, where $h$ is a constant, and the properties of the gamma function and the beta function.

- The gamma function is defined by

$$
\Gamma(x) = \int_{0}^{\infty} t^{x-1} e^{-t} \, dt
$$

- The beta function is defined by

$$
B(x,y) = \int_{0}^{1} t^{x-1} (1-t)^{y-1} \, dt
$$

- The gamma function and the beta function are related by

$$
B(x,y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}
$$

- Liouville's extension can be used to evaluate some multiple integrals that are not of the form $f(x+y+z)$, by using suitable transformations or symmetries. For example, see .