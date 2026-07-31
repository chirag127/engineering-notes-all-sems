### Beta and Gamma Function and Their Properties

- The beta function is a function of two variables, denoted by B(x,y), that is defined by the integral

  `B(x,y) = int_0^1 t^(x-1) (1-t)^(y-1) dt`

  for any positive real numbers x and y.

- The gamma function is a function of one variable, denoted by Γ(x), that is defined by the integral

  `Γ(x) = int_0^∞ t^(x-1) e^(-t) dt`

  for any positive real number x.

- The beta function is symmetric, meaning that B(x,y) = B(y,x) for any x and y.

- The beta function is related to the gamma function by the formula

  `B(x,y) = (Γ(x) Γ(y)) / Γ(x+y)`

  This can be proved by using the substitution `t = u/(u+v)` in the integral for B(x,y) and then using the properties of the gamma function.

- The beta function is also related to the binomial coefficients by the formula

  `B(x,y) = (x-1)! (y-1)! / (x+y-1)!`

  for any positive integers x and y. This can be proved by using the binomial theorem and the definition of the gamma function as a generalization of the factorial function.

- The gamma function is a generalization of the factorial function, meaning that Γ(n) = (n-1)! for any positive integer n.

- The gamma function satisfies the recurrence relation

  `Γ(x+1) = x Γ(x)`

  for any positive real number x. This can be proved by integrating by parts in the integral for Γ(x+1).

- The gamma function also satisfies the reflection formula

  `Γ(x) Γ(1-x) = π / sin(πx)`

  for any x that is not an integer. This can be proved by using the substitution `t = sin^2(θ)` in the integral for Γ(x) and then using the trigonometric identity `sin(2θ) = 2 sin(θ) cos(θ)`.

- The gamma function has a unique analytic continuation to the complex plane, except for the negative integers, where it has simple poles. The residue at the pole -n is (-1)^n / n! for any positive integer n.