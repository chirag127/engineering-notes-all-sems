### Cauchy-Euler equation

The Cauchy-Euler equation is a type of linear differential equation with variable coefficients. It is also known as the Euler-Cauchy equation or the equidimensional equation. The general form of the Cauchy-Euler equation of order n is given by:

```
x^n y^(n) + a_(n-1) x^(n-1) y^(n-1) + ... + a_1 x y' + a_0 y = 0
```

where `a_0, a_1, ..., a_(n-1)` are constants.

The Cauchy-Euler equation can be solved using the method of undetermined coefficients. The first step is to assume a solution of the form `y = x^m`. Substituting this into the Cauchy-Euler equation and simplifying, we obtain a polynomial equation in `m` called the characteristic equation. The roots of the characteristic equation determine the form of the general solution.

If all the roots of the characteristic equation are distinct, the general solution is given by:

```
y = C_1 x^(m_1) + C_2 x^(m_2) + ... + C_n x^(m_n)
```

where `C_1, C_2, ..., C_n` are arbitrary constants and `m_1, m_2, ..., m_n` are the roots of the characteristic equation.

If the characteristic equation has repeated roots, the general solution will include terms of the form `x^m ln(x)^k` where `k` is a non-negative integer. The exact form of the general solution depends on the multiplicities of the roots.

The Cauchy-Euler equation is commonly encountered in problems involving scale-invariant phenomena, such as power laws and fractals. It also arises in the separation of variables in partial differential equations, particularly in problems with cylindrical or spherical symmetry.