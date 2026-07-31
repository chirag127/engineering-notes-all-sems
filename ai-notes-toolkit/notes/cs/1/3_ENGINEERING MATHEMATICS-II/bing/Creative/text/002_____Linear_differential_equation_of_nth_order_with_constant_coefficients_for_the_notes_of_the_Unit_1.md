### Linear differential equation of nth order with constant coefficients

- A linear differential equation of nth order with constant coefficients is an equation of the form

$$
a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_2 y'' + a_1 y' + a_0 y = f(x)
$$

where $a_n, a_{n-1}, \ldots, a_0$ are constants, $a_n \neq 0$, and $f(x)$ is a given function.

- The equation is called **homogeneous** if $f(x) = 0$, and **non-homogeneous** otherwise.

- The general solution of a homogeneous linear differential equation with constant coefficients is a linear combination of $n$ linearly independent solutions, which can be found by assuming a solution of the form $y = e^{rx}$ and solving the **characteristic equation** 

$$
a_n r^n + a_{n-1} r^{n-1} + \cdots + a_2 r^2 + a_1 r + a_0 = 0
$$

- Depending on the nature of the roots of the characteristic equation, the solutions may be real or complex, distinct or repeated, and may involve exponential, trigonometric, or hyperbolic functions.

- The general solution of a non-homogeneous linear differential equation with constant coefficients is the sum of the general solution of the homogeneous equation and a **particular solution** of the non-homogeneous equation, which can be found by various methods, such as **undetermined coefficients** or **variation of parameters** .

- The method of undetermined coefficients involves guessing a particular solution of the same form as $f(x)$, with some unknown coefficients, and then plugging it into the equation to determine the coefficients.

- The method of variation of parameters involves finding $n$ functions $u_1(x), u_2(x), \ldots, u_n(x)$ such that the particular solution is given by

$$
y_p = u_1 y_1 + u_2 y_2 + \cdots + u_n y_n
$$

where $y_1, y_2, \ldots, y_n$ are the solutions of the homogeneous equation, and then solving a system of linear equations to find the functions $u_1, u_2, \ldots, u_n$.

- The general solution of a linear differential equation of nth order with constant coefficients is unique up to a linear combination of the solutions of the homogeneous equation.