### Surface Integral

A surface integral is a generalization of multiple integrals to integration over surfaces. It can be thought of as the double integral analog of the line integral. Given a surface, one may integrate over its scalar fields (that is, functions which return scalars as values), and vector fields (that is, functions which return vectors as values).

Surface integrals have applications in physics, particularly with the theories of classical electromagnetism. For example, Gauss's law, which relates the electric flux through a closed surface to the charge enclosed within the surface, can be expressed in terms of a surface integral.

There are two types of surface integrals: the surface integral of a scalar field and the surface integral of a vector field.

1. **Surface integral of a scalar field**: Given a scalar field f(x,y,z) defined over a surface S, the surface integral of f over S is defined as the integral of f over the projection of S onto the xy-plane. This can be expressed mathematically as: `∬S f(x,y,z) dS = ∬D f(x,y,g(x,y)) dA`, where D is the projection of S onto the xy-plane and g(x,y) gives the z-coordinate of the surface S.

2. **Surface integral of a vector field**: Given a vector field F(x,y,z) defined over a surface S, the surface integral of F over S is defined as the integral of the dot product of F with the unit normal vector to the surface. This can be expressed mathematically as: `∬S F • dS`, where dS is the differential surface element and the dot product represents the flux of the vector field through the surface.

In order to evaluate a surface integral, it is often necessary to parameterize the surface S by introducing a coordinate system. This allows us to express the surface integral in terms of a double integral over the parameter domain.