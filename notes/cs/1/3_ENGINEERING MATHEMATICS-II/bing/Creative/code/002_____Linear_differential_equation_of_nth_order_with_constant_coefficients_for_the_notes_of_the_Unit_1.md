### Linear differential equation of nth order with constant coefficients

A linear differential equation of nth order with constant coefficients is an equation of the form

```math
a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = f(x)
```

where \(a_n, a_{n-1}, \ldots, a_0\) are constants, \(y\) is the unknown function, and \(f(x)\) is a given function. The equation is called **homogeneous** if \(f(x) = 0\) and **non-homogeneous** otherwise.

The general solution of a linear differential equation of nth order with constant coefficients is given by the sum of the **complementary function** and the **particular integral**. The complementary function is the general solution of the homogeneous equation, and the particular integral is any one solution of the non-homogeneous equation.

To find the complementary function, we assume a solution of the form \(y = e^{rx}\) and substitute it into the homogeneous equation. This gives us a polynomial equation in \(r\) called the **characteristic equation**:

```math
a_n r^n + a_{n-1} r^{n-1} + \cdots + a_1 r + a_0 = 0
```

The roots of the characteristic equation determine the form of the complementary function. There are three possible cases:

- If the characteristic equation has \(n\) distinct real roots \(r_1, r_2, \ldots, r_n\), then the complementary function is

```math
y_c = c_1 e^{r_1 x} + c_2 e^{r_2 x} + \cdots + c_n e^{r_n x}
```

where \(c_1, c_2, \ldots, c_n\) are arbitrary constants.

- If the characteristic equation has repeated real roots, then we need to multiply the exponential terms by powers of \(x\) to obtain linearly independent solutions. For example, if \(r\) is a root of multiplicity \(k\), then the corresponding terms in the complementary function are

```math
y_c = (c_1 + c_2 x + \cdots + c_k x^{k-1}) e^{rx}
```

- If the characteristic equation has complex roots, then we use Euler's formula to write them as

```math
r = \alpha \pm i \beta
```

where \(\alpha\) and \(\beta\) are real numbers. Then the corresponding terms in the complementary function are

```math
y_c = e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x)
```

To find the particular integral, we use different methods depending on the form of \(f(x)\). Some of the common methods are:

- **Method of undetermined coefficients**: This method works when \(f(x)\) is a polynomial, an exponential, a sine, a cosine, or a linear combination of these functions. We assume a particular integral of the same form as \(f(x)\), but with unknown coefficients, and substitute it into the non-homogeneous equation. Then we solve for the unknown coefficients by equating the coefficients of the same powers of \(x\) or the same trigonometric functions on both sides of the equation.

- **Method of variation of parameters**: This method works for any \(f(x)\), but it is more complicated than the method of undetermined coefficients. We assume a particular integral of the form

```math
y_p = u_1 y_1 + u_2 y_2 + \cdots + u_n y_n
```

where \(y_1, y_2, \ldots, y_n\) are \(n\) linearly independent solutions of the homogeneous equation, and \(u_1, u_2, \ldots, u_n\) are unknown functions. Then we impose the condition that

```math
u_1' y_1 + u_2' y_2 + \cdots + u_n' y_n = 0
```

This reduces the order of the non-homogeneous equation by one, and allows us to solve for \(u_1', u_2', \ldots, u_n'\) by using a system of linear equations. Then we integrate to find \(u_1, u_2, \ldots, u