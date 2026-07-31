### Triple integral

- A triple integral is a generalization of a double integral to three dimensions. It is used to calculate the volume of a solid region in space, or the amount of a function over a solid region.
- A triple integral can be written as ∭Bf(x, y, z)dV, where B is the solid region of integration, f(x, y, z) is the integrand function, and dV is the differential volume element.
- A triple integral can be evaluated by iterated integration, that is, by integrating first with respect to one variable, then with respect to another, and finally with respect to the third. The order of integration can be chosen to simplify the calculation, as long as the limits of integration are consistent with the region B.
- A triple integral can also be expressed in different coordinate systems, such as cylindrical or spherical coordinates, depending on the shape and symmetry of the region B. The differential volume element dV must be changed accordingly to match the coordinate system.
- A triple integral can be used to find the volume, mass, center of mass, moment of inertia, and other physical quantities of a solid object, as well as the average value of a function over a solid region.

#### Examples

- Example 1: Find the volume of the solid bounded by the planes x = 0, y = 0, z = 0, and x + y + z = 1.

  - Solution: The region of integration B is a tetrahedron with vertices at (0, 0, 0), (1, 0, 0), (0, 1, 0), and (0, 0, 1). The integrand function is f(x, y, z) = 1, since we want to find the volume. We can choose any order of integration, but let us use the order dzdydx. The limits of integration are:

    - For x, from 0 to 1.
    - For y, from 0 to 1 - x, since y + x ≤ 1.
    - For z, from 0 to 1 - x - y, since z + x + y ≤ 1.

  - The triple integral is:

    - ∭Bf(x, y, z)dV = ∭B1dV = ∫0^1∫0^(1-x)∫0^(1-x-y)1dzdydx
    - = ∫0^1∫0^(1-x)(1 - x - y)dydx
    - = ∫0^1(1 - x - 1/2(1 - x)^2)dx
    - = 1/2 - 1/3 - 1/12 = 1/6

  - Therefore, the volume of the solid is 1/6.

- Example 2: Find the mass of the solid hemisphere x^2 + y^2 + z^2 ≤ 1, z ≥ 0, if the density function is ρ(x, y, z) = z.

  - Solution: The region of integration B is a hemisphere with radius 1 and center at the origin. The integrand function is f(x, y, z) = ρ(x, y, z) = z, since we want to find the mass. We can use spherical coordinates to simplify the calculation, since the region B has spherical symmetry. The spherical coordinates are:

    - x = rcosθsinφ
    - y = rsinθsinφ
    - z = rcosφ
    - dV = r^2sinφdrdθdφ

  - The limits of integration are:

    - For r, from 0 to 1, since the radius is 1.
    - For θ, from 0 to 2π, since we cover the whole circle.
    - For φ, from 0 to π/2, since we only consider the upper hemisphere.

  - The triple integral is:

    - ∭Bf(x, y, z)dV = ∭Bρ(x, y, z)dV = ∭Bzr^2sinφdrdθdφ
    - = ∫0^(π/2)∫0^(2π)∫0^1rcosφr^2sinφdrdθdφ
    - = ∫0^(π/2)∫0^(2π)cosφsinφr^4