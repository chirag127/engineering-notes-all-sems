### Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function, denoted by $u(t)$, is defined as
$$
u(t) = \begin{cases}
0, & t < 0 \\
1, & t \geq 0
\end{cases}
$$
- The unit step function can be used to model a switch that turns on or off at a certain time.
- The graph of the unit step function is a horizontal line that jumps from 0 to 1 at the origin.

- The Laplace transform of the unit step function is given by
$$
\mathcal{L}\{u(t)\} = \int_0^\infty u(t) e^{-st} dt = \int_0^\infty e^{-st} dt = \frac{1}{s}, \quad s > 0
$$
- The Laplace transform of the unit step function can be used to find the Laplace transform of a function that is defined piecewise by using the time displacement theorem, which states that
$$
\mathcal{L}\{u(t-a) f(t-a)\} = e^{-as} \mathcal{L}\{f(t)\}, \quad a > 0
$$
- This theorem allows us to shift a function to the right by $a$ units and multiply it by the unit step function $u(t-a)$, which effectively makes the function zero for $t < a$ and equal to $f(t-a)$ for $t \geq a$.
- For example, if we want to find the Laplace transform of the function
$$
f(t) = \begin{cases}
0, & t < 2 \\
t-2, & t \geq 2
\end{cases}
$$
we can write it as
$$
f(t) = u(t-2) (t-2)
$$
and then apply the time displacement theorem to get
$$
\mathcal{L}\{f(t)\} = \mathcal{L}\{u(t-2) (t-2)\} = e^{-2s} \mathcal{L}\{t\} = e^{-2s} \frac{1}{s^2}
$$