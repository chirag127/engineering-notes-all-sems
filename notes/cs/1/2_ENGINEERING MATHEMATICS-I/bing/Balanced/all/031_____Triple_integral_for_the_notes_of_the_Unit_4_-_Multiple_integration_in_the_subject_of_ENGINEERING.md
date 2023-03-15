# Triple integral

- A triple integral is a generalization of a double integral to three dimensions. It is used to calculate the volume of a solid region in space, or the amount of a function over such a region.
- A triple integral can be written as ∭Bf(x, y, z)dV, where B is the region of integration, f(x, y, z) is the integrand function, and dV is the differential volume element.
- A triple integral can be evaluated by iterated integration, that is, by integrating first with respect to one variable, then with respect to another, and finally with respect to the third. The order of integration can be chosen to simplify the calculation, as long as the limits of integration are consistent with the region B.
- A triple integral can also be evaluated by changing the coordinates to a more suitable system, such as cylindrical or spherical coordinates. This can make the region B easier to describe and the integrand function easier to integrate. The change of coordinates requires the use of the Jacobian determinant to adjust the differential volume element.
- A triple integral can be used to find the volume of a solid region by setting the integrand function to 1. It can also be used to find the mass of a solid region with variable density, the center of mass, the moment of inertia, the electric charge, the heat flow, and other physical quantities.

## Examples

- Find the volume of the solid region bounded by the planes x = 0, y = 0, z = 0, and x + y + z = 1.

Solution: The region B can be described by the inequalities 0 ≤ x ≤ 1, 0 ≤ y ≤ 1 - x, and 0 ≤ z ≤ 1 - x - y. The integrand function is 1. The triple integral is

∭BdV = ∫0^1∫0^(1-x)∫0^(1-x-y)dzdydx

= ∫0^1∫0^(1-x)(1 - x - y)dydx

= ∫0^1(1/2 - x/2 - x^2/3)dx

= 1/6

- Find the mass of the solid region bounded by the sphere x^2 + y^2 + z^2 = 4, if the density function is ρ(x, y, z) = x^2 + y^2 + z^2.

Solution: The region B can be described by the spherical coordinates 0 ≤ r ≤ 2, 0 ≤ θ ≤ 2π, and 0 ≤ φ ≤ π. The integrand function is ρ(r, θ, φ) = r^2. The differential volume element is dV = r^2sinφdrdθdφ. The Jacobian determinant is 1. The triple integral is

∭BρdV = ∫0^2∫0^2π∫0^πr^4sinφdφdθdr

= ∫0^2r^4dr∫0^2πdθ∫0^πsinφdφ

= (2^5/5 - 0^5/5)(2π - 0)(-cosπ + cos0)

= 64π/5