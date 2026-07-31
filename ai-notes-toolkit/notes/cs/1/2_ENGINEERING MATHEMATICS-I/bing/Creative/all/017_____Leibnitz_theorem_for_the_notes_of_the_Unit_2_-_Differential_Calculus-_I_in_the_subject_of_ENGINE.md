# Leibnitz Theorem

- Leibnitz theorem is a generalization of the product rule of differentiation .
- It states that if the functions u(x) and v(x) are differentiable n times, then their product u(x).v(x) is also differentiable n times  .
- The formula for the nth derivative of the product of two functions is given by  :

$$
(uv)^{(n)} = \sum_{k=0}^n {n \choose k} u^{(n-k)}v^{(k)}
$$

- Where ${n \choose k}$ is the binomial coefficient, and $u^{(n-k)}$ and $v^{(k)}$ are the (n-k)th and kth derivatives of u and v respectively  .
- The proof of this theorem is based on induction and the product rule of differentiation  .
- The theorem can be extended to the case where the limits of integration are functions of x, and the integrand is a function of both x and t. This is known as the Leibniz integral rule or the differentiation under the integral sign.
- The formula for the Leibniz integral rule is given by:

$$
\frac{d}{dx} \int_{a(x)}^{b(x)} f(x,t) dt = f(x,b(x))\frac{db}{dx} - f(x,a(x))\frac{da}{dx} + \int_{a(x)}^{b(x)} \frac{\partial}{\partial x} f(x,t) dt
$$

- Where $a(x)$ and $b(x)$ are the lower and upper limits of integration, and $f(x,t)$ is the integrand.
- The proof of this rule is based on the fundamental theorem of calculus and the chain rule of differentiation.