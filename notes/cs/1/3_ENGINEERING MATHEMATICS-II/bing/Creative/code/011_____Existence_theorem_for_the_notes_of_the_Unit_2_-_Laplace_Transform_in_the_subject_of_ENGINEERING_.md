# Existence theorem for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The Laplace transform is an integral transform that converts a function of time, f(t), into a function of a complex variable, s, denoted by L(f(t)) or F(s).
- The Laplace transform is particularly useful in solving linear ordinary differential equations such as those arising in the analysis of electronic circuits.
- The Laplace transform existence theorem states that, if f(t) is piecewise continuous on every finite interval in [0, ∞) and satisfies the condition

$$
|f(t)| \leq Me^{at}
$$

for some constants M and a and for all t ≥ 0, then L(f(t)) exists for all s > a   .
- The condition |f(t)| ≤ Me^at means that f(t) is of exponential order, and it ensures that the integral

$$
L(f(t)) = \int_{0}^{\infty} e^{-st} f(t) dt
$$

converges for s > a.
- As an example, every exponential function f(t) = e^bt has a Laplace transform for all finite values of b and s.
- Not every function has a Laplace transform. For example, it can be shown that f(t) = e^t^2 does not have a Laplace transform, since the integral

$$
\int_{0}^{\infty} e^{-st} e^{t^2} dt = \infty
$$

for every real number s.