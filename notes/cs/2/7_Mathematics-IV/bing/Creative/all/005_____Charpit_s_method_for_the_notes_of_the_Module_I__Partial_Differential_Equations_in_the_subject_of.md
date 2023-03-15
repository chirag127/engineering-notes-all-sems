# Charpit's method

Charpit's method is a general method for finding the complete solution of non-linear partial differential equation of the first order of the form

`f(x, y, z, p, q) = 0` (1)

where `p = dz/dx` and `q = dz/dy` are the partial derivatives of `z` with respect to `x` and `y` respectively.

The main steps of Charpit's method are:

- Introduce a new variable `lambda` and a compatible first order PDE of the form

`g(x, y, z, p, q, lambda) = 0` (2)

where `g` is an arbitrary function of six variables and `lambda` is an arbitrary constant.

- Solve the system of six equations obtained by equating the total differentials of (1) and (2) to zero, i.e.

`df = f_x dx + f_y dy + f_z dz + f_p dp + f_q dq = 0` (3)

`dg = g_x dx + g_y dy + g_z dz + g_p dp + g_q dq + g_lambda dlambda = 0` (4)

where the subscripts denote partial derivatives.

- Eliminate `lambda` and `dlambda` from the system and obtain five equations in five unknowns `x, y, z, p, q`.

- Integrate these equations to obtain the complete integral of the original PDE (1).

## Example

Consider the following PDE of the first order:

`2x(q^2z^2 + 1) = pz` (5)

where `p = dz/dx` and `q = dz/dy`.

To apply Charpit's method, we introduce a new variable `lambda` and a compatible PDE of the form

`lambda = qz` (6)

Then, the total differentials of (5) and (6) are

`df = (q^2z^2 + 1) dx + 4xqz dq + (2xq^2z - p) dz - z dp = 0` (7)

`dg = z dq + q dz + dlambda = 0` (8)

From (8), we can eliminate `dlambda` and get

`dlambda = -z dq - q dz` (9)

Substituting this into (7), we get

`df - g_lambda dlambda = (q^2z^2 + 1) dx + (4xqz + g_lambda z) dq + (2xq^2z - p - g_lambda q) dz - z dp = 0` (10)

Now, we have to solve the system of five equations obtained by equating the coefficients of `dx, dy, dz, dp, dq` to zero, i.e.

`q^2z^2 + 1 = 0` (11)

`4xqz + g_lambda z = 0` (12)

`2xq^2z - p - g_lambda q = 0` (13)

`z = 0` (14)

`p = 0` (15)

From (11), we get

`q = +- i/z` (16)

where `i` is the imaginary unit.

From (12), we get

`g_lambda = -4xq` (17)

Substituting (16) and (17) into (13), we get

`p = 2xq^2z + 4xq^2` (18)

From (14) and (15), we get

`z = 0` (19)

`p = 0` (20)

Now, we have to integrate these equations to obtain the complete integral of (5).

From (19) and (20), we get

`z = c_1` (21)

`p = c_2` (22)

where `c_1` and `c_2` are arbitrary constants.

From (16), we get

`q = +- i/z` (23)

Integrating this with respect to `y`, we get

`z^2 y = +- i x + c_3` (24)

where `c_3` is an arbitrary constant.

From (18), we get

`p = 2xq^2z + 4xq^2` (25)

Integrating this with respect to `x`, we get