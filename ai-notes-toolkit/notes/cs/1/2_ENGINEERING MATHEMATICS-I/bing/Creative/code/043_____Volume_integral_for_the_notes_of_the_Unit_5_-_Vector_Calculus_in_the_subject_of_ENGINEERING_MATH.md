# Volume integral

- A volume integral is a type of multiple integral that extends the concept of area integral to three-dimensional regions.
- A volume integral can be used to calculate the volume, mass, charge, or other properties of a solid object or a region of space.
- A volume integral can be expressed in Cartesian, cylindrical, or spherical coordinates, depending on the shape and symmetry of the region of integration.
- A volume integral can be evaluated by applying the fundamental theorem of calculus iteratively, or by using techniques such as substitution, integration by parts, or change of variables.
- A volume integral can be related to a surface integral by using the divergence theorem or the Stokes' theorem, which are generalizations of the fundamental theorem of calculus for vector fields.

## Definition and notation

- A volume integral is denoted by the symbol ∭, which is a triple integral sign.
- A volume integral has the form

  ∭<sub>V</sub> f(x,y,z) dV

  where V is the region of integration, f(x,y,z) is the integrand function, and dV is the differential volume element.
- The differential volume element dV can be written in different coordinate systems as follows:

  - In Cartesian coordinates (x,y,z), dV = dx dy dz
  - In cylindrical coordinates (r,θ,z), dV = r dr dθ dz
  - In spherical coordinates (ρ,θ,φ), dV = ρ<sup>2</sup> sin φ dρ dθ dφ

- The limits of integration for each variable depend on the shape and boundaries of the region V, and may be constants or functions of other variables.
- The order of integration can be changed if the limits of integration are adjusted accordingly, and if the integrand function is continuous in the region V.

## Examples

- To calculate the volume of a sphere of radius R, we can use a volume integral in spherical coordinates as follows:

  ∭<sub>V</sub> dV = ∭<sub>V</sub> ρ<sup>2</sup> sin φ dρ dθ dφ

  where V is the region defined by 0 ≤ ρ ≤ R, 0 ≤ θ ≤ 2π, and 0 ≤ φ ≤ π.

  Evaluating the integral, we get

  ∭<sub>V</sub> dV = ∫<sub>0</sub><sup>R</sup> ∫<sub>0</sub><sup>2π</sup> ∫<sub>0</sub><sup>π</sup> ρ<sup>2</sup> sin φ dφ dθ dρ

  = ∫<sub>0</sub><sup>R</sup> ρ<sup>2</sup> dρ ∫<sub>0</sub><sup>2π</sup> dθ ∫<sub>0</sub><sup>π</sup> sin φ dφ

  = [ρ<sup>3</sup>/3]<sub>0</sub><sup>R</sup> [θ]<sub>0</sub><sup>2π</sup> [-cos φ]<sub>0</sub><sup>π</sup>

  = R<sup>3</sup>/3 (2π) (2)

  = 4πR<sup>3</sup>/3

  which is the well-known formula for the volume of a sphere.

- To calculate the mass of a solid cone of height h and base radius R, with density ρ = kx, where k is a constant and x is the distance from the vertex, we can use a volume integral in cylindrical coordinates as follows:

  ∭<sub>V</sub> ρ dV = ∭<sub>V</sub> kx dV = ∭<sub>V</sub> kx r dr dθ dz

  where V is the region defined by 0 ≤ r ≤ Rz/h, 0 ≤ θ ≤ 2π, and 0 ≤ z ≤ h.

  Evaluating the integral, we get

  ∭<sub>V</sub> ρ dV = ∫<sub>0</sub><sup>h</sup> ∫<sub>0</sub><sup>2π</sup> ∫<sub>0</sub><sup>Rz/h</sup> kx r dr dθ dz

  = ∫<sub>0</sub><