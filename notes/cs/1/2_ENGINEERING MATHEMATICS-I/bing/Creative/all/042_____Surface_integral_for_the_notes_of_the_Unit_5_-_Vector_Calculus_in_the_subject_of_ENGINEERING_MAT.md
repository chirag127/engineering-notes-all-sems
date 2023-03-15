# Surface Integral

- A surface integral is a generalization of a line integral to account for surfaces in three dimensions.
- A surface integral is used to add a bunch of values associated with points on a surface, such as area, mass, flux, etc.
- A surface integral can be of two types: scalar or vector.
- A scalar surface integral is used to integrate a scalar function over a surface, such as the surface area of a sphere.
- A vector surface integral is used to integrate a vector field over a surface, such as the electric flux through a closed surface.
- A surface integral can be computed by using a parameterization of the surface, such as spherical or cylindrical coordinates, and applying the change of variables formula.
- A surface integral can also be computed by using the divergence theorem or the Stokes' theorem, which relate surface integrals to volume integrals or line integrals, respectively.

## Examples

- Example 1: Find the surface area of a hemisphere of radius r.

  - Solution: The surface of a hemisphere can be parameterized by using spherical coordinates as follows:

    - x = r sin θ cos φ
    - y = r sin θ sin φ
    - z = r cos θ

    where 0 ≤ θ ≤ π/2 and 0 ≤ φ ≤ 2π.

  - The surface element dS can be found by taking the cross product of the partial derivatives of the parameterization with respect to θ and φ:

    - dS = |∂(x, y, z)/∂θ × ∂(x, y, z)/∂φ| dθ dφ
    - dS = r^2 sin θ dθ dφ

  - The surface area of the hemisphere is then given by the scalar surface integral:

    - A = ∫∫ S dS
    - A = ∫∫ r^2 sin θ dθ dφ
    - A = r^2 ∫_0^π/2 sin θ dθ ∫_0^2π dφ
    - A = r^2 [-cos θ]_0^π/2 [φ]_0^2π
    - A = r^2 (1 - 0) (2π - 0)
    - A = 2πr^2

- Example 2: Find the electric flux through a cube of side length a centered at the origin, if the electric field is given by E = (x, y, z).

  - Solution: The electric flux through a surface is given by the vector surface integral:

    - Φ = ∫∫ S E · dS

    where dS is the outward normal vector to the surface.

  - The cube has six faces, each of which can be parameterized by using Cartesian coordinates as follows:

    - Face 1: x = a/2, -a/2 ≤ y ≤ a/2, -a/2 ≤ z ≤ a/2
    - Face 2: x = -a/2, -a/2 ≤ y ≤ a/2, -a/2 ≤ z ≤ a/2
    - Face 3: y = a/2, -a/2 ≤ x ≤ a/2, -a/2 ≤ z ≤ a/2
    - Face 4: y = -a/2, -a/2 ≤ x ≤ a/2, -a/2 ≤ z ≤ a/2
    - Face 5: z = a/2, -a/2 ≤ x ≤ a/2, -a/2 ≤ y ≤ a/2
    - Face 6: z = -a/2, -a/2 ≤ x ≤ a/2, -a/2 ≤ y ≤ a/2

  - The surface element dS for each face can be found by taking the cross product of the partial derivatives of the parameterization with respect to x and y or y and z or z and x, depending on the face, and multiplying by the appropriate sign to get the outward normal vector:

    - dS_1 = (a/2, 0, 0) dy dz
    - dS_2 = (-a/2, 0, 0) dy dz
    - dS_3 = (0, a/2, 0) dx dz
    - dS_4 = (0, -a/2, 0) dx