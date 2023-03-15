# Beta and Gamma Function and Their Properties

## Definition of Beta Function

The beta function, also known as the Euler integral of the first kind, is a function of two variables that is defined as

$$B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1} dt$$

for any positive real numbers $x$ and $y$.

## Definition of Gamma Function

The gamma function, also known as the Euler integral of the second kind, is a function of one variable that is defined as

$$\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt$$

for any positive real number $x$.

## Relationship between Beta and Gamma Function

A key property of the beta function is its close relationship to the gamma function:

$$B(x,y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$$

A proof of this formula can be found in  or .

## Properties of Beta Function

Some of the properties of the beta function are:

- The beta function is symmetric, meaning that $B(x,y) = B(y,x)$ for all $x$ and $y$.
- The beta function is closely related to binomial coefficients, as $B(n+1,m+1) = \frac{n!m!}{(n+m+1)!}$ for any non-negative integers $n$ and $m$.
- The beta function satisfies the recurrence relation $B(x+1,y) = \frac{x}{x+y} B(x,y+1)$ for all $x$ and $y$.
- The beta function can be expressed in terms of the hypergeometric function as $B(x,y) = \frac{1}{x} {}_2F_1(1,y;x+1;1)$ for all $x$ and $y$.

## Properties of Gamma Function

Some of the properties of the gamma function are:

- The gamma function is a generalization of the factorial function, as $\Gamma(n) = (n-1)!$ for any positive integer $n$.
- The gamma function satisfies the functional equation $\Gamma(x+1) = x\Gamma(x)$ for all $x$.
- The gamma function has a unique analytic continuation to the complex plane, except for the negative integers where it has simple poles.
- The gamma function can be expressed in terms of the incomplete gamma function as $\Gamma(x) = \gamma(x,0)$ for all $x$.
- The gamma function can be approximated by Stirling's formula as $\Gamma(x) \approx \sqrt{2\pi x} \left(\frac{x}{e}\right)^x$ for large $x$.