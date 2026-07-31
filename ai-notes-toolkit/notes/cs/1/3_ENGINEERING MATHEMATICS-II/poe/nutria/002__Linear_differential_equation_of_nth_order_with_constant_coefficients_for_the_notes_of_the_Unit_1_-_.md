
### Linear differential equation of nth order with constant coefficients

A linear differential equation of nth order with constant coefficients is an equation of the form:

$$a_n \frac{d^ny}{dx^n} + a_{n-1}\frac{d^{n-1}y}{dx^{n-1}} + \dots + a_1 \frac{dy}{dx} + a_0y = g(x)$$

where $a_n, a_{n-1}, \dots, a_1, a_0$ are constants and $g(x)$ is a given function of $x$.

The general solution of this equation can be expressed as a linear combination of $n$ linearly independent solutions of the homogeneous equation:

$$a_n \frac{d^ny}{dx^n} + a_{n-1}\frac{d^{n-1}y}{dx^{n-1}} + \dots + a_1 \frac{dy}{dx} + a_0y = 0$$

The homogeneous equation can be solved using the method of undetermined coefficients. The general solution of the homogeneous equation is given by:

$$y = c_1y_1 + c_2y_2 + \dots + c_ny_n$$

where $y_1, y_2, \dots, y_n$ are the $n$ linearly independent solutions of the homogeneous equation and $c_1, c_2, \dots, c_n$ are arbitrary constants.

The particular solution of the non-homogeneous equation can be obtained by the method of variation of parameters. The particular solution of the non-homogeneous equation is given by:

$$y_p = y_1u_1 + y_2u_2 + \dots + y_nu_n$$

where $u_1, u_2, \dots, u_n$ are the solutions of the system of $n$ linear equations:

$$\begin{cases}
  a_n \frac{d^ny_1}{dx^n} + a_{n-1}\frac{d^{n-1}y_1}{dx^{n-1}} + \dots + a_1 \frac{dy_1}{dx} + a_0y_1 = g(x) \\
  a_n \frac{d^ny_2}{dx^n} + a_{n-1}\frac{d^{n-1}y_2}{dx^{n-1}} + \dots + a_1 \frac{dy_2}{dx} + a_0y_2 = 0 \\
  \vdots \\
  a_n \frac{d^ny_n}{dx^n} + a_{n-1}\frac{d^{n-1}y_n}{dx^{n-1}} + \dots + a_1 \frac{dy_n}{dx} + a_0y_n = 0
\end{cases}$$

The general solution of the non-homogeneous equation is given by:

$$y = c_1y_1 + c_2y_2 + \dots + c_ny_n + y_p$$