### Surface Integral

- A surface integral is a generalization of a line integral to account for surfaces in three dimensions.
- A surface integral is used to add a bunch of values associated with points on a surface, such as area, mass, flux, etc.
- A surface integral can be of two types: scalar or vector.
- A scalar surface integral is used to integrate a scalar function over a surface, such as the surface area of a sphere.
- A vector surface integral is used to integrate a vector field over a surface, such as the electric flux through a closed surface.
- A surface integral can be computed by using a parameterization of the surface, such as spherical or cylindrical coordinates, and applying the change of variables formula.
- A surface integral can also be computed by using the divergence theorem or the Stokes' theorem, which relate surface integrals to volume integrals or line integrals, respectively.

#### Examples

- Example 1: Find the surface area of a sphere of radius r.

  - Solution: The surface area of a sphere is given by the scalar surface integral of 1 over the sphere. We can parameterize the sphere using spherical coordinates as follows:

    - x = r sin θ cos φ
    - y = r sin θ sin φ
    - z = r cos θ
    - where 0 ≤ θ ≤ π and 0 ≤ φ ≤ 2π.

  - The surface element dS can be found by taking the cross product of the partial derivatives of the parameterization with respect to θ and φ, and taking the magnitude:

    - dS = |∂(x,y,z)/∂θ × ∂(x,y,z)/∂φ| dθ dφ
    - dS = r^2 sin θ dθ dφ

  - The surface integral is then given by:

    - ∫∫ S 1 dS = ∫∫ r^2 sin θ dθ dφ
    - = r^2 ∫_0^π sin θ dθ ∫_0^2π dφ
    - = r^2 [-cos θ]_0^π [φ]_0^2π
    - = r^2 (2) (2π)
    - = 4πr^2

  - This is the familiar formula for the surface area of a sphere.

- Example 2: Find the electric flux through a cube of side length a centered at the origin, if the electric field is given by E = (x,y,z).

  - Solution: The electric flux through a closed surface is given by the vector surface integral of the electric field dotted with the outward unit normal vector to the surface. We can divide the cube into six faces, each of which is a square, and compute the flux through each face separately. We can use Cartesian coordinates to parameterize each face as follows:

    - Front face: x = a/2, -a/2 ≤ y ≤ a/2, -a/2 ≤ z ≤ a/2
    - Back face: x = -a/2, -a/2 ≤ y ≤ a/2, -a/2 ≤ z ≤ a/2
    - Right face: y = a/2, -a/2 ≤ x ≤ a/2, -a/2 ≤ z ≤ a/2
    - Left face: y = -a/2, -a/2 ≤ x ≤ a/2, -a/2 ≤ z ≤ a/2
    - Top face: z = a/2, -a/2 ≤ x ≤ a/2, -a/2 ≤ y ≤ a/2
    - Bottom face: z = -a/2, -a/2 ≤ x ≤ a/2, -a/2 ≤ y ≤ a/2

  - The surface element dS can be found by taking the cross product of the partial derivatives of the parameterization with respect to x and y, or y and z, or z and x, depending on the face, and taking the magnitude. For example, for the front face, we have:

    - dS = |∂(x,y,z)/∂y × ∂(x,y,z)/∂z| dy dz
    - dS = |(0,1,0) × (0,0,1)| dy dz
    - dS = |(1,0,0)| dy dz
    - dS = dy dz