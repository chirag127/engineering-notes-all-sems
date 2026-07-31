### Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function, denoted by $u(t)$, is defined as

$$
u(t) = \begin{cases}
0, & t < 0 \\
1, & t \geq 0
\end{cases}
$$

- The unit step function can be used to model a switch that is turned on at a certain time.

- The Laplace transform of the unit step function is given by 

$$
\mathcal{L}\{u(t)\} = \int_{0}^{\infty} u(t) e^{-st} dt = \int_{0}^{\infty} e^{-st} dt = \frac{1}{s}, \quad s > 0
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
\mathcal{L}\{u_c(t)\} = \int_{0}^{\infty} u_c(t) e^{-st} dt = \int_{c}^{\infty} e^{-st} dt = \frac{e^{-cs}}{s}, \quad s > 0
$$

- The shifted unit step function can be used to model a switch that is turned on at a certain time $c$.

- The Laplace transform of a function multiplied by a unit step function is given by the time displacement theorem 

$$
\mathcal{L}\{u_c(t) f(t-c)\} = e^{-cs} \mathcal{L}\{f(t)\}, \quad s > 0
$$

- The time displacement theorem can be used to find the Laplace transform of a piecewise continuous function that has different expressions for different intervals of time.

- For example, if $f(t) = \begin{cases}
t, & 0 \leq t < 2 \\
2, & t \geq 2
\end{cases}$, then we can write $f(t) = t u_0(t) + (2-t) u_2(t)$ and use the time displacement theorem to find its Laplace transform as

$$
\mathcal{L}\{f(t)\} = \mathcal{L}\{t u_0(t)\} + \mathcal{L}\{(2-t) u_2(t)\} = \frac{1}{s^2} + e^{-2s} \left(\frac{2}{s} - \frac{1}{s^2}\right) = \frac{1 - e^{-2s}}{s^2}
$$

- The inverse Laplace transform of a function multiplied by an exponential term can be found by using the inverse of the time displacement theorem

$$
\mathcal{L}^{-1}\{e^{-cs} F(s)\} = u_c(t) \mathcal{L}^{-1}\{F(s)\}(t-c), \quad s > 0
$$

- For example, if $F(s) = \frac{1}{s^2 + 4}$, then we can find the inverse Laplace transform of $e^{-2s} F(s)$ as

$$
\mathcal{L}^{-1}\{e^{-2s} F(s)\} = u_2(t) \mathcal{L}^{-1}\{F(s)\}(t-2) = u_2(t) \frac{\sin(2(t-2))}{2}
$$