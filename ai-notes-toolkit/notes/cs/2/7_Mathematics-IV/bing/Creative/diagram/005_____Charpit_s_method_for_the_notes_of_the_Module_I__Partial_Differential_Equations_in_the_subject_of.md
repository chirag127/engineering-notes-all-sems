### Charpit's method

- Charpit's method is a general method for finding the complete solution of non-linear partial differential equation of the first order of the form f(x, y, z, p, q) = 0, where p = dz/dx and q = dz/dy .
- The method is based on the idea of finding a family of characteristic curves that satisfy the given equation, and then finding a surface that contains these curves .
- The steps of the method are as follows :

  1. Write the given equation in the form F(x, y, z, p, q) = 0 and assume that z is a function of x and y, i.e. z = z(x, y).
  2. Differentiate the equation partially with respect to x and y, and obtain two equations of the form Fx + Fp dx + Fq dz = 0 and Fy + Fp dy + Fq dz = 0, where Fx, Fy, Fp, Fq are the partial derivatives of F with respect to x, y, p, q respectively.
  3. Eliminate dz from the above two equations and obtain an equation of the form P(x, y, z, p, q) dx + Q(x, y, z, p, q) dy = 0, where P and Q are some functions of x, y, z, p, q.
  4. Write the Charpit's equations as dx/P = dy/Q = dz/R = dp/S = dq/T, where R, S, T are some functions of x, y, z, p, q obtained by equating the coefficients of dx, dy, dz, dp, dq in the equation F = 0.
  5. Solve the Charpit's equations either by eliminating the variables x, y, z, p, q or by finding the integrals of the form f(x, y, z, p, q) = c, where c is a constant.
  6. The solution of the Charpit's equations will give the complete integral of the given equation, which is a function of the form z = z(x, y, c1, c2, ..., cn), where c1, c2, ..., cn are arbitrary constants.

- An example of applying Charpit's method is the following :

  - Find the complete integral of the equation p^2 + q^2 - 2z = 0.
  - The Charpit's equations are dx/(2p) = dy/(2q) = dz/(p^2 + q^2) = dp/(-p) = dq/(-q).
  - From the last two equations, we get p = a/e^x and q = b/e^y, where a and b are constants.
  - Substituting these values into the first two equations, we get dx/a = dy/b = dz/(a^2 + b^2).
  - Integrating the first equation, we get ax + c1 = c, where c1 and c are constants.
  - Integrating the second equation, we get by + c2 = d, where c2 and d are constants.
  - Integrating the third equation, we get z = (a^2 + b^2)/2 + c3, where c3 is a constant.
  - The complete integral is z = (a^2 + b^2)/2 + c3, where a = e^(-x)(c - c1), b = e^(-y)(d - c2), and c3, c1, c2, c, d are arbitrary constants.