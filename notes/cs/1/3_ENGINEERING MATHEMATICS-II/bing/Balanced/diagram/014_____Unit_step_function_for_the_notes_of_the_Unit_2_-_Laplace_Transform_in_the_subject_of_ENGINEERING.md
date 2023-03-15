### Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function, denoted by $u(t)$, is defined as

$$
u(t) = \begin{cases}
0, & t < 0 \\
1, & t \geq 0
\end{cases}
$$

- The unit step function can be used to model a switch that turns on or off at a certain time.

- The Laplace transform of the unit step function is given by 

$$
\mathcal{L}\{u(t)\} = \int_0^\infty u(t) e^{-st} dt = \int_0^\infty e^{-st} dt = \frac{1}{s}, \quad s > 0
$$

- The Laplace transform of a shifted unit step function, denoted by $u_c(t)$, where $c$ is a positive constant, is defined as 

$$
u_c(t) = \begin{cases}
0, & t < c \\
1, & t \geq c
\end{cases}
$$

- The Laplace transform of a shifted unit step function is given by 

$$
\mathcal{L}\{u_c(t)\} = \int_c^\infty e^{-st} dt = \frac{e^{-cs}}{s}, \quad s > 0
$$

- The shifted unit step function can be used to represent a function that starts at a certain time $c$.

- The Laplace transform of a function multiplied by a shifted unit step function, denoted by $u_c(t) f(t-c)$, where $f(t)$ is any function, is given by 

$$
\mathcal{L}\{u_c(t) f(t-c)\} = e^{-cs} \mathcal{L}\{f(t)\}, \quad s > 0
$$

- This property is called the time displacement theorem or the time shift theorem. It allows us to find the Laplace transform of a function that is delayed by a certain time $c$.

- The Laplace transform of a piecewise continuous function, which is a function that is continuous on every finite interval but may have a finite number of jumps or discontinuities, can be found by using the unit step function to represent the function as a sum of simpler functions, and then using the linearity property of the Laplace transform to find the transform of each term. For example, if

$$
f(t) = \begin{cases}
t, & 0 \leq t < 1 \\
2, & 1 \leq t < 2 \\
t^2, & t \geq 2
\end{cases}
$$

- Then we can write

$$
f(t) = t u_0(t) + (2-t) u_1(t) + (t^2-2) u_2(t)
$$

- And then use the Laplace transform properties to find

$$
\mathcal{L}\{f(t)\} = \mathcal{L}\{t u_0(t)\} + \mathcal{L}\{(2-t) u_1(t)\} + \mathcal{L}\{(t^2-2) u_2(t)\}
$$

$$
= \frac{1}{s^2} + e^{-s} \left(\frac{2}{s} - \frac{1}{s^2}\right) + e^{-2s} \left(\frac{2}{s^3} - \frac{2}{s}\right)
$$

- The Laplace transform of a piecewise continuous function can be used to solve differential equations with discontinuous forcing functions or initial conditions.