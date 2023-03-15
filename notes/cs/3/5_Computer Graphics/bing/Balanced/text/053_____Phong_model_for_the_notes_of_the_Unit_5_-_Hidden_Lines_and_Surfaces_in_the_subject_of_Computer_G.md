### Phong model

The Phong model is a widely used model for the local illumination of points on a surface in computer graphics. It was designed by Bui Tuong Phong in 1973 and is based on the empirical observation of how light interacts with different materials.

The Phong model consists of three components: ambient, diffuse, and specular. Each component represents a different aspect of the light reflection from a surface.

- Ambient component: This is the constant term that accounts for the background or indirect illumination of the surface. It is independent of the light source and the viewing direction and is usually set to a small value to avoid completely dark areas.
- Diffuse component: This is the term that models the diffuse reflection of light from a surface. It is proportional to the cosine of the angle between the light direction and the surface normal and depends on the color and the reflectivity of the surface. It is also known as Lambertian reflection, as it follows Lambert's cosine law.
- Specular component: This is the term that models the specular reflection of light from a surface. It is proportional to the cosine of the angle between the viewing direction and the reflection direction and depends on the color, the reflectivity, and the shininess of the surface. It is also known as Phong reflection, as it follows Phong's empirical formula.

The Phong model can be expressed mathematically as follows:

I = I_a + I_d + I_s

where I is the total intensity of the reflected light, I_a is the ambient component, I_d is the diffuse component, and I_s is the specular component.

The ambient component can be calculated as:

I_a = k_a I_a

where k_a is the ambient reflectivity of the surface and I_a is the ambient light intensity.

The diffuse component can be calculated as:

I_d = k_d I_d (N ⋅ L)

where k_d is the diffuse reflectivity of the surface, I_d is the diffuse light intensity, N is the unit surface normal, and L is the unit light direction.

The specular component can be calculated as:

I_s = k_s I_s (R ⋅ V)^n

where k_s is the specular reflectivity of the surface, I_s is the specular light intensity, R is the unit reflection direction, V is the unit viewing direction, and n is the shininess exponent of the surface.

The Phong model can be implemented in different ways, such as:

- Phong shading: This is the technique of applying the Phong model at each pixel of the surface, using the interpolated normals and the actual light and viewing directions. This produces smooth and realistic shading effects, but it is computationally expensive.
- Gouraud shading: This is the technique of applying the Phong model at each vertex of the surface, using the vertex normals and the average light and viewing directions. This produces fast and smooth shading effects, but it can cause artifacts such as Mach bands or specular highlights.
- Flat shading: This is the technique of applying the Phong model at each polygon of the surface, using the polygon normal and the average light and viewing direction. This produces fast and simple shading effects, but it can cause discontinuities and faceted appearance.