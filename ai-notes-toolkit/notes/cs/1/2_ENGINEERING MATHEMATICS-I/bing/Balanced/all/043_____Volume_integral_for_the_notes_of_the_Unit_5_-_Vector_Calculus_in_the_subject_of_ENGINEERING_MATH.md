# Volume integral

- A volume integral is the calculation of the volume of a three-dimensional object.
- The symbol for a volume integral is “∫”.
- A volume integral is a special case of multiple integrals, which are integrals over more than one variable.
- Volume integrals are especially important in physics for many applications, such as calculating flux densities, mass, center of mass, moment of inertia, etc.
- To evaluate a volume integral, we need to know the equation of the object and the limits of integration, which define the region of integration.
- Depending on the shape and orientation of the object, we may use different coordinate systems, such as Cartesian, cylindrical, or spherical coordinates, to simplify the calculation.
- In Cartesian coordinates, a volume integral has the form

$$\iiint_R f(x,y,z) \, dx \, dy \, dz$$

where R is the region of integration in the xyz-space.

- In cylindrical coordinates, a volume integral has the form

$$\iiint_R f(r,\theta,z) \, r \, dr \, d\theta \, dz$$

where R is the region of integration in the r$\theta$z-space.

- In spherical coordinates, a volume integral has the form

$$\iiint_R f(\rho,\phi,\theta) \, \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$$

where R is the region of integration in the $\rho\phi\theta$-space.

- To convert between different coordinate systems, we need to use the appropriate formulas for the variables and the Jacobian determinant for the differential element.

- For example, to convert from Cartesian to cylindrical coordinates, we use

$$x = r \cos \theta, \quad y = r \sin \theta, \quad z = z, \quad dx \, dy \, dz = r \, dr \, d\theta \, dz$$

- To convert from Cartesian to spherical coordinates, we use

$$x = \rho \sin \phi \cos \theta, \quad y = \rho \sin \phi \sin \theta, \quad z = \rho \cos \phi, \quad dx \, dy \, dz = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$$

- To convert from cylindrical to spherical coordinates, we use

$$r = \rho \sin \phi, \quad \theta = \theta, \quad z = \rho \cos \phi, \quad r \, dr \, d\theta \, dz = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$$

- To find the volume of a solid of revolution, which is a three-dimensional object that results from revolving a two-dimensional region about a particular axis, we can use the method of disks or washers, which involves taking slices perpendicular to the axis of revolution and integrating their areas.
- The method of disks applies when the region is bounded by a single curve and the axis of revolution, and the area of each slice is a circular disk with radius equal to the distance from the curve to the axis.
- The method of washers applies when the region is bounded by two curves and the axis of revolution, and the area of each slice is a circular ring or washer with inner radius equal to the distance from the inner curve to the axis and outer radius equal to the distance from the outer curve to the axis.
- The formulas for the volume of a solid of revolution using the method of disks or washers are

$$V = \pi \int_a^b [R(x)]^2 \, dx$$

if the region is revolved about the x-axis,

$$V = \pi \int_c^d [R(y)]^2 \, dy$$

if the region is revolved about the y-axis,

$$V = \pi \int_a^b [R(x)]^2 - [r(x)]^2 \, dx$$

if the region is revolved about the x-axis and bounded by two curves,

$$V = \pi \int_c^d [R(y)]^2 - [r(y)]^2 \, dy$$

if the region is revolved about the y-axis and bounded by two curves,

where R(x) or R(y) is the outer radius and r(x) or r(y) is the inner radius of the washer.

- To find the