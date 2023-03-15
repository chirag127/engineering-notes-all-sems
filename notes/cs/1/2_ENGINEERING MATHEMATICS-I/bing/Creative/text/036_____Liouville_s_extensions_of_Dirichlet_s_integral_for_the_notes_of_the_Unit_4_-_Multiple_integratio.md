### Liouville’s extensions of Dirichlet’s integral

- Dirichlet's integral is a special case of a multiple integral of the form

$$\int_{0}^{\infty} \int_{0}^{\infty} \frac{f(x+y)}{x^m y^n} dx dy$$

where $f$ is a continuous function, and $m$ and $n$ are positive integers.

- Dirichlet's theorem states that if $f$ is continuous on $[0,\infty)$ and has a finite limit as $x \to \infty$, then

$$\int_{0}^{\infty} \int_{0}^{\infty} \frac{f(x+y)}{x^m y^n} dx dy = \frac{\Gamma(m) \Gamma(n)}{\Gamma(m+n)} \int_{0}^{\infty} f(x) x^{m+n-1} dx$$

where $\Gamma$ is the gamma function.

- Liouville's extension of Dirichlet's theorem generalizes the result to higher dimensions and more general regions. It states that if $x_1, x_2, \dots, x_k$ are positive variables such that $h_1 < (x_1 + x_2 + \dots + x_k) < h_2$, where $h_1$ and $h_2$ are positive constants, and $f$ is a continuous function on $[h_1, h_2]$, then

$$\int_{V} x_1^{l_1-1} x_2^{l_2-1} \dots x_k^{l_k-1} f(x_1 + x_2 + \dots + x_k) dx_1 dx_2 \dots dx_k = \frac{\Gamma(l_1) \Gamma(l_2) \dots \Gamma(l_k)}{\Gamma(l_1 + l_2 + \dots + l_k)} \int_{h_1}^{h_2} f(h) h^{l_1 + l_2 + \dots + l_k - 1} dh$$

where $l_1, l_2, \dots, l_k$ are positive integers, and $V$ is the region defined by the inequalities $h_1 < (x_1 + x_2 + \dots + x_k) < h_2$ and $x_1, x_2, \dots, x_k > 0$.

- Liouville's extension of Dirichlet's theorem can be used to evaluate multiple integrals that involve functions of the sum of the variables, such as

$$\int_{0}^{1} \int_{0}^{1-x} \int_{0}^{1-x-y} \frac{e^{x+y+z}}{x y z} dx dy dz$$

or

$$\int_{0}^{\infty} \int_{0}^{\infty} \int_{0}^{\infty} \frac{\sin(x+y+z)}{x^2 y^2 z^2} dx dy dz$$

- Liouville's extension of Dirichlet's theorem can be proved by using the change of variables $u = x_1 + x_2 + \dots + x_k$, $v_1 = x_1/u$, $v_2 = x_2/u$, $\dots$, $v_{k-1} = x_{k-1}/u$, and applying Dirichlet's theorem to the resulting integral. Alternatively, it can be derived by using the properties of the beta and gamma functions, which are defined by

$$\Gamma(x) = \int_{0}^{\infty} t^{x-1} e^{-t} dt$$

and

$$B(x,y) = \int_{0}^{1} t^{x-1} (1-t)^{y-1} dt = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}$$