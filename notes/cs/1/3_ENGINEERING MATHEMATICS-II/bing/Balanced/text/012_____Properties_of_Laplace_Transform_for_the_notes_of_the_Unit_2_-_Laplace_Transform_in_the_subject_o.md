### Properties of Laplace Transform

- Laplace transform is a linear operator, which means that if $f(t)$ and $g(t)$ are two functions and $a$ and $b$ are constants, then
$$\mathcal{L}\{af(t)+bg(t)\}=a\mathcal{L}\{f(t)\}+b\mathcal{L}\{g(t)\}$$
- Laplace transform is a one-to-one mapping, which means that if $f(t)$ and $g(t)$ are two functions with the same Laplace transform, then they are equal except for a finite number of points.
- Laplace transform has the property of differentiation in the $s$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\left\{\frac{df}{dt}\right\}=sF(s)-f(0)$$
and in general,
$$\mathcal{L}\left\{\frac{d^nf}{dt^n}\right\}=s^nF(s)-s^{n-1}f(0)-s^{n-2}f'(0)-\cdots-f^{(n-1)}(0)$$
- Laplace transform has the property of integration in the $s$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\left\{\int_0^t f(\tau)d\tau\right\}=\frac{F(s)}{s}$$
- Laplace transform has the property of multiplication by $t^n$ in the $t$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\{t^nf(t)\}=(-1)^n\frac{d^nF}{ds^n}$$
- Laplace transform has the property of division by $t$ in the $t$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\left\{\frac{f(t)}{t}\right\}=\int_s^\infty F(u)du$$
- Laplace transform has the property of shifting in the $t$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\{f(t-a)u(t-a)\}=e^{-as}F(s)$$
where $u(t)$ is the unit step function and $a$ is a constant.
- Laplace transform has the property of shifting in the $s$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\{e^{at}f(t)\}=F(s-a)$$
where $a$ is a constant.
- Laplace transform has the property of scaling in the $t$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\{f(at)\}=\frac{1}{a}F\left(\frac{s}{a}\right)$$
where $a$ is a constant.
- Laplace transform has the property of convolution in the $t$-domain, which means that if $f(t)$ and $g(t)$ are two functions with Laplace transforms $F(s)$ and $G(s)$, then
$$\mathcal{L}\{f(t)*g(t)\}=F(s)G(s)$$
where $f(t)*g(t)$ is the convolution of $f(t)$ and $g(t)$ defined by
$$f(t)*g(t)=\int_0^t f(\tau)g(t-\tau)d\tau$$
- Laplace transform has the property of periodicity in the $t$-domain, which means that if $f(t)$ is a periodic function with period $T$, then
$$\mathcal{L}\{f(t)\}=\frac{1}{1-e^{-sT}}\int_0^T e^{-st}f(t)dt$$