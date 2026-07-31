### Volume integral

- A volume integral is the calculation of the volume of a three-dimensional object by integrating over a 3-dimensional domain.
- A volume integral is a special case of multiple integrals, where the integrand is a function of three variables (x, y, z) and the domain of integration is a solid region in 3-dimensional space.
- A volume integral can be written as ∭<sub>V</sub>f(x,y,z)dV, where f(x,y,z) is the integrand function and V is the solid region of integration.
- A volume integral can be evaluated by using different coordinate systems, such as Cartesian, cylindrical, or spherical coordinates, depending on the shape and symmetry of the solid region.
- A volume integral can be used to find the mass, density, charge, or flux of a solid object, as well as the average value of a function over a solid region.
- A volume integral can also be used to find the volume of a solid of revolution, which is a solid obtained by rotating a 2-dimensional region about an axis. In this case, the volume integral can be computed by using the method of disks or washers, which involves slicing the solid perpendicular to the axis of rotation and summing up the areas of the circular slices.

Some examples of volume integrals are:

- Example 1: Find the volume of the solid bounded by the planes x=0, y=0, z=0, and x+y+z=1.
  - Solution: The solid region is a tetrahedron with vertices at (0,0,0), (1,0,0), (0,1,0), and (0,0,1). We can use Cartesian coordinates to set up the volume integral as follows:

  ∭<sub>V</sub>dV = ∫<sub>0</sub><sup>1</sup>∫<sub>0</sub><sup>1-x</sup>∫<sub>0</sub><sup>1-x-y</sup>dzdydx

  - Evaluating the integral from the inside out, we get:

  ∭<sub>V</sub>dV = ∫<sub>0</sub><sup>1</sup>∫<sub>0</sub><sup>1-x</sup>(1-x-y)dydx = ∫<sub>0</sub><sup>1</sup>(1-x)(1/2-x/3)dx = (1/6)(1/2-1/4) = 1/24

  - Therefore, the volume of the solid is 1/24.

- Example 2: Find the volume of the solid obtained by rotating the region bounded by y=x<sup>2</sup> and y=1 about the x-axis.
  - Solution: The solid region is a solid of revolution with a hole in the middle. We can use the method of washers to set up the volume integral as follows:

  ∭<sub>V</sub>dV = ∫<sub>-1</sub><sup>1</sup>π(R<sup>2</sup>-r<sup>2</sup>)dx, where R is the outer radius and r is the inner radius of the washer.

  - Since the region is rotated about the x-axis, the outer radius is R=1 and the inner radius is r=x<sup>2</sup>. Therefore, the volume integral becomes:

  ∭<sub>V</sub>dV = ∫<sub>-1</sub><sup>1</sup>π(1-x<sup>4</sup>)dx = π(2-x<sup>5</sup>/5)<sub>-1</sub><sup>1</sup> = π(4/5)

  - Therefore, the volume of the solid is 4π/5.