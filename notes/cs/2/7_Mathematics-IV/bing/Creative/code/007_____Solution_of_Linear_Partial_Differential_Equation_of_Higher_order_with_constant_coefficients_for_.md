### Solution of Linear Partial Differential Equation of Higher order with constant coefficients

- A linear partial differential equation of higher order with constant coefficients is of the form

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The general solution of such an equation consists of two parts: the complementary function and the particular integral.

- The complementary function is the general solution of the homogeneous equation, i.e., when $f(x) = 0$. It can be obtained by using the method of characteristic equation, which is similar to the method for ordinary differential equations.

- The characteristic equation of the homogeneous equation is

$$
a_0 r^n + a_1 r^{n-1} + \cdots + a_n = 0
$$

where $r$ is a complex variable. The roots of this equation are called the characteristic roots, and they determine the form of the complementary function.

- If the characteristic equation has $n$ distinct real roots $r_1, r_2, \ldots, r_n$, then the complementary function is

$$
u_c(x) = c_1 e^{r_1 x} + c_2 e^{r_2 x} + \cdots + c_n e^{r_n x}
$$

where $c_1, c_2, \ldots, c_n$ are arbitrary constants.

- If the characteristic equation has repeated real roots, then the complementary function is obtained by multiplying each repeated root by a power of $x$. For example, if $r_1$ is a root of multiplicity $m$, then the terms corresponding to $r_1$ are

$$
c_1 e^{r_1 x} + c_2 x e^{r_1 x} + \cdots + c_m x^{m-1} e^{r_1 x}
$$

- If the characteristic equation has complex roots, then the complementary function is obtained by using the Euler's formula, which states that

$$
e^{i \theta} = \cos \theta + i \sin \theta
$$

where $i$ is the imaginary unit. For example, if $r = \alpha + i \beta$ is a complex root, then the terms corresponding to $r$ and its conjugate $\overline{r} = \alpha - i \beta$ are

$$
c_1 e^{(\alpha + i \beta) x} + c_2 e^{(\alpha - i \beta) x} = c_1 (e^{\alpha x} \cos \beta x + i e^{\alpha x} \sin \beta x) + c_2 (e^{\alpha x} \cos \beta x - i e^{\alpha x} \sin \beta x)
$$

which can be simplified by using the trigonometric identities to

$$
(c_1 + c_2) e^{\alpha x} \cos \beta x + i (c_1 - c_2) e^{\alpha x} \sin \beta x
$$

By letting $A = c_1 + c_2$ and $B = i (c_1 - c_2)$, we can write the above expression as

$$
A e^{\alpha x} \cos \beta x + B e^{\alpha x} \sin \beta x
$$

- The particular integral is a particular solution of the non-homogeneous equation, i.e., when $f(x) \neq 0$. It can be obtained by using various methods, such as the method of undetermined coefficients, the method of variation of parameters, or the method of Fourier transforms.

- The method of undetermined coefficients is based on guessing the form of the particular integral based on the form of $f(x)$. For example, if $f(x) = a e^{bx}$, then we can guess that the particular integral is of the form $u_p(x) = A e^{bx}$, where $A$ is an unknown constant. Then we substitute $u_p(x)$ into the original equation and solve for $A$.

- The method of variation of parameters is based on assuming that the