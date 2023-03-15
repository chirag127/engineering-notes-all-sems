# Phong model

The Phong model is a widely used model for the local illumination of points on a surface in computer graphics. It was designed by Bui Tuong Phong in 1973 and is based on the observation that different materials reflect light differently, depending on the angle of incidence and the angle of reflection.

The Phong model consists of three components: ambient, diffuse, and specular. Each component represents a different aspect of how light interacts with a surface.

- Ambient component: This component accounts for the general illumination of the scene, regardless of the direction of the light source or the viewer. It is usually a constant value that is added to the final color of the point.
- Diffuse component: This component represents the scattering of light in all directions by a rough or matte surface. It depends on the angle between the light source and the surface normal, and is proportional to the cosine of that angle. The diffuse component is also affected by the color and intensity of the light source and the surface.
- Specular component: This component represents the reflection of light by a shiny or glossy surface. It depends on the angle between the reflection vector and the viewer vector, and is proportional to the cosine of that angle raised to a power called the shininess. The specular component is also affected by the color and intensity of the light source and the surface.

The Phong model can be expressed mathematically as follows:

`I = I_a + I_d + I_s`

where `I` is the final color of the point, `I_a` is the ambient component, `I_d` is the diffuse component, and `I_s` is the specular component.

The ambient component can be calculated as:

`I_a = k_a * I_a_l`

where `k_a` is the ambient reflection coefficient of the surface, and `I_a_l` is the ambient light intensity.

The diffuse component can be calculated as:

`I_d = k_d * I_l * (N * L)`

where `k_d` is the diffuse reflection coefficient of the surface, `I_l` is the light intensity, `N` is the surface normal, and `L` is the light vector.

The specular component can be calculated as:

`I_s = k_s * I_l * (R * V)^n`

where `k_s` is the specular reflection coefficient of the surface, `R` is the reflection vector, `V` is the viewer vector, and `n` is the shininess.

The Phong model can produce realistic results for a variety of materials, but it also has some limitations. For example, it does not account for the global illumination effects, such as shadows, reflections, or refractions. It also assumes that the light source and the viewer are infinitely far away, which is not always true in real scenes. Furthermore, it does not consider the wavelength of the light, which can affect the color and intensity of the reflection. Therefore, the Phong model is often used as a basis for more advanced models that can handle these issues.