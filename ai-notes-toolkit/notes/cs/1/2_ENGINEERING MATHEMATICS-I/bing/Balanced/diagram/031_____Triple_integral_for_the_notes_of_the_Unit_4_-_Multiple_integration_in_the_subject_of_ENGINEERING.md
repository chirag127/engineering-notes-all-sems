### Triple integral

- A triple integral is a generalization of a double integral to three dimensions. It is used to calculate the volume of a solid region in space, or the amount of a function over a solid region.
- A triple integral of a function f(x, y, z) over a region D in space is denoted by ∭Df(x, y, z)dV, where dV is the infinitesimal volume element.
- A triple integral can be evaluated by iterated integration, that is, by integrating f(x, y, z) with respect to one variable, then integrating the result with respect to another variable, and finally integrating the result with respect to the third variable.
- The order of integration can be changed, as long as the limits of integration are adjusted accordingly. The order of integration can affect the difficulty and the efficiency of the calculation.
- A triple integral can be converted to a different coordinate system, such as cylindrical or spherical coordinates, if the region D or the function f(x, y, z) has a simpler expression in that system. This can also simplify the calculation and reduce the number of integrals.
- A triple integral can be used to find the volume, mass, center of mass, moment of inertia, and other physical quantities of a solid region in space, or a function over a solid region.

Example: Evaluate the triple integral ∭DxyzdV, where D is the region bounded by the planes x = 0, y = 0, z = 0, and x + y + z = 1.

Solution: One possible order of integration is dzdydx, with the following limits:

- For x, the lower limit is 0 and the upper limit is 1, since x is between 0 and 1 in D.
- For y, the lower limit is 0 and the upper limit is 1 - x, since y is between 0 and 1 - x in D.
- For z, the lower limit is 0 and the upper limit is 1 - x - y, since z is between 0 and 1 - x - y in D.

Therefore, the triple integral is:

∭DxyzdV = ∫0^1 ∫0^(1-x) ∫0^(1-x-y) xyzdzdydx

= ∫0^1 ∫0^(1-x) xy(1 - x - y)dydx

= ∫0^1 x(1 - x) ∫0^(1-x) y - y^2 dydx

= ∫0^1 x(1 - x) (1/2 - x/3 - x^2/6)dx

= (1/24 - 1/30 - 1/60) - (1/120 - 1/180 - 1/360)

= 1/120.