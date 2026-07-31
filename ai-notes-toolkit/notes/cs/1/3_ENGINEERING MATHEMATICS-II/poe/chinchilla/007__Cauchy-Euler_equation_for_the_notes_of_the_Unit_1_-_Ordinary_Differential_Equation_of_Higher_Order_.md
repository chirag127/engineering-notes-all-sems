### Cauchy-Euler Equation for the Notes of Unit 1 - Ordinary Differential Equations of Higher Order in the Subject of ENGINEERING MATHEMATICS-II

The Cauchy-Euler equation is a type of ordinary differential equation (ODE) that is used to solve problems in engineering, physics, and other related fields. It is also known as the Euler-Cauchy equation or the homogeneous linear second-order ODE. In this section, we will learn about the Cauchy-Euler equation and how to solve it.

#### Formulation of the Cauchy-Euler Equation

The Cauchy-Euler equation is a second-order linear differential equation of the form:

$$a_nx^n y'' + a_{n-1}x^{n-1}y' + \cdots + a_1xy + a_0y = 0$$

where $a_n, a_{n-1}, \cdots, a_1, a_0$ are constants, and $y$ is an unknown function of $x$. 

#### Solving the Cauchy-Euler Equation

To solve the Cauchy-Euler equation, we use the substitution $y=x^r$, where $r$ is a constant. Then, we differentiate this substitution with respect to $x$ to obtain $y'=rx^{r-1}$ and $y''=r(r-1)x^{r-2}$. Substituting these expressions into the Cauchy-Euler equation, we get:

$$a_nr(r-1)x^n x^{r-2} + a_{n-1}r x^{n-1} x^{r-1} + \cdots + a_1x x^r + a_0x^r = 0$$

Simplifying the equation, we get:

$$a_nr(r-1)x^r + a_{n-1}r x^r + \cdots + a_1x^r + a_0x^r = 0$$

$$x^r(a_nr(r-1) + a_{n-1}r + \cdots + a_1 + a_0) = 0$$

Since $x^r \neq 0$, we can divide both sides by $x^r$ to obtain:

$$a_nr(r-1) + a_{n-1}r + \cdots + a_1 + a_0 = 0$$

This is a quadratic equation in $r$, which we can solve using the quadratic formula to obtain the roots $r_1$ and $r_2$. Then, the general solution of the Cauchy-Euler equation is given by:

$$y = c_1x^{r_1} + c_2x^{r_2}$$

where $c_1$ and $c_2$ are constants determined by the initial or boundary conditions of the problem.

#### Special Cases of the Cauchy-Euler Equation

There are several special cases of the Cauchy-Euler equation, which have simpler solutions:

1. $a_n=0$: In this case, the Cauchy-Euler equation reduces to a first-order linear differential equation, which can be solved using standard methods.

2. $a_n=a_{n-1}=0$: In this case, the Cauchy-Euler equation reduces to a linear homogeneous equation with constant coefficients, which can be solved using the characteristic equation.

3. $a_n=a_{n-2}=0$: In this case, the Cauchy-Euler equation reduces to a linear homogeneous equation with constant coefficients, which can be solved using the method of undetermined coefficients.

In conclusion, the Cauchy-Euler equation is a powerful tool for solving second-order linear differential equations. By using the substitution $y=x^r$, we can reduce the problem to a quadratic equation in $r$, which can be easily solved to obtain the general solution of the equation.