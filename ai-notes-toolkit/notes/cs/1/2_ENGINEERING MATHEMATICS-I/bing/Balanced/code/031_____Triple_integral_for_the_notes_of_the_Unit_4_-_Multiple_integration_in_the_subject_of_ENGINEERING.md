# Triple integral

- A triple integral is a generalization of a double integral to three dimensions.
- It is used to calculate the volume of a solid region in space, or the amount of a function over a solid region.
- A triple integral can be written as ∭Bf(x, y, z)dV, where B is the region of integration, f(x, y, z) is the integrand function, and dV is the differential volume element.
- A triple integral can be evaluated by iterated integration, that is, by integrating first with respect to one variable, then with respect to another, and finally with respect to the third.
- The order of integration can be changed if the limits of integration are adjusted accordingly.
- A triple integral can also be evaluated by changing the coordinate system, such as cylindrical or spherical coordinates, to simplify the region of integration or the integrand function.

## Examples

- Example 1: Find the volume of the solid bounded by the planes x = 0, y = 0, z = 0, x + y + z = 1, and x + y = 1.

Solution: The region of integration B is a triangular prism with vertices (0, 0, 0), (0, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 0), and (1, 0, 0). The integrand function is f(x, y, z) = 1, since we want to find the volume. We can choose any order of integration, but let us choose dzdydx. Then the limits of integration are:

- 0 ≤ x ≤ 1
- 0 ≤ y ≤ 1 - x
- 0 ≤ z ≤ 1 - x - y

The triple integral is:

∭Bf(x, y, z)dV = ∭B1dV = ∫0^1∫0^(1-x)∫0^(1-x-y)1dzdydx

= ∫0^1∫0^(1-x)(1 - x - y)dydx

= ∫0^1(1 - x - (1 - x)^2/2)dx

= ∫0^1(1/2 - x/2 + x^2/2)dx

= (x/2 - x^2/4 + x^3/6)|0^1

= 1/6

Therefore, the volume of the solid is 1/6.

- Example 2: Find the triple integral ∭BxyzdV, where B is the region inside the sphere x^2 + y^2 + z^2 = 4.

Solution: The region of integration B is a sphere with radius 2 and center at the origin. The integrand function is f(x, y, z) = xyz. We can use spherical coordinates to simplify the region of integration and the integrand function. The spherical coordinates are:

- x = ρcosθsinφ
- y = ρsinθsinφ
- z = ρcosφ
- dV = ρ^2sinφdρdθdφ

The limits of integration are:

- 0 ≤ ρ ≤ 2
- 0 ≤ θ ≤ 2π
- 0 ≤ φ ≤ π

The triple integral is:

∭BxyzdV = ∭Bρ^3cosθsinθcos^2φsin^3φdρdθdφ

= ∫0^2∫0^(2π)∫0^πρ^3cosθsinθcos^2φsin^3φdφdθdρ

= ∫0^2ρ^3dρ∫0^(2π)cosθsinθdθ∫0^πcos^2φsin^3φdφ

= (ρ^4/4)|0^2(cos^2θ/2)|0^(2π)(cos^3φ/3 - cosφ)|0^π

= 4/4(0 - 0)(-1/3 - 1/3)

= 0

Therefore, the triple integral is zero. This is because the integrand function is odd with respect to x, y, and z, and the region of integration is symmetric with respect to the origin.