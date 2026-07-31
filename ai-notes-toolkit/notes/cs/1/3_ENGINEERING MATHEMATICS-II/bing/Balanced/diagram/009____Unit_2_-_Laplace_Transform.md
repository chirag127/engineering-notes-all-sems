## Unit 2 - Laplace Transform

- The Laplace transform is a mathematical technique that converts a function of time, f(t), into a function of a complex variable, F(s), where s is a complex number of the form s = σ + jω.
- The Laplace transform is useful for solving differential equations, analyzing linear systems, and studying the frequency response of circuits and signals.
- The Laplace transform is defined as:

```math
F(s) = \int_{0}^{\infty} f(t) e^{-st} dt
```

- The inverse Laplace transform is defined as:

```math
f(t) = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} F(s) e^{st} ds
```

- The inverse Laplace transform can be computed using various methods, such as partial fraction decomposition, residue theorem, convolution theorem, or tables of common Laplace transforms.
- Some properties of the Laplace transform are:

  - Linearity: If f(t) and g(t) are two functions with Laplace transforms F(s) and G(s), respectively, and a and b are constants, then:

  ```math
  \mathcal{L}\{af(t) + bg(t)\} = aF(s) + bG(s)
  ```

  - Time shifting: If f(t) has Laplace transform F(s), then:

  ```math
  \mathcal{L}\{f(t-a)u(t-a)\} = e^{-as}F(s)
  ```

  where u(t) is the unit step function.

  - Frequency shifting: If f(t) has Laplace transform F(s), then:

  ```math
  \mathcal{L}\{e^{at}f(t)\} = F(s-a)
  ```

  - Scaling: If f(t) has Laplace transform F(s), then:

  ```math
  \mathcal{L}\{f(at)\} = \frac{1}{a}F\left(\frac{s}{a}\right)
  ```

  - Differentiation in time domain: If f(t) has Laplace transform F(s), then:

  ```math
  \mathcal{L}\{f'(t)\} = sF(s) - f(0)
  ```

  - Differentiation in frequency domain: If f(t) has Laplace transform F(s), then:

  ```math
  \mathcal{L}\{tf(t)\} = -F'(s)
  ```

  - Integration in time domain: If f(t) has Laplace transform F(s), then:

  ```math
  \mathcal{L}\{\int_{0}^{t} f(\tau) d\tau\} = \frac{1}{s}F(s)
  ```

  - Integration in frequency domain: If f(t) has Laplace transform F(s), then:

  ```math
  \mathcal{L}\{\frac{f(t)}{t}\} = \int_{s}^{\infty} F(\xi) d\xi
  ```

  - Convolution: If f(t) and g(t) are two functions with Laplace transforms F(s) and G(s), respectively, then:

  ```math
  \mathcal{L}\{f(t) * g(t)\} = F(s)G(s)
  ```

  where * denotes the convolution operation defined as:

  ```math
  f(t) * g(t) = \int_{0}^{t} f(\tau) g(t - \tau) d\tau
  ```

- Some examples of common Laplace transforms are:

  - $\mathcal{L}\{1\} = \frac{1}{s}$, for $s > 0$
  - $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}$, for $s > 0$ and $n$ a positive integer
  - $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$, for $s > a$
  - $\mathcal{L}\{\sin(at)\} = \frac{a}{s^2 + a^2}$, for $s > 0$
  - $\mathcal{L}\{\cos(at)\} = \frac{s}{s^2 + a^2}$, for $s > 0$
  - $\mathcal{L}\{\delta(t)\} = 1