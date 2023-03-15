# Leibnitz Theorem

- Leibnitz theorem is a generalization of the product rule of differentiation.
- It states that if there are two functions, let them be u(x) and v(x), and if they both are differentiable n times, then their product u(x).v(x) is also differentiable n times.
- The formula for the nth derivative of the product of two functions is given by:

$$
(uv)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} u^{(n-k)} v^{(k)}
$$

- Where $\binom{n}{k}$ is the binomial coefficient, and $u^{(n-k)}$ and $v^{(k)}$ are the (n-k)th and kth derivatives of u and v, respectively.
- The proof of this theorem is based on induction and the product rule of differentiation.
- The theorem can be applied to find the derivatives of products of functions, such as polynomials, trigonometric functions, exponential functions, etc.
- The theorem can also be extended to the case of more than two functions, by applying it repeatedly. For example, the nth derivative of the product of three functions u, v, and w is given by:

$$
(uvw)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} (uv)^{(n-k)} w^{(k)} = \sum_{k=0}^{n} \sum_{j=0}^{n-k} \binom{n}{k} \binom{n-k}{j} u^{(n-k-j)} v^{(j)} w^{(k)}
$$

- The theorem can also be used to find the derivative of an integral with variable limits, which is known as the Leibniz integral rule. The formula for this rule is given by:

$$
\frac{d}{dx} \int_{a(x)}^{b(x)} f(x,t) dt = f(x,b(x)) \frac{db}{dx} - f(x,a(x)) \frac{da}{dx} + \int_{a(x)}^{b(x)} \frac{\partial f}{\partial x} (x,t) dt
$$

- Where $a(x)$ and $b(x)$ are the lower and upper limits of integration, and $f(x,t)$ is a function of two variables. The proof of this rule is based on the fundamental theorem of calculus and the chain rule of differentiation.