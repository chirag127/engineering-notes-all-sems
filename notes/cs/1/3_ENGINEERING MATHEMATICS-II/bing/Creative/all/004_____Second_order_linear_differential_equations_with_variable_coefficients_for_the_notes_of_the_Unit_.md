# Second order linear differential equations with variable coefficients

- A second-order linear differential equation is an equation of the form

  $$a_2(x)y'' + a_1(x)y' + a_0(x)y = r(x)$$

  where $a_2(x)$, $a_1(x)$, $a_0(x)$, and $r(x)$ are functions of the independent variable $x$ and $a_2(x)$ is not identically zero .

- If $r(x) \equiv 0$, the equation is called **homogeneous**; otherwise, it is called **nonhomogeneous**.

- The general solution of a homogeneous equation is a linear combination of two linearly independent solutions, which can be found by various methods depending on the form of the coefficients.

- The general solution of a nonhomogeneous equation is the sum of the general solution of the corresponding homogeneous equation and a **particular solution** of the nonhomogeneous equation, which can be found by various methods depending on the form of the nonhomogeneous term.

- Some common methods for finding solutions of second-order linear differential equations with variable coefficients are:

  - **Reduction of order**: This method can be used to find a second linearly independent solution of a homogeneous equation, given one known solution.

  - **Method of undetermined coefficients**: This method can be used to find a particular solution of a nonhomogeneous equation, if the nonhomogeneous term is a linear combination of exponential, sinusoidal, polynomial, or logarithmic functions.

  - **Method of variation of parameters**: This method can be used to find a particular solution of a nonhomogeneous equation, regardless of the form of the nonhomogeneous term, given two linearly independent solutions of the corresponding homogeneous equation.

  - **Power series method**: This method can be used to find solutions of homogeneous or nonhomogeneous equations, if the coefficients and the nonhomogeneous term are analytic functions, by assuming that the solution is a power series and finding its coefficients recursively.

  - **Frobenius method**: This method is a generalization of the power series method, which can be used to find solutions of homogeneous or nonhomogeneous equations, if the coefficients and the nonhomogeneous term are analytic functions, by assuming that the solution is a series of the form $x^r\sum_{n=0}^\infty a_nx^n$ and finding the values of $r$ and the coefficients $a_n$.