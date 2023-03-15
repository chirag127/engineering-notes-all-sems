# Linear differential equation of nth order with constant coefficients

- A linear differential equation of nth order with constant coefficients is an equation of the form

  \[a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_2 y'' + a_1 y' + a_0 y = f(x)\]

  where \(a_n, a_{n-1}, \ldots, a_0\) are constants and \(f(x)\) is a given function of \(x\).

- The equation is called **homogeneous** if \(f(x) = 0\) and **non-homogeneous** otherwise.

- The general solution of a homogeneous linear differential equation of nth order with constant coefficients is a linear combination of \(n\) linearly independent solutions, which can be found by assuming a solution of the form \(y = e^{rx}\) and solving the **characteristic equation**

  \[a_n r^n + a_{n-1} r^{n-1} + \cdots + a_2 r^2 + a_1 r + a_0 = 0\]

  The roots of the characteristic equation determine the form of the solutions. There are three cases to consider:

  - If the characteristic equation has \(n\) distinct real roots \(r_1, r_2, \ldots, r_n\), then the general solution is

    \[y = c_1 e^{r_1 x} + c_2 e^{r_2 x} + \cdots + c_n e^{r_n x}\]

    where \(c_1, c_2, \ldots, c_n\) are arbitrary constants.

  - If the characteristic equation has repeated real roots, then the general solution is

    \[y = (c_1 + c_2 x + \cdots + c_k x^{k-1}) e^{r x}\]

    where \(r\) is a root of multiplicity \(k\) and \(c_1, c_2, \ldots, c_k\) are arbitrary constants.

  - If the characteristic equation has complex roots, then the general solution is

    \[y = e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x)\]

    where \(\alpha \pm i \beta\) are complex conjugate roots and \(c_1, c_2\) are arbitrary constants.

- The general solution of a non-homogeneous linear differential equation of nth order with constant coefficients is the sum of the general solution of the homogeneous equation and a **particular solution** of the non-homogeneous equation, which can be found by various methods, such as:

  - **Method of undetermined coefficients**: This method works when \(f(x)\) is a polynomial, an exponential, a sine or cosine, or a linear combination of these functions. The idea is to assume a particular solution of the same form as \(f(x)\) (with some undetermined coefficients) and substitute it into the equation to find the coefficients.

  - **Method of variation of parameters**: This method works for any \(f(x)\). The idea is to assume a particular solution of the form

    \[y_p = u_1 y_1 + u_2 y_2 + \cdots + u_n y_n\]

    where \(y_1, y_2, \ldots, y_n\) are the linearly independent solutions of the homogeneous equation and \(u_1, u_2, \ldots, u_n\) are functions of \(x\) to be determined. The functions \(u_1, u_2, \ldots, u_n\) are found by solving a system of \(n\) linear equations obtained by substituting \(y_p\) and its derivatives into the equation and requiring that the coefficients of \(y_1, y_2, \ldots, y_n\) vanish.