### Leibnitz Theorem

- Leibnitz theorem is a generalization of the product rule of differentiation.
- It states that if `f(x)` and `g(x)` are two functions that are `n` times differentiable, then their product `f(x)g(x)` is also `n` times differentiable and its `n`th derivative is given by

```
(f(x)g(x))^(n) = sum_(k=0)^n (nCk f^(k)(x) g^(n-k)(x))
```

- where `nCk` is the binomial coefficient and `f^(k)(x)` and `g^(k)(x)` are the `k`th derivatives of `f(x)` and `g(x)` respectively.
- Leibnitz theorem can be proved by induction on `n`.
- Leibnitz theorem can be used to find the derivatives of products of functions, such as `sin(x)cos(x)`, `(x^2 + 1)(x^3 - 2)`, etc.
- Leibnitz theorem can also be extended to the case of differentiation under the integral sign, where the limits of integration are functions of `x`.
- In that case, the formula is

```
d/dx int_(a(x))^b(x) f(x,t) dt = f(x,b(x)) b'(x) - f(x,a(x)) a'(x) + int_(a(x))^b(x) d/dx f(x,t) dt
```

- where `a(x)` and `b(x)` are the lower and upper limits of integration, and `f(x,t)` is the integrand.