### Charpit's method

Charpit's method is a general method for finding the complete solution of non-linear partial differential equation of the first order of the form

`f(x, y, z, p, q) = 0`

where `p = dz/dx` and `q = dz/dy` are the partial derivatives of `z` with respect to `x` and `y` respectively.

The main idea of Charpit's method is to introduce two auxiliary variables `u` and `v` such that

`du = p dx + q dy`

`dv = dx + dy`

and then solve the system of equations

`f(x, y, z, p, q) = 0`

`du = p dx + q dy`

`dv = dx + dy`

for `x, y, z, p, q` in terms of `u, v`.

The steps of Charpit's method are as follows:

1. Write the given partial differential equation in the form `f(x, y, z, p, q) = 0`.
2. Write the expressions for `du` and `dv` in terms of `dx, dy, dz, p, q`.
3. Eliminate `dz` from the expressions for `du` and `dv` by using the relation `dz = p dx + q dy`.
4. Equate the coefficients of `dx` and `dy` in the expressions for `du` and `dv` to obtain two equations involving `p, q, u, v`.
5. Solve these two equations for `p` and `q` in terms of `u, v`.
6. Substitute the values of `p` and `q` in the given partial differential equation to obtain an equation involving `x, y, z, u, v`.
7. Solve this equation for `z` in terms of `x, y, u, v`.
8. Find the relations between `x, y, u, v` by integrating the expressions for `du` and `dv`.
9. Eliminate `u` and `v` from the relations between `x, y, u, v` and the expression for `z` to obtain the complete solution of the partial differential equation.

Here is an example of applying Charpit's method to solve a partial differential equation.

**Example:** Solve the partial differential equation `p^2 + q^2 = 1`.

**Solution:**

We write the given partial differential equation in the form `f(x, y, z, p, q) = 0` as

`p^2 + q^2 - 1 = 0`

We write the expressions for `du` and `dv` as

`du = p dx + q dy`

`dv = dx + dy`

We eliminate `dz` from these expressions by using the relation `dz = p dx + q dy` as

`du - dz = q dy`

`dv - dz = dx`

We equate the coefficients of `dx` and `dy` in these expressions to obtain two equations involving `p, q, u, v` as

`p - q = dv/du`

`q + p = 1`

We solve these two equations for `p` and `q` in terms of `u, v` as

`p = (1 + dv/du)/2`

`q = (1 - dv/du)/2`

We substitute the values of `p` and `q` in the given partial differential equation to obtain an equation involving `x, y, z, u, v` as

`((1 + dv/du)/2)^2 + ((1 - dv/du)/2)^2 - 1 = 0`

Simplifying, we get

`(dv/du)^2 = 0`

This implies that `dv/du` is a constant, say `c`. Hence, we have

`dv = c du`

We solve this equation for `z` in terms of `x, y, u, v` as

`z = u + c v`

We find the relations between `x, y, u, v` by integrating the expressions for `du` and `dv` as

`du = p dx + q dy`

`dv = dx + dy`

Integrating, we get

`u = p x + q y + k_1`

`v = x + y + k_2`

where `k_1` and `k_2` are constants of integration.

We

We eliminate `u` and `v` from the relations between `x, y, u, v` and the expression for `z` to obtain the complete solution of the partial differential equation as

`z = p x + q y + k_1 + c (x + y + k_2)`

where `p, q, c, k_1, k_2` are arbitrary constants.

This is the general solution of the partial differential equation `p^2 + q^2 = 1`.

One possible mnemonic to remember the steps of Charpit's method is:

**F**ind the equation in the form `f(x, y, z, p, q) = 0`

**D**ifferentiate `u` and `v` with respect to `x` and `y`

**E**liminate `dz` from the expressions for `du` and `dv`

**C**ompare the coefficients of `dx` and `dy` to get two equations

**S**olve for `p` and `q` in terms of `u` and `v`

**S**ubstitute `p` and `q` in the equation to get an equation in `x, y, z, u, v`

**S**olve for `z` in terms of `x, y, u, v`

**I**ntegrate `du` and `dv` to get the relations between `x, y, u, v`

**E**liminate `u` and `v` to get the complete solution

The mnemonic is **FDECSSSIE**, which can be pronounced as "FED-SESS-EE".