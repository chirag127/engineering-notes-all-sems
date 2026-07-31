### Phong model

The Phong model is a widely used model for the local illumination of points on a surface in computer graphics. It was designed by Bui Tuong Phong in 1973 and is based on the observation that different materials reflect light differently, depending on the angle of incidence and the angle of reflection. The Phong model consists of three components: ambient, diffuse, and specular reflection.

- Ambient reflection: This is the constant term that represents the light that is scattered by the environment and reaches the surface from all directions. It is independent of the light source position and the surface normal. It is usually given by a constant color value, denoted by I_a.

- Diffuse reflection: This is the term that represents the light that is reflected equally in all directions by a rough or matte surface. It depends on the angle between the light source direction and the surface normal, denoted by theta. It is proportional to the cosine of this angle, which is also the dot product of the light source direction vector L and the surface normal vector N. It is usually given by a color value that depends on the surface material, denoted by k_d, and the color of the light source, denoted by I_d. The diffuse reflection term is then given by k_d * I_d * (L . N).

- Specular reflection: This is the term that represents the light that is reflected in a narrow range of directions by a shiny or glossy surface. It depends on the angle between the reflection direction and the viewer direction, denoted by alpha. It is proportional to the cosine of this angle raised to some power, which is also the dot product of the reflection direction vector R and the viewer direction vector V raised to some power n. The power n controls the shininess or glossiness of the surface. A higher value of n means a smaller and sharper specular highlight, while a lower value of n means a larger and softer specular highlight. It is usually given by a color value that depends on the surface material, denoted by k_s, and the color of the light source, denoted by I_s. The specular reflection term is then given by k_s * I_s * (R . V)^n.

The total color of a point on a surface illuminated by a single light source is then given by the sum of the three components:

I = I_a + k_d * I_d * (L . N) + k_s * I_s * (R . V)^n

The following diagram illustrates the Phong model:

![Phong model diagram](https://upload.wikimedia.org/wikipedia/commons/6/6b/Phong_components_version_4.png)

The Phong model can be used with different interpolation methods to shade the surfaces of 3D objects. One of the most common methods is Phong shading, which computes the illumination at each pixel of the surface using the Phong model, based on the interpolated normal vectors at each pixel. Another method is Gouraud shading, which computes the illumination at each vertex of the surface using the Phong model, and then interpolates the color values across the surface. Phong shading produces more realistic results than Gouraud shading, but it is also more computationally expensive.