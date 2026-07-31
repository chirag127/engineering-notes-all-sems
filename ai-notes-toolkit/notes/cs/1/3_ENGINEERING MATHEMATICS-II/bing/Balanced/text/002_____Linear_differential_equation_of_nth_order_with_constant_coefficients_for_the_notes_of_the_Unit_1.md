### Linear differential equation of nth order with constant coefficients

- A linear differential equation of nth order with constant coefficients is an equation of the form

$$
a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = f(x)
$$

where $a_n, a_{n-1}, \ldots, a_1, a_0$ are constants and $f(x)$ is a given function of $x$.

- The equation is called **homogeneous** if $f(x) = 0$ and **non-homogeneous** otherwise.

- The general solution of a homogeneous linear differential equation of nth order with constant coefficients is a linear combination of $n$ linearly independent solutions, which can be found by solving the **characteristic equation**

$$
a_n r^n + a_{n-1} r^{n-1} + \cdots + a_1 r + a_0 = 0
$$

- The characteristic equation may have repeated or complex roots, which affect the form of the solutions.

- The general solution of a non-homogeneous linear differential equation of nth order with constant coefficients is the sum of the general solution of the homogeneous equation and a **particular solution** of the non-homogeneous equation, which can be found by various methods, such as **undetermined coefficients** or **variation of parameters**.

- The method of undetermined coefficients involves guessing a particular solution of the same form as $f(x)$, with some unknown coefficients, and then plugging it into the equation to determine the coefficients.

- The method of variation of parameters involves finding $n$ functions $u_1(x), u_2(x), \ldots, u_n(x)$ such that

$$
y_p(x) = u_1(x) y_1(x) + u_2(x) y_2(x) + \cdots + u_n(x) y_n(x)
$$

is a particular solution, where $y_1(x), y_2(x), \ldots, y_n(x)$ are the linearly independent solutions of the homogeneous equation. The functions $u_1(x), u_2(x), \ldots, u_n(x)$ can be found by solving a system of linear equations involving the Wronskian of the homogeneous solutions.